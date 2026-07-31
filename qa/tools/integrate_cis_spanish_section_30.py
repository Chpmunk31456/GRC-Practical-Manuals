#!/usr/bin/env python3
from pathlib import Path
import re

TARGET = Path('01-foundations/CIS_Controls_v8.1/Espanol/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md')
REPLACEMENT = Path('qa/rewrite/CIS_CONTROLS_V8_1_ES_SECTION_30_REVIEWED.md')

text = TARGET.read_text(encoding='utf-8')
replacement = REPLACEMENT.read_text(encoding='utf-8').rstrip() + '\n'

boundary_pattern = r'^#\s*30\.\s*Plantillas,\s*Glosario,\s*Índice\s*y\s*Referencias\s*$'
matches = list(re.finditer(boundary_pattern, text, flags=re.MULTILINE | re.IGNORECASE))
if len(matches) != 1:
    raise SystemExit(f'Expected exactly one Section 30 boundary; found {len(matches)}')

section_start = matches[0].start()
prefix = text[:section_start]
old_section = text[section_start:]

# The current residual state must contain one malformed delimiter in the cover
# and two inside the corrupted Section 30 block that will be replaced.
if prefix.count('|... |') != 1:
    raise SystemExit(f'Expected exactly one cover ellipsis delimiter; found {prefix.count("|... |")}')
if old_section.count('|... |') != 2:
    raise SystemExit(f'Expected exactly two Section 30 ellipsis delimiters; found {old_section.count("|... |")}')

prefix = prefix.replace('|... |', '|---|', 1)
new_text = prefix + replacement
block = replacement

for marker in ['## 30.1', '## 30.2', '## 30.3', '## 30.4', '## 30.5']:
    if block.count(marker) != 1:
        raise SystemExit(f'Expected exactly one marker: {marker}')

for token in ['Silencioso', 'TEN ', 'TENCIÓN', 'tención', '←', '|... |', '■img']:
    if token in block:
        raise SystemExit(f'Forbidden corruption token remains in Section 30: {token}')

for url in [
    'https://www.cisecurity.org/controls/v8-1',
    'https://www.cisecurity.org/controls/cis-controls-list',
    'https://www.cisecurity.org/controls/implementation-groups',
    'https://www.cisecurity.org/controls/cis-controls-assessment-specification',
]:
    if block.count(url) != 1:
        raise SystemExit(f'Expected exactly one official reference: {url}')

TARGET.write_text(new_text, encoding='utf-8')
print('Integrated reviewed CIS Spanish Section 30 and repaired cover delimiter')
