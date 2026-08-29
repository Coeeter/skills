---
name: review-fix-loop
description: Run a parent implementation task through a dedicated read-only reviewer until the committed range passes.
---

# Review Fix Loop

Use the current task as the **parent**: it owns decisions, edits, validation, and commits. Create one separate Codex task as the **reviewer** and reuse it for the whole loop.

1. Pin the review handoff. Resolve the repository project, immutable **original base**, latest end commit, approved feature section in global `docs/context.md`, and approved feature spec/plan paths at that end commit, plus validation evidence and prohibited actions. For a legacy plan-only feature, use applicable durable global context for product meaning and the plan as combined requirement/implementation authority; do not invent a missing spec. Incorporate every later behavior-changing user decision into the owning artifact and obtain approval before review; chat-only or draft decisions are not reviewer authority. Resolve the current parent task ID when the app exposes it; otherwise plan to collect the review with the task wait/read tools. Start only from a clean committed range. Completion: both commits and authority artifacts resolve from the end commit, and the brief can be understood without parent-task history.
2. Create a new project task with no forked conversation history, model `gpt-5.6-sol`, and reasoning effort `low`. Start it from the parent's committed working-tree state when supported; otherwise use the saved project checkout and require commit-object review. This is the reviewer task; record its ID. Its cold-reader prompt must:
   - name the parent task ID when available and always name the exact commit range;
   - make the reviewer read-only: inspect files and commit objects; run only repository commands verified not to mutate tracked/untracked files, databases, services, or external state; report skipped validation;
   - require one consolidated pass over the full range and surrounding contracts, reading authority artifacts from the named end commit; use global context for product meaning, feature spec for required behavior, and plan for implementation, while a legacy plan owns requirements and implementation; include normal flows, state transitions, authorization, persistence, retries, failures, and realistic non-happy paths;
   - prioritize reproducible product bugs for the stated team and threat model, with rare adversarial hardening separated from release-blocking findings;
   - require severity, exact file and line, evidence or reproduction, impact, recommended fix, and explicit validation gaps;
   - direct the reviewer to send its complete result to the parent task when its ID is available; otherwise the parent retrieves the result with the task wait/read tools.
   Completion: the reviewer task ID is recorded and `git cat-file -e <end>^{commit}` succeeds in its checkout. If HEAD differs, it reviews the named commit objects and reports any validation that cannot run against them.
3. Wait for the reviewer rather than editing concurrently. Treat each report as evidence: reproduce or verify every load-bearing claim against the repository and reject false positives. When authority documents and preserved existing behavior do not determine a materially different outcome, classify it as a decision rather than a bug and ask the human. Incorporate the answer into global context/spec/plan through the approval flow before implementation. Completion: every reported item is classified as confirmed bug, hardening, false positive, or human decision.
4. Fix every confirmed bug in the parent task, then continue auditing the affected lifecycle for sibling failures before stopping. Preserve scope and unrelated work. Run focused checks while iterating and the repository's required full validation once the batch is complete. Commit under the repository's current authorization. When no commit authorization exists, present the complete commit map and pause for approval; this pause is neither PASS nor a blocker, and re-review resumes only after an approved commit produces a new end SHA. Completion: all confirmed findings are fixed in one coherent batch, validation passes, and the worktree is clean.
5. Send the same reviewer task the cumulative `original-base..latest-end` range plus the incremental `previous-end..latest-end` fix context and concise evidence handoff. Require a fresh whole-flow pass over the cumulative feature and surrounding contracts, not only a check that named lines changed. Inspect commit objects if its checkout is behind. Completion: the reviewer returns one consolidated result:
   - **PASS** only when the cumulative range has zero confirmed in-scope bugs;
   - **FINDINGS** with the complete confirmed inventory; or
   - **INCOMPLETE** when a load-bearing path could not be inspected or validated.
   Hardening notes and non-material validation gaps remain separate and do not silently change PASS.
6. Repeat steps 3–5 while confirmed in-scope bugs remain. Stop on PASS, a material human decision, failed validation, INCOMPLETE review, or a genuine external blocker. Report the final cumulative range, commits, validation, remaining hardening notes, and mandatory reviewer task ID; include the parent task link/ID only when available.

## Review calibration

- **Actual bug:** reproducible through the product, supported API, realistic stale/retry path, or a plausible mistake by the small trusted team. Fix it.
- **Hardening:** requires a malicious trusted operator, corrupted historical state, extraordinary concurrency, or unsupported direct calls. Record it separately and fix only when cheap, requested, or materially protective.
- A concurrency issue may still be actual with one user when uploads, jobs, retries, or browser requests overlap. Tie severity to likelihood and impact rather than theoretical reachability.
- Search broadly before reporting. The reviewer's first response should be its best complete inventory, not the first defect it notices.
- The reviewer derives expected behavior only from pinned authority and preserved existing contracts. Ambiguity becomes a decision request with options and a recommendation, never an inferred finding.
- The reviewer never becomes the implementer. Keeping the roles separate preserves independent verification and prevents two tasks from editing one checkout.
