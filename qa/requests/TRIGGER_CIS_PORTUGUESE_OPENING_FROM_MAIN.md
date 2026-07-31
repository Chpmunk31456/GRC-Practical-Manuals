# Trigger CIS Spanish publication rebuild

Run the controlled CIS Controls v8.1 Spanish publication rebuild against `production/multilingual-grc-editions`.

The workflow must:

- preserve the reviewed canonical Spanish Markdown source;
- rebuild only the CIS Spanish DOCX and PDF;
- validate DOCX archive integrity;
- validate searchable PDF text and required Spanish markers;
- confirm embedded media is present;
- record SHA-256 checksums for Markdown, DOCX, and PDF; and
- commit only the rebuilt CIS Spanish publication files and checksum record to the production branch.

This PR exists only to generate an observable `pull_request` workflow event. It modifies no publication content on `main` and must not be merged.
