---
name: init-agent
description: Use when setting up agent context for an existing repository.
disable-model-invocation: true
---

# Initialize Agent Context

Make an existing repository easy for coding agents to understand and work in
without relying on prior conversation history.

1. Inspect the repository before asking questions.

   Read:
   - existing agent instructions;
   - README and important docs;
   - manifests and package structure;
   - scripts and supported commands;
   - relevant architecture and entrypoints;
   - tests, CI, deployment, and environment configuration;
   - obvious coding conventions and framework usage.

   Resolve anything discoverable from the repository yourself.

2. Ask the user one concise round of questions for context the repository cannot
   reveal, such as:
   - What is this project for?
   - What are its main goals?
   - What are explicit non-goals?
   - Who uses it and how?
   - What behavior or architectural decisions must be preserved?
   - What parts of the current project are temporary, legacy, or known bad?
   - Are there workflow preferences agents should know?

   Ask only questions that would materially improve future agent decisions.

3. Build a concise durable context model from the repository and the answers.

   Separate information by purpose:

   - `AGENTS.md` -> how agents should work in this repository;
   - `docs/context.md` -> what the project means and durable decisions behind it;
   - `CLAUDE.md` -> compatibility entrypoint for Claude;
   - nested instructions -> only when a directory genuinely needs different rules.

4. Create or refine `AGENTS.md`.

   Keep it short. Include only repository-specific guidance that changes agent
   behavior, such as:
   - supported development and validation commands;
   - important architectural conventions;
   - framework-specific expectations;
   - real validation boundaries;
   - important files or docs to read for certain work;
   - repository-specific traps or constraints.

   Do not copy facts that agents can cheaply discover from code.

5. Create or refine `docs/context.md`.

   Capture durable knowledge that future agents should not have to rediscover:
   - project purpose;
   - goals and non-goals;
   - users and important workflows;
   - architectural intent and invariants;
   - important terminology;
   - external constraints and quirks;
   - significant product or engineering decisions with brief rationale;
   - known legacy areas or intentional compromises.

   Keep transient task state and implementation trivia out.

6. Create or refine `CLAUDE.md` as:

   `@AGENTS.md`

   Add more only when Claude genuinely requires different instructions.

7. Audit available project-relevant skills when useful.

   Recommend only skills that clearly improve this repository's recurring
   workflow or framework usage. Avoid redundant skills and unnecessary context
   cost.

   Ask before installing or creating skills.

8. Reconcile the result.

   Remove stale or duplicated guidance, preserve useful existing instructions,
   and ensure each important rule has one clear source of truth.

9. Present:
   - your understanding of the project;
   - files created or changed;
   - important conventions captured;
   - remaining uncertainties;
   - optional skill recommendations.

The finished repository should let a capable coding agent understand the
project's purpose, constraints, conventions, and correct way to validate work
without needing the conversation that created these files.

Do not commit, push, deploy, or perform destructive actions unless separately
requested.
