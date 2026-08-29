# Manual 03 — Durable Package Upload Gate

**Status: COMPLETE for durable repository placement.**

The controlled workflow generated the full trilingual publication package and QA evidence, and the six binary publication artifacts are now durably committed under `01-foundations/NIST_AI_RMF_1.0/publication/` on the Manual 03 release branch:

1. `Manual_03_NIST_AI_RMF_Implementation_EN.docx`
2. `Manual_03_NIST_AI_RMF_Implementation_EN.pdf`
3. `Manual_03_NIST_AI_RMF_Implementation_ES-419.docx`
4. `Manual_03_NIST_AI_RMF_Implementation_ES-419.pdf`
5. `Manual_03_NIST_AI_RMF_Implementation_PT-BR.docx`
6. `Manual_03_NIST_AI_RMF_Implementation_PT-BR.pdf`

The durable-placement blocker is therefore closed. This metadata reconciliation commit also provides a non-bot exact head so repository workflows can execute against the durable package.

Manual 03 remains fail-closed until the remaining substantive evidence is complete: competent human semantic/terminology review for `es-419` and `pt-BR`, human rendered-document accessibility/visual review, exact changed-scope review, and exact-final repository/security/provenance reconciliation. Standing Final Human Release Approval is already recorded and requires no additional owner prompt once those preceding gates are green.
