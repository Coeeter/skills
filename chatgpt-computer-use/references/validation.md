# Validate and diagnose

Run the script from a scratch directory. It connects to the installed runtime
as a separate MCP client, not through the current ChatGPT conversation.
Choose a private output directory; observations and screenshots are saved there.

```sh
python3 <skill-directory>/scripts/runtime.py probe handshake --output <scratch>/handshake
python3 <skill-directory>/scripts/runtime.py --surfaces browser probe chrome --approve-test-targets --output <scratch>/chrome
python3 <skill-directory>/scripts/runtime.py --surfaces computer probe computer --approve-test-targets --exercise-input --output <scratch>/computer
```

`--approve-test-targets` authorizes only the probe's newly generated loopback
origin and low-risk Calculator operations, for that probe session. All other
approval requests fail with `pending-request.json` for inspection. It neither
accepts credentials nor requests persistent global approval. For a normal task,
use the MCP client's human approval handling instead of the test harness.

Chrome validation creates a local page in a new extension-controlled Chrome tab,
clicks its button, checks the changed DOM, captures an inline screenshot, and
closes that disposable tab. Native validation toggles and restores Calculator's
sidebar. Opening Calculator can leave it running if it was closed beforehand.

## Sandbox boundary

The OpenAI REPL launches its own macOS sandbox. Wrapping `probe chrome/computer`
in `codex sandbox` failed with `sandbox_apply: Operation not permitted` because
Seatbelt sandboxes cannot be nested this way. Run the standalone MCP client
normally and retain the runtime's own sandbox. An outer sandbox successfully
validated the handshake only. No sandbox or native permission was disabled.

The setup script can be tested without changing live configuration:

```sh
python3 <skill-directory>/scripts/runtime.py setup --codex-home <scratch>/codex-home
CODEX_HOME=<scratch>/codex-home codex mcp list
```

The setup also passed strict configuration loading through a fresh Codex
app-server with an ephemeral thread. That app-server discovered the server and
successfully called `js` to enumerate the real Chrome extension backend.
That direct API test explicitly supplied turn metadata. It does not prove T3's
normal agent tool calls and approval UI handle every required protocol detail.
An end-to-end T3 conversation and operation with ChatGPT quit remain separate
tests; do not claim they passed based on the standalone probe.

## Concrete failures

| Failure | Next step |
|---|---|
| Runtime manifest or executable missing | Install/enable Computer Use in ChatGPT, then rerun `doctor`. |
| Tools still absent after setup | Check T3's actual Codex home and restart/reload its provider. |
| Missing required Codex turn metadata | Use Codex's MCP tool call path; a custom MCP client needs its own `x-codex-turn-metadata` with session and turn IDs. |
| Client does not support form elicitation | Use a client that implements MCP approval requests; listing tools is not enough. |
| Site or app approval denied | Report the denial and let the user decide the relevant permission. |
| Kernel exited with `sandbox_apply` | Avoid nesting the runtime inside another Seatbelt sandbox; retain its internal sandbox. |
| Path stale after a ChatGPT update | Rerun setup to refresh paths from the latest installed manifest. |

`runtime.py serve` starts the same MCP stdio implementation for a different
client. Preserve a single connection for a task and handle cleanup. A skill
does not supply client-side elicitation support or ChatGPT trusted-turn status.
