# Trigger ISO Spanish reviewed-baseline recovery

Run the fail-closed ISO Spanish recovery workflow against `production/multilingual-grc-editions` using the current workflow definition on `main`.

The workflow must:

- preserve the current production Spanish source in `qa/recovery/ISO_IEC_27001_27002_ES_PRE_RECOVERY_2026-08-01.md`;
- restore the exact Spanish Markdown blob `1dec4df93c0ce5c279d958d56ed23553535c0170` from `fix/publication-readiness-batch-1-spanish`;
- verify the restored blob before committing;
- rerun the strengthened Spanish and Brazilian Portuguese localized-source audit;
- commit the recovered Spanish source, quarantine copy, and refreshed Markdown/JSON audit evidence to the production branch;
- remain fail-closed while any structural, language, image, or table blocker remains;
- not rebuild DOCX/PDF files or alter graphics and publication metadata; and
- not merge this trigger-only PR.
