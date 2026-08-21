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
   - numbered implementation phases, split only at independently verifiable boundaries;
   - within each phase, the spec requirements covered, affected surfaces, concrete changes, and verification evidence required;
   - risks, migration or rollout needs, explicit non-goals, and a compact execution-state section initialized as `Not started`.
   Prefer the smallest complete design. Additional machinery must be justified by a requirement, constraint, observed blocker, or approved tradeoff. Completion: every spec requirement maps to at least one phase and one verification boundary.
4. Reconcile spec requirement → plan phase → expected evidence. Present unresolved choices and a concise plan summary, then wait for approval. Incorporate requested changes and mark the plan `Approved` only after explicit approval. Completion: a fresh agent with only the repository, spec, and plan can begin execution without knowing the model, thread, or conversation that produced them.

## Ledger contract

The plan becomes a ledger only after approval. `execute-approved-plan` owns its execution-state updates. Keep approved intent and execution records separate: update current phase, phase status, requirement coverage, changed surfaces, concise verification results, deviations, blockers, and next action. Change requirements or approach only through an explicit plan revision approved by the user.

This skill plans but does not implement. It does not authorize commits, pushes, deployments, destructive actions, or unrelated changes.
