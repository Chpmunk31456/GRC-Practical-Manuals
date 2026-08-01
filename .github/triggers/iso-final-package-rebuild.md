# Trigger final ISO localized package rebuild

Run the bounded rebuild, full-page raster preflight, checksum, and QA evidence workflow against `production/multilingual-grc-editions`.

This retry normalizes resolvable Portuguese raw-HTML image tags to Pandoc-native Markdown while preserving alt text and dimensions, then requires all nine source image placements to be embedded in the rebuilt DOCX.

Trigger only. Do not merge this branch or pull request.
