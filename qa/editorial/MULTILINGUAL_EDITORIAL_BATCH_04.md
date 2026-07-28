# Multilingual Editorial Review — Batch 04

**Base production SHA:** `ce3122ce5d8cbd49c822c502562690ba3f2068d8`

**Manuals:** PCI DSS v4.0.1 and Incident Response, Business Continuity, and Disaster Recovery.

**Languages reviewed:** Latin American Spanish and Brazilian Portuguese.

**Status:** Machine-assisted editorial corrections only. All editions remain drafts and are not publication-ready.

## Corrections

### PCI DSS v4.0.1

Spanish:

- Replaced mixed-language playbook terminology with `Manual de PCI DSS para gerentes` in the table of contents and chapter heading.
- Replaced `Dashboard` with `Panel` in the table of contents and chapter heading.
- Translated the `PCI Evidence Coordinator` role label.

Brazilian Portuguese:

- Replaced mixed-language playbook terminology with `Manual do PCI DSS para gerentes` in the table of contents and chapter heading.
- Corrected two malformed `# #` heading markers.
- Translated the PCI SSC Document Library link label without changing its URL.

### Incident Response, Business Continuity, and Disaster Recovery

Spanish:

- Translated two English table-of-contents chapter labels concerning digital evidence and compliance mapping.
- Translated the English playbook-design heading, evidence-integrity caption, evidence-record heading, and evidence/chain-of-custody heading.
- Replaced mixed-language manager-playbook terminology with `Manual de resiliencia para gerentes` in the table of contents and chapter heading.

Brazilian Portuguese:

- Replaced mixed-language manager-playbook terminology with `Manual de resiliência para gerentes` in the table of contents and chapter heading.
- Corrected two malformed `# #` heading markers.
- Translated the CISA incident and vulnerability response playbooks link label without changing its URL.

## Rebuilt deliverables

- PCI DSS v4.0.1 Spanish DOCX and PDF.
- PCI DSS v4.0.1 Brazilian Portuguese DOCX and PDF.
- Incident Response/BCDR Spanish DOCX and PDF.
- Incident Response/BCDR Brazilian Portuguese DOCX and PDF.

## Validation

- Translation/checkpoint regression tests: **7 passed**.
- Multilingual batch QA: **22 files scanned; 11 mechanical passes; 11 review-gated**.
- Package inventory: **11 manual families complete; no missing DOCX/PDF deliverables**.
- DOCX integrity: all four rebuilt DOCX files passed ZIP integrity and `word/document.xml` extraction.
- Searchable PDFs:
  - PCI DSS Spanish: 61,466 extracted characters.
  - PCI DSS Brazilian Portuguese: 73,270 extracted characters.
  - Incident Response/BCDR Spanish: 74,212 extracted characters.
  - Incident Response/BCDR Brazilian Portuguese: 69,443 extracted characters.
- `git diff --check`: **passed**.
- Required machine-assisted draft notices: preserved in all four changed Markdown editions.
- Missing legacy image references: **82 repository-wide, unchanged**.

## Unresolved gates

Batch-specific unresolved image references:

- PCI DSS Brazilian Portuguese: `media/image1.png` through `media/image9.png`.
- Incident Response/BCDR Brazilian Portuguese: `media/image1.png` through `media/image10.png`.

The QA suite reports no parsed missing image source in the two Spanish editions. This mechanical result does not replace the required page-by-page visual and accessibility reviews.

No image was invented, replaced, deleted, suppressed, or concealed.

The following remain required before publication:

- native-speaker line-by-line review of both languages;
- qualified legal/regulatory review;
- technical and factual review of framework interpretations and examples;
- accessibility review, including reading order, headings, tables, links, captions, and assistive-technology behavior;
- page-by-page visual review of DOCX and PDF output;
- review and resolution of all 82 legacy non-NIST image references;
- review of residual mixed-language prose, malformed Markdown and tables, and extraction damage outside the narrow high-confidence corrections in this batch.
