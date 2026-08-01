#!/usr/bin/env python3
from pathlib import Path
import json,re
ROOT=Path('02-management-systems/ISO_IEC_27001_27002')
ES=ROOT/'Espanol/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md'
EN=ROOT/'English_Source_ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_v1.0.md'
OUT=Path('qa/ISO_IEC_27001_27002_ES_FINAL_SECTION_DIAGNOSTIC.md')
HEAD=re.compile(r'^#\s+(\d+)\.\s+(.+)$',re.M)
ENG=re.compile(r'\b(?:Purpose|Evidence|Management Review|Statement of Applicability|People controls|Foundations)\b')
BAD=re.compile(r'\b(?:Silencioso|TEN(?:CIÓN|ENCIA)?|tención|La inmortalidad)\b|\|\. \||\b(?:Plain signification|Shows root cause|Fulfillment of a requirement)\b',re.I)
def split(text):
    ms=list(HEAD.finditer(text)); out={}
    for i,m in enumerate(ms): out[int(m.group(1))]=text[m.start():(ms[i+1].start() if i+1<len(ms) else len(text))]
    return out
es=split(ES.read_text(encoding='utf-8')); en=split(EN.read_text(encoding='utf-8'))
lines=['# ISO Spanish Final-Section Diagnostic','','Audit-only evidence for sections 1, 17, 25, and 28.','']
for n in (1,17,25,28):
    s=es.get(n,''); e=en.get(n,'')
    lines += [f'## Section {n}','',f'- Spanish characters: {len(s)}',f'- English characters: {len(e)}',f'- Spanish table rows: {sum(x.count("|")>=2 for x in s.splitlines())}',f'- English table rows: {sum(x.count("|")>=2 for x in e.splitlines())}']
    eh=[x.strip() for x in s.splitlines() if ENG.search(x)]
    bh=[x.strip() for x in s.splitlines() if BAD.search(x)]
    lines += [f'- Residual-English lines: {len(eh)}',f'- Corruption-token lines: {len(bh)}','']
    if eh:
        lines += ['### Residual-English lines','']+[f'- `{x}`' for x in eh]+['']
    if bh:
        lines += ['### Corruption-token lines','']+[f'- `{x}`' for x in bh]+['']
    table=[x for x in s.splitlines() if x.count('|')>=2]
    lines += ['### Spanish table lines','']+[f'```text\n{x}\n```' for x in table]+['']
OUT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(OUT)
