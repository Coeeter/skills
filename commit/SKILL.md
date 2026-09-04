---
name: commit
description: Use when asked to commit current changes locally.
disable-model-invocation: true
---

# Commit

Prepare local commits for the current worktree. Never push.

**Invoking this skill does not authorize committing.**
First propose the commit list, then STOP. Commit only after the user explicitly
approves it in a later message.

1. Inspect repository instructions, branch, status, complete diff, and recent
   commit style.

2. Treat all current changes as intended unless something is clearly accidental,
   unsafe, generated junk, or secret-bearing.

3. Group changes into the smallest reasonable number of coherent commits.
   Prefer one commit for one overall feature, fix, or refactor. Split only
   clearly independent work.

4. Check for credible validation. Unit tests, lint, types, and CI are supporting
   evidence only; substantial runtime behavior should have real-boundary
   validation when practical.

5. Propose the ordered commit list using exact **single-line Conventional Commit
   messages**.

6. **STOP. Do not stage or commit. Wait for explicit user approval.**

7. After approval, stage the approved changes, verify the staged diff, and
   commit.

   Commit messages MUST:
   - be exactly one line;
   - use `<type>(<optional-scope>): <summary>`;
   - contain no body, description, heredoc, newline, or additional paragraphs.

   Use `git commit -m "<message>"` or the repository's equivalent one-line
   commit command.

8. Never push, force-push, amend, rewrite history, or bypass hooks.

9. Report the created commit hashes/messages and whether the worktree is clean.
