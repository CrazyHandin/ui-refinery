"""Smoke test and negative fixtures. No model, browser or credentials required."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from validate_skill import REQUIRED, validate

ROOT = Path(__file__).resolve().parents[1]


class SmokeTest(unittest.TestCase):
    def test_repository_contract(self):
        self.assertEqual(validate(ROOT), [])


class ValidatorRegressionTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for relative in REQUIRED:
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)
        # Use minimal docs so fixtures do not depend on README navigation additions.
        for doc in ("README.md", "README.en.md"):
            (self.root / doc).write_text("Use $ui-refinery.\n[Skill](SKILL.md)\n")

    def change(self, relative, old, new):
        path = self.root / relative
        path.write_text(path.read_text().replace(old, new), encoding="utf-8")

    def assert_failure(self, expected):
        errors = validate(self.root)
        self.assertTrue(any(expected in error for error in errors), errors)

    def test_valid_fixture(self):
        self.assertEqual(validate(self.root), [])

    def test_cli_returns_nonzero_for_invalid_root(self):
        (self.root / "SKILL.md").unlink()
        result = subprocess.run([sys.executable, str(ROOT / "tests/validate_skill.py"),
                                 "--root", str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("FAIL missing required file: SKILL.md", result.stdout)

    def test_missing_required_file(self):
        (self.root / "references/review-and-media.md").unlink()
        self.assert_failure("missing required file")

    def test_frontmatter_delimiter(self):
        self.change("SKILL.md", "---", "bad")
        self.assert_failure("front matter")

    def test_malformed_yaml(self):
        self.change("SKILL.md", "name: ui-refinery", "name: [")
        self.assert_failure("SKILL.md:")

    def test_duplicate_yaml_key(self):
        self.change("SKILL.md", "name: ui-refinery",
                    "name: ui-refinery\nname: ignored")
        self.assert_failure("duplicate YAML key")

    def test_missing_description(self):
        self.change("SKILL.md", "description:", "unused:")
        self.assert_failure("description must be a non-empty string")

    def test_description_wrong_type(self):
        self.change("SKILL.md", "description:", "unused:")
        self.change("SKILL.md", "name: ui-refinery",
                    "name: ui-refinery\ndescription: 123")
        self.assert_failure("description must be a non-empty string")

    def test_metadata_length_limits(self):
        path = self.root / "SKILL.md"
        path.write_text("---\nname: ui-refinery\ndescription: " + "a" * 1025 + "\n---\nBody")
        self.assert_failure("exceeds 1024")

    def test_agent_yaml_malformed_or_duplicate(self):
        path = self.root / "agents/openai.yaml"
        original = path.read_text()
        path.write_text("interface: [")
        self.assert_failure("agents/openai.yaml:")
        path.write_text(original + "\ninterface: {}\n")
        self.assert_failure("duplicate YAML key")

    def test_empty_display_field(self):
        path = self.root / "agents/openai.yaml"
        path.write_text('interface:\n  display_name: ""\n')
        self.assert_failure("display_name must be a non-empty string")

    def test_bad_icon_or_brand_color(self):
        path = self.root / "agents/openai.yaml"
        original = path.read_text()
        path.write_text(original + '  icon_small: "../outside.png"\n')
        self.assert_failure("icon_small")
        path.write_text(original + '  brand_color: "red"\n')
        self.assert_failure("brand_color")

    def test_bad_name(self):
        self.change("SKILL.md", "name: ui-refinery", "name: Wrong_Name")
        self.assert_failure("lowercase")

    def test_empty_body(self):
        path = self.root / "SKILL.md"
        path.write_text("---\nname: ui-refinery\n"
                        "description: A design workflow\n---\n")
        self.assert_failure("instruction body is empty")

    def test_prompt_name_mismatch(self):
        self.change("agents/openai.yaml", "$ui-refinery", "$different-skill")
        self.assert_failure("default_prompt")

    def test_interface_wrong_type(self):
        (self.root / "agents/openai.yaml").write_text("interface: []\n")
        self.assert_failure("interface must be a mapping")

    def test_policy_boolean(self):
        with (self.root / "agents/openai.yaml").open("a") as stream:
            stream.write('\npolicy:\n  allow_implicit_invocation: "false"\n')
        self.assert_failure("must be a boolean")

    def test_documented_name_mismatch(self):
        self.change("README.en.md", "$ui-refinery", "$wrong-skill")
        self.assert_failure("documented $skill calls")

    def test_shell_environment_variable_is_not_a_skill_call(self):
        for relative in ("README.md", "README.en.md"):
            path = self.root / relative
            with path.open("a", encoding="utf-8") as stream:
                stream.write('\n```powershell\ngit clone https://example.com/skill.git '
                             '"$env:USERPROFILE\\.agents\\skills\\ui-refinery"\n```\n')
        self.assertEqual(validate(self.root), [])

    def test_missing_reference_link(self):
        (self.root / "README.md").write_text(
            "Use $ui-refinery.\n[Guide][ref]\n\n[ref]: missing.md\n")
        self.assert_failure("missing.md")

    def test_image_and_escaped_link(self):
        (self.root / "extra.md").write_text("![image](missing.png)\n[escape](../outside.md)\n")
        self.assert_failure("missing.png")
        self.assert_failure("../outside.md")

    def test_code_external_fragment_and_encoded_links(self):
        (self.root / "space file.md").write_text("# Title\n")
        (self.root / "extra.md").write_text(
            "```md\n[Example](not-a-real-file.md)\n```\n"
            "`[Inline](not-real.md)`\n[External](https://example.invalid/404)\n"
            "[Anchor](#heading)\n[File](space%20file.md?download=1#title)\n")
        self.assertEqual(validate(self.root), [])

    def test_invalid_utf8(self):
        (self.root / "README.md").write_bytes(b"\xff")
        self.assert_failure("README.md:")


if __name__ == "__main__":
    unittest.main()
