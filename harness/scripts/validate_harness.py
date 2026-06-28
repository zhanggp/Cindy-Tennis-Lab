#!/usr/bin/env python3
"""Validate Cindy Tennis Lab skill and harness structure."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[2]

SKILL_REQUIRED_SECTIONS = [
    "## Inputs",
    "## Workflow",
    "## Output Format",
    "## Guardrails",
]

CASE_REQUIRED_FIELDS = [
    "id:",
    "skill:",
    "title:",
    "input:",
    "expected_sections:",
    "quality_bar:",
]

RUBRIC_REQUIRED_FIELDS = [
    "id:",
    "criteria:",
    "evidence:",
    "clarity:",
    "safety:",
    "focus:",
    "long_termism:",
    "passing_rule:",
]


def fail(message: str) -> None:
    print(f"Harness validation failed: {message}", file=sys.stderr)
    sys.exit(1)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def validate_skill(path: Path) -> None:
    text = read(path)
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)} missing frontmatter")
    frontmatter_match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if not frontmatter_match:
        fail(f"{path.relative_to(ROOT)} has invalid frontmatter")
    frontmatter = frontmatter_match.group(1)
    for field in ("name:", "description:"):
        if field not in frontmatter:
            fail(f"{path.relative_to(ROOT)} missing frontmatter field {field}")
    for section in SKILL_REQUIRED_SECTIONS:
        if section not in text:
            fail(f"{path.relative_to(ROOT)} missing section {section}")


def validate_case(path: Path, skill_names: set[str]) -> None:
    text = read(path)
    for field in CASE_REQUIRED_FIELDS:
        if field not in text:
            fail(f"{path.relative_to(ROOT)} missing field {field}")
    skill_match = re.search(r"^skill:\s*([a-z0-9-]+)\s*$", text, re.MULTILINE)
    if not skill_match:
        fail(f"{path.relative_to(ROOT)} has invalid skill field")
    skill_name = skill_match.group(1)
    if skill_name not in skill_names:
        fail(f"{path.relative_to(ROOT)} references unknown skill {skill_name}")


def validate_rubric(path: Path) -> None:
    text = read(path)
    for field in RUBRIC_REQUIRED_FIELDS:
        if field not in text:
            fail(f"{path.relative_to(ROOT)} missing field {field}")


def main() -> None:
    skill_paths = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skill_paths:
        fail("no skills found")

    skill_names = set()
    for path in skill_paths:
        validate_skill(path)
        skill_names.add(path.parent.name)

    case_paths = sorted((ROOT / "harness" / "cases").glob("*.yaml"))
    if not case_paths:
        fail("no harness cases found")
    for path in case_paths:
        validate_case(path, skill_names)

    validate_rubric(ROOT / "harness" / "rubrics" / "ai-output-rubric.yaml")
    print("Harness validation passed.")


if __name__ == "__main__":
    main()
