# Multilingual Publication QA

This directory records controlled human-review findings for the Spanish and Brazilian Portuguese editions before publication.

## Current status

- Automated package generation: complete
- Automated DOCX ZIP integrity validation: complete
- Automated PDF searchable-text validation: complete
- Human language/terminology review: in progress
- Page-by-page DOCX/PDF visual review: pending completion
- Accessibility review: pending completion
- Technical/factual currency review: pending completion

## NIST CSF 2.0 remediation status

The original NIST CSF 2.0 multilingual QA findings documented publication-blocking machine-translation, terminology, mixed-language, and Markdown defects in earlier Spanish and Brazilian Portuguese drafts.

Reviewed Spanish and Brazilian Portuguese rewrites were subsequently integrated into the production branch. Current-source verification confirms that the specifically cited defects—including `Tiros`, `Policía (GV.PO)`, `Función del PROTECTO`, `Silencio.`, `mudadores de carreira`, and `Conteúdo verdadeiro da palavra`—are absent from the current editions. The opening sections, NIST function terminology, tables, captions, and localized image references now reflect the reviewed rewrites.

Automated graphics and package validation is recorded as PASS, including localized PNG inventory, image dimensions, DOCX integrity, embedded media, searchable PDF text, and corrected figure-page contact sheets.

This remediation closes the original defect set as a current-source blocker. It does **not** constitute final publication approval. The following gates remain open:

- Full native-language review across both complete editions
- Page-by-page DOCX and PDF visual inspection
- Human inspection of the final contact sheets for clipping, overlap, font rendering, contrast, and grayscale comprehension
- Accessibility structure, reading order, metadata, and assistive-technology review
- Technical and factual currency review

## CIS Controls v8.1 current blocker

Current-source verification on 30 July 2026 confirms that the Latin American Spanish CIS Controls v8.1 edition remains publication-blocked.

The current Markdown source contains material extraction and translation corruption in the Control 18 and open-source-tools sections, including:

- malformed table delimiters and incomplete rows;
- repeated generated tokens such as `TEN`, `TEN TODO`, and `tención`;
- untranslated English phrases and mixed-language descriptions;
- corrupted safeguard names and missing column boundaries;
- stray generated words such as `Silencioso` and `tóxico` in technical-tool entries.

Because these defects affect meaning, navigation, tables, and the generated DOCX/PDF packages, automated package integrity does not establish publication readiness for this edition.

Required remediation:

1. Rewrite the affected Spanish sections from the authoritative English source using controlled CIS terminology.
2. Repair all table structures and verify the complete Control 18 safeguard set.
3. Remove generated tokens, stray words, and residual English fragments.
4. Rebuild the Spanish DOCX and PDF only after the Markdown passes language and structural QA.
5. Perform page-level visual, accessibility, link, and factual verification on the regenerated package.

The Brazilian Portuguese CIS edition and all localized CIS figures still require their own complete language, structural, visual, accessibility, and factual review before final approval.

## Review records

- [NIST CSF 2.0 multilingual QA findings](NIST_CSF_2_MULTILINGUAL_QA_FINDINGS.md) — historical defect record for the superseded machine-generated drafts.
- [NIST CSF 2.0 localized graphics completion](NIST_CSF_2_GRAPHICS_COMPLETION.md) — automated graphics/package validation evidence and the remaining human visual-review boundary.
- Reviewed rewrite records are maintained in `qa/rewrite/`.
- Corrected figure-page review evidence is maintained in `qa/nist_visual_qa_final/`.
- CIS Controls current-source blocker evidence is in the Spanish Markdown source around the Control 18 and tools sections.

No multilingual edition should be marked final solely because automated generation or targeted remediation succeeded.
