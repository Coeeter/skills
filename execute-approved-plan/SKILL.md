---
name: execute-approved-plan
description: Execute an approved implementation plan with complete requirement coverage.
---

# Execute Approved Plan

Execute an approved `docs/<feature>/plan.md` continuously, commit each phase locally, and deliver the **smallest complete** solution. Reduce machinery, never acceptance coverage.

1. Invoke `writing-for-agents`; its rules govern ledger updates. Read the approved plan, linked spec, relevant `docs/context.md`, repository instructions, worktree, and ledger once at startup. Reject a draft, missing commit map, internal inconsistency, or overlapping unrelated work. Confirm completed phases against repository state. Completion: the approved route and next phase are trustworthy without a chat-only assumption.
2. Execute phases in order without approval pauses. Work on one phase only; make routine file-level decisions that preserve its outcome, then run its listed validation. Focused checks protect local behavior. Run integration, browser, E2E, or production-equivalent checks only at the phase whose validation tier requires that boundary. Completion: the phase outcome and mapped requirements have the planned evidence.
3. Triage validation failures against the current diff. Fix failures caused by the phase. When a broad check exposes unrelated breakage, record it and continue if it does not invalidate the phase evidence; ask before repairing unrelated infrastructure. A required boundary that cannot produce credible evidence is a blocker. Completion: failures are classified without turning execution into unrelated repair work.
4. At the phase boundary, update only its status, requirement IDs, concise evidence, deviations, blockers, and next phase. For the final phase, first run final validation and reconcile spec requirement → phase → diff → evidence once; mark the ledger `Complete` only when every requirement is covered, otherwise record `Partial` or `Blocked` and each gap. Stage the complete phase normally, verify the staged diff matches the approved outcome, and commit with the plan's exact message. Do not start the next phase until the commit succeeds and the worktree contains only known unrelated changes. Expected surfaces are guidance: routine adjacent implementation or test files are allowed when the outcome and message remain accurate. Completion: the phase is a coherent local commit and the ledger is resumable.
5. After the final commit, verify the commit sequence and worktree, then report outcomes, evidence, commits, and every remaining uncertainty. Do not repeat validation that already passed. Completion: the repository and durable documents tell the full truth without conversation context.

Stop and ask only when repository reality requires a material product, UX, scope, architecture, data, security, cost, destructive, or irreversible decision; an approved assumption is false; required evidence is blocked; unrelated work overlaps unsafely; or a phase can no longer produce its approved outcome or commit. Explain the blocker, recommendation, and required plan change. Do not pause for routine choices, expected intermediate failures, or fresh commit approval.

Approval of the plan's complete commit map authorizes its local phase commits. This skill never pushes, deploys, performs destructive actions, expands scope, or fixes unrelated problems without separate approval.
