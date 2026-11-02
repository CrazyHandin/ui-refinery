"""Behavioral checks for fixture resources and existing-directory protection."""
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from validate_skill import markdown_targets
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PREPARE = ROOT / "tests/e2e/prepare.py"


def hashes(root):
    return {path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in root.rglob("*") if path.is_file()}


class PrepareFixtureTest(unittest.TestCase):
    def prepare(self, destination):
        return subprocess.run(
            [sys.executable, "-X", "utf8", str(PREPARE), str(destination)],
            capture_output=True, encoding="utf-8")

    def test_runtime_references_and_source_hashes_are_complete(self):
        with tempfile.TemporaryDirectory(prefix="skill-fixture-test-") as temporary:
            destination = Path(temporary) / "fixture"
            result = self.prepare(destination)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            skill = destination / ".agents/skills/ui-refinery"
            self.assertEqual(hashes(ROOT / "references"), hashes(skill / "references"))
            record = (destination / "evidence/source-revision.txt").read_text(encoding="utf-8")
            for relative in ("SKILL.md", "agents/openai.yaml"):
                original = (ROOT / relative).read_bytes()
                self.assertEqual(original, (skill / relative).read_bytes())
                self.assertIn(hashlib.sha256(original).hexdigest(), record)
            for path in skill.rglob("*.md"):
                for target in markdown_targets(path.read_text(encoding="utf-8")):
                    url = urlsplit(target)
                    if not url.scheme and not url.netloc and url.path:
                        resolved = (path.parent / unquote(url.path)).resolve()
                        self.assertTrue(resolved.is_relative_to(skill.resolve()), target)
                        self.assertTrue(resolved.exists(), target)
            self.assertTrue((destination / "index.html").is_file())
            self.assertTrue((destination / "design-prompt.txt").is_file())
            self.assertFalse((skill / "tests").exists())

    def test_existing_fixture_is_not_overwritten(self):
        with tempfile.TemporaryDirectory(prefix="skill-fixture-test-") as temporary:
            destination = Path(temporary) / "fixture"
            first = self.prepare(destination)
            self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
            (destination / "user-work.txt").write_text("keep my changes", encoding="utf-8")
            before = hashes(destination)
            repeated = self.prepare(destination)
            self.assertNotEqual(repeated.returncode, 0)
            self.assertEqual(before, hashes(destination))


if __name__ == "__main__":
    unittest.main()
