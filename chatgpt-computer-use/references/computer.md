# Native apps through the OpenAI runtime

On macOS the installed Codex Computer Use helper needs Screen Recording and
Accessibility permission. App approvals are separate. Treat an OS permission
prompt or app denial as a concrete access issue, not an invitation to replace
the runtime.

First call, with exactly one operation:

```javascript
var app = await cua.getApp("Calculator");
```

The result includes documentation and the initial app state. You can also select
an app by its observed bundle identifier or path. If several windows are open,
choose the window relevant to the user's task.

Follow-ups:

```javascript
await app.getAXState();
await app.getScreenshot();
```

```javascript
await app.click(42); // Replace with an index from the current observation.
await app.getAXState();
```

```javascript
await app.pressKey("Return");
await app.getAXState();
```

Use fresh observed indices or screenshot-relative coordinates. A new observation
can change indices. `getApp`, state, and screenshot methods emit their own
results; avoid wrapping them in `nodeRepl.write` or emitting their image again.
Use `nodeRepl.write` for additional text and `nodeRepl.emitImage` for other images
when documented.

For long-running multi-agent work, assign clear app/window ownership. Reusing one
desktop is not the same as giving each agent an isolated computer. The helper
can operate many Mac apps in the background, but validate the actual target app.

The standalone test opened Calculator, toggled its sidebar, verified changed AX
state, restored the exact initial AX state, and received an inline screenshot.
It did not replace the user's current calculation.
