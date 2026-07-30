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

## Current state

The translation branch and controls are established. Translation content, build artifacts, and publication approval remain in progress.