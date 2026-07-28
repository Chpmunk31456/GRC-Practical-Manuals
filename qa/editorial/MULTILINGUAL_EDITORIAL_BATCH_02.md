# Multilingual Editorial Review — Batch 02

**Base production SHA:** `ce3122ce5d8cbd49c822c502562690ba3f2068d8`

**Manuals:** NIST Risk Management Framework / SP 800-53 and ISO/IEC 27001/27002.

**Languages:** Latin American Spanish and Brazilian Portuguese.

**Status:** Machine-assisted editorial corrections only. All editions remain drafts and are not publication-ready.

## Corrections

### NIST Risk Management Framework / SP 800-53

Spanish:

- Replaced the literal mixed-language chapter title `Libro de juegos RMF de Manager` with `Manual del RMF para gerentes`.

Brazilian Portuguese:

- Replaced `Playbook RMF do gestor` and `RMF Playbook do gerente` with `Manual do RMF para gerentes` in the table of contents and chapter heading.
- Corrected the malformed heading marker in `Como usar este manual` from `# #` to `##`.

### ISO/IEC 27001/27002

Spanish:

- Replaced the literal mixed-language playbook title with `Manual del SGSI para gerentes` in the table of contents and chapter heading.
- Translated one unambiguous English sentence about recording evidence and findings.

Brazilian Portuguese:

- Replaced the mixed-language playbook title with `Manual do SGSI para gerentes` in the table of contents and chapter heading.
- Translated one unambiguous English management-review instruction while preserving clause `9.3.3`.
- Translated the English alt text for `media/image4.png` without changing its unresolved image path.
- Corrected the malformed heading marker in `Uso ético e autorizado` from `# #` to `##`.

## Rebuilt deliverables

- NIST RMF / SP 800-53 Spanish DOCX and PDF.
- NIST RMF / SP 800-53 Brazilian Portuguese DOCX and PDF.
- ISO/IEC 27001/27002 Spanish DOCX and PDF.
- ISO/IEC 27001/27002 Brazilian Portuguese DOCX and PDF.

## Validation

- Translation/checkpoint regression tests: **7 passed**.
- Multilingual batch QA: **22 files scanned; 11 mechanical passes; 11 review-gated**.
- Package inventory: **11 manual families complete; no missing DOCX/PDF deliverables**.
- DOCX integrity: all four rebuilt DOCX files passed ZIP integrity and `word/document.xml` extraction.
- Searchable PDFs:
  - NIST RMF Spanish: 73,224 extracted characters.
  - NIST RMF Brazilian Portuguese: 71,274 extracted characters.
  - ISO/IEC 27001/27002 Spanish: 69,344 extracted characters.
  - ISO/IEC 27001/27002 Brazilian Portuguese: 78,804 extracted characters.
- `git diff --check`: **passed**.
- Draft notices: preserved in all four changed Markdown editions.
- Missing legacy image references: **82 repository-wide, unchanged**.

## Unresolved gates

Batch-specific unresolved image references:

- NIST RMF Brazilian Portuguese: `media/image1.png` through `media/image10.png`.
- ISO/IEC 27001/27002 Brazilian Portuguese: `media/image1.png` through `media/image9.png`.

The QA suite reports no parsed missing image source in the two Spanish editions. This mechanical result does not replace the required page-by-page visual and accessibility reviews.

No image was invented, replaced, deleted, suppressed, or concealed.

The following remain required before publication:

- native-speaker line-by-line review of both languages;
- qualified legal/regulatory review;
- technical and factual review of framework interpretations and examples;
- accessibility review, including reading order, headings, tables, links, captions, and assistive-technology behavior;
- page-by-page visual review of DOCX and PDF output;
- review and resolution of all 82 legacy non-NIST image references;
- review of residual mixed-language prose and extraction damage outside the narrow high-confidence corrections in this batch.
