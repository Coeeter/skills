---
name: second-opinion
description: Use when another coding model should independently advise or review current work.
disable-model-invocation: true
---

# Second Opinion

Ask another local coding model for one independent read-only opinion. The current
agent remains responsible for decisions, implementation, and validation.

1. Choose the advisor.
   - Use the model/provider requested by the user.
   - Otherwise prefer a different provider from the current agent.

2. Give it a concise cold-reader prompt with only what it needs:
   - objective;
   - relevant spec/plan paths;
   - question or review scope;
   - important constraints;
   - relevant validation evidence.

3. Invoke the local CLI read-only from the repository root.
   - Claude -> non-interactive with read-only/plan tools.
   - Codex -> ephemeral read-only sandbox.

   The advisor must not edit, commit, push, deploy, or perform destructive actions.

4. Use the mode implied by the user's request:

   **Advice**
   Ask one bounded technical or design question.

   **Review**
   Review the implementation against its spec and intended behavior. Require
   concrete findings with file locations, impact, evidence, and recommended
   fixes. Separate actual bugs from optional hardening.

5. Treat the response as evidence, not authority.

   Verify important claims against the repository and reject false positives.
   The current agent owns any resulting implementation or validation.

Make exactly one advisor call per invocation. A further opinion or review
requires the user to invoke this skill again.

Do not commit or push.
