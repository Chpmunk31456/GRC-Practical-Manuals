#!/usr/bin/env python3
from pathlib import Path

TARGET = Path("01-foundations/NIST_CSF_2/English_Source_NIST_CSF_2_Practical_GRC_and_Junior_Analyst_Manual_v1.0.md")
OLD = "**True Word contents:**"
NEW = "**Word table of contents:**"

text = TARGET.read_text(encoding="utf-8")
count = text.count(OLD)
if count != 1:
    raise SystemExit(f"Expected exactly one '{OLD}' marker, found {count}")
TARGET.write_text(text.replace(OLD, NEW, 1), encoding="utf-8")
print(f"Corrected Word table-of-contents label in {TARGET}")
