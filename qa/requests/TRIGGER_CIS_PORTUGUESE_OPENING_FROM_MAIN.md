# Trigger strengthened ISO localized-source audit

Run the audit-only ISO/IEC 27001 and 27002 localized-source workflow against `production/multilingual-grc-editions` using the current workflow definition on `main`.

The workflow must:

- inspect the Spanish and Brazilian Portuguese Markdown sources without modifying them;
- identify missing and duplicate major sections and image references;
- detect malformed image markup, injected corruption tokens, malformed links and emphasis, untranslated headings, captions and control text, mixed PT-BR terminology, and known mistranslations;
- treat collapsed or malformed table structures as release blockers;
- write refreshed Markdown and JSON evidence to the production branch;
- remain fail-closed while any configured structural, language or table blocker remains;
- not rebuild DOCX/PDF files or alter graphics, prose or publication metadata; and
- not merge this trigger-only PR.
