---
name: commit
description: Use when asked to commit current changes locally.
disable-model-invocation: true
---

# Commit

Commit the entire current worktree locally. Never push.

1. Inspect the repository instructions, branch, status, complete diff, and recent
   commit style.

2. Treat all current worktree changes as intended for this commit operation
   unless something is clearly accidental, unsafe, generated junk, or secret-bearing.

3. Group the work into the smallest reasonable number of coherent commits.
   - Prefer one commit when the accumulated work represents one overall feature,
     fix, or refactor.
   - Split only when there are clearly independent changes that would make sense
     to review or revert separately.
   - Do not create one commit per file, phase, test, or minor concern.
   - Do not over-optimize for perfectly atomic history.

4. Check that the work has credible validation evidence.
   - Unit tests, lint, type checks, and CI are supporting evidence only.
   - Substantial runtime behavior should have been exercised through the real
     boundary where it can fail when practical.
   - Do not create mocked tests merely to justify committing.

5. Propose the concise ordered commit list with exact Conventional Commit
   messages. Keep the explanation short.

6. Wait for the user to approve the commit list.

7. Stage all worktree changes into the approved commits.
   Use hunk-level staging only when needed to separate genuinely independent
   changes.

8. Verify each staged diff, then commit.

9. Never push, force-push, amend, rewrite history, or bypass hooks.

10. Report the created commit hashes/messages and whether the worktree is clean.
