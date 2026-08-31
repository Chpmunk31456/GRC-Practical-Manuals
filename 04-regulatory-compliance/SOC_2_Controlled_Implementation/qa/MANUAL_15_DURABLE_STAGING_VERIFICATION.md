# Manual 15 — Durable Staging Verification

Status: deterministic staging evidence only; no human-review decision is asserted.

- Source artifact: `manual15-publication-candidate`
- Artifact ID: `9741396149`
- Source workflow run: `33343953303`
- Artifact digest: `sha256:2d097bf623090162ce3f258ded56ff6fa584e80a7dd101b9d155d8107a140021`
- Durable-staging workflow: `37 - Manual 15 Durable Staging`
- Successful staging run: `33344920539`
- Staged binaries: six exact EN/es-419/pt-BR DOCX/PDF files

The staging transaction downloaded the previously successful publication-candidate artifact and verified all six fixed SHA-256 identities before copying bytes into the controlled publication tree. It did not regenerate publication artifacts. The temporary write-enabled staging workflow self-removed in the staging commit.

Any subsequent binary change requires a new candidate identity, new SHA-256 binding, and reopening of affected review/QA gates. Publication-state reconciliation remains separate and must not occur unless the durable files are present on `main` and applicable exact-head checks are green.

## Exact-head QA retrigger record

On 2026-08-30, the first Release Package QA run for this durable-staging head was canceled during PDF validation before the release-readiness gate could complete. This text-only evidence update intentionally retriggers exact-head QA without changing any of the six staged publication binaries or their recorded SHA-256 identities. Publication remains fail-closed until the replacement exact-head release workflow completes successfully.
