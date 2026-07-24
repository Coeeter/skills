---
name: commit
description: Split current Git worktree changes into logical commits with one-line Conventional Commit messages without pushing. Use when the user asks to commit changes, create commits, group changes into commits, or use conventional commit messages but does not ask to push.
---

# Commit

1. Read repository instructions, then inspect the branch, status, diff, and recent commit style.
2. Preserve all user changes. Group files and hunks by coherent concern; do not create one commit per file or mix unrelated concerns.
3. Run the repository's required checks unless they already passed after the latest change. Stop if checks or hooks fail.
4. Stage explicit paths or hunks for one group at a time. Never use `git add .` when unrelated changes exist.
5. Commit each group with a single-line Conventional Commit message: `<type>(<optional-scope>): <imperative summary>`. Use no body. Prefer `feat`, `fix`, `refactor`, `test`, `docs`, or `chore`.
6. Inspect the remaining diff after every commit. Do not amend, rewrite history, bypass hooks, or push.
7. Report the commit hashes/messages and whether the worktree is clean.

If the worktree has no changes, do not create an empty commit. If safe grouping is ambiguous, keep overlapping changes together.
