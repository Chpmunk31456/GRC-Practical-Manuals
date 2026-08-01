#!/usr/bin/env python3
from pathlib import Path

TARGET = Path("02-management-systems/ISO_IEC_27001_27002/English_Source_ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_v1.0.md")

old = "**True Word contents:**"
new = "**Word table of contents:**"

text = TARGET.read_text(encoding="utf-8")
count = text.count(old)
if count != 1:
    raise SystemExit(f"Expected exactly one label to replace; found {count}")
TARGET.write_text(text.replace(old, new, 1), encoding="utf-8")
print(f"Corrected {TARGET}")
