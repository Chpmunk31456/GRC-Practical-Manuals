# Trigger diagnostic CIS Spanish figure restoration

Run the controlled CIS Controls v8.1 Spanish figure-restoration and publication workflow against `production/multilingual-grc-editions` using the diagnostic validation committed on `main`.

The workflow must:

- preserve the reviewed Spanish Markdown content;
- generate deterministic Spanish Figures 1, 2, and 4–10 while retaining reviewed Figure 3;
- require all ten source figure files;
- rebuild only the CIS Spanish DOCX and PDF;
- report the exact missing PDF caption or DOCX embedded-media count if validation fails;
- record updated SHA-256 checksums after success; and
- render every rebuilt PDF page for a new visual-review artifact.

This PR is trigger-only, modifies no publication content on `main`, and must not be merged.
