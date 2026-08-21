---
name: execute-approved-plan
description: Execute an approved implementation plan with complete requirement coverage.
---

# Execute Approved Plan

Execute `docs/<feature>/plan.md` as a portable live ledger and deliver the **smallest complete** solution: reduce machinery, never acceptance coverage. If no durable plan exists, use the agreed plan already provided; persist it first when execution may outlive the current context.

1. Invoke `writing-for-agents`; its rules govern every ledger update. Read the approved plan, its linked spec, relevant `docs/context.md`, repository instructions, current worktree, and existing execution state. Reject a draft or internally inconsistent plan. Completion: every approved outcome and already-completed phase is accounted for without a chat-only assumption.
2. Reinspect the current implementation before editing. Confirm each phase's affected surfaces and note drift from the plan. Stop for approval when drift changes product behavior, scope, architecture, or a material tradeoff; adapt routine file-level details directly. Completion: the next phase remains a valid smallest-complete route.
3. Implement one independently verifiable phase at a time. Prefer direct code for local behavior and independently verifiable units for cross-boundary work. Extra abstractions earn their place through a requirement, hard constraint, observed blocker, or approved tradeoff. Preserve unrelated work. Completion: the phase's mapped requirements are implemented without speculative machinery.
4. Verify the phase at its nearest real behavior boundary. Compilation proves compilation; use integration, browser, CLI, persisted-data, or production-equivalent evidence when the requirement crosses that boundary. Completion: fresh evidence covers the phase, or the exact gap is known.
5. Update the plan ledger after each phase with current phase, phase status, requirement coverage, changed surfaces, concise command or behavior evidence, deviations, blockers, and the exact next action. Record durable facts and outcomes, not reasoning traces or conversation summaries. Confirm the ledger against the worktree before trusting inherited status. Completion: a fresh agent or thread can resume using only repository state and the documents, regardless of model or reasoning level.
6. Before claiming completion, reconcile spec requirement → plan phase → diff → evidence. Mark the plan `Complete` only when all requirements have fresh evidence; otherwise record `Partial` or `Blocked` and every gap. Completion: every requirement maps to changed behavior and fresh evidence, or is explicitly unresolved.

Respect repository verification commands and approval gates. This skill never authorizes commits, pushes, destructive actions, deployments, or unrelated fixes.
