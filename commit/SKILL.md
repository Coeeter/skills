---
name: commit
description: Split current Git worktree changes into logical commits with one-line Conventional Commit messages without pushing. Use when the user asks to commit changes, create commits, group changes into commits, or use conventional commit messages but does not ask to push.
---

# Commit

1. Read repository instructions, then inspect the branch, status, diff, and recent commit style.
2. Preserve all user changes. Before staging, write a short commit map grouping files and hunks by user-visible feature or coherent concern.
   - Default to multiple commits when changes span distinct features, packages, or product areas. A large diff (roughly 25+ files) is a strong signal to split, not a reason to collapse.
   - Shared files, generated files, migrations, and cross-package wiring do not by themselves justify one mega-commit. Stage hunks where practical; place inseparable shared changes with the earliest commit that needs them.
   - Use one commit only when the diff represents one behavior and splitting would leave misleading or incoherent commits. If safe grouping remains ambiguous after inspecting hunks, choose fewer broader commits—but never combine clearly independent features merely because they overlap.
   - Do not create one commit per file.
3. Run the repository's required checks unless they already passed after the latest change. Stop if checks or hooks fail.
4. Stage explicit paths or hunks for one group at a time. Never use `git add .` when unrelated changes exist.
5. Commit each group with a single-line Conventional Commit message: `<type>(<optional-scope>): <imperative summary>`. Use no body. Prefer `feat`, `fix`, `refactor`, `test`, `docs`, or `chore`.
6. Inspect the remaining diff after every commit. Do not amend, rewrite history, bypass hooks, or push.
7. Report the commit hashes/messages and whether the worktree is clean.

If the worktree has no changes, do not create an empty commit. When grouping is ambiguous, prefer several coherent feature commits over one repository-wide commit.
