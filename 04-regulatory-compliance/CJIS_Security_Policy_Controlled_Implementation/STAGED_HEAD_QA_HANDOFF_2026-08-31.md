# Manual 40 — Exact Staged-Head QA Handoff

This handoff is metadata-only. It changes no controlled source and no publication binary.

## Exact candidate identity

- Frozen candidate workflow run: `33439699453`
- Frozen artifact ID: `9775761693`
- EN DOCX SHA-256: `8ba4e7d27c20d649c546efab734a83b9400604ff22d051982f0ebf30a0d62edb`
- EN PDF SHA-256: `9e1b0ac4bfdd79e345d10ebe9a553643c85d61d8dda2fa00b41c63f470589219`
- es-419 DOCX SHA-256: `54de09ad9267038a0c22be1a275291ecc5b4ae961671af93a6ea119fb2a6adfe`
- es-419 PDF SHA-256: `3f03bc68b383bb44b3e9664d9db12e9717c7484d16877a0e6fb67ff1bca35e7c`
- pt-BR DOCX SHA-256: `aaad35c5d378a775d1ccfb9546e29d98b4e4a87ff4c32f8bad0087b216d57716`
- pt-BR PDF SHA-256: `5a8a7c13ad265e5b03c76cb1a425ef2a299c6fffb557e41f91f75e82657bd1a3`

Independent hashing of the downloaded frozen artifact matched the repository provenance identities. All three DOCX files returned zero high, medium, and low findings from the repository document accessibility audit. Each DOCX rendered successfully to four pages and all rendered pages were visually inspected without observed clipping, overlap, broken glyphs, or blank-page defects. Each frozen PDF opened successfully, is unencrypted, is text/searchable rather than scanned, contains four populated pages, and rendered cleanly; all rendered PDF pages were visually inspected without observed clipping, overlap, broken glyphs, or blank-page defects. No candidate bytes were regenerated or modified during this inspection.

PR #450 durably staged the exact six provenance-bound candidate binaries. The staging transaction removed its temporary write-enabled workflow. Manual 39 is now published on `main`; the earlier PR-head QA failures occurred before that predecessor publication was present on the staging branch. This handoff exists to attach the ordinary exact-head repository QA matrix to current `main` state with the published predecessor present.
