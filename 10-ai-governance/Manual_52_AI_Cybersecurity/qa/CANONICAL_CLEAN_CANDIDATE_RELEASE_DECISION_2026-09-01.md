# Manual 52 — Canonical Clean-Candidate Release Decision

Date: 1 September 2026

## Exact candidate identity

- Candidate workflow run: `33572657882`
- Candidate artifact: `9825508927` (`manual52-six-binary-candidate`)
- Candidate source head: `92c33de440f0d043a80883308ca4cafb3e858453`
- Artifact ZIP digest: `sha256:ffad71cdb140b41108c73e247a58c8c575367b4bfa874ac9722fa7473f7b55db`

## Exact six-binary identities

- EN DOCX — 41,052 bytes — `8f96740b87be8e0a35cb5aa998f4b23ccd640a2fdc319e04c6a8f3ba363da602`
- EN PDF — 70,738 bytes — `fc0db0fd978f13b8de1dc719af0a3417bee6e34370b0bf5da9c21bc6a2dfe7ba`
- es-419 DOCX — 39,707 bytes — `3243d69ef87f2cd017f3e1a5afa4e23955c5893dc1727c12c43a14e09a5f2fdc`
- es-419 PDF — 66,239 bytes — `903be0e25b8698fe7263578004db0534fba8101f9516bfcb81df00848cbfb0e2`
- pt-BR DOCX — 39,715 bytes — `d56fea909c93884839cae8b5819c1d493f9a989b7d12a5cee0e5ddbd671fa720`
- pt-BR PDF — 66,903 bytes — `849bc04c3fa223dff0114ebb74c533b5945b01d01bec81dc3b56d83547a24e6d`

## Gate determination

The candidate workflow completed successfully. Deterministic build, non-empty DOCX/PDF generation, visible-text validation, first-page raster rendering, and AC-01 through AC-20 trilingual parity checks passed. Source-status language preserves OWASP as community guidance, MITRE ATLAS as a living knowledge base, and NIST AI RMF / AI 600-1 as voluntary guidance. No unresolved substantive defect is documented.

Under the repository canonical clean-candidate rule, standing owner release authorization applies. The exact candidate may proceed to controlled exact-byte staging. The temporary write-enabled transfer workflow must self-delete before the final publication tree, and the final exact head remains subject to retained repository CI before merge.
