#!/usr/bin/env python3
"""Ensure Python scripts invoked by PR workflows are included in those workflows' path triggers."""

from __future__ import annotations

import fnmatch
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github/workflows"

RUN_SCRIPT_RE = re.compile(r"(?:python3?|python)\s+(scripts/[A-Za-z0-9_./-]+\.py)")
PATH_LINE_RE = re.compile(
    r"^\s*-\s+(?P<quote>['\"]?)(?P<path>scripts/[A-Za-z0-9_./*?\[\]-]+)(?P=quote)\s*(?:#.*)?$"
)


def extract_trigger_paths(text: str) -> set[str]:
    """Return normalized scripts/* path entries from YAML list lines.

    Handles unquoted, single-quoted, and double-quoted path entries plus trailing comments.
    """
    paths: set[str] = set()
    for line in text.splitlines():
        match = PATH_LINE_RE.match(line)
        if match:
            paths.add(match.group("path"))
    return paths


def path_is_covered(script: str, trigger_paths: set[str]) -> bool:
    """Return True when an exact or glob trigger path covers the invoked script."""
    return any(fnmatch.fnmatchcase(script, pattern) for pattern in trigger_paths)


def self_test_parser(errors: list[str]) -> None:
    fixtures = {
        "- scripts/compliance_qa.py": "scripts/compliance_qa.py",
        "- 'scripts/compliance_qa.py'": "scripts/compliance_qa.py",
        '- "scripts/pdf_content_preflight.py"': "scripts/pdf_content_preflight.py",
        "      - 'scripts/**' # helper changes": "scripts/**",
        "      - 'scripts/generate_nist_ai_rmf_manual_03_publication*.py'": "scripts/generate_nist_ai_rmf_manual_03_publication*.py",
    }
    for line, expected in fixtures.items():
        parsed = extract_trigger_paths(line)
        if parsed != {expected}:
            errors.append(
                f"parser regression: expected {expected!r} from {line!r}, got {sorted(parsed)!r}"
            )

    coverage_fixtures = [
        ("scripts/compliance_qa.py", {"scripts/compliance_qa.py"}, True),
        ("scripts/pdf_content_preflight.py", {"scripts/**"}, True),
        (
            "scripts/generate_nist_ai_rmf_manual_03_publication_v3.py",
            {"scripts/generate_nist_ai_rmf_manual_03_publication*.py"},
            True,
        ),
        ("scripts/pdf_content_preflight.py", {"scripts/compliance_qa.py"}, False),
    ]
    for script, patterns, expected in coverage_fixtures:
        actual = path_is_covered(script, patterns)
        if actual != expected:
            errors.append(
                f"coverage regression: {script!r} with {sorted(patterns)!r} expected {expected}, got {actual}"
            )


def main() -> int:
    errors: list[str] = []
    checked = 0

    self_test_parser(errors)

    for workflow in sorted(list(WORKFLOWS.glob("*.yml")) + list(WORKFLOWS.glob("*.yaml"))):
        text = workflow.read_text(encoding="utf-8")
        if "pull_request:" not in text or "paths:" not in text:
            continue
        invoked = sorted(set(RUN_SCRIPT_RE.findall(text)))
        if not invoked:
            continue
        trigger_paths = extract_trigger_paths(text)
        checked += 1
        for script in invoked:
            if path_is_covered(script, trigger_paths):
                continue
            errors.append(
                f"{workflow.relative_to(ROOT)} invokes {script} but does not include it in pull_request.paths"
            )

    print(f"Workflow trigger dependency QA: checked {checked} pull-request workflows")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print("FAIL: workflow execution dependencies and trigger paths are inconsistent")
        return 1

    print("PASS: invoked Python workflow dependencies are covered by pull_request path triggers")
    return 0


if __name__ == "__main__":
    sys.exit(main())
