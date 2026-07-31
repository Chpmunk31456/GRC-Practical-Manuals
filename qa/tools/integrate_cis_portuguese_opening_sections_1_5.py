#!/usr/bin/env python3
from pathlib import Path
import re

TARGET = Path('01-foundations/CIS_Controls_v8.1/Portugues_BR/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md')
REPLACEMENT = Path('qa/rewrite/CIS_CONTROLS_V8_1_PTBR_OPENING_SECTIONS_1_5_REVIEWED.md')

text = TARGET.read_text(encoding='utf-8')
replacement = REPLACEMENT.read_text(encoding='utf-8').rstrip() + '\n\n'

boundary = re.compile(r'^#\s*6\.\s*Controle\s+1\b.*$', re.MULTILINE | re.IGNORECASE)
matches = list(boundary.finditer(text))
if len(matches) != 1:
    raise SystemExit(f'Expected exactly one Control 1 boundary; found {len(matches)}')

new_text = replacement + text[matches[0].start():]
opening = new_text[:new_text.index(text[matches[0].start():])]

for marker in ['# 1.', '# 2.', '# 3.', '# 4.', '# 5.']:
    if opening.count(marker) != 1:
        raise SystemExit(f'Expected exactly one opening marker: {marker}')

for marker in ['media/image1.png', 'media/image2.png', 'media/image3.png']:
    if opening.count(marker) != 1:
        raise SystemExit(f'Expected exactly one image reference: {marker}')

for token in ['□', '■img', '# # ', 'No interior:**', '*Conteúdo:**']:
    if token in opening:
        raise SystemExit(f'Forbidden opening corruption token remains: {token}')

if new_text.count('# 6. Controle 1') != 1:
    raise SystemExit('Control 1 boundary was not preserved exactly once')

TARGET.write_text(new_text, encoding='utf-8')
print('Integrated reviewed CIS Portuguese opening and Sections 1-5')
