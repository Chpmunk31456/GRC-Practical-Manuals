#!/usr/bin/env python3
"""Validate the Manual 02 human semantic-review boundary.

This gate deliberately verifies that human review is required and remains open.
It must never auto-approve a localized edition.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / ".compliance" / "iso-42001-manual-02-baseline.json"
MANUAL_ROOT = ROOT / "02-management-systems" / "ISO_IEC_42001_AIMS"


def main() -> int:
    errors: list[str] = []

    try:
        baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: cannot read Manual 02 baseline: {exc}")
        return 1

    if baseline.get("localized_full_source_status") != "draft-human-review-required":
        errors.append("localized full-source status must remain draft-human-review-required")
    if baseline.get("human_review_gate") != "open":
        errors.append("human review gate must remain open until explicit human sign-off")
    if baseline.get("human_review_required_languages") != ["es-419", "pt-BR"]:
        errors.append("human review must explicitly require es-419 and pt-BR")

    relative = baseline.get("human_review_checklist")
    if not isinstance(relative, str) or not relative:
        errors.append("human_review_checklist must be a repository-relative Manual 02 path")
        checklist = None
    else:
        checklist = MANUAL_ROOT / relative
        if ".." in Path(relative).parts or not checklist.resolve().is_relative_to(MANUAL_ROOT.resolve()):
            errors.append("human_review_checklist must remain inside Manual 02")
            checklist = None

    if checklist is not None:
        if not checklist.is_file():
            errors.append("human semantic-review checklist is missing")
        else:
            text = checklist.read_text(encoding="utf-8")
            semantic_text = text.replace("**", "")
            required_markers = (
                "Gate status: OPEN",
                "human review required",
                "must not mark this gate complete or impersonate a human language/domain reviewer",
                "Spanish (`es-419`) terms to verify consistently",
                "Brazilian Portuguese (`pt-BR`) terms to verify consistently",
                "Visible labels in those raster images remain an open release issue",
                "Human sign-off gate",
                "zero open Critical and Major issues",
                "baseline must remain `draft-human-review-required`",
            )
            for marker in required_markers:
                if marker not in semantic_text:
                    errors.append(f"human review checklist is missing controlled marker: {marker}")

            if "| `es-419` | Pending | Pending | Pending | Pending | Pending |" not in text:
                errors.append("Spanish human sign-off row must remain pending")
            if "| `pt-BR` | Pending | Pending | Pending | Pending | Pending |" not in text:
                errors.append("Portuguese human sign-off row must remain pending")

    print("ISO/IEC 42001 Manual 02 human semantic-review gate")
    print("  required languages: es-419, pt-BR")
    print("  expected gate state: OPEN")
    for error in errors:
        print(f"  ERROR: {error}")
    if errors:
        print("FAIL: human semantic-review boundary is not controlled")
        return 1
    print("PASS: human semantic-review boundary remains controlled and open")
    return 0


if __name__ == "__main__":
    sys.exit(main())
