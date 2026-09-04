---
name: commit
description: Use when asked to commit current changes locally.
disable-model-invocation: true
---

# Commit

Prepare and create local commits for the entire current worktree. Never push.

**Invoking this skill does not authorize creating a commit.**
First propose the commit list, then STOP. Create commits only after the user
explicitly approves that proposal in a later message.

1. Inspect repository instructions, branch, status, complete diff, and recent
   commit style.

2. Treat all current worktree changes as intended unless something is clearly
   accidental, unsafe, generated junk, or secret-bearing.

3. Group the work into the smallest reasonable number of coherent commits.
   - Prefer one commit for one overall feature, fix, or refactor.
   - Split only clearly independent changes.
   - Do not over-optimize for atomic history.

4. Check that the work has credible validation evidence.
   Unit tests, lint, types, and CI are supporting evidence only; substantial
   runtime behavior should have real-boundary validation when practical.

5. Propose a concise ordered list of exact Conventional Commit messages.

6. **STOP. Do not stage or commit yet. Wait for explicit user approval.**

7. After approval, stage the approved commits, verify each staged diff, and
   commit.

8. Never push, force-push, amend, rewrite history, or bypass hooks.

9. Report the created commits and whether the worktree is clean.
