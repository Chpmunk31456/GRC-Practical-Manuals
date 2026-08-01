# Trigger ISO localized structural repair batch 02

Run the bounded ISO/IEC 27001 and 27002 localized-source repair-and-audit workflow against `production/multilingual-grc-editions` using the current workflow definition on `main`.

The workflow must:

- apply only Markdown-structure repairs defined in `qa/tools/repair_iso_localized_structural_batch_02.py`;
- normalize malformed nested table-of-contents links while preserving visible labels, page references, and anchors;
- add missing `#` markers only to standalone major body section headings numbered 1–28;
- abort on mismatched anchors or unexpected source state;
- rerun the deterministic Spanish and Brazilian Portuguese localized-source audit;
- commit both repaired Markdown sources and refreshed Markdown/JSON audit evidence to the production branch;
- remain fail-closed while any configured defect remains;
- not rewrite prose, tables, terminology, images, DOCX/PDF files, or publication metadata; and
- not merge this trigger-only PR.
