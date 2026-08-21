---
name: create-spec
description: Define and stress-test a feature before implementation.
---

# Create Spec

Turn an idea into an approved, agent-neutral statement of **what** must change and why. The output is `docs/<feature>/spec.md`; implementation choices belong in the plan.

1. Invoke `writing-for-agents`; its rules govern every document this skill creates or edits. Resolve `<feature>` to a short stable kebab-case name. Inspect the repository for facts that shape the feature, including existing behavior, constraints, and relevant `docs/context.md`. Completion: questions for the user contain decisions, not facts the repository can answer.
2. Invoke `grilling` on the feature. Carry repository facts into the design tree and settle goals, users, behavior, boundaries, failure behavior, acceptance outcomes, and non-goals. Do not write the spec while decisions remain open. Completion: the user confirms shared understanding and the grilling frontier is empty.
3. Write `docs/<feature>/spec.md` with status `Draft` as the source of truth for product intent. Include:
   - problem and desired outcome;
   - stable requirement IDs stated as observable behavior;
   - scope and non-goals;
   - constraints and invariants;
   - key decisions and rationale needed to preserve intent;
   - unresolved questions, if the user deliberately defers any.
   Keep architecture, file lists, task breakdowns, chat history, and code sketches out of the spec unless they are themselves user requirements. Use repository-relative references. Completion: every settled decision appears once, and every requirement is testable or has an explicit acceptance observation.
4. Reconcile the written spec against the completed design tree, then show the user the path and a concise requirement summary. Wait for approval; incorporate requested changes and mark the spec `Approved` only after explicit approval. Completion: a fresh agent with only the repository and spec can recover the approved intent without knowing the model, thread, or conversation that produced it.

## Durable project context

Use `docs/context.md` only for confirmed project-wide knowledge that should govern multiple features: enduring product rules, architectural invariants, external quirks, or recurring workflow constraints. Keep each item decision-rich and point to its deeper source when one exists. Feature decisions stay in the feature spec; transient status, conversation summaries, and facts cheaply discoverable from the repository stay out.

When the session reveals new durable context, propose the exact addition and update it only with user approval. For ordinary tasks to load this context, the repository needs a concise pointer in its governing `AGENTS.md`; creating the file alone does not make it ambient.

This skill produces documentation. It does not implement the feature or authorize commits, pushes, deployments, destructive actions, or unrelated changes.
