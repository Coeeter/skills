---
name: execute-approved-plan
description: Use when implementing a feature from its approved portable plan.
disable-model-invocation: true
---

# Execute Approved Plan

Implement an approved feature continuously and keep its plan resumable without
the original conversation.

1. Read the approved spec and plan, relevant durable context, repository
   instructions, worktree state, and affected code.

2. Implement the approved outcome using the simplest complete solution.

   Exercise engineering judgment for architecture, refactors, framework usage,
   file organization, errors, concurrency, and other reversible choices.

   Do not preserve bad architecture merely because it already exists.
   Do not pause for routine implementation decisions.

3. Use relevant project or framework skills when available.

4. Validate through the real boundary where the changed behavior can fail.

   Prefer the simplest realistic execution:
   - UI -> use the real app in a browser;
   - backend or CLI -> run the real flow end to end locally;
   - container -> build and run the actual container;
   - API integration -> exercise the real boundary when safe;
   - persistence -> use the real persistence path.

   Do not build test machinery when running the actual feature is simpler and
   stronger evidence.

   Unit tests, type checks, lint, and CI are regression evidence only. Do not
   treat them as proof that substantial runtime behavior works.

5. When real validation exposes a failure, fix the root cause and repeat that
   boundary. Record unrelated existing failures without expanding scope.

6. Keep `plan.md` resumable. After meaningful milestones or before stopping,
   record only:
   - completed work;
   - important discoveries or deviations;
   - validation performed and its result;
   - remaining work;
   - blockers.

7. Before claiming completion:
   - reconcile implementation against the spec;
   - exercise the important reachable real boundaries;
   - inspect resulting state or output;
   - run broad regression checks where useful.

8. Report the feature as `Complete`, `Partial`, or `Blocked`, including any
   meaningful remaining uncertainty.

Stop and ask only when continuing requires a material change to approved product
behavior, UX, scope, public contracts, security, cost, destructive state, or
another explicit product decision.

Do not commit, push, deploy, or perform destructive actions unless separately
requested.
