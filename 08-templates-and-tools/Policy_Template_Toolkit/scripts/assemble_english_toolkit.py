#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "chapters"
TEMPLATES = ROOT / "templates"
OUT = ROOT / "English"
STEM = "GRC_Policy_Template_Toolkit_English_v1.0"

CHAPTER_ORDER = [
    "01_Policy_Governance_and_Document_Hierarchy.md",
    "02_Template_Adaptation_Approval_and_Publication.md",
    "03_Implementation_Evidence_Training_and_Monitoring.md",
    "04_Exceptions_Review_Records_and_Lifecycle.md",
]
TEMPLATE_ORDER = [
    "01_Information_Security_Policy_Template.md",
    "02_Access_Control_Policy_Template.md",
    "03_Acceptable_Use_Policy_Template.md",
    "04_Incident_Response_Policy_Template.md",
    "05_Business_Continuity_and_Disaster_Recovery_Policy_Template.md",
    "06_Third_Party_and_Vendor_Risk_Policy_Template.md",
    "07_Data_Protection_and_Privacy_Policy_Template.md",
    "08_Change_Management_Policy_Template.md",
    "09_Vulnerability_and_Patch_Management_Policy_Template.md",
    "10_Logging_and_Monitoring_Policy_Template.md",
]

FRONT = '''---
title: "GRC Policy Template Toolkit"
author: "Alberto Al Leiva"
date: "1 August 2026"
lang: en
subject: "GRC, policy governance, information security, privacy, resilience, technology risk"
rights: "CC BY-NC-SA 4.0 unless a file states otherwise"
status: "Controlled English publication candidate"
---

# GRC Policy Template Toolkit

This toolkit contains educational starter templates. It does not constitute legal, regulatory, privacy, labor, accounting, certification, or formal audit advice. Each template must be adapted, reviewed, approved, implemented, and evidenced for the adopting organization.

'''

SAFEGUARD_TERMS = ("review", "adapt", "validate", "resolve", "confirm", "consult")


def load(path: Path, require_placeholder: bool = False) -> dict[str, object]:
    if not path.is_file():
        raise SystemExit(f"Missing controlled source: {path}")
    text = path.read_text(encoding="utf-8").strip()
    if "TODO" in text or "TBD" in text:
        raise SystemExit(f"Unresolved development marker in {path.name}")
    if not text.startswith("# "):
        raise SystemExit(f"Missing level-one heading in {path.name}")
    if require_placeholder:
        if "[" not in text or "]" not in text:
            raise SystemExit(f"Template lacks controlled placeholders: {path.name}")
        opening_lines = text.splitlines()[1:10]
        warning_lines = [line.strip() for line in opening_lines if line.lstrip().startswith(">")]
        warning = " ".join(warning_lines).lower()
        if not warning or not any(term in warning for term in SAFEGUARD_TERMS):
            raise SystemExit(f"Template lacks a substantive pre-adoption drafting safeguard: {path.name}")
    return {
        "path": str(path.relative_to(ROOT)),
        "text": text,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "words": len(text.split()),
    }


def main() -> None:
    sources = [load(CHAPTERS / name) for name in CHAPTER_ORDER]
    sources += [load(TEMPLATES / name, require_placeholder=True) for name in TEMPLATE_ORDER]
    parts = [FRONT]
    for source in sources:
        parts.append(str(source["text"]) + "\n")
    OUT.mkdir(parents=True, exist_ok=True)
    master = OUT / f"{STEM}.md"
    master.write_text("\n\\newpage\n\n".join(parts).strip() + "\n", encoding="utf-8")
    report = {
        "status": "PASS",
        "chapter_count": len(CHAPTER_ORDER),
        "template_count": len(TEMPLATE_ORDER),
        "source_count": len(sources),
        "sources": [{k: v for k, v in source.items() if k != "text"} for source in sources],
        "master": str(master.relative_to(ROOT)),
        "master_sha256": hashlib.sha256(master.read_bytes()).hexdigest(),
        "master_words": len(master.read_text(encoding="utf-8").split()),
    }
    (OUT / "ENGLISH_ASSEMBLY_REPORT.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    (OUT / "ENGLISH_ASSEMBLY_REPORT.md").write_text(
        "# English Assembly Report\n\n"
        f"- Status: **PASS**\n- Controlled chapters: {report['chapter_count']}\n"
        f"- Controlled policy templates: {report['template_count']}\n"
        f"- Total controlled sources: {report['source_count']}\n"
        f"- Master words: {report['master_words']}\n"
        f"- Master SHA-256: `{report['master_sha256']}`\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
