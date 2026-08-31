# Manual 28 — Exact Candidate Provenance and Deterministic QA

Date: 2026-08-31
Manual: 28 — AI Privacy & Automated Decision Governance Controlled Implementation
Status: exact candidate bound; publication state unchanged pending durable exact-byte staging and final reconciliation.

## Candidate identity

- Candidate workflow run: `33398466434`
- Workflow artifact ID: `9760280725`
- Artifact name: `manual28-six-binary-candidate`
- Artifact digest: `sha256:559b7d499aa74a64130935be81ff13f4fbf0fd8cf51643685a18890f275e75e7`
- Manifest source commit: `31debfd4cbfbd2e2068ad68e96dee5a33dfa20d1`
- Candidate PR: #382
- Candidate build, workflow-security, release-pipeline meta-QA, and release-readiness: PASS.

## Exact six binary identities

| Locale | File | Bytes | SHA-256 |
|---|---|---:|---|
| en | `Manual_28_AI_Privacy_Automated_Decision_Governance_Controlled_EN.docx` | 44988 | `b34efd30c233adc435de653f6cdad3bdf6e2a24f2a863c36b69a9852aa3fae1d` |
| en | `Manual_28_AI_Privacy_Automated_Decision_Governance_Controlled_EN.pdf` | 112727 | `b8dbc416b0c49b5e31ea9c0426fe64f29656b4258bb7025567acf9b87b4d0627` |
| es-419 | `Manual_28_AI_Privacy_Automated_Decision_Governance_Controlled_ES-419.docx` | 44847 | `5cf5894188d653fe3e66d05f5597eced6e49065be57ebc690559b5c7b0da08b1` |
| es-419 | `Manual_28_AI_Privacy_Automated_Decision_Governance_Controlled_ES-419.pdf` | 113453 | `bb50a1713926b89cad90c809c24e8e655d32524e561abb800ba8eebdebd59374` |
| pt-BR | `Manual_28_AI_Privacy_Automated_Decision_Governance_Controlled_PT-BR.docx` | 44912 | `662a02982b6140e33e4072a7426791b5580f64e3716c67d5ed302d8c58abb78c` |
| pt-BR | `Manual_28_AI_Privacy_Automated_Decision_Governance_Controlled_PT-BR.pdf` | 113877 | `6d4eb978dea3dd73f407a05ae1ec52e0215317e3d0f102ea19e1a49f2f349af8` |

All six locally calculated SHA-256 values matched the workflow manifest exactly. No candidate binary was regenerated during QA.

## Deterministic package and content QA

### DOCX

- All three DOCX files passed ZIP/package integrity checks.
- `word/document.xml` was readable in every package.
- All 32 controlled chapter markers were present in EN, es-419, and pt-BR.
- Accessibility audit using the repository document QA tooling returned `high=0`, `medium=0`, `low=0` for each of the three DOCX files.

### PDF

- All three PDFs opened successfully and are unencrypted.
- All three PDFs are tagged and use letter page size.
- Each PDF contains 12 pages and searchable text: EN 25,778 extracted characters; es-419 26,840; pt-BR 27,141.
- All 32 controlled chapter markers were present in each PDF.

## Full rendered-page review

The exact downloaded artifact was rendered without modification using the controlled PDF and DOCX render workflows. Every rendered page was visually inspected:

- EN PDF: 12/12 pages clean.
- es-419 PDF: 12/12 pages clean.
- pt-BR PDF: 12/12 pages clean.
- EN DOCX: 12/12 pages clean.
- es-419 DOCX: 12/12 pages clean.
- pt-BR DOCX: 12/12 pages clean.

Total inspected: 72 rendered pages.

No clipping, overlap, broken glyphs, missing headings/sections, malformed pages, or deterministic layout defect requiring regeneration was identified.

## Release boundary

The exact six binaries above are the only candidate bytes eligible for durable staging under this transaction. Staging must fail closed if any SHA-256 value differs. The staging transaction must copy the exact artifact bytes without regeneration. Publication remains sequential after published Manual 27 and must not be reconciled until ordinary exact-head structure, trilingual-parity, and release-package QA pass on the durably staged bytes.