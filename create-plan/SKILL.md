---
name: create-plan
description: Turn an approved feature spec into an implementation plan.
---

# Create Plan

Turn `docs/<feature>/spec.md` into an approved, agent-neutral implementation route at `docs/<feature>/plan.md`. The spec owns intent; the plan owns implementation and execution state.

1. Invoke `writing-for-agents`; its rules govern the plan. Read the approved spec, relevant `docs/context.md`, repository instructions, and the current implementation. If the spec is not approved or has unresolved product decisions that affect implementation, return it to `create-spec` rather than guessing. Completion: every spec requirement is understood against current code.
2. Trace each requirement through its affected surfaces and real verification boundary. Resolve technical facts from the repository or primary documentation. Put meaningful implementation tradeoffs to the user with a recommendation; make routine engineering choices directly. Completion: no requirement depends on an unexamined surface or silent product decision.
3. Write `docs/<feature>/plan.md` with status `Draft` and:
   - the repository-relative spec path and requirement mapping;
   - the chosen approach and important rejected alternatives;
   - three to six numbered phases by default, each a meaningful, committable working slice;
   - within each phase, the requirements covered, outcome, expected surfaces, concrete changes, validation commands, validation tier (`Focused`, `Integration`, or `Final`), and exact Conventional Commit message;
   - risks, migration or rollout needs, explicit non-goals, and a compact execution-state section initialized as `Not started`.
   Combine adjacent work when splitting it would require temporary fallbacks, shared-file hunk surgery, or commits that are not independently understandable. Use focused checks during implementation; reserve broad workspace, browser, E2E, and production-equivalent checks for the few phases that reach those boundaries. Prefer the smallest complete design. Completion: every requirement maps to a phase, evidence boundary, and local commit.
4. Present unresolved choices, the plan summary, and the complete ordered commit map. State that approval authorizes one-shot execution and the listed local commits, but not pushing, deployment, destructive actions, material scope changes, or unrelated fixes. Incorporate requested changes and mark the plan `Approved` only after explicit approval. Completion: a fresh agent can execute and commit the plan without another decision unless blocked.

## Ledger contract

The plan becomes a ledger only after approval. `execute-approved-plan` updates it at commit boundaries with phase status, requirement IDs covered, concise evidence, deviations, blockers, and the next phase. Keep approved intent and execution records separate. Change requirements, approach, validation boundaries, or commit outcomes only through an explicit plan revision approved by the user.

This skill plans but does not implement. Plan approval authorizes only the local commits listed in its commit map. It does not authorize pushes, deployments, destructive actions, material scope changes, or unrelated fixes.
