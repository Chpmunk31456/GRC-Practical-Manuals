# Manual 15 — SOC 2 Preflight Baseline

Status: downstream preflight only; not publication authorization.

## Authoritative baseline

Primary source family: AICPA & CIMA SOC 2 materials.

Current official baseline verified for this preflight:
- 2017 Trust Services Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy, with revised points of focus (2022).
- 2018 SOC 2 Description Criteria, with revised implementation guidance (2022).
- AICPA SOC 2 examination guidance reflecting SSAE No. 20 and SSAE No. 21.

Primary official sources:
- https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2/
- https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022
- https://www.aicpa-cima.com/cpe-learning/publication/soc-2-reporting-on-an-examination-of-controls-at-a-service-organization-relevant-to-security-availability-processing-integrity-confidentiality-or-privacy

Release-time source verification is mandatory because AICPA guidance and implementation materials may change even when the underlying criteria designation remains stable.

## Scope boundary

SOC 2 is an attestation/reporting framework for controls at a service organization relevant to security, availability, processing integrity, confidentiality, or privacy. Do not present SOC 2 as a certification, regulation, law, or generic cybersecurity framework.

Keep distinct:
- Trust Services Criteria used to evaluate controls;
- Description Criteria used to evaluate management's system description;
- attestation standards and practitioner responsibilities;
- management responsibilities and assertions;
- SOC 2 versus SOC 1, SOC 3, SOC for Cybersecurity, and SOC for Supply Chain.

## Controlled architecture

Pre-stage the manual around:
1. Engagement purpose, intended users, service-organization boundary and system definition.
2. Management responsibilities, assertion, system description and description criteria.
3. Trust Services Criteria structure and category selection.
4. Common criteria and additional availability, processing integrity, confidentiality and privacy criteria where applicable.
5. Risk assessment, control design, implementation and operating effectiveness.
6. Type 1 versus Type 2 examination distinctions without oversimplifying practitioner judgment.
7. Complementary user-entity controls and subservice-organization considerations.
8. Evidence design, sampling readiness, change management and exception handling.
9. Vendor/cloud dependencies, logical access, system operations, change management, risk mitigation and monitoring evidence.
10. Report-reading guidance, exceptions, qualifications and remediation planning.

## Evidence and audit design

Every implementation section should map: criterion -> risk -> control objective -> control activity -> owner -> frequency -> population -> evidence -> test approach -> exception/remediation -> change trigger.

Pre-stage evidence patterns for access provisioning/deprovisioning, privileged access, MFA, vulnerability management, incident response, backup/recovery, availability monitoring, secure development/change management, logging, vendor oversight, risk assessment, policy governance, privacy operations and management review.

## Copyright and use boundary

AICPA criteria and guidance are copyrighted. Do not reproduce protected standards text beyond permissible quotation. Use controlled paraphrase, original implementation guidance and traceable citations. Preserve criterion identifiers only where necessary for mapping and verification.

## Fail-closed gates

Before publication, require at minimum:
- release-time AICPA source/version verification;
- competent SOC 2 technical/attestation review;
- editorial review for precise distinction among criteria, engagement standards and management/practitioner responsibilities;
- es-419 semantic review tied to exact candidate/artifact hashes;
- pt-BR semantic review tied to exact candidate/artifact hashes;
- rendered accessibility/visual review;
- exact changed-scope reconciliation after material changes;
- workflow-security, package-durability, provenance, checksums and release-manifest reconciliation;
- standing Final Human Release Approval only after all other required gates are green.

## Forward watch

At release time, verify whether AICPA has revised the Trust Services Criteria, Description Criteria, SOC 2 guide, SSAE references, illustrative reporting guidance, or terminology. Do not infer current requirements from older SOC 2 marketing summaries or third-party compliance platforms.
