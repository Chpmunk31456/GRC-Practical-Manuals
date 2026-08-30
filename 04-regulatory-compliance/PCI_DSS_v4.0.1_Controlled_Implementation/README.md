# Manual 14 — PCI DSS v4.0.1 Controlled Implementation

**Series order:** 14
**State:** active controlled-build lane / not yet published
**Controlling language:** English
**Localized editions:** es-419 and pt-BR

Manual 14 is the front-of-line manual after publication of Manual 13. It converts the existing PCI DSS v4.0.1 practical-manual material into the repository's controlled implementation architecture while preserving PCI SSC copyright and applicability boundaries.

## Current authoritative baseline

- PCI DSS v4.0.1 is the current baseline captured by the repository preflight record.
- Release-time source/version verification is mandatory because PCI SSC is actively evolving the standard.
- PCI DSS is a payment-card security standard, not a statute. Contractual, acquirer, payment-brand, and jurisdiction-specific legal obligations remain separate applicability layers.
- English controls interpretation. PCI SSC translated material may guide terminology but does not make this repository an authorized PCI SSC translation.

## Controlled-build architecture

The manual will use 32 chapters organized into four controlled source blocks:

1. Chapters 01–08 — governance, applicability, scoping, CDE boundaries, data flows, roles, implementation paths, evidence architecture.
2. Chapters 09–16 — network/security controls, secure configuration, account-data protection, cryptography, malware defenses, secure development, vulnerability management, change control.
3. Chapters 17–24 — identity/access, MFA, physical access, logging, monitoring, testing, scans, penetration testing, service-provider and third-party evidence.
4. Chapters 25–32 — incident response, exceptions/compensating controls, validation paths, continuous compliance, remediation, management assurance, maturity, scenario-based implementation.

Each implementation chapter must carry: applicability -> objective -> owner -> procedure -> frequency -> evidence artifact -> evidence location -> reviewer/test method -> exception/remediation -> reassessment trigger.

## Reuse boundary

The existing `04-regulatory-compliance/PCI_DSS_v4.0.1` manual is a source asset for controlled redevelopment, not proof that Manual 14 is release-ready. Existing English, Spanish, Portuguese, DOCX, and PDF assets must be reconciled into the controlled-build lineage rather than silently relabeled.

## Release path

1. Freeze and verify authoritative PCI SSC source/version state.
2. Complete the controlled 32-chapter English source.
3. Produce es-419 and pt-BR controlled localized drafts.
4. Run structural, source-boundary, terminology, copyright, link, and predecessor regression QA.
5. Generate exact-head DOCX/PDF publication candidates.
6. Run rendered page/accessibility and content-regression QA.
7. Stage exact validated binaries durably without mutation.
8. Reconcile SHA-256 provenance, catalog, release registry, and manifest.
9. Publish automatically when the repository clean-candidate rule is satisfied and no substantive defect remains.

Manual 15 and later manuals continue in parallel preflight/build preparation and may not bypass Manual 14 in publication order.
