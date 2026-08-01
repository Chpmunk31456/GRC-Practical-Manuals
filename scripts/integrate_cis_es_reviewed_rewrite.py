#!/usr/bin/env python3
"""Integrate the reviewed CIS Controls Spanish sections 23-24.

This script replaces exactly one source range, beginning with section 23 and
ending immediately before section 25. It fails closed if the expected markers,
row counts, tools, or forbidden corruption tokens do not match.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "01-foundations/CIS_Controls_v8.1/Espanol/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md"
REVIEWED = ROOT / "qa/rewrite/CIS_CONTROLS_V8_1_ES_CONTROL_18_AND_TOOLS_REVIEWED.md"

START = "# 23. Control 18 — Pruebas de penetración"
ACCEPTANCE = "## Criterios de aceptación para la integración"
SOURCE_RANGE = re.compile(r"(?ms)^# 23\..*?(?=^# 25\.)")
FORBIDDEN = ("TEN", "TEN TODO", "tención", "Silencioso", "tóxico")
TOOLS = (
    "CIS Controls Navigator",
    "CIS Controls Assessment Specification",
    "CIS-CAT Lite",
    "CISO Assistant",
    "Wazuh",
    "osquery",
    "OpenSCAP",
    "Lynis",
    "Nmap",
    "Greenbone Community Edition",
    "Trivy",
    "OWASP ZAP",
    "Suricata",
    "Keycloak",
    "DefectDojo",
    "Velociraptor",
)


def fail(message: str) -> None:
    raise SystemExit(f"INTEGRATION ERROR: {message}")


def main() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    reviewed = REVIEWED.read_text(encoding="utf-8")

    if START not in reviewed:
        fail("reviewed section 23 marker is missing")
    if ACCEPTANCE not in reviewed:
        fail("reviewed acceptance marker is missing")

    replacement = reviewed.split(START, 1)[1]
    replacement = START + replacement.split(ACCEPTANCE, 1)[0].rstrip() + "\n\n"

    matches = list(SOURCE_RANGE.finditer(source))
    if len(matches) != 1:
        fail(f"expected exactly one sections 23-24 source range, found {len(matches)}")

    safeguard_rows = re.findall(r"^\| 18\.[1-5] \|", replacement, flags=re.MULTILINE)
    if len(safeguard_rows) != 5:
        fail(f"expected five Control 18 safeguard rows, found {len(safeguard_rows)}")

    missing_tools = [tool for tool in TOOLS if f"| {tool} |" not in replacement]
    if missing_tools:
        fail(f"reviewed tools matrix is incomplete: {missing_tools}")

    for token in FORBIDDEN:
        if token in replacement:
            fail(f"forbidden corruption token remains in replacement: {token!r}")

    updated, count = SOURCE_RANGE.subn(replacement, source, count=1)
    if count != 1:
        fail(f"replacement count was {count}, expected 1")
    if updated == source:
        fail("replacement produced no source change")
    if updated.count("# 23. Control 18") != 1:
        fail("section 23 heading count is not exactly one after replacement")
    if updated.count("# 24. Herramientas de código abierto") != 1:
        fail("section 24 heading count is not exactly one after replacement")

    SOURCE.write_text(updated, encoding="utf-8")
    print(f"Integrated reviewed CIS Spanish sections 23-24 into {SOURCE.relative_to(ROOT)}")
    print("Validated 5 safeguard rows, 16 tools, exact boundaries, and forbidden-token removal.")


if __name__ == "__main__":
    main()
