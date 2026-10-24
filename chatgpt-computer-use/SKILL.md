---
name: chatgpt-computer-use
description: Use the exact installed ChatGPT Chrome and native Computer Use runtime from Codex or T3 Code, including setup and connection diagnosis. Use when the user requests Chrome use, desktop app control, or this runtime's away/locked settings.
---

# ChatGPT Computer Use

Use the locally installed OpenAI `cua_repl` runtime for Chrome and desktop apps.
This skill connects the existing implementation; it does not ship its binaries.
Supported here: macOS with ChatGPT desktop, its Computer Use runtime, and the
ChatGPT Chrome extension already installed.

## Connect

1. If an existing `cua_repl` or `chatgpt_cua` MCP server exposes `js`, use it.
   Otherwise run the bundled script using the absolute path to this skill:

   ```sh
   python3 <skill-directory>/scripts/runtime.py doctor
   python3 <skill-directory>/scripts/runtime.py setup
   ```

   `setup` registers the exact installed runtime as `chatgpt_cua` in
   `${CODEX_HOME:-~/.codex}/config.toml`, preserves unrelated configuration, and
   backs up an existing file. Python 3.11+ is required. If T3 uses a separate
   Codex home, pass `setup --codex-home /absolute/path/to/that/home`.
   `--runtime-home /absolute/path` selects where ChatGPT keeps its managed
   runtime; place that option before the subcommand. Keep the two homes distinct
   when the provider uses an isolated configuration.

2. Reload MCP configuration if the client supports it; otherwise restart T3's
   Codex provider/session. A shell command cannot add tools to an already-running
   agent's tool list. Confirm `chatgpt_cua` exposes `js` before attempting UI work.

3. Call that server's `js` tool with exactly one entry-point API operation on
   its first invocation, and read the returned API documentation. For example:

   ```javascript
   await cua.listBrowsers();
   ```

   Complete setup only when the requested surface responds to a real operation.
   A successful `tools/list` alone proves discovery, not UI access.

The client must supply Codex turn metadata and handle MCP approval requests.
The standalone probe implements those pieces for bounded tests; the direct
app-server validation supplied metadata explicitly. Validate a normal T3 agent
turn separately, including its approval handling. A raw Node import or
plain `tools/call` without them is insufficient. Use normal runtime approvals;
this skill does not grant global access or bypass app/site policy.

## Operate

- For Chrome, read [references/chrome.md](references/chrome.md).
- For native apps, read [references/computer.md](references/computer.md).
- For remote work, sleep, or a locked Mac, read
  [references/away.md](references/away.md).
- For missing tools, approval failures, or standalone validation, read
  [references/validation.md](references/validation.md).

Use the tool's current returned documentation as the API authority. Keep the
same MCP session between calls so `cua`, tab/app bindings, and observations persist.
After resetting or restoring compacted context, reacquire its documentation.
Observe after actions and verify the requested result through the UI.

If this exact runtime fails, report the actual failure. Switching to a separately
installed Playwright/Puppeteer or desktop engine requires the user's choice.
The `tab.playwright` API documented by this runtime is part of the exact OpenAI
browser integration and is appropriate to use.
