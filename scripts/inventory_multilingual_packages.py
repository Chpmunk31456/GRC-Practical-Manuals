#!/usr/bin/env python3
"""Inventory GRC manual language packages and report missing DOCX/PDF editions."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT_MD = ROOT / "MULTILINGUAL_PACKAGE_INVENTORY.md"
REPORT_JSON = ROOT / "MULTILINGUAL_PACKAGE_INVENTORY.json"

MANUALS = {
    "01-foundations/NIST_CSF_2": "NIST Cybersecurity Framework 2.0",
    "01-foundations/CIS_Controls_v8.1": "CIS Critical Security Controls v8.1",
    "01-foundations/NIST_RMF_SP_800-53": "NIST Risk Management Framework / SP 800-53",
    "02-management-systems/ISO_IEC_27001_27002": "ISO/IEC 27001 and ISO/IEC 27002",
    "03-assurance-and-audit/SOC2_Audit_Readiness_Bilingual_v1.0": "SOC 2 Audit Readiness",
    "04-regulatory-compliance/GDPR": "GDPR",
    "04-regulatory-compliance/HIPAA": "HIPAA",
    "04-regulatory-compliance/PCI_DSS_v4.0.1": "PCI DSS v4.0.1",
    "05-operational-resilience/Incident_Response_BCDR": "Incident Response, Business Continuity, and Disaster Recovery",
    "06-cloud-and-technology-risk/Cloud_Security_and_Compliance": "Cloud Security and Compliance",
    "07-third-party-risk/Third_Party_Risk_and_Supply_Chain": "Third-Party Risk and Cyber Supply-Chain Security",
}

LANG_PATTERNS = {
    "English": re.compile(r"(?:^|[/_. -])(en|eng|english)(?:$|[/_. -])", re.I),
    "Spanish (Latin America)": re.compile(r"(?:^|[/_. -])(es|es-419|spa|spanish|espanol|español)(?:$|[/_. -])", re.I),
    "Brazilian Portuguese": re.compile(r"(?:^|[/_. -])(pt|pt-br|ptbr|por|portuguese|portugues|português)(?:$|[/_. -])", re.I),
}


def language_for(path: Path) -> str:
    text = path.as_posix().lower()
    for language, pattern in LANG_PATTERNS.items():
        if pattern.search(text):
            return language
    return "Unclassified"


def main() -> int:
    records: list[dict[str, object]] = []
    blocking: list[str] = []

    for rel_dir, title in MANUALS.items():
        manual_dir = ROOT / rel_dir
        files = []
        if manual_dir.exists():
            files = sorted(
                p for p in manual_dir.rglob("*")
                if p.is_file() and p.suffix.lower() in {".docx", ".pdf", ".md"}
            )

        inventory: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
        for path in files:
            language = language_for(path)
            inventory[language][path.suffix.lower().lstrip(".")].append(path.relative_to(ROOT).as_posix())

        missing = []
        for language in ("English", "Spanish (Latin America)", "Brazilian Portuguese"):
            for fmt in ("docx", "pdf"):
                if not inventory[language][fmt]:
                    missing.append(f"{language} {fmt.upper()}")

        if not manual_dir.exists():
            blocking.append(f"Missing expected manual directory: {rel_dir}")

        records.append({
            "manual": title,
            "directory": rel_dir,
            "inventory": {lang: dict(formats) for lang, formats in inventory.items()},
            "missing": missing,
        })

    lines = [
        "# Multilingual Package Inventory",
        "",
        "Automated inventory of English, Latin American Spanish, and Brazilian Portuguese DOCX/PDF packages.",
        "",
        "| Manual | English | Spanish | Portuguese | Missing deliverables |",
        "|---|---|---|---|---|",
    ]

    for record in records:
        inv = record["inventory"]
        def status(language: str) -> str:
            formats = inv.get(language, {})
            present = [fmt.upper() for fmt in ("docx", "pdf") if formats.get(fmt)]
            return " + ".join(present) if present else "Not present"

        missing_text = ", ".join(record["missing"]) if record["missing"] else "None"
        lines.append(
            f"| {record['manual']} | {status('English')} | "
            f"{status('Spanish (Latin America)')} | {status('Brazilian Portuguese')} | {missing_text} |"
        )

    lines.extend(["", "## Blocking inventory defects", ""])
    lines.extend(f"- {item}" for item in blocking) if blocking else lines.append("- None detected.")
    lines.extend([
        "",
        "## Scope",
        "",
        "This report inventories files only. It does not certify translation quality, visual layout, accessibility, factual currency, or publication readiness.",
        "",
    ])

    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")
    REPORT_JSON.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n".join(lines))
    return 1 if blocking else 0


if __name__ == "__main__":
    raise SystemExit(main())
