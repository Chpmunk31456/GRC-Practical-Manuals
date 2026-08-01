#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

TARGET = Path("06-cloud-and-technology-risk/Cloud_Security_and_Compliance/English_Source_Cloud_Security_and_Cloud_Compliance_Practical_Manager_and_Junior_Analyst_Manual_v1.0.md")
REPORT = Path("qa/CLOUD_SECURITY_COMPLIANCE_ENGLISH_MASTER_AUDIT.md")

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
    "shared responsibility": "Shared Responsibility",
    "IaaS": "IaaS",
    "PaaS": "PaaS",
    "SaaS": "SaaS",
    "identity and privileged access": "Identity and Privileged Access",
    "data security and privacy": "Data Security and Privacy",
    "encryption and key management": "Encryption, Keys, Certificates, and Secrets",
    "logging and monitoring": "Logging, Monitoring, and Detection",
    "infrastructure as code": "Infrastructure as Code",
    "containers and Kubernetes": "Containers and Kubernetes",
    "resilience and disaster recovery": "Resilience, Backup, and Disaster Recovery",
    "cloud incident response": "Cloud Incident Response and Forensics",
    "CSA CCM v4.1": "CSA Cloud Controls Matrix v4.1",
    "207 controls": "207 control objectives",
    "17 domains": "17 domains",
    "January 2026 release": "January 2026",
    "provider evidence": "Cloud Assurance and Provider Evidence",
    "evidence testing": "Assessment, Evidence Testing, and Metrics",
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
        "# Cloud Security and Compliance English Master Audit",
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
    report.append(f"- Missing required cloud-security facts: **{len(missing_facts)}**")

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
        report.extend(["", "### Missing required cloud-security facts", ""])
        report.extend(f"- {item}" for item in missing_facts)

    report.extend([
        "",
        "## Currentness note",
        "",
        "The dedicated CSA CCM/CAIQ v4.1 release artifact identifies v4.1 as the January 2026 release with 207 controls across 17 domains. A separate CSA landing page may retain an older control count; the version-specific release artifact governs this baseline.",
        "",
        "## Review boundary",
        "",
        "This automated baseline checks structural integrity, placeholders, section counts, shared-responsibility and service-model concepts, identity, data, encryption, logging, IaC, Kubernetes, resilience, incident response, CSA CCM v4.1 markers, provider evidence, and testing concepts. It does not replace detailed technical, editorial, legal, link, visual, accessibility, provider-specific, or standards-currentness review.",
        "",
    ])
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote {REPORT}: {status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
