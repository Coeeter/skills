#!/usr/bin/env bun

import { mkdtempSync, readFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";

type Advisor = "claude" | "codex";
type Effort = "low" | "medium" | "high" | "xhigh" | "max";

type Options = {
  advisor: Advisor;
  promptFile: string;
  cwd: string;
  model?: string;
  effort?: Effort;
  dryRun: boolean;
};

function fail(message: string, code = 2): never {
  console.error(message);
  process.exit(code);
}

function usage(): string {
  return "Usage: ask-advisor.ts --advisor claude|codex --prompt-file PATH [--cwd PATH] [--model MODEL] [--effort LEVEL] [--dry-run]";
}

function parseArgs(argv: string[]): Options {
  const values = new Map<string, string>();
  let dryRun = false;
  for (let index = 0; index < argv.length; index += 1) {
    const argument = argv[index];
    if (argument === "--help" || argument === "-h") {
      console.log(usage());
      process.exit(0);
    }
    if (argument === "--dry-run") {
      dryRun = true;
      continue;
    }
    if (!argument.startsWith("--")) fail(`Unexpected argument: ${argument}\n${usage()}`);
    const value = argv[index + 1];
    if (!value || value.startsWith("--")) fail(`Missing value for ${argument}\n${usage()}`);
    values.set(argument, value);
    index += 1;
  }

  const advisor = values.get("--advisor");
  if (advisor !== "claude" && advisor !== "codex") fail(`Invalid or missing --advisor\n${usage()}`);
  const promptFile = values.get("--prompt-file");
  if (!promptFile) fail(`Missing --prompt-file\n${usage()}`);
  const effort = values.get("--effort");
  if (effort && !["low", "medium", "high", "xhigh", "max"].includes(effort)) {
    fail(`Invalid --effort: ${effort}`);
  }

  return {
    advisor,
    promptFile: resolve(promptFile),
    cwd: resolve(values.get("--cwd") ?? process.cwd()),
    model: values.get("--model"),
    effort: effort as Effort | undefined,
    dryRun,
  };
}

function gitSnapshot(cwd: string): Buffer | null {
  const result = Bun.spawnSync({
    cmd: ["git", "-C", cwd, "status", "--porcelain=v1", "-z", "--untracked-files=all"],
    stdout: "pipe",
    stderr: "ignore",
  });
  return result.exitCode === 0 ? Buffer.from(result.stdout) : null;
}

function claudeCommand(options: Options): string[] {
  const command = [
    "claude",
    "--print",
    "--no-session-persistence",
    "--permission-mode",
    "plan",
    "--tools",
    "Read,Glob,Grep",
    "--disallowedTools",
    "Edit,Write,NotebookEdit,Bash,mcp__*",
    "--output-format",
    "text",
  ];
  if (options.model) command.push("--model", options.model);
  if (options.effort) command.push("--effort", options.effort);
  return command;
}

function codexCommand(options: Options, outputPath: string): string[] {
  const command = [
    "codex",
    "--ask-for-approval",
    "never",
    "exec",
    "--sandbox",
    "read-only",
    "--ephemeral",
    "--cd",
    options.cwd,
    "--output-last-message",
    outputPath,
  ];
  if (options.model) command.push("--model", options.model);
  if (options.effort) command.push("--config", `model_reasoning_effort="${options.effort}"`);
  command.push("-");
  return command;
}

function main(): number {
  const options = parseArgs(Bun.argv.slice(2));
  if (!Bun.which(options.advisor)) fail(`${options.advisor} executable not found on PATH`, 127);

  let prompt: string;
  try {
    prompt = readFileSync(options.promptFile, "utf8");
  } catch {
    fail(`Cannot read prompt file: ${options.promptFile}`);
  }
  if (!prompt.trim()) fail("Prompt file is empty");

  const before = gitSnapshot(options.cwd);
  const temporaryDirectory = mkdtempSync(join(tmpdir(), "inline-advisor-"));
  const outputPath = join(temporaryDirectory, "answer.md");
  try {
    const command = options.advisor === "claude" ? claudeCommand(options) : codexCommand(options, outputPath);
    if (options.dryRun) {
      console.log(JSON.stringify(command));
      return 0;
    }

    const environment = { ...process.env };
    delete environment.CLAUDECODE;
    const result = Bun.spawnSync({
      cmd: command,
      cwd: options.cwd,
      stdin: Buffer.from(prompt),
      stdout: "pipe",
      stderr: "pipe",
      env: environment,
    });
    if (result.exitCode !== 0) {
      process.stderr.write(result.stderr);
      return result.exitCode;
    }

    const answer =
      options.advisor === "claude" ? result.stdout.toString() : readFileSync(outputPath, "utf8");
    if (!answer.trim()) fail(`${options.advisor} returned an empty answer`);
    process.stdout.write(answer.endsWith("\n") ? answer : `${answer}\n`);
  } finally {
    rmSync(temporaryDirectory, { recursive: true, force: true });
  }

  const after = gitSnapshot(options.cwd);
  if (before && (!after || !before.equals(after))) {
    console.error("Advisor call changed Git worktree state; inspect before continuing");
    return 3;
  }
  return 0;
}

process.exitCode = main();
