# Trigger complete CIS Spanish figure restoration

Run the controlled CIS Controls v8.1 Spanish figure-restoration and publication workflow against `production/multilingual-grc-editions`.

The workflow must:

- preserve the reviewed Spanish Markdown content;
- generate deterministic Spanish Figures 1, 2, and 4–10 while retaining reviewed Figure 3;
- require all ten figure files to exist;
- rebuild only the CIS Spanish DOCX and PDF;
- require at least ten embedded DOCX media assets and all ten figure captions in searchable PDF text;
- record updated SHA-256 checksums; and
- render every rebuilt PDF page for a new page-level visual review artifact.

This PR exists only to generate an observable `pull_request` workflow event. It modifies no publication content on `main` and must not be merged.
