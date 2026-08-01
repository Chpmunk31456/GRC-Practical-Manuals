#!/usr/bin/env python3
"""Assemble and validate the English controlled master for the risk-register manual."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "English"

ORDER = [
    ROOT / "chapters/01_Risk_Management_Foundations.md",
    ROOT / "chapters/02_Risk_Identification_and_Scenario_Writing.md",
    ROOT / "chapters/03_Risk_Analysis_and_Scoring.md",
    ROOT / "chapters/04_Risk_Response_Treatment_and_Acceptance.md",
    ROOT / "chapters/05_Monitoring_Reporting_and_Escalation.md",
    ROOT / "chapters/06_Operating_Procedure_and_Worked_Example.md",
    ROOT / "templates/Risk_Acceptance_Record.md",
    ROOT / "SOURCES.md",
]

TITLE = "GRC Risk Register and Risk Treatment Practical Manual"
STEM = "GRC_Risk_Register_and_Risk_Treatment_Practical_Manual_English_v1.0"

FRONT = f"""---
title: "{TITLE}"
author: "Alberto Al Leiva"
date: "1 August 2026"
lang: en-US
subject: "Governance, risk, compliance, risk registers, and risk treatment"
keywords:
  - governance
  - risk management
  - GRC
  - risk register
  - risk treatment
  - enterprise risk management
rights: "CC BY-NC-SA 4.0 unless a file states otherwise"
---

# {TITLE}

**Version 1.0 — August 2026**

**Author:** Alberto “Al” Leiva

ChatGPT assisted under the author's direction. The author remains responsible for editorial and release decisions.

## Educational-use notice

This manual and its companion tools are educational resources. They must be adapted to the organization's objectives, risk appetite, legal and contractual obligations, systems, data, decision authority, and operating context. They do not constitute legal, accounting, regulatory, certification, or formal audit advice.

## How to use this manual

Use the chapters in order when establishing a new risk register. Existing programs may use individual sections for scenario quality, scoring, treatment, acceptance, monitoring, or governance improvement. Preserve the rationale, evidence, ownership, approvals, and review history for every material risk decision.

"""


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    missing = [str(path.relative_to(ROOT)) for path in ORDER if not path.is_file()]
    if missing:
        raise SystemExit(f"Missing assembly sources: {missing}")

    sections = [FRONT.rstrip()]
    for path in ORDER:
        text = path.read_text(encoding="utf-8").strip()
        if not text.startswith("#"):
            raise SystemExit(f"Source lacks a Markdown heading: {path}")
        sections.append(text)

    master = OUT / f"{STEM}.md"
    master.write_text("\n\n\\newpage\n\n".join(sections) + "\n", encoding="utf-8")

    required_phrases = [
        "Risk Management Foundations",
        "Risk Identification and Scenario Writing",
        "Risk Analysis and Scoring",
        "Risk Response, Treatment, and Acceptance",
        "Monitoring, Reporting, and Escalation",
        "Operating Procedure and Worked Example",
        "Risk Acceptance Record",
        "Authoritative Source Register",
    ]
    text = master.read_text(encoding="utf-8")
    absent = [phrase for phrase in required_phrases if phrase not in text]
    if absent:
        raise SystemExit(f"Assembly missing required sections: {absent}")

    report = {
        "title": TITLE,
        "version": "1.0",
        "language": "en-US",
        "source_count": len(ORDER),
        "word_count": len(text.split()),
        "line_count": len(text.splitlines()),
        "sha256": sha256(master),
        "sources": [str(path.relative_to(ROOT)) for path in ORDER],
        "status": "PASS",
    }
    (OUT / "ENGLISH_ASSEMBLY_REPORT.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    (OUT / "ENGLISH_ASSEMBLY_REPORT.md").write_text(
        "# English Assembly Report\n\n"
        f"- Status: **PASS**\n"
        f"- Sources assembled: {report['source_count']}\n"
        f"- Word count: {report['word_count']}\n"
        f"- Line count: {report['line_count']}\n"
        f"- Master SHA-256: `{report['sha256']}`\n",
        encoding="utf-8",
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
