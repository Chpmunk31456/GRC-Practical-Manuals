#!/usr/bin/env python3
import json
from pathlib import Path

CATALOG = Path('.compliance/manual-catalog.json')
RELEASES = Path('.compliance/work-product-releases.json')
MID = 'ai-privacy-automated-decision-governance-controlled'
TITLE = 'Manual 28 — AI Privacy & Automated Decision Governance Controlled Implementation'
ROOT = '04-regulatory-compliance/AI_Privacy_Automated_Decision_Governance'

EXPECTED = [
    Path(ROOT) / 'publication/en/Manual_28_AI_Privacy_Automated_Decision_Governance_Controlled_EN.docx',
    Path(ROOT) / 'publication/en/Manual_28_AI_Privacy_Automated_Decision_Governance_Controlled_EN.pdf',
    Path(ROOT) / 'publication/es-419/Manual_28_AI_Privacy_Automated_Decision_Governance_Controlled_ES-419.docx',
    Path(ROOT) / 'publication/es-419/Manual_28_AI_Privacy_Automated_Decision_Governance_Controlled_ES-419.pdf',
    Path(ROOT) / 'publication/pt-BR/Manual_28_AI_Privacy_Automated_Decision_Governance_Controlled_PT-BR.docx',
    Path(ROOT) / 'publication/pt-BR/Manual_28_AI_Privacy_Automated_Decision_Governance_Controlled_PT-BR.pdf',
]

catalog = json.loads(CATALOG.read_text(encoding='utf-8'))
releases = json.loads(RELEASES.read_text(encoding='utf-8'))

if not any(x.get('series_order') == 27 and x.get('status') == 'published' and x.get('release_state') == 'published' for x in catalog['manuals']):
    raise SystemExit('Manual 27 predecessor is not published in catalog')
if not any(x.get('id') == 'data-governance-privacy-engineering-controlled' and x.get('release_state') == 'published' for x in releases['released_work_products']):
    raise SystemExit('Manual 27 predecessor is not published in release registry')

missing = [str(p) for p in EXPECTED if not p.is_file() or p.stat().st_size == 0]
if missing:
    raise SystemExit('Missing or empty exact publication artifacts: ' + ', '.join(missing))

catalog_entry = {
    'id': MID,
    'title': TITLE,
    'path': ROOT,
    'status': 'published',
    'release_state': 'published',
    'layout': 'controlled-build',
    'series_order': 28,
}
existing = next((x for x in catalog['manuals'] if x.get('id') == MID), None)
if existing:
    existing.update(catalog_entry)
else:
    idx = next((i for i, x in enumerate(catalog['manuals']) if x.get('id') == 'ai-governance-audit-toolkit'), len(catalog['manuals']))
    catalog['manuals'].insert(idx, catalog_entry)

release_evidence = (
    'Manual 28 AI Privacy & Automated Decision Governance controlled EN/es-419/pt-BR package merged through PR #381 after release-time source revalidation kept NIST Privacy Framework 1.0 as the published baseline, PF 1.1 as draft/change-watch, NIST AI RMF 1.0 as published but under revision, and jurisdiction-specific automated-decision/privacy obligations as separate legal layers. '
    'The exact six-binary candidate was generated successfully by workflow run 33398466434 / artifact 9760280725 with artifact digest sha256:559b7d499aa74a64130935be81ff13f4fbf0fd8cf51643685a18890f275e75e7. '
    'Candidate Build, Workflow Security, Release Pipeline Meta QA, Manual Structure QA, Trilingual Publication Parity, and Release Package QA passed. '
    'PR #383 bound all six immutable SHA-256 identities plus deterministic DOCX/PDF integrity, 32-chapter completeness, accessibility with zero findings, searchable/tagged PDF checks, and full 72-page render-review evidence with no identified defect requiring regeneration. '
    'PR #384 durably staged the exact EN/es-419/pt-BR DOCX/PDF bytes after fail-closed verification of all six SHA-256 identities; its owner-authored exact staging head 9d0acae4ed75b86bf31abf1e34005de4ca8fdf8a passed Manual Structure QA, Trilingual Publication Parity, and Release Package QA before merge at 5dc217f59fe4ff60ae28bdf370401d6a9cb39fea. '
    'Predecessor Manual 27 is published. Standing release authorization applies because applicable objective gates are green and no unresolved material source, applicability, technical, localization, integrity, packaging, accessibility, provenance, workflow-security, or substantive defect is recorded.'
)
release_entry = {'id': MID, 'type': 'manual', 'release_state': 'published', 'release_evidence': release_evidence}
existing_release = next((x for x in releases['released_work_products'] if x.get('id') == MID), None)
if existing_release:
    existing_release.update(release_entry)
else:
    releases['released_work_products'].append(release_entry)

catalog['last_updated'] = '2026-08-31'
releases['last_updated'] = '2026-08-31'
CATALOG.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
RELEASES.write_text(json.dumps(releases, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('Manual 28 publication state reconciled.')
