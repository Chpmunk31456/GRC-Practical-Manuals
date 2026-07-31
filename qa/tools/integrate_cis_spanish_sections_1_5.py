#!/usr/bin/env python3
from pathlib import Path
import re

TARGET = Path('01-foundations/CIS_Controls_v8.1/Espanol/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md')
REPLACEMENT = Path('qa/rewrite/CIS_CONTROLS_V8_1_ES_SECTIONS_1_5_REVIEWED.md')

text = TARGET.read_text(encoding='utf-8')
replacement = REPLACEMENT.read_text(encoding='utf-8').rstrip() + '\n\n'

# The corrupted source does not consistently preserve the period after the
# section number. Match a line-level Section 1 heading and the exact bounded
# Section 6 / Control 1 endpoint. Fail closed if either boundary is ambiguous.
start_matches = list(re.finditer(r'^#\s*1(?:\.|\s)\s*.*$', text, flags=re.MULTILINE))
end_matches = list(re.finditer(r'^#\s*6\.\s*Control\s+1\b.*$', text, flags=re.MULTILINE | re.IGNORECASE))

if len(start_matches) != 1:
    raise SystemExit(f'Expected exactly one Section 1 boundary; found {len(start_matches)}')
if len(end_matches) != 1:
    raise SystemExit(f'Expected exactly one Section 6 / Control 1 boundary; found {len(end_matches)}')

start = start_matches[0].start()
end = end_matches[0].start()
if end <= start:
    raise SystemExit('Section 6 boundary occurs before Section 1 boundary')

new_text = text[:start] + replacement + text[end:]

for marker in [f'# {n}.' for n in range(1, 6)]:
    if new_text.count(marker) != 1:
        raise SystemExit(f'Expected exactly one marker after replacement: {marker}')

new_start = new_text.find('# 1.')
new_end = new_text.find('# 6.', new_start + 1)
if new_start < 0 or new_end < 0 or new_end <= new_start:
    raise SystemExit('Unable to validate replacement boundaries')

block = new_text[new_start:new_end]
for token in ['■img', '|... |', '← Salvaguardia', 'Silencioso Propietario', 'TEN IT / Engineering', 'tención Auditoría']:
    if token in block:
        raise SystemExit(f'Forbidden corruption token remains in replacement block: {token}')

TARGET.write_text(new_text, encoding='utf-8')
print('Integrated reviewed CIS Spanish Sections 1-5')
