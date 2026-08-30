# Manual 14 — PCI DSS Preflight Baseline

Status: downstream preflight only; not publication authorization.

## Authoritative baseline

- Current published PCI DSS baseline verified for this preflight: PCI DSS v4.0.1, published by PCI Security Standards Council (PCI SSC) on 2024-06-11.
- PCI SSC states v4.0.1 is a limited revision with no added or deleted requirements and that the 2025-03-31 effective date for the future-dated v4 requirements was unchanged.
- PCI SSC was running a 2026 RFC on the currently published PCI DSS v4.0.1 to inform the next iteration. Treat that RFC as future-change intelligence only; do not treat unpublished RFC material as authoritative current requirements.
- Release-time source verification is mandatory because PCI SSC is actively evolving the standard.

Primary official sources:
- https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1
- https://www.pcisecuritystandards.org/
- https://blog.pcisecuritystandards.org/request-for-comments-pci-data-security-standard-pci-dss-v4.0.1
- https://www.pcisecuritystandards.org/es/document_library/
- https://www.pcisecuritystandards.org/pt/document_library/

## Scope boundary

Manual 14 must distinguish the PCI DSS standard from PCI SSC validation/reporting instruments and from adjacent PCI standards. The controlled scope should center on entities that store, process, or transmit cardholder data and/or sensitive authentication data, or that can impact the security of the cardholder data environment.

Do not represent PCI DSS as law. Treat contractual/acquirer/payment-brand obligations and jurisdiction-specific legal requirements as separate applicability layers.

## Controlled architecture

Pre-stage the manual around:
1. Applicability, roles, merchant/service-provider context, and scoping.
2. Cardholder data environment and connected-to / security-impacting system boundaries.
3. Data flows, account-data lifecycle, retention, storage and transmission controls.
4. PCI DSS requirement-domain implementation with control intent, evidence, ownership and operating-frequency fields.
5. Customized approach vs defined approach decision controls where applicable.
6. Vulnerability management, secure configuration, access control, authentication, logging/monitoring, testing and incident-response evidence.
7. Service-provider and third-party dependency governance.
8. SAQ/ROC/AOC validation-path decisioning without conflating validation evidence with the underlying security requirements.
9. Exception, compensating-control and remediation governance where applicable under the current standard and official guidance.
10. Continuous compliance, change control, evidence retention and reassessment triggers.

## Localization architecture

- English remains the controlling source language for requirement interpretation.
- PCI SSC provides translated Spanish and Portuguese document-library material, but its translated libraries state that the English text is the official version and prevails in case of ambiguity/inconsistency.
- es-419 and pt-BR manual content must therefore be semantically reviewed against the controlled English interpretation and may use official translated terminology as a reference, without claiming that the manual itself is an authorized PCI SSC translation.

## Evidence and audit design

Every implementation section should map: requirement/control objective -> applicability -> owner -> implementation procedure -> operating frequency -> evidence artifact -> evidence location -> reviewer/test method -> exception/remediation path -> reassessment trigger.

Pre-stage evidence patterns for network/data-flow diagrams, system inventories, configuration standards, access reviews, MFA, vulnerability scans, penetration tests, secure-development evidence, logging/monitoring, key-management evidence, third-party attestations, incident-response tests, change records and management sign-off.

## Fail-closed gates

Before publication, require at minimum:
- release-time PCI SSC version/effective-date verification;
- technical/control-mapping review by a competent PCI DSS practitioner;
- legal/editorial review of applicability language and non-legal-standard boundary;
- es-419 semantic review tied to exact candidate/artifact hashes;
- pt-BR semantic review tied to exact candidate/artifact hashes;
- rendered accessibility/visual review;
- exact changed-scope reconciliation after material changes;
- workflow-security, package-durability, provenance, checksums and release-manifest reconciliation;
- standing Final Human Release Approval only after all other required gates are green.

## Forward watch

At release time, specifically check whether PCI SSC has published a successor to v4.0.1 or changed validation/supporting-document versions following the 2026 RFC. Do not silently incorporate draft/RFC text into normative guidance.
