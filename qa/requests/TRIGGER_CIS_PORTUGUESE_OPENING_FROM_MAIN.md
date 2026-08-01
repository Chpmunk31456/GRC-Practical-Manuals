# Trigger CIS Spanish figure-markup normalization and rebuild

Run the controlled CIS Controls v8.1 Spanish publication workflow against `production/multilingual-grc-editions` using the current workflow definition on `main`.

The workflow must:

- preserve the reviewed Spanish language content;
- normalize only Figures 4–8 from raw HTML image tags to equivalent Markdown image syntax;
- preserve each figure filename, alt text, caption, and surrounding prose;
- generate deterministic Spanish Figures 1, 2, and 4–10 while retaining reviewed Figure 3;
- require all ten source figure files and at least ten embedded DOCX media objects;
- require all ten figure captions in searchable PDF text;
- rebuild only the CIS Spanish DOCX and PDF;
- commit the normalized Markdown, figures, rebuilt files, and updated SHA-256 record to the production branch; and
- render every rebuilt PDF page for a new visual-review artifact.

This PR is trigger-only, modifies no publication content on `main`, and must not be merged.
