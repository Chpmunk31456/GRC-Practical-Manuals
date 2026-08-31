# Manual 33 — SEC Cybersecurity Exact Candidate Provenance

## Candidate identity

- Manual: 33 — SEC Cybersecurity Governance and Disclosure Controlled Implementation
- Candidate workflow run: `33419060069`
- Artifact: `9768178273` (`manual33-six-binary-candidate`)
- Artifact digest: `sha256:8b3428492a6f5cdf43c53a38259332822286cc79947868cbcb2b514c114f628f`
- Workflow head: `0e7c0e8a91e4590daa87fdc235779804c960d699`
- Manifest source commit: `5ebe52d41a208d65d52e90882f56f07f5a7f2624`
- Candidate builder/workflow merged to `main` through PR #410 at `8ae433755a9d87dc65a09c3ff7a1f3951913f1ce`.

## Exact six publication identities

| Locale | File | Bytes | SHA-256 |
|---|---|---:|---|
| en | `Manual_33_SEC_Cybersecurity_Governance_Disclosure_Controlled_EN.docx` | 41255 | `b1b4ca7e336a11c8afc6c3f3e4d021d883eeb0de7201915d347d3868d483ac6f` |
| en | `Manual_33_SEC_Cybersecurity_Governance_Disclosure_Controlled_EN.pdf` | 67787 | `729e8f0f46b34b87653dd5f58cbdb30fc108dfba0b2e7c34fa943bb326eab13a` |
| es-419 | `Manual_33_SEC_Cybersecurity_Governance_Disclosure_Controlled_ES-419.docx` | 41089 | `d1293f03eb42662dcc677b6912de2492ad73793cc12991d1c8c8a87065a73674` |
| es-419 | `Manual_33_SEC_Cybersecurity_Governance_Disclosure_Controlled_ES-419.pdf` | 68839 | `2674cd2b4a7f469344ba0ca75f3df222648caee49081cbf91a0d1cf16f0e16ea` |
| pt-BR | `Manual_33_SEC_Cybersecurity_Governance_Disclosure_Controlled_PT-BR.docx` | 41026 | `e68e98ef272a24da2cf8f3ac5527902fc55a3ce4a554c20e225e96552ec46f07` |
| pt-BR | `Manual_33_SEC_Cybersecurity_Governance_Disclosure_Controlled_PT-BR.pdf` | 69267 | `41cc7cbe9561027264d73cd8c103f3e0a5a3fa8dde186c6886c1d91919fdb26d` |

## Deterministic exact-artifact QA

The artifact ZIP downloaded directly from GitHub Actions was inspected without regeneration.

- All six byte counts and SHA-256 values match the workflow manifest exactly.
- All three DOCX packages open structurally and contain Chapters 01–32.
- All three PDFs open successfully, contain extractable/searchable text, and contain Chapters 01–32.
- PDF pages: EN 5; es-419 5; pt-BR 5.
- Full rendered review of every PDF page in all three locales found no clipping, overlap, missing chapter, broken glyph, blank-page, or other deterministic layout defect requiring regeneration.
- DOCX package inspection found no tables or images requiring table-header/alternative-text remediation in this candidate and no missing chapter structure.
- No deterministic integrity, packaging, accessibility, or rendering defect requiring candidate regeneration was identified.

## Release-time source boundary

The official SEC source was revalidated on 2026-08-31. SEC Release No. 33-11216 remains the final rule, effective September 5, 2023, covering cybersecurity incident disclosure plus risk-management, strategy, governance, and Inline XBRL requirements. Binding rules/forms remain distinct from Commission or staff guidance, petitions/proposals, enforcement facts, and issuer-specific materiality/legal determinations. The manual does not purport to make an issuer-specific materiality, filing, legal-compliance, or disclosure decision.

## Release state

Predecessor Manual 32 is published in both central registries. This provenance record does not itself publish Manual 33. Exact-byte durable staging, exact-head regression QA, and final catalog/work-product registry reconciliation remain required. No reviewed candidate binary may be regenerated or modified after this provenance point unless a real defect requires an explicitly superseding candidate and new provenance.