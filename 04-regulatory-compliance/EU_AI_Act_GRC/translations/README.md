# EU AI Act GRC Manual — Spanish and Brazilian Portuguese Editions

**Status:** Published and validated  
**Source:** frozen English production edition  
**Languages:** Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`)  
**Localized production PR:** #35  
**Main publication PR:** #38

## Published scope

Both localized editions contain:

- Chapters 1–138
- Appendices A–Z
- controlled Markdown master
- DOCX edition
- PDF edition
- source and build manifests
- automated QA report
- PDF metadata
- SHA-256 checksums

## Directory structure

- `es-419/source/` — Spanish Markdown sources and controlled master
- `es-419/docx/` — Spanish Word edition
- `es-419/pdf/` — Spanish PDF edition
- `pt-BR/source/` — Brazilian Portuguese Markdown sources and controlled master
- `pt-BR/docx/` — Brazilian Portuguese Word edition
- `pt-BR/pdf/` — Brazilian Portuguese PDF edition
- `terminology/` — controlled bilingual glossary
- `quality/` — translation manifests, QA evidence, and publication records
- `tools/` — translation, assembly, and QA automation

## Publication controls completed

The approved publication process:

1. translated from the canonical English corrected masters;
2. preserved the 138-chapter and 26-appendix structure;
3. preserved legal references, numbering, controls, evidence, and audit tests;
4. generated integrated Markdown, DOCX, and PDF editions;
5. validated localized headings and tables of contents;
6. validated Figure 12-1 and Portuguese Appendix Q;
7. ran fail-closed structural and artifact QA;
8. generated source/build manifests and SHA-256 checksums;
9. merged the validated packages into `production/multilingual-grc-editions` through PR #35;
10. published the focused EU AI Act v1.3 package to the default `main` branch through PR #38.

## Maintenance rule

Future legal or editorial changes must be applied to the controlled English source first, translated into both localized editions, and revalidated through the same structural, linguistic, document-integrity, PDF, and checksum gates before publication.

## Important notice

These editions are educational and operational guidance. They do not constitute legal advice and do not guarantee compliance, certification, audit success, or protection from every AI, privacy, cybersecurity, or operational risk.
