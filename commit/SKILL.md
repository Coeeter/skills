---
name: commit
description: Commit requested worktree changes without pushing.
---

# Commit

1. Read repository instructions, then inspect the branch, status, diff, and recent commit style.
2. Preserve all user changes. Before staging, build an ordered commit map grouping files and hunks by user-visible feature or coherent concern.
   - Default to multiple commits when changes span distinct features, packages, or product areas. A large diff (roughly 25+ files) is a strong signal to split, not a reason to collapse.
   - Shared files, generated files, migrations, and cross-package wiring do not by themselves justify one mega-commit. Stage hunks where practical; place inseparable shared changes with the earliest commit that needs them.
   - Use one commit only when the diff represents one behavior and splitting would leave misleading or incoherent commits. If safe grouping remains ambiguous after inspecting hunks, choose fewer broader commits—but never combine clearly independent features merely because they overlap.
   - Do not create one commit per file.
3. Run the repository's required checks unless they already passed after the latest change. Stop if checks or hooks fail.
4. Present the complete ordered commit map before staging anything. For every proposed commit show:
   - `Commit N`
   - `Message:` the exact single-line Conventional Commit message: `<type>(<optional-scope>): <imperative summary>`. Use no body. Prefer `feat`, `fix`, `refactor`, `test`, `docs`, or `chore`.
   - `Changes:` every path and hunk it will include, each with a concise summary.
   Every worktree change must be assigned to exactly one proposed commit or explicitly listed as excluded.
5. Wait for one approval of the complete commit map. The user may approve the entire map, revise any entry, or stop. A revision invalidates the prior proposal; present the complete revised map for approval.
6. Stage and create the approved commits in order. Stage only each commit's approved paths or hunks. Never use `git add .` when unrelated changes exist. Before each commit, verify the staged diff matches that entry in the approved map. If the worktree or grouping has changed, stop and present a complete revised map for approval.
7. Do not amend, rewrite history, bypass hooks, or push.
8. Report the commit hashes/messages, excluded changes, and whether the worktree is clean.

If the worktree has no changes, do not create an empty commit. When grouping is ambiguous, prefer several coherent feature commits over one repository-wide commit.
