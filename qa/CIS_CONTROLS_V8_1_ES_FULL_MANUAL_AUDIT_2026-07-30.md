# CIS Controls v8.1 Spanish Full-Manual Audit

Target: `01-foundations/CIS_Controls_v8.1/Espanol/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md`

Source workflow run: `30590759747`

Artifact: `cis-spanish-full-manual-audit` (artifact ID `8778247619`)

Audit candidate SHA: `c0b744c3e66594cf9d1d4486f86e78df803be3e4`

## Result

**FAIL — publication-blocking defects remain**

## Summary

- ANTER corruption: **3**
- Silencioso token: **36**
- TEN token: **257**
- arrow artifact: **32**
- broken image marker: **6**
- ellipsis table delimiter: **22**
- residual English phrases: **4**
- tención token: **182**
- Missing expected numbered sections: **9**
  - `# 1.`, `# 3.`, `# 8.`, `# 10.`, `# 12.`, `# 17.`, `# 21.`, `# 22.`, `# 28.`

## Publication decision

The defect distribution demonstrates that the current Spanish edition cannot be remediated safely through isolated token deletion or a small number of section patches. Corruption affects headings, tables, safeguard names, safeguard descriptions, evidence fields, image markup, role matrices, management guidance, and career/laboratory content across the manual.

The current edition must therefore be treated as a superseded machine-generated draft. Publication requires a controlled full-edition replacement derived from the authoritative English source, followed by native-language review, structural comparison, document regeneration, page-level visual inspection, accessibility review, link verification, and technical/factual review.

## Representative findings

| Category | Line | Excerpt |
|---|---:|---|
| ellipsis table delimiter | 16 | `|... |` |
| arrow artifact | 212 | `← Salvaguardia | Acción focalizada que puede ser asignada, implementada y medida` |
| broken image marker | 222 | `■img src="media/image2.png" ...` |
| Silencioso token | 226 | `| **La situación física** Silencioso** |` |
| TEN token | 266 | `TEN IT / Engineering | Implementación...` |
| tención token | 268 | `tención Auditoría interna / evaluador` |
| broken image marker | 335 | `■img src="media/image4.png" ...` |
| corrupted safeguard row | 344 | Control 1.1 row contains generated tokens and broken column boundaries |
| corrupted safeguard row | 361 | Control 2.1 row begins with `TEN` and contains malformed translated text |
| broken image marker | 471 | `■img src="media/image7.png" ...` |
| mixed-language safeguard | 484 | Control 7.5 contains untranslated English safeguard language |
| arrow artifact | 499 | Control 8.1 contains an arrow marker inside the row |

The complete line-by-line findings remain available in workflow artifact `8778247619`, digest:

`sha256:59e7c45455edf3d7d773ab3d06672bfa5c1c2b898f2e71c4efb187fcd1dfe70e`

## Required replacement gates

1. Reconstruct all numbered sections from the authoritative English source.
2. Preserve the 18 Controls and all 153 Safeguards with complete table rows.
3. Preserve localized figures using valid Markdown image syntax and verified captions/alt text.
4. Eliminate all known generated-token and malformed-table patterns.
5. Compare the Spanish heading and safeguard-ID inventory against the English source.
6. Regenerate DOCX and searchable PDF packages.
7. Validate DOCX ZIP integrity, PDF text extraction, embedded media, links, and metadata.
8. Conduct complete native-language, visual, accessibility, and technical/factual reviews.
9. Re-run the full-manual fail-closed audit at the exact candidate SHA.

No merge or publication approval should be granted to the current CIS Spanish edition.
