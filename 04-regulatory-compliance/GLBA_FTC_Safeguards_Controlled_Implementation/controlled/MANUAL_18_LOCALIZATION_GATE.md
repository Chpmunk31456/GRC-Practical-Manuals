# Manual 18 Controlled Localization Gate

**Series order:** 18  
**Frozen English blob:** `be0b0c0d1b692ac0eb9e5e1692901e2a3237d739`  
**Frozen source path:** `04-regulatory-compliance/GLBA_FTC_Safeguards_Controlled_Implementation/controlled/en/MANUAL_18_CONTROLLED_EN.md`

## Required controlled editions

- `controlled/es-419/MANUAL_18_CONTROLLED_ES_419.md`
- `controlled/pt-BR/MANUAL_18_CONTROLLED_PT_BR.md`

## Meaning-preservation rules

1. Preserve the separation among GLBA statutory context, 16 CFR Part 314 requirements, FTC amendments/effective dates, official FTC guidance, and organization-specific implementation practices.
2. Do not broaden FTC jurisdiction or present the manual as legal advice.
3. Preserve the notification-event decision boundary exactly as an implementation decision workflow; do not generalize the threshold or timing beyond the FTC Safeguards Rule context.
4. Treat translations as controlled project localizations, not official FTC translations.
5. Preserve all 32 chapter headings, chapter order, evidence expectations, test language, control ownership concepts, and release boundaries.
6. Any material change to the frozen English source invalidates localization parity and reopens affected semantic, rendered, and provenance gates.

## Fail-closed review boundary

Machine-assisted drafting or deterministic transformation may prepare localized editions, but it does not satisfy any documented requirement for genuine human semantic/legal/editorial review. Final localization acceptance must remain tied to the exact localized source blobs and later exact DOCX/PDF artifact hashes.

## Next executable gates

1. Produce complete es-419 and pt-BR controlled source editions from the frozen English source.
2. Run structure and trilingual parity checks.
3. Freeze accepted localized source identities.
4. Build reproducible six-binary DOCX/PDF candidate package.
5. Run rendered/page/accessibility, workflow-security, release-package, source-state and provenance checks.
6. Durably stage the exact candidate bytes and reconcile catalog/release registry only after all applicable gates are green.
