# Release Manifest and Provenance Control

Every published manual release must have a machine-readable release manifest that ties the published artifacts to the exact repository state and review evidence.

## Required manifest fields

At minimum record:

- manual ID and manual number;
- title;
- version / edition;
- release status;
- languages;
- repository;
- source branch;
- release Git commit SHA;
- source-verification date;
- authoritative-source baseline identifier or evidence reference;
- translation-review status per language;
- editorial-QA status per language;
- human-approval status and evidence reference;
- visual-QA status;
- accessibility-QA status;
- repository/security-QA status;
- generated artifact list;
- SHA-256 checksum for each artifact where practical;
- GitHub release/tag;
- Zenodo concept DOI and version DOI when assigned;
- release date;
- known exceptions / limitations;
- supersedes / superseded-by relationship where applicable.

## Provenance rules

1. A manifest must identify the exact Git commit used to create the release package.
2. Generated DOCX/PDF artifacts must not be treated as controlled source.
3. A later regeneration from a different commit requires a new manifest or an explicitly versioned manifest revision.
4. Do not insert a Zenodo DOI before Zenodo has actually assigned it. Use `pending` or null according to the schema.
5. Do not silently alter checksums after publication. Changed bytes require an updated release/version record.
6. Human approval evidence must be referential and auditable; an automated PASS cannot impersonate a human sign-off.
7. GitHub release metadata, README/CITATION references, and Zenodo metadata must be reconciled before completion.

## Artifact record

Each artifact should record:

- filename;
- language;
- media type / format;
- source commit;
- generated date;
- generation method/tool if known;
- byte size;
- SHA-256 checksum;
- accessibility status;
- page-by-page QA status where relevant.

## Release gate

The release manifest is finalized only after all required pre-release gates pass. Zenodo identifiers may be appended after Zenodo publication, but the final manifest must then be reconciled to the published record without changing historical release facts.

The companion schema is `.compliance/release-manifest.schema.json`.
