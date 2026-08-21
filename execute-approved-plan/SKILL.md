---
name: execute-approved-plan
description: Execute an approved feature plan continuously with local phase commits.
---

# Execute Approved Plan

Execute an approved `docs/<feature>/plan.md` continuously and deliver the smallest complete solution.

1. Read the approved plan, repository instructions, worktree, ledger, and code referenced by the active phase. Load other context only when a pointer or conflicting evidence requires it. Reject a draft, missing commit map, inconsistent plan, or unsafe overlap with unrelated work. Confirm inherited status against repository state. Completion: the route and next phase are trustworthy.
2. Execute phases in order without approval pauses. Work on one phase only and make routine file-level decisions that preserve its outcome. Run its listed validation; use broader boundaries only at the phase whose tier requires them. Completion: the phase outcome and mapped requirements have fresh evidence.
3. Triage validation failures against the current diff. Fix failures caused by the phase. When a broad check exposes unrelated breakage, record it and continue if it does not invalidate the phase evidence; ask before repairing unrelated infrastructure. A required boundary that cannot produce credible evidence is a blocker. Completion: failures are classified without turning execution into unrelated repair work.
4. At the phase boundary, update its status, acceptance evidence, deviations, blockers, and next action. For the final phase, first run final validation and reconcile acceptance → diff → evidence once; mark the plan `Complete`, `Partial`, or `Blocked`. Stage the complete phase normally, verify it matches the approved outcome, and commit with the exact planned message. Do not start the next phase until the commit succeeds. Routine adjacent implementation and test files are allowed when the outcome and message remain accurate. Completion: the phase is a coherent local commit and the plan is resumable.
5. After the final commit, verify the commit sequence and worktree, then report outcomes, evidence, commits, and remaining uncertainty. Do not repeat passing validation. Completion: repository state and the plan tell the full truth.

Stop and ask only when repository reality requires a material product, UX, scope, architecture, data, security, cost, destructive, or irreversible decision; an approved assumption is false; required evidence is blocked; unrelated work overlaps unsafely; or a phase can no longer produce its approved outcome or commit. Explain the blocker, recommendation, and required plan change. Do not pause for routine choices, expected intermediate failures, or fresh commit approval.

Plan approval authorizes its local phase commits. This skill never pushes, deploys, performs destructive actions, expands scope, or fixes unrelated problems without separate approval.
