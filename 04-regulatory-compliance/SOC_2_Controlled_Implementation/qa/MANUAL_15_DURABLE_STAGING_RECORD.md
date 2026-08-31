# Manual 15 — Durable Publication Candidate Record

Status: exact candidate bound for final release reconciliation; publication authorization remains subject to the repository clean-candidate release rule.

## Exact candidate identity

- Source PR: #231 — `Build Manual 15 — publication candidate artifacts and QA`
- Source head SHA: `c2b2878c86078ac7e6856a91453c1f6ee520965d`
- Merged artifact-gate commit: `cc590511fa31e9885915bb7d0cf7145097c046ac`
- Manual-specific workflow: `36 - Manual 15 Publication Candidate`
- Workflow run: `33343953303`
- Workflow result: success
- Artifact ID: `9741396149`
- Artifact name: `manual15-publication-candidate`
- Artifact digest: `sha256:2d097bf623090162ce3f258ded56ff6fa584e80a7dd101b9d155d8107a140021`

## Exact candidate files

The six generated candidate binaries were independently re-hashed after downloading the workflow artifact and match `MANUAL_15_SHA256SUMS.txt` exactly:

- EN DOCX: `335c1219291f2528f1c769ea190df375d454586150f7123b129d8d0711008de9`
- EN PDF: `6b70290b538cd201cae82e85ea70d0380899c01ce03e7e74eb71618fee8707ee`
- es-419 DOCX: `6c8ca66c19db10178f30b83093dd50bf737fd206246c436474d83ffe3fe2f4ce`
- es-419 PDF: `11a27d858bea59d4e80612a09bb85253a00eed7f1c14e878cc3c47c87934aaaa`
- pt-BR DOCX: `7ebbb4bfef17c79f1f13e271a1a9166f272333d2cf3dd6b66ce048467953da6c`
- pt-BR PDF: `0b2faa2c479d78ab376a66a23936f12b29f49137146a7af344d5facef4ade454`

## Release boundary

No regeneration is permitted after this binding unless a defect requires remediation, in which case the candidate must be regenerated, re-hashed, re-reviewed, and rebound as a new exact candidate. Final publication requires release-state/catalog reconciliation and any remaining repository-mandated review evidence to be green with no unresolved defects.
