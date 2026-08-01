#!/usr/bin/env python3
"""Remove exactly two standalone collapsed table-rule remnants from ISO PT-BR source."""
from pathlib import Path
import re

path = Path('02-management-systems/ISO_IEC_27001_27002/Portugues_BR/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md')
text = path.read_text(encoding='utf-8')
lines = text.splitlines()
indexes = [i for i, line in enumerate(lines) if re.fullmatch(r'-{20,}', line)]
if len(indexes) != 2:
    raise SystemExit(f'expected exactly 2 standalone collapsed rule rows, found {len(indexes)}')
for i in reversed(indexes):
    del lines[i]
updated = '\n'.join(lines) + ('\n' if text.endswith('\n') else '')
if re.search(r'(?m)^-{20,}$', updated):
    raise SystemExit('collapsed rule row remains after bounded cleanup')
path.write_text(updated, encoding='utf-8')
print('Removed exactly two standalone ISO PT-BR collapsed rule rows')
