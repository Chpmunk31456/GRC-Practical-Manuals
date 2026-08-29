#!/usr/bin/env python3
"""Fail-closed controlled-build QA for Manual 11 — GDPR."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '.compliance' / 'gdpr-manual-11-baseline.json'
SOURCES = ROOT / '.compliance' / 'gdpr-manual-11-sources.json'
CAT = ROOT / '.compliance' / 'manual-catalog.json'
MAN = ROOT / '04-regulatory-compliance' / 'GDPR_Controlled_Implementation'
WF = ROOT / '.github' / 'workflows' / '30-gdpr-manual-11-qa.yml'

ENGLISH_MASTER = [
    MAN/'English/source/01_FOUNDATIONS_CHAPTERS_01_08.md',
    MAN/'English/source/02_LAWFULNESS_RIGHTS_DESIGN_CHAPTERS_09_16.md',
    MAN/'English/source/03_DPIA_SECURITY_BREACH_TRANSFERS_CHAPTERS_17_24.md',
    MAN/'English/source/04_GOVERNANCE_ENFORCEMENT_EMERGING_TECH_CHAPTERS_25_32.md',
]

REQUIRED_GATES = [
    MAN/'qa/SOURCE_VERIFICATION_2026-08-27.md',
    MAN/'qa/LOCALIZATION_SEMANTIC_REVIEW_GATE.md',
    MAN/'qa/DOCUMENT_ACCESSIBILITY_PUBLICATION_QA_GATE.md',
    MAN/'qa/RELEASE_READINESS_PRESTAGE.md',
]


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def chapter_numbers(text):
    return [int(x) for x in re.findall(r'(?mi)^##\s+Chapter\s+(\d+)\s+—', text)]


def main():
    errors = []
    try:
        base, sources, catalog = load(BASE), load(SOURCES), load(CAT)
    except Exception as exc:
        print(f'FAIL: {exc}')
        return 1

    if base.get('manual_id') != 'gdpr-controlled-manual-11':
        errors.append('unexpected Manual 11 id')
    if base.get('series_order') != 11:
        errors.append('series order must be 11')
    if base.get('planned_publication_languages') != ['en', 'es-419', 'pt-BR']:
        errors.append('language plan changed')
    if not base.get('training_grade'):
        errors.append('training-grade requirement missing')

    if sources.get('manual_id') != 'gdpr-controlled-manual-11':
        errors.append('unexpected source supplement id')
    source_rows = [x for x in sources.get('sources', []) if isinstance(x, dict)]
    source_ids = {x.get('id') for x in source_rows}
    for sid in base.get('required_source_ids', []):
        if sid not in source_ids:
            errors.append(f'missing controlled source id: {sid}')

    gdpr = [x for x in source_rows if x.get('id') == 'eu-gdpr-2016-679']
    if len(gdpr) != 1 or gdpr[0].get('source_type') != 'binding-law' or gdpr[0].get('status') != 'in-force':
        errors.append('GDPR binding-law source classification invalid')
    edpb = [x for x in source_rows if str(x.get('id', '')).startswith('edpb-')]
    if not edpb or any(x.get('source_type') != 'non-binding-official-guidance' for x in edpb):
        errors.append('EDPB guidance must remain non-binding official guidance')

    missing = [str(p.relative_to(ROOT)) for p in ENGLISH_MASTER if not p.is_file()]
    if missing:
        errors.extend(f'missing English master source: {p}' for p in missing)
    else:
        master = '\n'.join(p.read_text(encoding='utf-8') for p in ENGLISH_MASTER)
        chapters = chapter_numbers(master)
        if chapters != list(range(1, 33)):
            errors.append(f'English chapter inventory must be exactly 01-32, found {chapters}')
        for concept in [
            'lawful basis', 'data-subject rights', 'DPIA', 'security of processing',
            'personal-data breach', 'processor', 'international transfers',
            'DPO', 'automated decision', 'Final Human Release Approval'
        ]:
            if concept.casefold() not in master.casefold():
                errors.append(f'English master missing required topic/boundary: {concept}')

    for path in REQUIRED_GATES:
        if not path.is_file():
            errors.append(f'missing release-control file: {path.relative_to(ROOT)}')

    readme = (MAN/'README.md').read_text(encoding='utf-8') if (MAN/'README.md').is_file() else ''
    paths = (MAN/'MANUAL_11_IMPLEMENTATION_PATHS.md').read_text(encoding='utf-8') if (MAN/'MANUAL_11_IMPLEMENTATION_PATHS.md').is_file() else ''
    narrative = readme + '\n' + paths
    for phrase in [
        'binding law', 'non-binding official guidance', 'no automatic lawful-basis determination',
        'no automatic DPIA sufficiency determination', 'no automatic breach-notification determination',
        'human legal and privacy judgment'
    ]:
        if phrase.casefold() not in narrative.casefold() and phrase.casefold() not in json.dumps(base).casefold():
            errors.append(f'missing controlled legal boundary: {phrase}')

    if paths.count('```mermaid') != 3:
        errors.append('expected exactly three Mermaid learning graphics')
    if paths.count('**Accessible explanation:**') != 3:
        errors.append('each learning graphic requires an accessible explanation')

    entries = [x for x in catalog.get('manuals', []) if x.get('id') == 'gdpr-controlled']
    if len(entries) != 1:
        errors.append('Manual 11 catalog entry missing or duplicated')
    else:
        entry = entries[0]
        if entry.get('status') != 'development' or entry.get('layout') != 'controlled-build' or entry.get('series_order') != 11:
            errors.append('Manual 11 catalog entry invalid')

    if not WF.is_file():
        errors.append('Manual 11 workflow missing')
    else:
        workflow = WF.read_text(encoding='utf-8')
        if 'permissions:\n  contents: read' not in workflow:
            errors.append('workflow not read-only')
        if re.search(r'(?m)^\s*push:\s*$', workflow):
            errors.append('workflow must not push')
        if 'pull_request_target' in workflow:
            errors.append('workflow must not use pull_request_target')

    print('Manual 11 GDPR controlled-build QA')
    for error in errors:
        print('  ERROR:', error)
    if errors:
        print('FAIL')
        return 1
    print('PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
