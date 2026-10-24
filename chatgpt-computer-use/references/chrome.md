# Chrome through the OpenAI runtime

Keep Chrome running in the profile with the ChatGPT extension. Keep ChatGPT
desktop running initially; operation with it fully quit has not been validated.

Use these as first-call entry points, one operation per initial call:

```javascript
// Open a new task tab in the user's Chrome, not the built-in browser.
var tab = await cua.createBrowserTab("chrome", "http://localhost:3000", {
  sessionName: "🔎 UI check"
});
```

```javascript
// Bind a specific existing URL when the user asks to work in that tab.
var tab = await cua.getTab({url: "http://localhost:3000"}, {browser: "chrome"});
```

```javascript
// Discover profiles when the intended one is unclear.
await cua.listBrowsers();
```

Read the returned documentation before following up. URL lookup must match
exactly one tab; resolve ambiguity using observed IDs. For a tab mention, pass
the entire `plugin://…` reference to `cua.getTab({mention: reference})`.

Typical follow-ups, when present in the returned API:

```javascript
await tab.getAXState();
await tab.getScreenshot();
```

Chrome's DOM interface is exposed through the runtime's own `playwright` member:

```javascript
nodeRepl.write(await tab.playwright.domSnapshot());
```

```javascript
await tab.playwright.getByRole("button", {name: "Save", exact: true}).click();
nodeRepl.write(await tab.playwright.domSnapshot());
```

Use observed roles/names or fresh AX indices. Native tab input may be unavailable
on DOM-only surfaces; use the documented locators there. `evaluate` is a read-only
page scope, not a replacement for interacting with controls. Only close tabs
created for disposable work; preserve tabs the user wants to keep.

`"iab"` selects ChatGPT's built-in browser and is a distinct surface. It is not
the requested Chrome extension integration. Chrome was validated here as
`type: "extension"`, using the existing running Chrome profile.
