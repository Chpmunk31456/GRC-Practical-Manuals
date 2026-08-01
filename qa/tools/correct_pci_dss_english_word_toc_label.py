#!/usr/bin/env python3
from pathlib import Path

TARGET = Path("04-regulatory-compliance/PCI_DSS_v4.0.1/English_Source_PCI_DSS_v4.0.1_Practical_Manager_and_Junior_Analyst_Manual_v1.0.md")
OLD = "**True Word contents:**"
NEW = "**Word table of contents:**"


def main() -> int:
    text = TARGET.read_text(encoding="utf-8")
    count = text.count(OLD)
    if count != 1:
        raise SystemExit(f"Expected exactly one occurrence of {OLD!r}; found {count}")
    TARGET.write_text(text.replace(OLD, NEW, 1), encoding="utf-8")
    print(f"Corrected one Word table-of-contents label in {TARGET}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
