#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = {
    "elon-flow",
    "first-principles",
    "experiment",
    "architecture",
    "implement",
    "debug",
    "compound",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def frontmatter(text: str, path: Path) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail(f"{path}: missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail(f"{path}: unterminated YAML frontmatter")
    block = text[4:end]
    data: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip():
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not match:
            fail(f"{path}: unsupported frontmatter line: {line}")
        key, value = match.groups()
        data[key] = value.strip().strip('"').strip("'")
    return data


def main() -> int:
    manifest_path = ROOT / "plugin.json"
    if not manifest_path.exists():
        fail("plugin.json missing")

    manifest = json.loads(manifest_path.read_text())
    if manifest.get("name") != "elon-flow":
        fail("plugin name must be elon-flow")
    if not re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", "")):
        fail("plugin version must be strict semver")

    interface = (
        manifest.get("extensions", {})
        .get("com.openai", {})
        .get("interface", {})
    )
    short = interface.get("shortDescription", "")
    if len(short) > 30:
        fail(f"shortDescription is {len(short)} chars, max 30")

    skills_root = ROOT / "skills"
    skill_dirs = {
        path.parent.name
        for path in skills_root.glob("*/SKILL.md")
    }
    if skill_dirs != EXPECTED_SKILLS:
        fail(
            "skill set mismatch: "
            f"expected {sorted(EXPECTED_SKILLS)}, got {sorted(skill_dirs)}"
        )

    for name in sorted(EXPECTED_SKILLS):
        path = skills_root / name / "SKILL.md"
        meta = frontmatter(path.read_text(), path)
        if meta.get("name") != name:
            fail(f"{path}: frontmatter name must match directory")
        if not meta.get("description"):
            fail(f"{path}: description missing")

    controller = (skills_root / "elon-flow" / "SKILL.md").read_text()
    for ref in ("references/doctrine.md", "references/routing.md"):
        if ref not in controller:
            fail(f"controller missing pointer to {ref}")
        if not (skills_root / "elon-flow" / ref).exists():
            fail(f"controller reference does not exist: {ref}")

    if (ROOT / "SKILL.md").exists():
        fail("duplicate root SKILL.md exists outside portable skills/ layout")

    cases_path = ROOT / "tests" / "routing-cases.json"
    cases = json.loads(cases_path.read_text())
    if not cases:
        fail("routing cases are empty")
    for case in cases:
        for route in case.get("expected_route", []):
            if route not in EXPECTED_SKILLS:
                fail(f"routing case {case.get('id')} names unknown route {route}")

    required_case_ids = {
        "no-op",
        "observable-uncertainty",
        "bug",
        "small-known-change",
        "contested-architecture",
        "repeated-correction",
    }
    seen = {case.get("id") for case in cases}
    missing = required_case_ids - seen
    if missing:
        fail(f"missing required routing cases: {sorted(missing)}")

    print(
        "PASS: manifest, seven skill entrypoints, frontmatter, "
        "controller references, and routing fixtures are structurally valid"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
