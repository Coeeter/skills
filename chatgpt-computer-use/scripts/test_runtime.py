import contextlib
import io
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest

from runtime import setup


class SetupTests(unittest.TestCase):
    def test_shadow_home_keeps_config_symlink(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            source = root / "base/config.toml"
            source.parent.mkdir()
            original = 'model = "example"\n'
            source.write_text(original)
            shadow = root / "shadow"
            shadow.mkdir()
            link = shadow / "config.toml"
            link.symlink_to(source)
            config = {"command": "/usr/bin/true", "args": [], "env": {},
                      "startup_timeout_sec": 120, "tool_timeout_sec": 180}
            args = SimpleNamespace(codex_home=shadow)
            with contextlib.redirect_stdout(io.StringIO()):
                setup(args, root / "manifest.json", config)
                first = source.read_bytes()
                setup(args, root / "manifest.json", config)
            self.assertTrue(link.is_symlink())
            self.assertEqual(link.resolve(), source)
            self.assertEqual(source.read_bytes(), first)
            self.assertIn(b"[mcp_servers.chatgpt_cua]", first)
            backups = list(source.parent.glob("config.toml.before-chatgpt-cua.*"))
            self.assertEqual(len(backups), 1)
            self.assertEqual(backups[0].read_text(), original)


if __name__ == "__main__":
    unittest.main()
