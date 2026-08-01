# Trigger ISO localized-source fail-closed audit

Run the bounded ISO/IEC 27001 and 27002 localized-source audit against `production/multilingual-grc-editions` using the current workflow definition on `main`.

The workflow must:

- inspect the Spanish and Brazilian Portuguese Markdown sources;
- compare expected major-section and image-reference structure;
- identify configured corrupted markup, malformed links and emphasis, collapsed table signals, untranslated headings, known mistranslations, and mixed-locale terminology;
- write detailed Markdown and JSON audit evidence to the production branch;
- fail closed while any configured defect remains; and
- make no changes to localized prose, DOCX, PDF, graphics, or publication metadata.

This PR is trigger-only, modifies no publication content on `main`, and must not be merged.
