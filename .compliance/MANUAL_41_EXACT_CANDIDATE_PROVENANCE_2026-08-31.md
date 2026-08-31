# Manual 41 — Exact Candidate Provenance and QA

**Manual:** Manual 41 — UK GDPR / Data Protection Act Controlled Implementation  
**Frozen candidate workflow run:** `33440744859`  
**Frozen artifact ID:** `9776138801`  
**Artifact name:** `manual41-six-binary-candidate`  
**Artifact digest:** `sha256:c2fdde24ffa5e549b2e46cac474f244739f67125f369b0452f9c3664e875dd6f`  
**Candidate workflow head:** `0426c7c5e6b3c4c1a6c8b06b41d17786ec7f6a6f`  
**Manifest source commit:** `1e775b0211607f39a7343f6fc7bf037126240b6b`

## Immutable six-binary identities

- EN DOCX — `4b97c7233db7488bccc2556965ca9b75255c3928b100ef2665fb85afd050a282` — 39,975 bytes
- EN PDF — `2ce430e8ce0b94c039195f8d95fc5cf0e08fc72eaee9a107e38c802c4698dce1` — 61,982 bytes
- es-419 DOCX — `6b91ffb2452da3e3565eefb6f92e2c602c8065a673db0414e15959cabec371d3` — 39,811 bytes
- es-419 PDF — `3f350f3c3e134b3e1f752ffe926fdb8868b6c3f21f8403c31a33cfa915d1c4fa` — 60,911 bytes
- pt-BR DOCX — `70e894de6214d5b62ed48d48df9629dbd3137962e0eff5168f7b817ec0114732` — 39,818 bytes
- pt-BR PDF — `a961953a9a114e2675e58067cd61c3ad1c14aece4eb759b10c0cf46bd944da10` — 62,653 bytes

## Exact-candidate verification

The downloaded workflow artifact was independently re-hashed without regeneration. Every SHA-256 identity and byte size matches the generated manifest exactly. Every DOCX contains all 32 controlled chapters. Each PDF contains searchable text, is nonblank, and is unencrypted. The candidate build transaction passed Workflow Security, Release Pipeline Meta QA, Manual Structure QA, Trilingual Publication Parity, Release Package QA, and the dedicated read-only Manual 41 Candidate Build.

Publication remains sequential after Manual 40. Exact-byte staging and staged-head QA must preserve these identities.