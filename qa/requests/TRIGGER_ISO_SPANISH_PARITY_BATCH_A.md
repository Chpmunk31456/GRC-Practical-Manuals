# Trigger ISO Spanish parity batch A

Run the isolated ISO Spanish parity batch A workflow against `production/multilingual-grc-editions`.

The workflow must:

- apply only `qa/tools/repair_iso_spanish_parity_batch_a.py`;
- correct the verified residual-English and mistranslated instructions in sections 1 and 4;
- avoid the malformed section-4 table and all other structural content;
- rerun both the strengthened source audit and 28-section parity audit;
- commit only the Spanish source and refreshed audit evidence;
- rebase before pushing to prevent concurrent-update loss;
- remain fail-closed while any localized-source or parity blocker remains; and
- not merge this trigger-only branch or PR.
