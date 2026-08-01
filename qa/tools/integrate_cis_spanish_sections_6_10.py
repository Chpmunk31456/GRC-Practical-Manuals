#!/usr/bin/env python3
from pathlib import Path
import re

TARGET = Path('01-foundations/CIS_Controls_v8.1/Espanol/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md')
REPLACEMENT = Path('qa/rewrite/CIS_CONTROLS_V8_1_ES_SECTIONS_6_10_REVIEWED.md')

text = TARGET.read_text(encoding='utf-8')
replacement = REPLACEMENT.read_text(encoding='utf-8').rstrip() + '\n\n'

start_matches = list(re.finditer(r'^#\s*6\.\s*Control\s+1\b.*$', text, flags=re.MULTILINE | re.IGNORECASE))
end_matches = list(re.finditer(r'^#\s*11\.\s*Control\s+6\b.*$', text, flags=re.MULTILINE | re.IGNORECASE))

if len(start_matches) != 1:
    raise SystemExit(f'Expected exactly one Section 6 / Control 1 boundary; found {len(start_matches)}')
if len(end_matches) != 1:
    raise SystemExit(f'Expected exactly one Section 11 / Control 6 boundary; found {len(end_matches)}')

start = start_matches[0].start()
end = end_matches[0].start()
if end <= start:
    raise SystemExit('Section 11 boundary occurs before Section 6 boundary')

new_text = text[:start] + replacement + text[end:]

for marker in [f'# {n}.' for n in range(6, 11)]:
    if new_text.count(marker) != 1:
        raise SystemExit(f'Expected exactly one marker after replacement: {marker}')

new_start = new_text.find('# 6.')
new_end_match = re.search(r'^#\s*11\.\s*Control\s+6\b.*$', new_text, flags=re.MULTILINE | re.IGNORECASE)
if new_start < 0 or new_end_match is None or new_end_match.start() <= new_start:
    raise SystemExit('Unable to validate replacement boundaries')

block = new_text[new_start:new_end_match.start()]
for token in ['■img', 'יimg', '|... |', 'TEN ', 'Silencioso', '←', 'Ø']:
    if token in block:
        raise SystemExit(f'Forbidden corruption token remains in replacement block: {token}')

# Detect the known standalone corruption token without rejecting legitimate
# Spanish words such as "retención".
if re.search(r'(?<![A-Za-zÁÉÍÓÚÜÑáéíóúüñ])tención(?![A-Za-zÁÉÍÓÚÜÑáéíóúüñ])', block, flags=re.IGNORECASE):
    raise SystemExit('Forbidden corruption token remains in replacement block: tención')

for image in ['media/image4.png', 'media/image5.png']:
    if block.count(image) != 1:
        raise SystemExit(f'Expected exactly one valid image reference: {image}')

TARGET.write_text(new_text, encoding='utf-8')
print('Integrated reviewed CIS Spanish Sections 6-10')
