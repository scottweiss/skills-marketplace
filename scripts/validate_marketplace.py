#!/usr/bin/env python3
"""Validate the marketplace registry against per-skill contracts."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
MIRRORED = ("id", "slug", "name", "version", "summary", "description", "entry", "readme", "tags")
README_HEADINGS = ("## Summary", "## When to use", "## Quick start", "## Skill files", "## Limitations")
ENTRY_HEADINGS = ("## Operating contract", "## Core loop", "## Evidence report", "## Limitations")


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else ROOT
    errors: list[str] = []
    registry = json.loads((root / "registry.json").read_text(encoding="utf-8"))
    skills = registry.get("skills", [])
    ids = [skill.get("id") for skill in skills]

    if not SEMVER.fullmatch(str(registry.get("marketplace", {}).get("version", ""))):
        errors.append("marketplace version must use semantic versioning")
    actual_ids = sorted(path.name for path in (root / "skills").iterdir() if path.is_dir())
    str_ids = [i for i in ids if isinstance(i, str)]
    if str_ids != sorted(set(str_ids)) or actual_ids != sorted(str_ids) or len(str_ids) != len(ids):
        errors.append("registry ids must be sorted, unique, and match skill directories")

    referenced = 0
    for item in skills:
        skill_id = item.get("id")
        if not isinstance(skill_id, str):
            errors.append("registry entry is missing a valid string id")
            continue
        prefix = f"skills/{skill_id}/"
        expected = {
            "slug": skill_id,
            "path": prefix,
            "entry": f"{prefix}{skill_id}.md",
            "readme": f"{prefix}README.md",
        }
        for key, value in expected.items():
            if item.get(key) != value:
                errors.append(f"{skill_id}.{key} must equal {value!r}")
        if not SEMVER.fullmatch(str(item.get("version", ""))):
            errors.append(f"{skill_id}.version must use semantic versioning")
        if item.get("tags") != sorted(set(item.get("tags", []))):
            errors.append(f"{skill_id}.tags must be sorted and unique")

        contract_path = root / prefix / "skill.yaml"
        contract = yaml.safe_load(contract_path.read_text(encoding="utf-8"))
        for key in MIRRORED:
            if item.get(key) != contract.get(key):
                errors.append(f"{skill_id}.{key} must match skill.yaml")
        if item.get("harnesses") != contract.get("harness_compatibility"):
            errors.append(f"{skill_id}.harnesses must match skill.yaml")

        examples = contract.get("examples", [])
        declared = {root / path for path in examples}
        actual = set((root / prefix / "examples").glob("*.md"))
        if not examples or len(examples) != len(set(examples)) or declared != actual:
            errors.append(f"{skill_id} examples must be unique, declared, and present")
        meta = contract.get("metadata", {})
        if item.get("metadata") != {
            "author": contract.get("author"),
            "license": contract.get("license"),
            "maturity": meta.get("maturity"),
            "examples": examples,
            "keywords": contract.get("tags"),
        }:
            errors.append(f"{skill_id}.metadata must mirror skill.yaml")

        entry = (root / item["entry"]).read_text(encoding="utf-8")
        readme = (root / item["readme"]).read_text(encoding="utf-8")
        if not all(heading in entry for heading in ENTRY_HEADINGS):
            errors.append(f"{skill_id} entry is missing required sections")
        if not all(heading in readme for heading in README_HEADINGS):
            errors.append(f"{skill_id} README is missing required sections")
        referenced += 3 + len(examples)

    for path in root.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file() and path.suffix in {".json", ".md", ".py", ".txt", ".yaml", ".yml"}:
            text = path.read_text(encoding="utf-8")
            if "\r" in text or (text and not text.endswith("\n")):
                errors.append(f"{path.relative_to(root)} must use LF and end with a newline")

    if errors:
        print(f"Validation failed with {len(errors)} error(s):", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Validation passed: {len(skills)} skill(s), {referenced} referenced skill file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
