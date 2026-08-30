# Front-Line Promotion Release-Ready Control

Effective immediately, a manual may not be promoted into the front-of-line publication lane merely because its architecture, source watch, or generic QA lane is green.

## Required pre-front-line state
Before a manual becomes the next publication-front manual, it must already have, to the maximum extent safely possible:

1. Controlled English source complete across the required 32-chapter architecture.
2. es-419 and pt-BR controlled localized drafts complete and aligned to the English controlling interpretation.
3. Authoritative-source/version verification current enough for candidate build, with only a final release-time delta check remaining.
4. Publication-candidate DOCX/PDF generation completed or reproducibly ready from the exact controlled source.
5. Rendered-document QA completed for content, accessibility, links, headings, tables, language metadata and visual integrity.
6. Terminology and trilingual parity QA completed on the candidate lineage.
7. SHA-256 checksums, provenance, manifest inputs and durable-binary staging plan complete; validated binaries must not be resaved/regenerated after hash binding.
8. Catalog, work-product release registry and lifecycle reconciliation prepared as a near-final publication transaction.
9. No unresolved technical, source, integrity, packaging or substantive defect that would predictably delay publication once predecessor order clears.

## Promotion rule
A downstream manual that does not meet this pre-front-line state remains in build/QA/pre-publication and is not treated as publication-front ready. Instead, its missing candidate work is accelerated while later manuals continue in parallel.

## Rolling conveyor
While Manual N is front-of-line:
- Manual N+1 should be pre-publication/release-candidate ready.
- Manual N+2 should have candidate build and QA substantially complete.
- Manual N+3 should be in full controlled build/localization.
- Later manuals remain source-verified, architected and pre-staged, and should be promoted as capacity permits.

Publication order remains strictly sequential. This control changes preparation timing, not release order. Genuine technical/integrity/source/security failures remain fail-closed. Missing duplicate approval paperwork alone does not block a clean candidate under the canonical release rule.
