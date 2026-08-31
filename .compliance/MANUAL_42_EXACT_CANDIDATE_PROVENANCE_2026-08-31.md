# Manual 42 — Exact Candidate Provenance and QA

**Manual:** Manual 42 — Canada Privacy Controlled Implementation  
**Frozen candidate workflow run:** `33445214696`  
**Frozen artifact ID:** `9777769425`  
**Artifact name:** `manual42-six-binary-candidate`  
**Artifact digest:** `sha256:ac270e6af7e514fada095a3a2d6898ce97bc3064bf526788b8828b46e4d33ee7`  
**Candidate workflow head:** `3e2748b249025f5ecee1380579e712f3427fa0e3`  
**Manifest source commit:** `36f7214e9a8455f470504043e3178b465c65cb21`

## Immutable six-binary identities

- EN DOCX — `ef3911d260c4c222d54b47e8959e744275dc1ab93f1a583fe6f63d8bd9611f3f` — 39,923 bytes
- EN PDF — `b9646b813e376655b8d764a44f8438a46ba34c61422d4813850cd055b817ca20` — 59,134 bytes
- es-419 DOCX — `520e54d6b5c71b16c14945fba2e80864b9dd765d793deec4ed1a8ae1ad7bd62c` — 39,566 bytes
- es-419 PDF — `647159d160f533d9dd6e448a0aeb5d9d79b740872ed8bf674b71ebd979648747` — 59,570 bytes
- pt-BR DOCX — `833ea6c2f25b23facbef3edd9b1b27c6c3cc2f2de02dab9dd6b29b9f7489788d` — 39,534 bytes
- pt-BR PDF — `88ee01f84ec3d1eecd716aa3adeecba4fed5711c6e5b36ccfc7ab25f1a1e1aac` — 59,616 bytes

## Exact-candidate verification

The downloaded workflow artifact was independently re-hashed without regeneration. Every SHA-256 identity and byte size matches the generated manifest exactly. Every DOCX contains all 32 controlled chapters. Each PDF contains searchable text, is nonblank, four pages long, and is unencrypted. The candidate build transaction passed Workflow Security, Release Pipeline Meta QA, Manual Structure QA, Trilingual Publication Parity, Release Package QA, and the dedicated read-only Manual 42 Candidate Build.

Publication remains sequential after Manual 41. Exact-byte staging and staged-head QA must preserve these identities.