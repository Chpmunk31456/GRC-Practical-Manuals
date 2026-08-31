# Manual 29 — Exact Candidate Provenance and Deterministic QA

Manual: **Software / AI Supply Chain Assurance**

Candidate workflow run: `33403413629`

Artifact: `9762169998` (`manual29-six-binary-candidate`)

Artifact digest: `sha256:6abe47518c493b6c67447c0e21ca9d855b5a6189e78205f30f2eee3ec461b6b0`

Manifest source commit: `5063eeffb06805d7e8c36c3fc0f8a65a78926698`

## Immutable binary identities

| Locale | File | Bytes | SHA-256 |
|---|---|---:|---|
| en | `Manual_29_Software_AI_Supply_Chain_Assurance_Controlled_EN.docx` | 41017 | `1396adae831ce8e564d69be254ec4559082b9f3b43c7796b225abfb94af039b3` |
| en | `Manual_29_Software_AI_Supply_Chain_Assurance_Controlled_EN.pdf` | 68222 | `b3ed3e5ba625dbaf0d7b5d72d8f1ba7e584f2e85784bc503da6f60e8d6e1ca61` |
| es-419 | `Manual_29_Software_AI_Supply_Chain_Assurance_Controlled_ES-419.docx` | 40181 | `faaab9abc32816742e806023aa01bdbc6657eed48ce82160c1b19bd11e3a83fc` |
| es-419 | `Manual_29_Software_AI_Supply_Chain_Assurance_Controlled_ES-419.pdf` | 68373 | `78de8c2cfc7386e3b9304862f45570176436f9d987c3bb3bc2eb2e3d1bd71df9` |
| pt-BR | `Manual_29_Software_AI_Supply_Chain_Assurance_Controlled_PT-BR.docx` | 40179 | `260515992de52104d213d66a810bc59c008d16e32cec95f81dd53a4e51016208` |
| pt-BR | `Manual_29_Software_AI_Supply_Chain_Assurance_Controlled_PT-BR.pdf` | 68319 | `8178bd3255c4393722d2db355b9ff3d24b1c7b79d06cb3da82946382401c76e0` |

## Deterministic QA performed on the downloaded exact artifact

- All six file byte counts and SHA-256 identities match the workflow manifest exactly.
- All three DOCX packages pass ZIP/package integrity checks and contain Chapters 01–32 in `word/document.xml`.
- DOCX accessibility audit: zero high, medium, or low findings for EN, es-419, and pt-BR.
- All three PDFs are openable, unencrypted, tagged, letter-size, and text-searchable.
- PDF text inspection confirms Chapters 01–32 in each locale; line wrapping in extracted headings does not remove chapter content.
- Exact PDF page counts: EN 5, es-419 5, pt-BR 5.
- Independent DOCX rendering produced EN 5, es-419 5, pt-BR 4 pages; every rendered page was visually inspected.
- Full PDF and DOCX render review found no clipping, overlap, broken glyphs, missing sections, or malformed pages.
- No deterministic defect was identified that requires candidate regeneration.

## Release constraint

These six identities are the only reviewed Manual 29 candidate binaries eligible for durable staging in this release transaction. Staging must re-verify every SHA-256 value and copy the exact bytes without regeneration. Publication remains sequential after published Manual 28 and remains fail-closed on any material source, applicability, integrity, packaging, accessibility, provenance, or substantive defect.