# Manual 17 — Exact Candidate Artifact Handoff

**Status:** EXACT CANDIDATE BUILT / DURABLE STAGING PENDING  
**Manual:** 17 — NIST Privacy Framework Controlled Implementation  
**Candidate PR head:** `c73320bc40990918f805e1f29602cebfa4f56be3`  
**Merged candidate builder commit:** `4764ea2e0e7903f65f7f3dd9001992442b001922`  
**Candidate workflow run:** `33349530887`  
**Candidate artifact ID:** `9743124097`  
**Artifact name:** `manual17-six-binary-candidate`  
**Artifact ZIP digest:** `sha256:09ba46423ca930228da1d8d33eba244e9975c47af8acfda82f067aa90a155f36`

## Exact candidate identities

| Locale | File | SHA-256 | Bytes |
|---|---|---|---:|
| en | `Manual_17_NIST_Privacy_Framework_Controlled_EN.docx` | `8eb3d6270158e43d75e7a18c3202ff8fcfb3b2dbde8e707cd605d1f0a7419180` | 42659 |
| en | `Manual_17_NIST_Privacy_Framework_Controlled_EN.pdf` | `542ea854027c0c6f2a908263aee80db118ac5aaa6514b7e0a69ceee4f6b0b547` | 83205 |
| es-419 | `Manual_17_NIST_Privacy_Framework_Controlled_ES-419.docx` | `3dce5cb82d71cd0124c368aca8e03cb424869593e72f49678e403cf4dc649d00` | 43008 |
| es-419 | `Manual_17_NIST_Privacy_Framework_Controlled_ES-419.pdf` | `45458495a9d51557d5a4ddeb824fe4e7f67dd58ea9cbad22aeb2afb5305ce52c` | 87370 |
| pt-BR | `Manual_17_NIST_Privacy_Framework_Controlled_PT-BR.docx` | `55b67932cfab909178c6ef81374e593902d961379fc34d4ab010458dfb5abb3a` | 43003 |
| pt-BR | `Manual_17_NIST_Privacy_Framework_Controlled_PT-BR.pdf` | `1ab13ad82bed84d041869ad90ee7699322c502c3bd70638eca7daec7cfbb4973` | 87731 |

Candidate manifest SHA-256: `68a7b6f2d42e88255dea42ce09055abdeb749ea7f3d6f3668fda8daed0446d70`.

## Exact-head QA observed before candidate merge

The exact candidate head completed successfully in all observed required candidate-stage workflows:

- `06 - Workflow Security`
- `21 - Release Pipeline Meta QA`
- `07 - Release Package QA`
- `17 - Manual 17 Candidate Build`

The candidate-build job also completed its explicit PDF nonblank preflight before artifact upload.

## Fail-closed staging rule

Durable staging must use the six exact bytes identified above. Do not regenerate substitutes after this handoff. Before publication-state reconciliation, the repository must contain these exact files in the Manual 17 publication tree, with hashes reverified against this record and the candidate manifest. Publication remains unchanged until durable staging, applicable release QA/provenance, and catalog/release-registry reconciliation are complete. No human-review evidence is asserted by this handoff.