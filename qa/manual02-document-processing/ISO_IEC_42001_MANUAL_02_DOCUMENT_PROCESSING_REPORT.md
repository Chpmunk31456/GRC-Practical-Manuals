# DOCUMENT PROCESSING REPORT

- Source branch: `build/iso-iec-42001-manual-02-2026`
- Source commit: `647c88fa905a16cba4e3ec162a32aad56f48c58b`
- Generation date: `2026-08-24`
- Localized status: **DRAFT — HUMAN SEMANTIC REVIEW REQUIRED**
- Assurance boundary: generation and QA do not establish ISO authorization, certification, conformity, legal compliance, or audit assurance.

## Publication artifacts

| Language | Markdown master | DOCX | PDF | Pages |
|---|---|---|---|---:|
| en | `02-management-systems/ISO_IEC_42001_AIMS/English/ISO_IEC_42001_2023_Practical_AIMS_Manual_English_v1.0.md` | `02-management-systems/ISO_IEC_42001_AIMS/publication/qa-candidate/Manual_02_ISO_IEC_42001_AI_Management_System_EN.docx` | `02-management-systems/ISO_IEC_42001_AIMS/publication/qa-candidate/Manual_02_ISO_IEC_42001_AI_Management_System_EN.pdf` | 55 |
| es-419 | `02-management-systems/ISO_IEC_42001_AIMS/translations/es-419/source/Manual_02_ISO_IEC_42001_AI_Management_System_ES-419.md` | `02-management-systems/ISO_IEC_42001_AIMS/publication/qa-candidate/Manual_02_ISO_IEC_42001_AI_Management_System_ES-419.docx` | `02-management-systems/ISO_IEC_42001_AIMS/publication/qa-candidate/Manual_02_ISO_IEC_42001_AI_Management_System_ES-419.pdf` | 41 |
| pt-BR | `02-management-systems/ISO_IEC_42001_AIMS/translations/pt-BR/source/Manual_02_ISO_IEC_42001_AI_Management_System_PT-BR.md` | `02-management-systems/ISO_IEC_42001_AIMS/publication/qa-candidate/Manual_02_ISO_IEC_42001_AI_Management_System_PT-BR.docx` | `02-management-systems/ISO_IEC_42001_AIMS/publication/qa-candidate/Manual_02_ISO_IEC_42001_AI_Management_System_PT-BR.pdf` | 40 |

## Quality gates

| Gate | Result |
|---|---|
| Gate 1 — Source integrity | PASS |
| Gate 2 — DOCX generation | PASS |
| Gate 3 — PDF generation | PASS |
| Gate 4 — Page-by-page visual QA | PASS |
| Gate 5 — Trilingual parity | PASS |
| Gate 6 — Human semantic approval | OPEN — NOT AUTOMATICALLY CLOSED |
| Gate 7 — Release package | BLOCKED |

## Accessibility findings

No unresolved high/critical DOCX accessibility finding.

## Visual QA findings

Every generated PDF page has a recorded page-level result. No unresolved high/critical visual finding.

## Trilingual parity findings

All editions contain chapters 1–32 in order, ten figures, 33 data tables, controlled references, and the required risk/impact and applicability terminology.

## Human-review dependency

The Spanish and Brazilian Portuguese semantic/terminology review gate remains OPEN. These artifacts are layout and accessibility QA candidates only and are not release-ready.

## QA workflows run

- Controlled-source, human-gate, source-registry, and manual-catalog repository checks
- DOCX semantic/accessibility package inspection
- PDF content, link, font, and page-by-page raster inspection (136 pages)
- Trilingual chapter, figure, table, terminology, graphic-language, and reference parity
- SHA-256 artifact manifest generation

DOCUMENT PROCESSING STATUS: BLOCKED BY TRANSLATION REVIEW
