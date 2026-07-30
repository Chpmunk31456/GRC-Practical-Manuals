# EU AI Act GRC Manual — Translation Workstream

**Branch:** `translation/eu-ai-act-es-ptbr`  
**Source:** frozen English production edition  
**Target languages:** Spanish for Latin America (`es-419`) and Brazilian Portuguese (`pt-BR`)

## Objective

Produce complete Spanish and Brazilian Portuguese editions from the approved English source while preserving structure, numbering, legal references, tables, controls, evidence, audit tests, appendices, captions, and accessibility meaning.

## Mandatory controls

1. Translate only from the canonical English corrected masters on `production/multilingual-grc-editions`.
2. Preserve Chapters 1–138 and Appendices A–Z in exactly the same order.
3. Preserve article, annex, recital, date, deadline, role, control, and evidence references unless the English source is formally corrected.
4. Keep binding duties, organization controls, recommended practices, and optional enhancements clearly distinguished.
5. Use neutral Latin American Spanish and natural Brazilian Portuguese.
6. Reconstruct non-English figures with translated text; do not reuse English-language graphics.
7. Maintain captions, alt text, accessible contrast, non-colour cues, and written explanations.
8. Run terminology, legal-reference, unresolved-English-fragment, cross-reference, DOCX, PDF, and page-rendering QA separately for each language.
9. Do not merge into production until both language editions pass their independent release checklists.

## Directory structure

- `es-419/source/` — translated Markdown sources
- `es-419/docx/` — reviewed Word edition
- `es-419/pdf/` — reviewed PDF edition
- `pt-BR/source/` — translated Markdown sources
- `pt-BR/docx/` — reviewed Word edition
- `pt-BR/pdf/` — reviewed PDF edition
- `terminology/` — controlled bilingual glossary
- `quality/` — translation manifests, QA findings, and sign-off evidence
- `tools/` — canonical translation, assembly, and QA automation

## Translation sequence

1. Front matter and legal disclaimer
2. Chapters 1–35
3. Chapters 36–70
4. Chapters 71–103
5. Chapters 104–138
6. Appendices A–Z
7. Graphics, captions, and alt text
8. Integrated Markdown assembly
9. DOCX and PDF production
10. Page-by-page visual and linguistic QA
11. Production pull request and publication

## Autonomous publication pipeline

The workflow `.github/workflows/build-eu-ai-act-spanish-portuguese.yml` now performs the controlled translation and build sequence without routine owner input:

1. selects the same 138 canonical chapters and 26 canonical appendices used by the English publication builder;
2. translates independent shards into `es-419` and `pt-BR` using controlled Marian translation models;
3. preserves Markdown, URLs, inline code, numbering, article references, and source hashes;
4. assembles one integrated Markdown master per language;
5. generates separate DOCX and PDF editions;
6. renders every PDF page for inspection;
7. runs fail-closed structural, terminology, unresolved-English, manifest, DOCX, and PDF checks;
8. records checksums and translation manifests;
9. commits only successful generated editions back to this branch;
10. uploads complete publication-candidate packages.

A failed translation shard or QA gate prevents publication artifacts from being committed.

## Current state

The controlled glossary, translation requirements, canonical source manifest, translation engine, bilingual assembly process, fail-closed QA, and autonomous GitHub Actions publication workflow are established. The workflow has been triggered from this branch. Neither localized edition may be labeled published until generated source files and artifacts exist and all configured gates pass.
