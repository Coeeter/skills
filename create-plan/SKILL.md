---
name: create-plan
description: Grill and turn a feature into approved context, specification, and implementation plan artifacts.
---

# Create Plan

Turn a feature into one approved authority chain:

- global `docs/context.md` preserves shared product understanding across features and agent tasks;
- `docs/<feature>/spec.md` defines the feature's exact required behavior;
- `docs/<feature>/plan.md` defines how the repository will deliver and verify it.

Each fact has one owner. Context owns meaning and rationale; spec restates every observable promise normatively; plan points to spec IDs instead of paraphrasing behavior.

1. Inspect repository instructions, global `docs/context.md`, current behavior, and supported commands. Invoke `grilling`; answer discoverable facts from the repository. When the authority documents do not determine a choice that could change observable behavior, UX, scope, architecture, data, authorization, cost, or failure semantics, present the options and recommendation to the human and wait. Never resolve that ambiguity from convention, model preference, or likely intent. Capture concrete user journeys and examples, including details that feel visually obvious or repetitive: those are where independent agents otherwise invent different interpretations. Completion: the human confirms the actors, vocabulary, current and desired experience, boundaries, failure behavior, examples, and non-goals, with every material decision recorded.
2. Create or update the feature's named section in global `docs/context.md` and mark that section `Draft`. At product altitude, record purpose, actors and operating model, terminology, current and desired happy/non-happy journeys, invariants, explicit examples, decisions with minimum rationale, assumptions, and non-goals. Record literal UX details when their omission permits multiple reasonable implementations—for example, whether a cover appears on a starter, inside its thread, or both. Link the feature spec. Preserve unrelated feature sections and their statuses. Exclude implementation phases, file-level design, transient execution status, and cheap repository facts. Completion: a fresh implementer and reviewer form the same mental model without conversation history, and no agent can mistake the proposed section for durable authority.
3. Write `spec.md` with status `Draft`. Convert the context into stable requirement IDs and normative behavior: inputs, states, outputs, authorization, persistence, retries/idempotency, failure handling, compatibility, and acceptance scenarios. State every observable product promise explicitly with MUST/SHOULD language even when context already illustrates it; for example, “the cover MUST appear on the starter and again as page 1.” Link to context for meaning and rationale, and exclude implementation design. Completion: every desired journey and invariant is testable, and every meaningful edge or error path has an explicit expected result.
4. Trace the specification through technical surfaces and meaningful verification boundaries. Resolve repository facts and primary documentation. Recommend material tradeoffs; make routine engineering choices directly. Completion: no requirement depends on an unexamined surface or silent decision.
5. Write `plan.md` with status `Draft`. Use spec IDs as pointers and include:
   - three to six committable phases by default;
   - for each phase: requirement IDs, outcome, touchpoints, concrete changes, validation tier and commands, and exact Conventional Commit message;
   - execution state with every requirement's evidence initialized as `Pending`, plus deviations and blockers.
   Combine adjacent work when separation would require temporary fallbacks, shared-file hunk surgery, or meaningless commits. Use focused checks during implementation and reserve broad workspace, browser, E2E, or production-equivalent checks for phases that reach those boundaries. Completion: every requirement maps to a phase, evidence boundary, and local commit.
6. Reconcile global context → feature spec → feature plan, then present the product summary, acceptance requirements, and complete commit map. Incorporate requested changes and mark the feature's context section, spec, and plan `Approved` only after explicit approval; never apply one feature's status to the whole global context file. Approval authorizes one-shot execution and the listed local commits, not pushing, deployment, destructive actions, scope expansion, or unrelated fixes. Completion: an independent implementer and reviewer agree on what the feature means, what must be true, and how it will be delivered.

## Ledger contract

After approval, the feature's global-context section, requirements, phases, validation boundaries, and commits are fixed. `execute-approved-plan` may update only plan execution status, evidence, deviations, blockers, and next action. A product decision changes the feature section in global `docs/context.md`; a behavioral requirement changes `spec.md`; an implementation change updates `plan.md`. Any fixed-contract change requires Nas's approval and a reconciliation of downstream artifacts.

For an amendment, pause execution; edit the owning artifact and every affected downstream artifact; mark the affected feature context section plus its spec/plan `Draft`; present the product/requirement changes and complete revised commit map; and resume only after the human explicitly re-approves the reconciled authority chain. Chat decisions do not become durable authority until incorporated this way.

## Decision gate

Discover facts from code and authoritative sources. Preserve documented or existing behavior when the requested feature does not change it. A routine implementation choice is autonomous only when every reasonable option produces the same approved behavior and risk. Any undocumented choice with a materially different outcome belongs to the human; ask, record the answer in the owning artifact, reconcile downstream artifacts, and then continue.

This skill plans but does not implement.
