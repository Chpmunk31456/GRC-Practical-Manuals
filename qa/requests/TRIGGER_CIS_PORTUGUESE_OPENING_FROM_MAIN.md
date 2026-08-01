# Trigger ISO localized section-parity audit

Run the audit-only ISO/IEC 27001 and 27002 localized-source workflow against `production/multilingual-grc-editions` using the current workflow definition on `main`.

The workflow must:

- run the strengthened localized-source audit;
- compare each of the 28 Spanish and Brazilian Portuguese major sections with the approved English master;
- identify missing headings, table-structure drift, image drift, corruption tokens, residual English, and material length drift by section;
- write both coarse and section-level Markdown/JSON evidence to the production branch;
- remain fail-closed while any source or section-parity blocker remains;
- not modify localized prose, tables, images, DOCX/PDF files, or publication metadata; and
- not merge this trigger-only PR.
