---
name: execute-approved-plan
description: Implement an agreed plan or specification with complete requirement coverage.
---

# Execute Approved Plan

Deliver the **smallest complete** solution: reduce machinery, never acceptance coverage.

1. Convert the agreed plan into numbered acceptance requirements. A local one-behavior change needs one requirement; add structure only as scope or risk demands. Record explicit non-goals. Completion: every agreed outcome is represented once.
2. Inspect the current implementation and map each requirement to affected surfaces before editing. Preserve unrelated work. Completion: every requirement has a plausible implementation and verification surface.
3. Implement proportionally. Prefer direct code for local behavior and independently verifiable units for cross-boundary work. Extra abstractions earn their place through a requirement, hard constraint, observed blocker, or explicit authorization. Completion: every acceptance requirement is implemented without speculative machinery.
4. Verify at the nearest real behavior boundary. Compilation proves compilation; use integration, browser, CLI, persisted-data, or production-equivalent evidence when the requirement crosses that boundary. Completion: fresh evidence covers every acceptance requirement, or the uncovered requirement is identified.
5. Reconcile requirement → diff → evidence before claiming completion. Report `complete`, `partial`, or `blocked`; name every gap. Completion: every requirement maps to both changed behavior and evidence, or is explicitly unresolved.

Respect repository verification commands and approval gates. This skill never authorizes commits, pushes, destructive actions, deployments, or unrelated fixes.
