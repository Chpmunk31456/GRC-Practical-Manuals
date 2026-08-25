# Publication Control Stack

This directory defines the repository-wide control framework for preparing, approving, releasing, maintaining, correcting, and, where necessary, withdrawing practical GRC manuals.

## Controlled publication sequence

1. Engram continuity check and live GitHub reconciliation.
2. Authoritative-source verification and citation QA.
3. English controlled-source QA.
4. Translation and semantic review for localized editions.
5. Editorial QA for spelling, grammar, logic, terminology, and flow.
6. Human semantic approval.
7. Visual-learning and localized-graphics QA.
8. DOCX/PDF generation.
9. Accessibility and page-by-page visual QA.
10. Repository/security release audit.
11. Release manifest and provenance finalization.
12. GitHub release/tag.
13. Zenodo publication and DOI reconciliation.
14. Post-release monitoring.
15. Correction or withdrawal workflow when triggered.

No automated tool may close a human approval gate on its own. Passing repository checks demonstrates repository integrity and evidence readiness only; it does not establish legal compliance, certification, conformity, or an audit opinion.

## Required control records

- `HUMAN_APPROVAL_RECORD_TEMPLATE.md`
- `ACCESSIBILITY_COMPLIANCE_AUDIT.md`
- `REPOSITORY_SECURITY_RELEASE_AUDIT.md`
- `RELEASE_MANIFEST_AND_PROVENANCE.md`
- `POST_RELEASE_CHANGE_MONITORING.md`
- `CORRECTION_AND_WITHDRAWAL_PROCEDURE.md`
- `.compliance/release-manifest.schema.json`

## Release gate rule

A manual may be described as release-ready only when every applicable pre-release gate has a documented PASS or approved exception, all required human approvals are recorded, and the release manifest identifies the exact Git commit and generated artifacts.
