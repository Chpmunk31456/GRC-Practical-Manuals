#!/usr/bin/env python3
"""Fail-closed controlled intake QA for the AI Governance and Audit Toolkit."""

import json, re, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'.compliance'/'ai-governance-audit-toolkit-baseline.json'
SCHEMAS=ROOT/'08-templates-and-tools'/'AI_Governance_and_Audit_Toolkit'/'TEMPLATE_SCHEMAS.json'
README=ROOT/'08-templates-and-tools'/'AI_Governance_and_Audit_Toolkit'/'README.md'
AAIA=ROOT/'.compliance'/'isaca-aaia-source.json'
CAT=ROOT/'.compliance'/'manual-catalog.json'
WF=ROOT/'.github'/'workflows'/'17-ai-governance-audit-toolkit-qa.yml'

def load(p): return json.loads(p.read_text(encoding='utf-8'))

def main():
    errors=[]
    try:
        base, schemas, aaia, cat = load(BASE), load(SCHEMAS), load(AAIA), load(CAT)
    except Exception as exc:
        print(f'FAIL: {exc}'); return 1
    if base.get('toolkit_id')!='ai-governance-audit-toolkit': errors.append('unexpected toolkit id')
    if base.get('planned_publication_languages')!=['en','es-419','pt-BR']: errors.append('language plan changed')
    planned=base.get('planned_tools',[])
    actual=list(schemas.get('tools',{}).keys())
    if planned!=actual: errors.append('planned tool list and schema pack differ')
    if len(actual)!=9: errors.append('toolkit must retain nine controlled tools')
    common=set(base.get('required_fields_across_toolkit',[]))
    schema_common=set(schemas.get('common_control_fields',[]))
    if common-schema_common: errors.append('schema pack missing required common control fields')
    for name, fields in schemas.get('tools',{}).items():
        if len(fields)!=len(set(fields)): errors.append(f'duplicate fields in {name}')
        for required in ('record_id','status'):
            if required not in fields: errors.append(f'{name} missing {required}')
        if 'evidence' not in fields: errors.append(f'{name} missing evidence')
        if 'decision' not in fields: errors.append(f'{name} missing decision')
        if 'reviewer' not in fields or 'review_date' not in fields: errors.append(f'{name} missing human review fields')
    if aaia.get('source_id')!='isaca-aaia': errors.append('controlled AAIA source missing')
    readme=README.read_text(encoding='utf-8') if README.is_file() else ''
    for domain in ('AI Governance and Risk','AI Operations','AI Auditing Tools and Techniques'):
        if domain not in readme: errors.append(f'toolkit README missing AAIA domain: {domain}')
    matches=[x for x in cat.get('manuals',[]) if x.get('id')=='ai-governance-audit-toolkit']
    if len(matches)!=1 or matches[0].get('status')!='development' or matches[0].get('layout')!='toolkit': errors.append('catalog toolkit entry invalid')
    if not WF.is_file(): errors.append('workflow missing')
    else:
        text=WF.read_text(encoding='utf-8')
        if 'permissions:\n  contents: read' not in text: errors.append('workflow not read-only')
        if re.search(r'(?m)^\s*push:\s*$',text): errors.append('workflow must not push')
    print('AI Governance and Audit Toolkit QA')
    print(f'  schemas checked: {len(actual)}')
    for e in errors: print('  ERROR:',e)
    if errors: print('FAIL'); return 1
    print('PASS'); return 0

if __name__=='__main__': sys.exit(main())
