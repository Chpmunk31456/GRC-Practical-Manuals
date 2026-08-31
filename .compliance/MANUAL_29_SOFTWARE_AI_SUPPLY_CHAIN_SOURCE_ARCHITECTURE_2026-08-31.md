# Manual 29 — Software / AI Supply Chain and Component Assurance — Source / Architecture Gate

Status: active downstream prebuild. Publication remains sequential behind Manual 28.

## Current source boundary

- NIST SP 800-218 SSDF Version 1.1 remains final. NIST SP 800-218 Rev. 1 / SSDF Version 1.2 is currently draft and is change-watch only until final publication.
- NIST SP 800-218A is final and augments SSDF 1.1 with secure-development practices for generative AI and dual-use foundation models.
- SLSA Version 1.2 is the current approved SLSA specification. Working-draft material is not treated as the controlled baseline.
- CISA secure-by-design and software-supply-chain/SBOM guidance are implementation guidance, not universally binding law.
- Contractual, procurement, sector, government-acquisition, export, licensing, and vulnerability-disclosure requirements remain separate source layers.

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

Every control will preserve source layer, software/model/component scope, owner, procedure, artifact/evidence identity, validation method, exception/remediation route, and reassessment trigger.

## Next parallel work

Build the controlled English master; create SBOM/VEX/provenance evidence templates; define model/data provenance mappings; maintain SSDF 1.2 draft as change-watch; prepare es-419 and pt-BR localization terminology; and design reproducible candidate-generation and exact-binary provenance gates.