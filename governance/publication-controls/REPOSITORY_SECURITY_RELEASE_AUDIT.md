# Repository and Security Release Audit

Run this audit immediately before a release candidate is declared ready for publication.

## Repository protections

Verify:

- default branch is the intended protected branch;
- release work reached the branch through reviewed pull requests;
- no uncontrolled direct-push path was introduced;
- no deleted historical branch was recreated solely to bypass process;
- merge method and release tag are intentional;
- release commit SHA is known and recorded.

## GitHub Actions and CI/CD

Verify:

- workflow permissions are least privilege;
- read-only workflows remain read-only unless a write permission is explicitly justified;
- third-party Actions are pinned to immutable commit SHAs where practical;
- no workflow can silently push generated changes to protected `main`;
- pull-request workflows do not execute untrusted code with write-capable secrets;
- workflow_dispatch or release triggers cannot bypass required review gates;
- scripts use safe paths and fail closed on missing prerequisites.

## Secrets and sensitive data

Verify:

- no API keys, tokens, passwords, private keys, credentials, or sensitive exports are committed;
- generated artifacts do not embed secrets, local paths, usernames, or private metadata unnecessarily;
- workflow logs do not expose secrets;
- examples use placeholders rather than live credentials.

## Dependencies and supply chain

Verify:

- dependency files and lock files are internally consistent where present;
- newly introduced dependencies have a documented purpose;
- no untrusted binary or generated artifact is treated as authoritative without provenance;
- release-generation tools and third-party Actions are reviewed for supply-chain risk;
- downloaded tools/artifacts are verified by checksum/signature where practical.

## Scripts and file operations

Verify:

- scripts cannot delete or overwrite outside intended repository/output paths;
- temporary/output paths are deterministic and reviewable;
- shell commands avoid unsafe interpolation where practical;
- destructive operations require explicit targets;
- release scripts do not mutate protected source unexpectedly.

## Generated-artifact integrity

For every release artifact record:

- filename;
- language;
- format;
- originating Git commit SHA;
- generation tool/version where available;
- file size;
- SHA-256 checksum where practical;
- QA result;
- approval status.

## Findings

Classify findings as `LOW`, `MEDIUM`, `HIGH`, or `CRITICAL`. Distinguish confirmed findings from observations and recommendations.

## Gate outcome

Use exactly one:

- `SECURITY RELEASE QA STATUS: PASS`
- `SECURITY RELEASE QA STATUS: PASS WITH APPROVED EXCEPTIONS`
- `SECURITY RELEASE QA STATUS: CORRECTIONS REQUIRED`

Unresolved HIGH or CRITICAL findings block release unless a documented accountable exception explicitly accepts the risk. This audit is passive unless a separately authorized change is required; it does not perform exploitation or destructive testing.
