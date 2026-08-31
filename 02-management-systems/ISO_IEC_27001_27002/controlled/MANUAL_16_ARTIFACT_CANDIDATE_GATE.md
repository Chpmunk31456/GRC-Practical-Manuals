# Manual 16 — Artifact Candidate Gate

**State:** active front-line publication-candidate preparation.

The controlled English, es-419 and pt-BR Markdown sources are frozen on `main`. This gate advances Manual 16 into durable publication-candidate production without changing publication state.

## Required candidate set

Produce exactly six durable binaries from the frozen controlled sources:

- English DOCX
- English PDF
- Spanish (es-419) DOCX
- Spanish (es-419) PDF
- Portuguese (pt-BR) DOCX
- Portuguese (pt-BR) PDF

## Candidate acceptance requirements

Each candidate must:

1. derive only from the frozen controlled source for its locale;
2. preserve heading hierarchy, tables, links and document semantics;
3. pass PDF content preflight and rendered/visual review;
4. pass required accessibility checks, including language metadata, reading order, headings, tables, links and alternative text where applicable;
5. have a recorded SHA-256 identity;
6. be bound to source lineage and workflow evidence;
7. be staged durably on `main` before publication-state reconciliation.

Any binary content change after hashing invalidates the candidate and requires re-generation, re-hashing and revalidation.

## Front-line automatic advancement

When the six binaries, QA evidence, hashes and provenance are complete and no substantive defect remains, advance immediately to durable staging and release QA under the repository-wide Future Manual Pipeline Standard. Do not wait for another routine prompt.
