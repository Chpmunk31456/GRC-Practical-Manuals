# Manual 36 — Brazil LGPD exact candidate provenance and QA

**State:** immutable publication candidate bound; publication state unchanged.  
**Candidate workflow run:** `33426527901`  
**Candidate artifact:** `9770956924` (`manual36-six-binary-candidate`)  
**Artifact digest:** `sha256:c94b5d53ac5a80e6c668d99d10eb1acf1fd7d2ef8891e2815b9a9d542ad84886`  
**Workflow head:** `bfb3f75c78286207f17dece61619935b3dd2e3dd`

## Exact artifact identities

| Locale | File | Bytes | SHA-256 |
|---|---|---:|---|
| en | `Manual_36_Brazil_LGPD_Controlled_EN.docx` | 42631 | `00f9e2dcbcc0821205ab294505470ce300c6930d87e4752d45548b10e7a0244c` |
| en | `Manual_36_Brazil_LGPD_Controlled_EN.pdf` | 80037 | `daa982822b3d7196a2086e44011609d5109e3e42ef047573f59cf4cf5be4db4c` |
| es-419 | `Manual_36_Brazil_LGPD_Controlled_ES-419.docx` | 42187 | `4beb1f47dc48403fab22f84ff207e8c62a51ae67da168dc49e1e05b1566d55b3` |
| es-419 | `Manual_36_Brazil_LGPD_Controlled_ES-419.pdf` | 78503 | `90379290467faf6a14c7896ec290c00586668a9a8e38af5aee33e741e32eeb82` |
| pt-BR | `Manual_36_Brazil_LGPD_Controlled_PT-BR.docx` | 42184 | `826dc9a096feabc117b263bb4dca12f857976a3a0ef3816e4935cbdcc26bbd16` |
| pt-BR | `Manual_36_Brazil_LGPD_Controlled_PT-BR.pdf` | 79101 | `639378950c6119fa816a6d1c79f445616ebd5c7d7a571838d381aae3efb5f593` |

## Deterministic QA performed on downloaded immutable artifact

- All six independently recomputed SHA-256 hashes match the workflow manifest.
- All six files are non-empty and structurally openable.
- Chapters 01–32 are present in every DOCX and PDF edition.
- All three PDFs are searchable, unencrypted, and seven pages each.
- DOCX accessibility audits for EN, es-419, and pt-BR returned 0 high, 0 medium, and 0 low findings.
- Every page of every exact DOCX and PDF candidate was rendered and visually inspected. No clipping, overlap, blank-page defect, broken glyph, missing section, or truncated chapter was observed.
- No candidate artifact was regenerated or modified after the workflow artifact was frozen.

## Release boundary

The candidate remains subject to exact-byte durable staging, staging-head structure/parity/release QA, predecessor-order verification (Manual 35 published), and final catalog/work-product release-registry reconciliation. Any material change to a reviewed artifact supersedes this candidate and requires a new candidate identity and review cycle.
