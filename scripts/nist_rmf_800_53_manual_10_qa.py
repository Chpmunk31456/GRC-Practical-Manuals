#!/usr/bin/env python3
"""Fail-closed preflight QA for Manual 10 — NIST RMF and SP 800-53."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '.compliance' / 'nist-rmf-800-53-manual-10-baseline.json'
REG = ROOT / '.compliance' / 'authoritative-sources.json'
SUPPLEMENT = ROOT / '.compliance' / 'nist-rmf-800-53-manual-10-sources.json'
CAT = ROOT / '.compliance' / 'manual-catalog.json'
MAN = ROOT / '01-foundations' / 'NIST_RMF_SP_800-53_Controlled_Implementation'
WF = ROOT / '.github' / 'workflows' / '22-nist-rmf-800-53-manual-10-qa.yml'

LANGUAGE_FILES = {
    'en': [
        MAN/'English/source/01_PREPARE_CATEGORIZE_CHAPTERS_01_08.md',
        MAN/'English/source/02_SELECT_IMPLEMENT_CHAPTERS_09_16.md',
        MAN/'English/source/03_ASSESS_AUTHORIZE_CHAPTERS_17_24.md',
        MAN/'English/source/04_MONITOR_CONTINUOUS_ASSURANCE_CHAPTERS_25_32.md',
    ],
    'es-419': [
        MAN/'Spanish_es-419/source/01_PREPARAR_CATEGORIZAR_CAPITULOS_01_08.md',
        MAN/'Spanish_es-419/source/02_SELECCIONAR_IMPLEMENTAR_CAPITULOS_09_16.md',
        MAN/'Spanish_es-419/source/03_EVALUAR_AUTORIZAR_CAPITULOS_17_24.md',
        MAN/'Spanish_es-419/source/04_MONITOREAR_ASEGURAMIENTO_CONTINUO_CAPITULOS_25_32.md',
    ],
    'pt-BR': [
        MAN/'Portuguese_pt-BR/source/01_PREPARAR_CATEGORIZAR_CAPITULOS_01_08.md',
        MAN/'Portuguese_pt-BR/source/02_SELECIONAR_IMPLEMENTAR_CAPITULOS_09_16.md',
        MAN/'Portuguese_pt-BR/source/03_AVALIAR_AUTORIZAR_CAPITULOS_17_24.md',
        MAN/'Portuguese_pt-BR/source/04_MONITORAR_ASSEGURACAO_CONTINUA_CAPITULOS_25_32.md',
    ],
}


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def normalized(text):
    return re.sub(r'\s+', ' ', text.casefold()).strip()


def chapter_numbers(text):
    return [int(x) for x in re.findall(r'(?mi)^##\s+(?:Chapter|Capítulo)\s+(\d+)\s+—', text)]


def main():
    errors = []
    try:
        base, reg, supplement, cat = load(BASE), load(REG), load(SUPPLEMENT), load(CAT)
    except Exception as exc:
        print(f'FAIL: {exc}')
        return 1

    if base.get('manual_id') != 'nist-rmf-800-53-manual-10':
        errors.append('unexpected manual id')
    if base.get('planned_publication_languages') != ['en', 'es-419', 'pt-BR']:
        errors.append('language plan changed')
    if base.get('rmf_steps') != ['PREPARE', 'CATEGORIZE', 'SELECT', 'IMPLEMENT', 'ASSESS', 'AUTHORIZE', 'MONITOR']:
        errors.append('RMF step sequence changed')

    if supplement.get('manual_id') != 'nist-rmf-800-53-manual-10':
        errors.append('unexpected Manual 10 source supplement id')

    shared_sources = [x for x in reg.get('sources', []) if isinstance(x, dict)]
    supplemental_sources = [x for x in supplement.get('sources', []) if isinstance(x, dict)]
    all_sources = shared_sources + supplemental_sources
    source_ids = {x.get('id') for x in all_sources}

    duplicate_ids = sorted({sid for sid in source_ids if sid and sum(1 for x in all_sources if x.get('id') == sid) > 1})
    if duplicate_ids:
        errors.append(f'duplicate authoritative source ids across registry/supplement: {duplicate_ids}')

    for sid in base.get('required_source_ids', []):
        if sid not in source_ids:
            errors.append(f'missing authoritative source id: {sid}')

    for sid in ['nist-sp-800-53b', 'nist-sp-800-18-r2']:
        matches = [x for x in supplemental_sources if x.get('id') == sid]
        if len(matches) != 1:
            errors.append(f'Manual 10 source supplement must contain exactly one {sid} record')
        elif matches[0].get('status') != 'final' or matches[0].get('last_verified') != '2026-08-27':
            errors.append(f'Manual 10 source supplement state invalid for {sid}')

    required_files = [
        MAN / 'README.md',
        MAN / 'MANUAL_10_IMPLEMENTATION_PATHS.md',
        MAN / 'qa' / 'SOURCE_VERIFICATION_2026-08-27.md',
        MAN / 'qa' / 'RELEASE_READINESS_PRESTAGE.md',
        MAN / 'qa' / 'LOCALIZATION_SEMANTIC_REVIEW_GATE.md',
        MAN / 'qa' / 'DOCUMENT_ACCESSIBILITY_PUBLICATION_QA_GATE.md',
    ]
    for path in required_files:
        if not path.is_file():
            errors.append(f'missing controlled preflight file: {path.relative_to(ROOT)}')

    for lang, files in LANGUAGE_FILES.items():
        missing = [str(p.relative_to(ROOT)) for p in files if not p.is_file()]
        if missing:
            errors.extend(f'missing {lang} source: {p}' for p in missing)
            continue
        language_text = '\n'.join(p.read_text(encoding='utf-8') for p in files)
        chapters = chapter_numbers(language_text)
        if chapters != list(range(1, 33)):
            errors.append(f'{lang} chapter inventory must be exactly 01-32, found {chapters}')
        if lang == 'es-419' and 'revisión semántica humana' not in language_text.casefold():
            errors.append('es-419 localization must retain explicit human semantic review boundary')
        if lang == 'pt-BR' and 'revisão semântica humana' not in language_text.casefold():
            errors.append('pt-BR localization must retain explicit human semantic review boundary')
        if lang == 'en':
            for step in base.get('rmf_steps', []):
                if step.casefold() not in language_text.casefold():
                    errors.append(f'English master missing RMF step: {step}')
            for boundary in ['no automatic authorization', 'human authorization decision', 'residual risk', 'evidence', 'oscal']:
                if boundary.casefold() not in language_text.casefold():
                    errors.append(f'English master missing assurance boundary/topic: {boundary}')

    text = ''
    for path in required_files[:2]:
        if path.is_file():
            text += '\n' + path.read_text(encoding='utf-8')
    norm = normalized(text)

    for step in base.get('rmf_steps', []):
        if step.casefold() not in norm:
            errors.append(f'missing RMF step in controlled narrative: {step}')

    for phrase in [
        'risk-based', 'tailorable', 'evidence-based',
        'no checklist-only compliance claim', 'no automatic authorization',
        'human authorization decision', 'oscal', 'plan of action and milestones',
    ]:
        if phrase.casefold() not in norm:
            errors.append(f'missing required boundary/topic: {phrase}')

    diagram_count = text.count('```mermaid')
    if diagram_count < 3:
        errors.append(f'expected at least 3 Mermaid learning graphics, found {diagram_count}')
    accessible_count = len(re.findall(r'(?im)^\*\*Accessible explanation', text))
    if accessible_count < 3:
        errors.append(f'expected at least 3 accessible graphic explanations, found {accessible_count}')

    matches = [x for x in cat.get('manuals', []) if x.get('id') == 'nist-rmf-800-53-controlled']
    if len(matches) != 1:
        errors.append('Manual 10 catalog entry missing or duplicated')
    else:
        entry = matches[0]
        if entry.get('status') != 'development' or entry.get('layout') != 'controlled-build' or entry.get('series_order') != 10:
            errors.append('Manual 10 catalog entry invalid')

    if not WF.is_file():
        errors.append('Manual 10 QA workflow missing')
    else:
        workflow = WF.read_text(encoding='utf-8')
        if 'permissions:\n  contents: read' not in workflow:
            errors.append('workflow not read-only')
        if re.search(r'(?m)^\s*push:\s*$', workflow):
            errors.append('workflow must not push')
        if 'pull_request_target' in workflow:
            errors.append('workflow must not use pull_request_target')

    print('Manual 10 NIST RMF / SP 800-53 preflight QA')
    for error in errors:
        print('  ERROR:', error)
    if errors:
        print('FAIL')
        return 1
    print('PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
