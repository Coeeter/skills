---
name: create-plan
description: Grill and turn a feature into an approved implementation plan.
---

# Create Plan

Turn a feature into the single source of truth at `docs/<feature>/plan.md`.

1. Inspect repository instructions, relevant `docs/context.md`, current behavior, and supported commands. Invoke `grilling`; answer discoverable facts from the repository and ask Nas only for material decisions. Completion: Nas confirms the outcome, behavior, boundaries, failure behavior, and non-goals.
2. Trace the confirmed behavior through its technical surfaces and meaningful verification boundaries. Resolve technical facts from the repository or primary documentation. Recommend material tradeoffs; make routine engineering choices directly. Completion: no requirement depends on an unexamined surface or silent decision.
3. Write the plan with status `Draft`. Record each fact once and use paths and stable IDs as pointers. Include:
   - outcome, decisions, acceptance requirements, and non-goals;
   - three to six committable phases by default;
   - for each phase: requirement IDs, outcome, touchpoints, concrete changes, validation tier and commands, and exact Conventional Commit message;
   - execution state with every requirement's evidence initialized as `Pending`, plus deviations and blockers.
   Combine adjacent work when separation would require temporary fallbacks, shared-file hunk surgery, or meaningless commits. Use focused checks during implementation and reserve broad workspace, browser, E2E, or production-equivalent checks for phases that reach those boundaries. Completion: every requirement maps to a phase, evidence boundary, and local commit.
4. Present the acceptance summary and complete commit map. Incorporate requested changes and mark the plan `Approved` only after explicit approval. Approval authorizes one-shot execution and the listed local commits, not pushing, deployment, destructive actions, scope expansion, or unrelated fixes. Completion: a fresh agent can execute without conversation context or another decision unless blocked.

## Ledger contract

After approval, outcome, decisions, acceptance, non-goals, phases, validation boundaries, and commits are fixed. `execute-approved-plan` may update only phase status, evidence, deviations, blockers, and next action. Changing the fixed contract requires Nas's approval.

This skill plans but does not implement.
