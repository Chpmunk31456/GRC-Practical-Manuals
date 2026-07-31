# Trigger CIS Spanish opening integration

Run the controlled opening-only integration against the canonical CIS Controls v8.1 Spanish source on `production/multilingual-grc-editions`.

The workflow must:

- replace only the opening block before Chapter 1 with the reviewed Spanish rewrite;
- verify an exact boundary match;
- reject known machine-translation and malformed-Markdown tokens;
- rerun the full-manual Spanish audit; and
- commit only the canonical Spanish Markdown source and refreshed audit report to the production branch.

This PR exists only to generate an observable `pull_request` workflow event. It modifies no publication content on `main` and must not be merged.
