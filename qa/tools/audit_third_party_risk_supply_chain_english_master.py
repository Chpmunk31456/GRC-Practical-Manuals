#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

TARGET = Path("07-third-party-risk/Third_Party_Risk_and_Supply_Chain/English_Source_Third_Party_Risk_Management_and_Cyber_Supply_Chain_Security_Manual_v1.0.md")
REPORT = Path("qa/THIRD_PARTY_RISK_SUPPLY_CHAIN_ENGLISH_MASTER_AUDIT.md")

PATTERNS = {
    "conversion box glyph": re.compile(r"□"),
    "broken image marker": re.compile(r"^[■□]img\b", re.MULTILINE | re.IGNORECASE),
    "double heading marker": re.compile(r"^#\s+#\s+", re.MULTILINE),
    "raw separator line": re.compile(r"^-{20,}$", re.MULTILINE),
    "empty markdown link": re.compile(r"\[[^\]]+\]\(\s*\)"),
    "placeholder token": re.compile(r"\b(?:TBD|TODO|FIXME|PLACEHOLDER)\b", re.IGNORECASE),
    "malformed Word contents label": re.compile(r"\*\*True Word contents:\*\*", re.IGNORECASE),
}

REQUIRED_SECTIONS = [re.compile(rf"^#\s+{n}\.\s+", re.MULTILINE) for n in range(1, 31)]
REQUIRED_FACTS = {
    "supplier lifecycle": "The Third-Party Life Cycle",
    "inventory and tiering": "Inventory, Classification, and Tiering",
    "inherent risk": "Intake and Inherent Risk",
    "due diligence": "Due Diligence and Research",
    "SP 1326": "NIST SP 1326",
    "SP 1326 final date": "July 8, 2026",
    "SP 800-18 Rev. 2": "NIST SP 800-18 Rev. 2",
    "SP 800-161 Rev. 1 Update 1": "NIST SP 800-161 Rev. 1 Update 1",
    "SP 1305": "NIST SP 1305",
    "risk treatment": "Risk Scoring and Treatment",
    "contract requirements": "Contract Requirements",
    "continuous monitoring": "Continuous Monitoring",
    "supplier incidents": "Supplier Incidents and Notification",
    "fourth-party risk": "Fourth Parties, Concentration, and Systemic Risk",
    "software supply chain": "Software and Open-Source Supply Chains",
    "SBOM limitations": "SBOM limits",
    "AI vendors": "Artificial Intelligence Vendors",
    "exit planning": "Resilience, Continuity, and Exit",
    "CSF 2.0 supplier outcomes": "NIST CSF 2.0 Supplier Outcomes",
    "evidence testing": "Evidence Testing and Metrics",
}


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def main() -> int:
    text = TARGET.read_text(encoding="utf-8")
    findings: list[tuple[str, int, str]] = []
    counts: Counter[str] = Counter()

    for label, pattern in PATTERNS.items():
        for match in pattern.finditer(text):
            line = line_number(text, match.start())
            excerpt = text.splitlines()[line - 1].strip()[:220]
            findings.append((label, line, excerpt))
            counts[label] += 1

    missing_sections = [str(i) for i, pattern in enumerate(REQUIRED_SECTIONS, start=1) if not pattern.search(text)]
    duplicate_sections = [str(i) for i, pattern in enumerate(REQUIRED_SECTIONS, start=1) if len(pattern.findall(text)) != 1]
    missing_facts = [label for label, marker in REQUIRED_FACTS.items() if marker not in text]

    status = "PASS" if not findings and not missing_sections and not duplicate_sections and not missing_facts else "REVIEW REQUIRED"
    report = [
        "# Third-Party Risk and Supply-Chain English Master Audit",
        "",
        f"Target: `{TARGET}`",
        "",
        "## Result",
        "",
        f"**{status}**",
        "",
        "## Summary",
        "",
    ]
    if counts:
        for label, count in sorted(counts.items()):
            report.append(f"- {label}: **{count}**")
    else:
        report.append("- No configured structural or placeholder markers found.")
    report.append(f"- Missing expected numbered sections: **{len(missing_sections)}**")
    report.append(f"- Sections not appearing exactly once: **{len(duplicate_sections)}**")
    report.append(f"- Missing required third-party-risk facts: **{len(missing_facts)}**")

    report.extend(["", "## Findings", ""])
    if findings:
        report.extend(["| Category | Line | Excerpt |", "|---|---:|---|"])
        for label, line, excerpt in sorted(findings, key=lambda item: (item[1], item[0])):
            report.append(f"| {label} | {line} | `{excerpt.replace('|', '\\|')}` |")
    else:
        report.append("No configured findings.")

    if missing_sections:
        report.extend(["", "### Missing sections", "", ", ".join(missing_sections)])
    if duplicate_sections:
        report.extend(["", "### Sections not appearing exactly once", "", ", ".join(duplicate_sections)])
    if missing_facts:
        report.extend(["", "### Missing required third-party-risk facts", ""])
        report.extend(f"- {item}" for item in missing_facts)

    report.extend([
        "",
        "## Review boundary",
        "",
        "This automated baseline checks structural integrity, placeholders, section counts, supplier-lifecycle concepts, due diligence, tiering, contracts, monitoring, supplier incidents, fourth-party and concentration risk, software supply-chain and SBOM limitations, exit planning, current NIST publication markers, and evidence testing. It does not replace detailed technical, editorial, legal, procurement, link, visual, accessibility, or standards-currentness review.",
        "",
    ])
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote {REPORT}: {status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
