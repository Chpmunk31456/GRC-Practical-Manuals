# Trigger ISO localized structural repair batch 01

Run the bounded ISO/IEC 27001 and 27002 localized-source repair-and-audit workflow against `production/multilingual-grc-editions` using the current workflow definition on `main`.

The workflow must:

- apply only exact, high-confidence structural repairs defined in `qa/tools/repair_iso_localized_structural_batch_01.py`;
- correct known corrupted image markup, injected tokens, placeholder rows, selected missing heading markers, mixed PT-BR terminology, and a small set of unambiguous technical mistranslations;
- abort if any exact expected source string is missing or duplicated;
- rerun the deterministic Spanish and Brazilian Portuguese localized-source audit;
- commit both repaired Markdown sources and refreshed Markdown/JSON audit evidence to the production branch;
- remain fail-closed while any configured defect remains;
- not rebuild DOCX/PDF files or alter publication metadata; and
- not merge this trigger-only PR.
