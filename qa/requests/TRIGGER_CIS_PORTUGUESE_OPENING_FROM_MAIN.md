# Trigger CIS Spanish visual review package

Run the controlled CIS Controls v8.1 Spanish visual-review packaging workflow against `production/multilingual-grc-editions`.

The workflow must:

- preserve the reviewed canonical Spanish Markdown source and rebuilt publication files;
- render every PDF page to an image;
- create numbered page indexes and contact sheets;
- record PDF metadata, page dimensions, layout-preserving extracted text, and SHA-256 checksums; and
- upload the review package as a temporary workflow artifact for page-level inspection.

This PR exists only to generate an observable `pull_request` workflow event. It modifies no publication content on `main` and must not be merged.
