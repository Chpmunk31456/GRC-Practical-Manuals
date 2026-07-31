#!/usr/bin/env python3
from pathlib import Path

TARGET = Path("01-foundations/CIS_Controls_v8.1/English_Source_CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_v1.0.md")
OLD = "**True Word contents:**"
NEW = "**Word table of contents:**"

text = TARGET.read_text(encoding="utf-8")
count = text.count(OLD)
if count != 1:
    raise SystemExit(f"Expected exactly one malformed Word contents label; found {count}")
text = text.replace(OLD, NEW)
if OLD in text or text.count(NEW) != 1:
    raise SystemExit("Word table-of-contents label correction did not validate")
TARGET.write_text(text, encoding="utf-8")
print("Corrected CIS English Word table-of-contents label")
