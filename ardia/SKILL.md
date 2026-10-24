---
name: ardia
description: Drive the user's Ardia browser (their default browser, with their logins). Use when a task needs a real logged-in browser, reading or acting on the page they're looking at, screenshots, scraping, running page JavaScript, or writing userscripts.
---

# Ardia

Ardia is a Chromium browser on this Mac (`/Applications/Ardia.app`, nightly channel) and the default browser.
Its data lives in `~/Library/Application Support/com.ardia.browser`.

## Pick the tool

| Need | Use |
| --- | --- |
| Read, scrape, script, screenshot or run JS on web pages | `ardia exec` (default: fast, works from any agent harness) |
| Site behaviour changed on every visit | `ardia scripts` (userscripts) |
| Visual, screenshot-and-click work across messy UIs, or `chrome://` / extension pages | Claude in Chrome (`mcp__claude-in-chrome__*`) or the ChatGPT extension. Both connect to Ardia |
| Ardia's own UI: sidebar, profiles, settings, import | Computer use on the Ardia app. `ardia exec` cannot reach it |

## `ardia exec`

Runs Python with top-level `await` against the running Ardia. The last expression is printed (`--json` for JSON).
Each run is a new process, so find your tab again by URL rather than keeping state in variables.

```sh
ardia exec 'await tab.current_url(), await tab.title()'          # the page the user is looking at
ardia exec --json '[await t.current_url() for t in tabs]'        # every web tab
ardia exec 't = await new_tab("https://example.com"); await js("document.title", tab=t)'
ardia exec -f script.py --json
```

In scope: `tab` (the user's current page, raises `NoPageTab` on New Tab), `tabs`, `new_tab(url, background=True)`,
`js(expr, tab=None)`, `await pinned()`, `await history(days=1)`, `browser`, `By`, `Key`, `asyncio`.
Element and tab methods are coroutines (`await t.query("css", timeout=10)`, `await el.click()`,
`await el.type_text("text\r")`, `await t.take_screenshot("/tmp/x.png")`). The full API is in
[references/pydoll.md](references/pydoll.md), and `ardia exec --help` has the rest.

Work in tabs you open with `new_tab` and close them with `await t.close()` when done. Read the user's `tab`; navigate
it only when they ask. Submitting forms, sending, posting, buying or deleting needs the user's go-ahead.

Exit 2 means Ardia isn't running or Settings › "Let the ardia command control Ardia" is off. `ardia exec` only reaches
http(s), `about:blank`, `data:` and `blob:` pages, and refuses cookie, storage and settings DevTools calls.

## Userscripts

`ardia scripts new NAME --match 'https://site/*'` → edit → `ardia scripts test FILE --url URL` until clean →
`ardia scripts install FILE` once the user approves. `ardia scripts list` / `uninstall NAME` manage them.

## Setup facts

- Profiles act as Arc spaces. Profiles with the same `dataId` in `session.json` share cookies, extensions, history
  and passwords, and each keeps its own tabs and pins. DEV and NUS share data; AniArt has its own.
- Claude in Chrome and the ChatGPT extension talk to their apps through native messaging manifests in
  `com.ardia.browser/Chromium/NativeMessagingHosts/`. If either says it can't connect, copy the matching
  `com.anthropic.*` or `com.openai.*` manifest from `~/Library/Application Support/Google/Chrome/NativeMessagingHosts/`.
- Ardia rewrites `session.json` and each profile's `Preferences` while running. Edit them only with Ardia quit,
  and back them up first.
- Bitwarden is the password manager. Ardia's own password saving is off in every profile.
