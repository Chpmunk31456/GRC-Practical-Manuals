# Manual 32 — Final Publication Handoff

The fail-closed Manual 32 FFIEC publication reconciliation succeeded on the publication branch and the temporary write-enabled reconciliation workflow removed itself. The only intended publication-state changes are the Manual 32 entries in `.compliance/manual-catalog.json` and `.compliance/work-product-releases.json`.

The six reviewed Manual 32 publication binaries remain exactly the provenance-bound bytes from workflow run `33415623228` / artifact `9766895211`; no binary was regenerated or modified during reconciliation.

This owner-authored metadata-only handoff exists solely to trigger the ordinary exact-head repository regression matrix. Merge is permitted only if all applicable structure, trilingual parity, release-package, and broad regression checks complete successfully with no unresolved material defect.