# Manual 32 — FFIEC Exact Candidate Provenance

## Candidate identity

- Manual: 32 — FFIEC Controlled Implementation
- Candidate workflow run: `33415623228`
- Artifact: `9766895211` (`manual32-six-binary-candidate`)
- Artifact digest: `sha256:ffc7f19ccf321e23bdcaa34ffb76f5b1e399e64cbe2f46278a187655987896f0`
- Workflow head: `00f17f2a4c004dc648c5bf3adc0eebf1e41c2a38`
- Manifest source commit: `5075a709805c0c5357da7801e9513a657010d5c0`
- Candidate builder/workflow merged to main at `3db4fe5174b72a967ce95f0c6f11c08c40fd1834`.

## Exact six publication identities

| Locale | File | Bytes | SHA-256 |
|---|---|---:|---|
| en | `Manual_32_FFIEC_Controlled_EN.docx` | 41436 | `9997aa25662657760290fdd36b58daec0e6be45dc567e0f06c034a0f21cb48b5` |
| en | `Manual_32_FFIEC_Controlled_EN.pdf` | 69268 | `9ea725e5a3a198677f4fb9dbf8112eb7f297f1940ada8a166accad3310d2264f` |
| es-419 | `Manual_32_FFIEC_Controlled_ES-419.docx` | 41064 | `c0132d94b58e5a952c4451afc6c6435e7aebc524d1e94d9d7468a789a24b2940` |
| es-419 | `Manual_32_FFIEC_Controlled_ES-419.pdf` | 67593 | `59b8e7f1a451f58089eba1d4487bdfcc1657c477f592eade83c8b6e2cd4f1861` |
| pt-BR | `Manual_32_FFIEC_Controlled_PT-BR.docx` | 41036 | `9d9f2a81f45de2ceaffdc41a085c80820a3c9cb7f690ca91ed79952741cf41db` |
| pt-BR | `Manual_32_FFIEC_Controlled_PT-BR.pdf` | 68290 | `e3a13598e2e8d18de23b5d84f2ed8b9da913d562e539a16199711aee83710aa8` |

## Deterministic exact-artifact QA

The artifact ZIP downloaded directly from GitHub Actions was used without regeneration.

- All six byte counts and SHA-256 values match the workflow manifest exactly.
- All three DOCX packages open structurally and contain Chapters 01–32.
- DOCX accessibility audit: EN `0 high / 0 medium / 0 low`; es-419 `0/0/0`; pt-BR `0/0/0`.
- All three PDFs are openable, unencrypted, non-scanned/searchable files with no XFA.
- PDF chapter extraction confirmed Chapters 01–32 in every locale.
- PDF pages: EN 6; es-419 5; pt-BR 5.
- Full rendered PDF and DOCX page review found no clipping, overlap, missing sections, broken glyphs, or other deterministic layout defect requiring regeneration.

## Source and applicability boundary

Release-time source preparation uses the active FFIEC IT Examination Handbook and applicable member-agency overlays. The FFIEC Cybersecurity Assessment Tool was sunset on August 31, 2025 and is not treated as a current FFIEC examination/self-assessment baseline. FFIEC examination guidance, binding law/regulation, member-agency overlays, institution-specific supervisory findings/commitments, and organisation implementation practice remain distinct.

## Release state

Predecessor Manual 31 is published. This provenance record does not itself publish Manual 32. Exact-byte durable staging and final catalog/work-product registry reconciliation remain required. No reviewed candidate binary may be regenerated or modified after this provenance point unless the candidate is explicitly superseded by a newly built and newly reviewed artifact.
