#!/usr/bin/env python3
from pathlib import Path
import json,re
ROOT=Path('02-management-systems/ISO_IEC_27001_27002')
FILES={
 'en':ROOT/'English_Source_ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_v1.0.md',
 'es-419':ROOT/'Espanol/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md',
 'pt-BR':ROOT/'Portugues_BR/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md'}
OUTJ=Path('qa/ISO_IEC_27001_27002_SECTION_PARITY_AUDIT.json')
OUTM=Path('qa/ISO_IEC_27001_27002_SECTION_PARITY_AUDIT.md')
BAD=re.compile(r'\b(?:Silencioso|TEN(?:CIÓN|ENCIA)?|tención|La inmortalidad)\b|\|\. \||\b(?:Plain signification|Purpose|Shows root cause|Fulfillment of a requirement)\b',re.I)
HEAD=re.compile(r'^#\s+(\d+)\.\s+(.+)$',re.M)
def split(text):
 m=list(HEAD.finditer(text)); d={}
 for i,x in enumerate(m):
  n=int(x.group(1)); d[n]=text[x.start():(m[i+1].start() if i+1<len(m) else len(text))]
 return d
def metrics(s):
 lines=s.splitlines()
 return {'chars':len(s),'pipe_rows':sum(x.count('|')>=2 for x in lines),'images':len(re.findall(r'media/image\d+\.png',s,re.I)),'bad_hits':len(BAD.findall(s)),'english_fragments':sum(bool(re.search(r'\b(?:Purpose|Control|Evidence|Management Review|Statement of Applicability|People controls|Foundations)\b',x)) for x in lines)}
texts={k:p.read_text(encoding='utf-8') for k,p in FILES.items()}; secs={k:split(v) for k,v in texts.items()}; rows=[]
for n in range(1,29):
 e=metrics(secs['en'].get(n,'')); row={'section':n,'en':e}
 for lang in ('es-419','pt-BR'):
  m=metrics(secs[lang].get(n,'')); ratio=(m['chars']/e['chars']) if e['chars'] else 0
  blockers=[]
  if n not in secs[lang]: blockers.append('missing_heading')
  if e['pipe_rows']>=2 and m['pipe_rows']<max(2,e['pipe_rows']//3): blockers.append('table_structure_drift')
  if m['bad_hits']: blockers.append('corruption_tokens')
  if m['english_fragments']: blockers.append('residual_english')
  if ratio<0.45 or ratio>1.8: blockers.append('length_drift')
  row[lang]={**m,'length_ratio':round(ratio,3),'blockers':blockers,'status':'FAIL' if blockers else 'PASS'}
 rows.append(row)
OUTJ.write_text(json.dumps({'sections':rows},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
md=['# ISO Localized Section-Parity Audit','','This audit compares each localized major section with the approved English master. It is structural evidence, not native-language approval.','']
for lang in ('es-419','pt-BR'):
 bad=[r for r in rows if r[lang]['status']=='FAIL']; md += [f'## {lang}','',f'- Failing sections: {len(bad)} of 28','']
 for r in bad: md.append(f"- Section {r['section']}: {', '.join(r[lang]['blockers'])}")
 md.append('')
OUTM.write_text('\n'.join(md),encoding='utf-8')
failed=any(r[l]['status']=='FAIL' for r in rows for l in ('es-419','pt-BR'))
print('ISO section-parity audit:', 'FAIL' if failed else 'PASS')
raise SystemExit(1 if failed else 0)
