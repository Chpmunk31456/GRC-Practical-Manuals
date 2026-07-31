#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

TARGET = Path("05-operational-resilience/Incident_Response_BCDR/English_Source_Incident_Response_Business_Continuity_and_Disaster_Recovery_Manual_v1.0.md")
REPORT = Path("qa/INCIDENT_RESPONSE_BCDR_ENGLISH_MASTER_AUDIT.md")

PATTERNS = {
    "conversion box glyph": re.compile(r"□"),
    "broken image marker": re.compile(r"^[■□]img\b", re.MULTILINE | re.IGNORECASE),
    "double heading marker": re.compile(r"^#\s+#\s+", re.MULTILINE),
    "raw separator line": re.compile(r"^-{20,}$", re.MULTILINE),
    "empty markdown link": re.compile(r"\[[^\]]+\]\(\s*\)"),
    "placeholder token": re.compile(r"\b(?:TBD|TODO|FIXME|PLACEHOLDER)\b", re.IGNORECASE),
    "malformed Word contents label": re.compile(r"\*\*True Word contents:\*\*", re.IGNORECASE),
}

REQUIRED_SECTIONS = [re.compile(rf"^#\s+{n}\.\s+", re.MULTILINE) for n in range(1, 30)]
REQUIRED_FACTS = {
    "NIST SP 800-61 Rev. 3": "NIST SP 800-61 Rev. 3",
    "April 3, 2025": "April 3, 2025",
    "NIST SP 800-34 Rev. 1 Update 1": "NIST SP 800-34 Rev. 1 Update 1",
    "ISO 22301:2019": "ISO 22301:2019",
    "Amendment 1:2024": "Amendment 1:2024",
    "business impact analysis": "Business Impact Analysis",
    "incident preparation": "# 5. Preparation and Readiness",
    "detection": "# 6. Detection and Event Validation",
    "containment": "# 9. Containment Strategy",
    "eradication": "# 10. Eradication and Remediation",
    "recovery": "# 11. Recovery and Return to Service",
    "lessons learned": "# 12. Lessons Learned and Improvement",
    "business continuity": "# 19. Business Continuity Management System",
    "disaster recovery": "# 21. Disaster Recovery Planning",
    "RTO": "RTO",
    "RPO": "RPO",
    "exercises": "# 24. Exercises, Training, and Plan Maintenance",
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
        "# Incident Response and BCDR English Master Audit",
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
    report.append(f"- Missing required resilience facts: **{len(missing_facts)}**")

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
        report.extend(["", "### Missing required resilience facts", "", "\n".join(f"- {item}" for item in missing_facts)])

    report.extend([
        "",
        "## Review boundary",
        "",
        "This automated baseline checks structural integrity, placeholders, section counts, current NIST and ISO publication markers, and core incident-response, continuity, recovery, exercise, and evidence concepts. It does not replace detailed technical, editorial, legal, link, visual, accessibility, or standards-currentness review.",
        "",
    ])
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote {REPORT}: {status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
