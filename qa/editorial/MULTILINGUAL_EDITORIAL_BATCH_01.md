# Multilingual Editorial Review — Batch 01

**Base production SHA:** `ce3122ce5d8cbd49c822c502562690ba3f2068d8`

**Manuals:** CIS Critical Security Controls v8.1 and GDPR.

**Languages:** Latin American Spanish and Brazilian Portuguese.

**Status:** Machine-assisted editorial corrections only. All editions remain drafts and are not publication-ready.

## Corrections

### CIS Critical Security Controls v8.1

Spanish:

- Replaced the untranslated and unnatural “Manager” playbook title with `Manual de los Controles CIS para gerentes` in the table of contents and chapter heading.
- Replaced the ambiguous `Registro de búsqueda y prueba` and untranslated `Finding and retest record` with `Registro de hallazgos y nuevas pruebas`.

Brazilian Portuguese:

- Replaced the mixed-language playbook title with `Manual dos Controles CIS para gerentes` in the table of contents and chapter heading.
- Replaced European Portuguese `Registo` and the malformed `Encontrar e reteste recorde` heading with `Registro de achados e retestes`.
- Corrected the malformed heading marker from `# #` to `##`.

### GDPR

Spanish:

- Replaced literal `cartera` usage with `portafolio` where the English source means a professional portfolio.
- Corrected `analistas juniores` and improved article agreement in the introductory learning-path sentence.
- Replaced `Manual de juegos GDPR` and `Libro de juegos GDPR` with `Manual del GDPR para gerentes`.
- Replaced the untranslated `Manager checkpoint` label with `Punto de control para gerentes` and repaired its table-cell syntax.
- Improved the career-path alt text without changing `media/image5.png`.
- Replaced the malformed `Honra sincera` portfolio notice with clear professional-honesty language while preserving its warning that laboratory work is not professional experience.
- Replaced the untranslated and malformed `16,5 Manager pre-launch checklist` heading with `16.5 Lista de verificación previa al lanzamiento para gerentes`.

Brazilian Portuguese:

- Replaced `GDPR Playbook` and `GDPR do gerente Playbook` with `Manual do GDPR para gerentes`.
- Replaced the mixed-language and malformed `16,5 Manager pré-lançamento checklist` heading with `16.5 Lista de verificação pré-lançamento para gerentes`.
- Corrected the malformed heading marker from `# #` to `##`.

## Rebuilt deliverables

- CIS Controls Spanish DOCX and PDF.
- CIS Controls Brazilian Portuguese DOCX and PDF.
- GDPR Spanish DOCX and PDF.
- GDPR Brazilian Portuguese DOCX and PDF.

## Validation

- Translation/checkpoint regression tests: **7 passed**.
- Multilingual batch QA: **22 files scanned; 11 mechanical passes; 11 review-gated**.
- Package inventory: **11 manual families complete; no missing DOCX/PDF deliverables**.
- DOCX integrity: all four rebuilt DOCX files passed ZIP integrity and `word/document.xml` extraction.
- Searchable PDFs:
  - CIS Spanish: 78,661 extracted characters.
  - CIS Brazilian Portuguese: 123,819 extracted characters.
  - GDPR Spanish: 74,478 extracted characters.
  - GDPR Brazilian Portuguese: 78,448 extracted characters.
- `git diff --check`: **passed**.
- Draft notices: preserved in all four changed Markdown editions.
- Missing legacy image references: **82 repository-wide, unchanged**.

## Unresolved gates

Batch-specific unresolved image references:

- CIS Spanish: `media/image3.png`.
- CIS Brazilian Portuguese: `media/image1.png` through `media/image10.png`.
- GDPR Spanish: `media/image5.png`.
- GDPR Brazilian Portuguese: `media/image1.png` through `media/image5.png`.

No image was invented, replaced, deleted, suppressed, or concealed.

The following remain required before publication:

- native-speaker line-by-line review of both languages;
- qualified legal/regulatory review;
- technical and factual review of framework interpretations and examples;
- accessibility review, including reading order, headings, tables, links, captions, and assistive-technology behavior;
- page-by-page visual review of DOCX and PDF output;
- review and resolution of all 82 legacy non-NIST image references;
- review of residual mixed-language prose and extraction damage outside the narrow high-confidence corrections in this batch.
