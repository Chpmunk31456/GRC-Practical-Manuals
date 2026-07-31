# Controlled integration request: CIS Controls v8.1 Spanish Sections 6–10

Integrate the reviewed Spanish replacement for Sections 6 through 10, covering Controls 1 through 5, into the production Markdown source.

Replacement source:
`qa/rewrite/CIS_CONTROLS_V8_1_ES_SECTIONS_6_10_REVIEWED.md`

Integration script:
`qa/tools/integrate_cis_spanish_sections_6_10.py`

After integration, refresh the full-manual corruption audit. Do not merge or publish PR #3.

Explicit retrigger requested on 2026-07-30 at 20:19 Colombia time after confirming the first request did not produce an integration commit.

Second explicit retrigger requested on 2026-07-30 at 20:30 Colombia time after the validator was confirmed to use a boundary-aware standalone `tención` check.
