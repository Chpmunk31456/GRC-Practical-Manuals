# Trigger ISO Spanish recovered-baseline cleanup batch 01

Run the bounded ISO Spanish cleanup-and-audit workflow against `production/multilingual-grc-editions` using the current workflow definition on `main`.

The workflow must:

- apply only `qa/tools/repair_iso_spanish_recovered_baseline_batch_01.py`;
- normalize malformed nested links only inside the Spanish table-of-contents boundary;
- remove verified conversion-artifact tokens and placeholder rows;
- restore the missing section 6 heading;
- correct the verified Word-TOC instruction, three English figure captions, and a small set of unambiguous terminology errors;
- rerun the strengthened Spanish and Brazilian Portuguese localized-source audit;
- commit only the repaired Spanish Markdown source and refreshed Markdown/JSON audit evidence;
- remain fail-closed while any structural, language, image, or table blocker remains;
- not rebuild DOCX/PDF files or alter graphics and publication metadata; and
- not merge this trigger-only PR.
