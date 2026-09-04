---
name: create-plan
description: Use when a substantial feature should be made portable before implementation.
disable-model-invocation: true
---

# Create Plan

Turn a feature into a portable spec and implementation plan that another agent
can understand without the original conversation.

1. Inspect repository instructions, relevant code, current behavior, docs, and
   supported commands. Resolve discoverable facts yourself.

2. Ask the user only about unresolved decisions that materially affect product
   behavior, UX, scope, public contracts, security, cost, or failure semantics.

   Use `grilling` only when meaningful ambiguity remains. Do not grill for
   routine engineering choices or facts available from the repository.

3. Create or update `docs/<feature>/spec.md` with:
   - goal and non-goals;
   - required observable behavior;
   - important invariants;
   - meaningful edge and failure cases;
   - explicit product decisions;
   - examples where they remove ambiguity.

   Keep implementation details out of the spec.

4. Create or update `docs/<feature>/plan.md` with:
   - the simplest complete implementation approach;
   - relevant repository surfaces;
   - important architectural constraints;
   - meaningful stages only when sequencing matters;
   - simple, real validation for important behavior;
   - current status, blockers, and remaining work.

   Prefer the smallest realistic validation that proves the feature:
   - UI -> exercise it in a real browser using browser control;
   - backend or CLI -> run the real flow end to end locally;
   - container -> build and run the actual container;
   - API integration -> exercise the real boundary when safe;
   - persistence -> use the real persistence path.

   Do not invent mocks, test harnesses, abstractions, or complex validation when
   running the real feature is simpler and stronger evidence.

   Unit tests, type checks, lint, and CI are supporting evidence only.

5. Update global `docs/context.md` only for durable knowledge that matters beyond
   this feature. Do not duplicate the spec or plan there.

6. Present the important decisions, implementation direction, and validation
   strategy. Mark the plan approved only after the user approves the direction.

The result must remain useful across agents, models, sessions, and time.

Approval authorizes implementation only. It does not authorize commits, pushes,
deployment, destructive actions, or unrelated work.

This skill plans; it does not implement.
