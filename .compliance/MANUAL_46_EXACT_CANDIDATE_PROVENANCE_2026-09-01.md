# Manual 46 — Exact Candidate Provenance and QA

**Manual:** Manual 46 — Universal AI Governance Foundation  
**Frozen candidate workflow run:** `33522796835`  
**Frozen artifact ID:** `9806432982`  
**Artifact name:** `manual46-six-binary-candidate`  
**Artifact digest:** `sha256:46816942ec7d6143fda3f4ec36eb32319328068d6643a43bdb82c1581a388fb3`  
**Candidate branch head:** `2ce16476501ca792d723f5f555ff6b792d90d484`  
**Manifest source/test-merge SHA:** `cb28946b6dd41bdecbd04a5554d76514ab0bd6b1`

## Immutable six-binary identities

- EN DOCX — `54e1e4a2c89b697b9a510810e551ed576543b62e1b0e405325295c0c091f1239` — 50,495 bytes
- EN PDF — `1c125e8e826ae66c0744a5ee0eba1872ff4cf20f722ddda958dd52a50b7017d1` — 381,058 bytes
- es-419 DOCX — `89cfecdda3130b52f405c366f0a4b53cf4bed9ece53795d01e33c1a08d3985eb` — 40,992 bytes
- es-419 PDF — `ee076e0803dc0d7726655e4b1db5c9b74b5ffc45d0d9c3d6c4b83bb6cbe72dd4` — 80,473 bytes
- pt-BR DOCX — `2f007b67fa636b9cf63595e1c5d6d521a3e250ea4f75a60ec350e12018e23aec` — 40,989 bytes
- pt-BR PDF — `bc46f30de88d447353b4ebd7a25fc7dfe5498a7bed6fd7f5119dbe16a691ae4e` — 80,983 bytes

## Independent verification

The exact workflow artifact was downloaded without regeneration. Independent local SHA-256 hashing matched all six manifest identities byte-for-byte.

Rendered QA was performed on all three PDFs and all three DOCX files. Page counts were EN 22 pages, es-419 5 pages and pt-BR 5 pages for both PDF and DOCX render paths. Contact-sheet inspection found no blank pages, clipped text, overlapping content, broken glyph blocks or obvious layout corruption.

The exact candidate head passed:

- Workflow Security;
- Release Pipeline Meta QA;
- Release Package QA; and
- Manual 46 Candidate Build, including automated PDF nonblank/content preflight.

## Release disposition

Manual 45 is already published. Manual 46 may proceed to exact-byte staging and exact staged-head QA. Under the canonical release authorization, no separate generic human approval prompt is required once all remaining applicable objective gates are green and no unresolved material issue remains.
