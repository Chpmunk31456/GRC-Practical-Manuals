#!/usr/bin/env python3
from pathlib import Path
import re

TARGET = Path('01-foundations/CIS_Controls_v8.1/Portugues_BR/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md')
REPLACEMENT = Path('qa/rewrite/CIS_CONTROLS_V8_1_PTBR_SECTIONS_27_30_REVIEWED.md')

text = TARGET.read_text(encoding='utf-8')
replacement = REPLACEMENT.read_text(encoding='utf-8').rstrip() + '\n'

boundary = re.compile(r'^#\s*27\.\s*Laborat[oó]rio\b.*$', re.MULTILINE | re.IGNORECASE)
matches = list(boundary.finditer(text))
if len(matches) != 1:
    raise SystemExit(f'Expected exactly one Section 27 boundary; found {len(matches)}')

new_text = text[:matches[0].start()] + replacement
block = replacement

for section in range(27, 31):
    found = re.findall(rf'^#\s+{section}\.\s+.+$', block, flags=re.MULTILINE)
    if len(found) != 1:
        raise SystemExit(f'Expected exactly one level-one heading for Section {section}; found {len(found)}')

for token in ['□', '# # ', '. . . . . .', '■img']:
    if token in block:
        raise SystemExit(f'Forbidden corruption token remains in Sections 27-30: {token}')

for url in [
    'https://www.cisecurity.org/controls/v8-1',
    'https://www.cisecurity.org/controls/cis-controls-list',
    'https://www.cisecurity.org/controls/implementation-groups',
    'https://www.cisecurity.org/controls/cis-controls-assessment-specification',
]:
    if block.count(url) != 1:
        raise SystemExit(f'Expected exactly one official reference: {url}')

TARGET.write_text(new_text, encoding='utf-8')
print('Integrated reviewed CIS Portuguese Sections 27-30')
