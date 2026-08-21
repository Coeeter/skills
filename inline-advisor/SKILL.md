---
name: inline-advisor
description: Consult another local coding model as a read-only advisor.
---

# Inline Advisor Agent

Ask Claude Code or Codex for one bounded outside opinion while the current agent retains planning, implementation, and verification authority. Even when the task says “implement,” the advisor proposes an implementation; it never edits the workspace.

1. Select the advisor the user named. If none was named, use a different provider only when a genuine competency gap or consequential uncertainty justifies the cost; prefer Claude for frontend and interaction judgment, and Codex for backend, data, debugging, and systems work. State the choice. Completion: the advisor and exact question are explicit.
2. Write a cold-reader brief to a temporary file. Include the objective, disputed or uncertain decision, binding constraints, relevant repository-relative paths or spec/plan pointers, evidence already observed, and the requested output. Include only context that changes the advice. Completion: a model with no conversation history can answer without guessing the task.
3. Run `scripts/ask-advisor.ts` with Bun from the project root using `--advisor claude|codex`, `--prompt-file`, and `--cwd`. Pass `--model` or `--effort` only when the user requested them; otherwise preserve the target CLI's configuration. Use a long timeout or background execution. Completion: the command returns a non-empty answer or a concrete failure.
4. Keep the call one-hop and read-only. The advisor may inspect named repository context but cannot edit, install, commit, push, deploy, or invoke another advisor. A missing CLI, authentication failure, or unavailable model is reported as that advisor's failure; the host does not impersonate it. Completion: repository state is unchanged by the call.
5. Present the response as attributed outside advice. Check load-bearing claims against the repository, then state what you accept, reject, or still need to resolve. The advisor's confidence is evidence to examine, not authority. Completion: the host owns the resulting decision and any later implementation.

The helper uses Claude's restricted read tools with no session persistence, or Codex's read-only ephemeral sandbox, and checks Git state before and after the call. Remove the temporary brief after reporting.
