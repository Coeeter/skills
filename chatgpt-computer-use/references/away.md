# Away, locked, and phone-controlled work

Checked against official OpenAI docs and the installed app on 2026-10-10.

## The remembered feature: Locked use

On macOS: **ChatGPT Settings > Computer Use > Locked use**. It is opt-in and
installs an Apple authorization plug-in. During an active trusted ChatGPT
Computer Use turn from a connected device, ChatGPT can temporarily unlock the
desktop with displays covered and local input blocked. Local input relocks it
and pauses automatic unlock until a manual unlock.

The docs explicitly restrict this to ChatGPT's trusted turns; other apps or local
processes cannot use it as a general unlock path. This skill's standalone MCP
tests do **not** establish Locked use support in T3. Preserve that limitation;
do not emulate a trusted ChatGPT turn or change the Mac's lock protections.
Windows Computer Use needs an unlocked foreground desktop.

Source: [Computer Use — Locked use](https://learn.chatgpt.com/docs/computer-use).

## Keep awake is separate

| Setting | Scope |
|---|---|
| Settings > General > **Prevent sleep while running** | Keep local work running while the user steps away. |
| Settings > Connections > Control this Mac > **Keep this Mac awake** | Keep the plugged-in host awake while remote access is enabled. |
| Codex `features.prevent_idle_sleep = true` | Experimental Codex-side setting; prevent sleep during active turns. Off by default. |

For T3's Codex process, the last setting can be useful independently of the
ChatGPT UI preferences. If the user requests it, edit the existing `[features]`
table in that provider's Codex home, preserving its other keys:

```toml
[features]
prevent_idle_sleep = true
```

Keep-awake prevents sleep; it does not authorize locked desktop access. The
setup script leaves sleep, unlock, remote access, and approval settings unchanged.

Sources: [Desktop settings](https://learn.chatgpt.com/docs/app/settings),
[Remote connections](https://learn.chatgpt.com/docs/remote-connections),
[Codex configuration](https://learn.chatgpt.com/docs/config-file/config-reference).

## Phone control

ChatGPT's supported pairing flow is **Settings > Connections > Control this Mac**.
The host needs the app running, network connectivity, and an awake machine. A
Mac laptop needs power and an open lid, or an external display for closed-lid
operation. Explicitly choosing Sleep still stops access.

That flow does not make T3-owned chats available in ChatGPT mobile. Use T3's own
remote interface to control T3, and validate runtime availability separately.
External Chrome's behavior while locked was not tested and is not established
by the native Locked use documentation.

`computer_use.allow_locked_computer_use` in managed requirements is a restriction
on enabling Locked use, not a user enablement switch. Setting it true is not a
substitute for the desktop setup flow.

Sources: [Remote connections](https://learn.chatgpt.com/docs/remote-connections),
[Managed configuration](https://learn.chatgpt.com/docs/enterprise/managed-configuration).
