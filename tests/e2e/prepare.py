"""Create a fresh repo-scoped skill fixture; never overwrite an existing directory."""
import argparse
import hashlib
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[2]
FILES = ("SKILL.md", "agents/openai.yaml")


def runtime_files():
    """Include the full reference tree so new entrypoint links remain usable."""
    return [ROOT / relative for relative in FILES] + sorted(
        path for path in (ROOT / "references").rglob("*") if path.is_file())


def source_record(paths):
    """Record actual runtime content even when installed from an archive."""
    revision = "Archive/local installation; no skill-root Git revision.\n"
    try:
        top = subprocess.check_output(
            ["git", "-C", str(ROOT), "rev-parse", "--show-toplevel"],
            text=True, stderr=subprocess.DEVNULL).strip()
        if Path(top).resolve() == ROOT.resolve():
            revision = subprocess.check_output(
                ["git", "-C", str(ROOT), "rev-parse", "HEAD"],
                text=True, stderr=subprocess.DEVNULL)
            revision += subprocess.check_output(
                ["git", "-C", str(ROOT), "status", "--short"], text=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    hashes = [f"{hashlib.sha256(path.read_bytes()).hexdigest()}  "
              f"{path.relative_to(ROOT).as_posix()}" for path in paths]
    return revision + "\nRuntime SHA-256:\n" + "\n".join(hashes) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    destination = args.destination.resolve()
    destination.mkdir(parents=True, exist_ok=False)
    subprocess.run(["git", "init", "-q", str(destination)], check=True)
    skill = destination / ".agents/skills/ui-refinery"
    paths = runtime_files()
    for source in paths:
        relative = source.relative_to(ROOT)
        target = skill / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    for filename in ("index.html", "design-prompt.txt"):
        shutil.copyfile(Path(__file__).parent / filename, destination / filename)
    (destination / "evidence").mkdir()
    (destination / "evidence/source-revision.txt").write_text(
        source_record(paths), encoding="utf-8")
    print(f"Prepared {destination}; Codex discovery and design are NOT VERIFIED.")


if __name__ == "__main__":
    main()
