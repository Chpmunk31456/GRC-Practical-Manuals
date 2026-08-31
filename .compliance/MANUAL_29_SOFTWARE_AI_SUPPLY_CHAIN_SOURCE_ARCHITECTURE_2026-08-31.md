# Manual 29 — Software / AI Supply Chain and Component Assurance — Source / Architecture Gate

Status: publication-front build after published Manual 28.

## Release-time source boundary

- NIST SP 800-218 SSDF Version 1.1 remains the final stable baseline.
- NIST SP 800-218A remains final and augments SSDF 1.1 with secure-development practices for generative AI and dual-use foundation models.
- NIST SP 800-218 Rev. 1 / SSDF Version 1.2 remains an Initial Public Draft and is change-watch only until final publication.
- SLSA Version 1.2 is the current approved SLSA specification; its working draft is not the controlled baseline.
- CISA secure-by-design, SBOM, vulnerability-disclosure, and software-supply-chain guidance are implementation guidance unless separately made binding by law, regulation, contract, procurement rule, or sector requirement.
- Contractual, government-acquisition, export, licensing, vulnerability-disclosure, and sector requirements remain separate source layers and are never universalized.

## Controlled 32-chapter architecture

1. Purpose, scope, and source boundaries
2. Supplier/component ecosystem inventory
3. Secure-development governance and accountability
4. SSDF organizational preparation
5. Development-environment security
6. Source-code and repository governance
7. Identity, access, and privileged build administration
8. Branch, review, and change controls
9. Dependency discovery and component inventory
10. SBOM generation, formats, and lifecycle
11. VEX and vulnerability-status evidence
12. Open-source intake and licensing interfaces
13. Third-party library and package assurance
14. Build-service and CI/CD security
15. Hermetic/reproducible build considerations
16. Artifact signing and verification
17. Provenance and attestation architecture
18. SLSA Build and Source track implementation
19. Secrets, keys, tokens, and signing-material governance
20. Container, image, and infrastructure component assurance
21. AI model provenance and model-supply-chain controls
22. Training/evaluation data provenance
23. AI component, plugin, tool, and agent dependency governance
24. Third-party model/API/service-provider assurance
25. Vulnerability discovery, prioritization, and response
26. Malicious-package and dependency-confusion defenses
27. Release approval, distribution, and rollback
28. Incident response and supply-chain compromise handling
29. Metrics, exceptions, and risk acceptance
30. Assurance, testing, red-team, and evidence validation
31. Localization, accessibility, licensing, and source control
32. Release roadmap, provenance, checksums, and sequential publication

## Evidence schema

Every implementation chapter preserves source layer, software/model/component scope, accountable owner, procedure, evidence object/location, validation method, exception/remediation route, and reassessment trigger.

## Release control

Controlled EN/es-419/pt-BR sources must preserve the source-layer distinctions above. Candidate DOCX/PDF generation must be reproducible, immutable candidate identities must be bound by SHA-256, exact bytes must be staged without regeneration, and publication remains sequential after Manual 28.