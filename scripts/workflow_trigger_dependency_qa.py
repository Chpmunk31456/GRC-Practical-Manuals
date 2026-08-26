#!/usr/bin/env python3
"""Ensure Python scripts invoked by PR workflows are included in those workflows' path triggers."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github/workflows"

RUN_SCRIPT_RE = re.compile(r"(?:python3?|python)\s+(scripts/[A-Za-z0-9_./-]+\.py)")
PATH_LINE_RE = re.compile(r"^\s*-\s+['\"]?(scripts/[A-Za-z0-9_./*-]+)['\"]?\s*$")


def main() -> int:
    errors: list[str] = []
    checked = 0

    for workflow in sorted(list(WORKFLOWS.glob("*.yml")) + list(WORKFLOWS.glob("*.yaml"))):
        text = workflow.read_text(encoding="utf-8")
        if "pull_request:" not in text or "paths:" not in text:
            continue
        invoked = sorted(set(RUN_SCRIPT_RE.findall(text)))
        if not invoked:
            continue
        trigger_paths = set(PATH_LINE_RE.findall(text))
        checked += 1
        for script in invoked:
            if script in trigger_paths or "scripts/**" in trigger_paths:
                continue
            errors.append(f"{workflow.relative_to(ROOT)} invokes {script} but does not include it in pull_request.paths")

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
