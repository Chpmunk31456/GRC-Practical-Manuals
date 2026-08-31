# Manual 44 — NIST SSDF / SP 800-218 Controlled Implementation — Source / Architecture Gate

Status: active downstream prebuild. Publication remains sequential behind Manual 43.

## Current source boundary

- NIST SP 800-218 SSDF Version 1.1 remains final and is the current stable baseline.
- NIST SP 800-218 Rev. 1 / SSDF Version 1.2 is draft and remains change-watch until final publication.
- NIST SP 800-218A is final and is a community profile that augments SSDF 1.1 for generative AI and dual-use foundation models.
- NIST guidance is voluntary guidance unless incorporated through another governing source. Contractual, government-acquisition, sector, product-security, and organizational requirements remain distinct.

## Controlled 32-chapter architecture

1. Purpose, scope, and source hierarchy
2. SSDF version/change control
3. Secure-development governance
4. Roles, competence, and accountability
5. Development-policy architecture
6. Secure development environment
7. Source repository protection
8. Identity, authentication, and access
9. Secrets and credential management
10. Threat modeling and design review
11. Secure coding standards and patterns
12. Dependency and component governance
13. Build pipeline and CI/CD controls
14. Code review and change approval
15. Static/dynamic/composition testing
16. Fuzzing and specialized security testing
17. Artifact integrity and signing
18. Release provenance and traceability
19. Environment/configuration hardening
20. Software distribution and deployment
21. Vulnerability intake and triage
22. Vulnerability remediation and verification
23. Root-cause and recurrence prevention
24. Coordinated vulnerability disclosure
25. Supplier and outsourced development assurance
26. Acquisition and consumer communication
27. AI-model development SSDF profile interfaces
28. Metrics, exceptions, and risk acceptance
29. Assurance and independent validation
30. Incident feedback into the SDLC
31. Localization, accessibility, source and evidence control
32. Release roadmap, provenance, checksums, and sequential publication

## Next parallel work

Build the controlled English implementation master from SSDF 1.1, maintain the SSDF 1.2 draft as change-watch, define an optional SP 800-218A overlay for AI development, prepare es-419/pt-BR terminology, and design reproducible publication-candidate and exact-provenance controls.