---
name: init-agent
description: Initialize or repair a repository's agent instructions and project skills.
---

# Initialize Agent Context

Create a concise, portable instruction system for a new or existing repository. Treat `AGENTS.md` as the shared index, `CLAUDE.md` as a compatibility entrypoint, and skills as procedures loaded only when relevant.

1. Invoke `writing-for-agents`; its rules govern all instruction files. Inspect the repository, existing agent instructions, manifests, scripts, CI, documentation, local skill inventory, and worktree state. Ask the user for project context they want agents to retain, while resolving discoverable facts yourself. Completion: existing guidance and authoritative validation commands are known before anything is written.
2. Classify candidate guidance:
   - `AGENTS.md`: concise repository-wide instructions, validation entrypoints, and context pointers;
   - nested `AGENTS.md` or `AGENTS.override.md`: rules that apply only below a directory;
   - `docs/context.md`: durable cross-feature decisions, invariants, external quirks, and recurring constraints;
   - skills: multi-step or conditional procedures;
   - environment: facts already obvious from code or configuration.
   Keep one source of truth for each meaning. Completion: no instruction is duplicated merely to support another agent.
3. Create or refine root `AGENTS.md` as an index. Include only rules that change agent behavior, repository-specific validation commands, and sharp pointers such as when to read `docs/context.md` or narrower documentation. Preserve relevant existing guidance and remove stale conflicts only when authorized. Completion: the file lets any coding agent find the next source without attempting to summarize the whole repository.
4. Create or refine root `CLAUDE.md` with `@AGENTS.md` as its shared source. Add Claude-specific material only when a real Claude-only constraint exists. Prefer nested instructions for narrower scope. Completion: shared rules exist once and Claude Code can load them.
5. Create or refine `docs/context.md` when durable context exists. Capture key decisions and the minimum rationale needed to preserve intent; link deeper sources. Exclude transient status, chat history, exhaustive architecture tours, and cheap repository lookups. Completion: every entry is useful across multiple features or recurring sessions.
6. Research project-relevant skills using Skills CLI results and the skills' primary repositories. Assess each candidate against the actual stack and workflows, overlap with existing instructions or skills, expected frequency, scope, maintenance, and context cost. Present one complete proposal containing source, purpose, global or project scope, install method, and exclusions. Wait for explicit approval. Completion: every proposed skill earns its place and the user can approve the batch in one response.
7. Install only approved skills with Skills CLI. For personal project-local installation, offer local Git exclusion; for team-shared installation, explain the tracked files before writing them. Do not infer sharing preference. Verify installed paths and agent discovery. Completion: approved skills are installed at the approved scope and no unapproved skill or repository file was added.
8. Validate the setup against repository commands and each agent's discovery rules. Report created or changed files, installed skills, local exclusions, unresolved uncertainty, and whether changes are tracked. Completion: another supported agent can enter the repository and locate instructions, durable context, validation, and relevant procedures without relying on this thread.

This skill does not authorize commits, pushes, deployments, destructive actions, or unrelated project changes.
