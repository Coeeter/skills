#!/usr/bin/env python3
"""Expose the installed ChatGPT CUA runtime; no copied OpenAI implementation."""

import argparse
import base64
import datetime
import http.server
import json
import os
from pathlib import Path
import queue
import re
import signal
import subprocess
import sys
import threading
import time
import tomllib
import uuid


SERVER_NAME = "chatgpt_cua"
BEGIN = "# BEGIN chatgpt-computer-use managed MCP\n"
END = "# END chatgpt-computer-use managed MCP\n"


def runtime_config(runtime_home, surfaces):
    root = runtime_home / "plugins/cache/openai-bundled/unified-computer-use"
    manifests = list(root.glob("*/.mcp.json"))
    if not manifests:
        raise RuntimeError("Install/enable Computer Use in ChatGPT desktop first; its unified runtime manifest is missing.")
    manifest = max(manifests, key=lambda p: p.stat().st_mtime_ns)
    config = json.loads(manifest.read_text())["mcpServers"]["cua_repl"]
    env = config.get("env", {}).copy()
    env["CUA_REPL_ENABLED_SURFACES"] = surfaces
    config = {
        "command": config["command"],
        "args": config.get("args", []),
        "env": env,
        "startup_timeout_sec": 120,
        "tool_timeout_sec": 180,
    }
    for label, path in [("Node", config["command"]), ("CUA launcher", config["args"][0]),
                        ("Node REPL", env.get("CUA_REPL_NODE_REPL_PATH", ""))]:
        if not path or not Path(path).is_file():
            raise RuntimeError(f"{label} is missing: {path}. Reopen/update ChatGPT to refresh its bundled runtime.")
    return manifest, config


def setup(args, manifest, config):
    home = args.codex_home.expanduser().resolve()
    # T3 shadow homes symlink this file; atomic replacement must target the source.
    path = (home / "config.toml").resolve()
    existing = path.read_text() if path.exists() else ""
    parsed = tomllib.loads(existing)
    if SERVER_NAME in parsed.get("mcp_servers", {}) and BEGIN not in existing:
        raise RuntimeError(f"{path} already defines {SERVER_NAME} outside this script's managed block; leaving it unchanged.")
    if existing.count(BEGIN) != existing.count(END) or existing.count(BEGIN) > 1:
        raise RuntimeError("Invalid managed-block markers; leaving configuration unchanged.")
    if BEGIN in existing:
        start = existing.index(BEGIN)
        stop = existing.index(END, start) + len(END)
        existing = existing[:start] + existing[stop:]
    q = lambda value: json.dumps(value, ensure_ascii=False)
    block = BEGIN + f"[mcp_servers.{SERVER_NAME}]\n"
    for key in ("command", "args", "startup_timeout_sec", "tool_timeout_sec"):
        block += f"{key} = {q(config[key])}\n"
    block += f"\n[mcp_servers.{SERVER_NAME}.env]\n"
    for key, value in config["env"].items():
        block += f"{q(key)} = {q(value)}\n"
    updated = existing.rstrip() + ("\n\n" if existing.strip() else "") + block + END
    tomllib.loads(updated)
    if path.exists() and path.read_text() == updated:
        print(f"Already configured: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        backup = path.with_name(f"config.toml.before-chatgpt-cua.{stamp}")
        backup.write_text(path.read_text())
        backup.chmod(0o600)
        print(f"Backup: {backup}")
    temporary = path.with_name(f".config.toml.chatgpt-cua.{os.getpid()}")
    try:
        temporary.write_text(updated)
        temporary.chmod(0o600)
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)
    print(f"Configured {SERVER_NAME} in {path}")
    print(f"Source runtime: {manifest}")
    print("Restart the T3 Codex provider/session, then use its chatgpt_cua js tool.")


def serve(config):
    env = os.environ.copy()
    env.update(config["env"])
    os.execve(config["command"], [config["command"], *config["args"]], env)


class McpClient:
    def __init__(self, config, output, approve_test_targets=False):
        env = os.environ.copy()
        env.update(config["env"])
        self.process = subprocess.Popen(
            [config["command"], *config["args"]], env=env, stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, start_new_session=True,
        )
        self.messages = queue.Queue()
        self.sequence = 0
        self.output = output
        self.output.mkdir(parents=True, exist_ok=True, mode=0o700)
        self.records = []
        self.image_count = 0
        self.session_id = str(uuid.uuid4())
        self.turn_id = str(uuid.uuid4())
        self.approve_test_targets = approve_test_targets
        self.fixture_origin = None
        threading.Thread(target=self.read, daemon=True).start()

    def read(self):
        try:
            for line in self.process.stdout:
                try:
                    self.messages.put(json.loads(line))
                except ValueError:
                    continue
        finally:
            self.messages.put(None)

    def send(self, message):
        self.process.stdin.write(json.dumps(message) + "\n")
        self.process.stdin.flush()

    def request(self, method, params, timeout=60):
        self.sequence += 1
        request_id = self.sequence
        self.send({"jsonrpc": "2.0", "id": request_id, "method": method, "params": params})
        deadline = time.monotonic() + timeout
        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise RuntimeError(f"{method} timed out after {timeout}s. Check ChatGPT approval prompts and backend availability.")
            try:
                message = self.messages.get(timeout=remaining)
            except queue.Empty:
                raise RuntimeError(f"{method} timed out after {timeout}s.") from None
            if message is None:
                raise RuntimeError(f"MCP runtime exited ({self.process.poll()}).")
            if "method" in message and "id" in message:
                (self.output / "pending-request.json").write_text(json.dumps(message, indent=2))
                params = message.get("params", {})
                meta = params.get("_meta", {})
                target = meta.get("tool_params", {})
                calculator = (meta.get("connector_id") == "computer-use"
                              and target.get("app") == "com.apple.calculator"
                              and meta.get("riskLevel") == "low")
                fixture = (self.fixture_origin is not None
                           and meta.get("connector_id") == "browser-use"
                           and meta.get("tool_name") == "access_browser_origin"
                           and target.get("origin") == self.fixture_origin)
                if (self.approve_test_targets and message["method"] == "elicitation/create"
                        and params.get("mode") == "form" and (calculator or fixture)
                        and not params.get("requestedSchema", {}).get("properties")):
                    self.send({"jsonrpc": "2.0", "id": message["id"], "result": {
                        "action": "accept", "content": {}, "_meta": {"persist": "session"}}})
                    print("Approved scoped test target for this session.", flush=True)
                    continue
                self.send({"jsonrpc": "2.0", "id": message["id"], "error": {
                    "code": -32601, "message": "This probe cannot approve requests; use an interactive MCP client."}})
                raise RuntimeError(f"Runtime requested {message['method']}; approval must be handled in the interactive client.")
            if message.get("id") == request_id:
                if "error" in message:
                    raise RuntimeError(str(message["error"]))
                return message["result"]

    def initialize(self):
        result = self.request("initialize", {
            "protocolVersion": "2025-06-18", "capabilities": {"elicitation": {"form": {}}},
            "clientInfo": {"name": "chatgpt-cua-standalone-probe", "version": "1"},
        })
        self.send({"jsonrpc": "2.0", "method": "notifications/initialized"})
        tools = self.request("tools/list", {}).get("tools", [])
        if not any(tool["name"] == "js" for tool in tools):
            raise RuntimeError("The runtime did not expose js.")
        (self.output / "tool-schema.json").write_text(json.dumps(tools, indent=2))
        print("MCP initialized; js exposed.", flush=True)
        return result

    def js(self, code, label, timeout=60):
        result = self.request("tools/call", {"name": "js", "arguments": {
            "code": code, "title": label, "timeout_ms": timeout * 1000,
        }, "_meta": {"x-codex-turn-metadata": {
            "session_id": self.session_id, "turn_id": self.turn_id,
            "call_id": str(uuid.uuid4()),
        }}}, timeout=timeout + 5)
        texts = []
        for item in result.get("content", []):
            if item.get("type") == "text":
                texts.append(item.get("text", ""))
            elif item.get("type") == "image":
                self.image_count += 1
                suffix = {"image/png": ".png", "image/jpeg": ".jpg", "image/webp": ".webp"}.get(item.get("mimeType"), ".image")
                (self.output / f"observation-{self.image_count}{suffix}").write_bytes(base64.b64decode(item["data"]))
        text = "\n".join(texts)
        self.records.append({"label": label, "code": code, "text": text, "isError": result.get("isError", False)})
        (self.output / "observations.json").write_text(json.dumps(self.records, indent=2))
        if result.get("isError"):
            raise RuntimeError(text.split("\n## ", 1)[0].strip())
        print(f"{label}: completed", flush=True)
        return text

    def close(self):
        try:
            self.request("tools/call", {"name": "turn_ended", "arguments": {
                "hook_event_name": "Stop", "session_id": self.session_id, "turn_id": self.turn_id,
            }}, timeout=3)
        except (RuntimeError, BrokenPipeError):
            pass
        if self.process.poll() is None:
            os.killpg(self.process.pid, signal.SIGTERM)
            try:
                self.process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                os.killpg(self.process.pid, signal.SIGKILL)
                self.process.wait()


class Fixture(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        body = b'''<!doctype html><html><head><title>ChatGPT CUA probe</title></head>
        <body><h1>ChatGPT CUA probe</h1><button onclick="document.getElementById('result').textContent='Clicked successfully'">Probe click</button>
        <p id="result">Waiting for click</p></body></html>'''
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


def probe(args, config):
    output = args.output.expanduser().resolve()
    client = McpClient(config, output, args.approve_test_targets)
    httpd = None
    opened = False
    try:
        client.initialize()
        if args.target == "handshake":
            return
        if args.target == "chrome":
            httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Fixture)
            threading.Thread(target=httpd.serve_forever, daemon=True).start()
            url = f"http://127.0.0.1:{httpd.server_port}/"
            client.fixture_origin = url.rstrip("/")
            client.js(f'var probeTab = await cua.createBrowserTab("chrome", {json.dumps(url)}, {{sessionName:"🧪 CUA skill probe"}});', "Open Chrome fixture")
            opened = True
            before = client.js('nodeRepl.write(await probeTab.playwright.domSnapshot());', "Read Chrome fixture")
            if "Waiting for click" not in before:
                raise RuntimeError("Fixture initial state was not observed; see observations.json.")
            after = client.js('await probeTab.playwright.getByRole("button", {name:"Probe click", exact:true}).click(); nodeRepl.write(await probeTab.playwright.domSnapshot());', "Click and verify Chrome fixture")
            if "Clicked successfully" not in after:
                raise RuntimeError("Click did not produce the expected browser state.")
            client.js('await probeTab.getScreenshot();', "Capture Chrome screenshot")
        elif args.target == "computer":
            observed = client.js('var probeApp = await cua.getApp("Calculator");', "Observe native Calculator")
            if "Calculator" not in observed:
                raise RuntimeError("Calculator was not observed; see observations.json.")
            if args.exercise_input:
                before = client.js('await probeApp.getAXState({disableDiffing:true});', "Read Calculator controls")
                match = re.search(r"^\s*(\d+) button Description: (?:Show|Hide) Sidebar", before, re.MULTILINE)
                if not match:
                    raise RuntimeError("Calculator sidebar button not found; leaving its state unchanged.")
                after = client.js(f'await probeApp.click({int(match[1])}); await probeApp.getAXState({{disableDiffing:true}});', "Toggle Calculator sidebar")
                if before == after:
                    raise RuntimeError("Native click produced no observable state change.")
                restore = re.search(r"^\s*(\d+) button Description: (?:Show|Hide) Sidebar", after, re.MULTILINE)
                if not restore:
                    raise RuntimeError("Sidebar changed but restore target was not found; inspect Calculator manually.")
                restored = client.js(f'await probeApp.click({int(restore[1])}); await probeApp.getAXState({{disableDiffing:true}});', "Restore Calculator sidebar")
                if before != restored:
                    raise RuntimeError("Calculator sidebar restoration did not match its initial accessibility state.")
            client.js('await probeApp.getScreenshot();', "Capture native Calculator screenshot")
        if not client.image_count:
            raise RuntimeError("No inline screenshot returned by the runtime.")
        clicked = args.target == "chrome" or args.exercise_input
        print(f"PASS: {args.target} observation and screenshot" + ("; real click verified." if clicked else "."))
    finally:
        if opened:
            try:
                client.js('await probeTab.close();', "Close probe tab", timeout=10)
            except (RuntimeError, BrokenPipeError) as error:
                print(f"Probe tab cleanup: {error}", file=sys.stderr)
        if httpd:
            httpd.shutdown()
            httpd.server_close()
        client.close()
        print(f"Probe artifacts: {output}", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime-home", type=Path, default=Path.home() / ".codex",
                        help="Home containing the desktop-managed plugins (default: ~/.codex)")
    parser.add_argument("--surfaces", choices=["browser", "computer", "browser,computer"], default="browser,computer")
    commands = parser.add_subparsers(dest="action", required=True)
    commands.add_parser("doctor", help="Check installed runtime paths without launching UI")
    commands.add_parser("serve", help="Launch exact ChatGPT runtime over MCP stdio")
    installer = commands.add_parser("setup", help="Register runtime in the selected Codex home; back up existing config")
    installer.add_argument("--codex-home", type=Path, default=Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))))
    tester = commands.add_parser("probe", help="Exercise the exact runtime from a standalone MCP client")
    tester.add_argument("target", choices=["handshake", "chrome", "computer"])
    tester.add_argument("--output", type=Path, required=True, help="Private directory for observations/screenshots")
    tester.add_argument("--approve-test-targets", action="store_true",
                        help="Approve only this probe's localhost fixture and low-risk Calculator access for the session")
    tester.add_argument("--exercise-input", action="store_true",
                        help="For computer probe, toggle and restore Calculator's sidebar without changing its calculation")
    args = parser.parse_args()
    manifest, config = runtime_config(args.runtime_home.expanduser().resolve(), args.surfaces)
    if args.action == "setup":
        setup(args, manifest, config)
    elif args.action == "serve":
        serve(config)
    elif args.action == "probe":
        probe(args, config)
    else:
        print(f"Manifest: {manifest}")
        print(f"Node: {config['command']}")
        print(f"Launcher: {config['args'][0]}")
        print(f"Surfaces: {config['env']['CUA_REPL_ENABLED_SURFACES']}")
        print(f"Desktop helper exists: {Path(config['env'].get('SKY_CUA_SERVICE_PATH', '')).exists()}")
        print("Paths verified. Run probe chrome/computer to verify live backend access.")


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, OSError, KeyError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
