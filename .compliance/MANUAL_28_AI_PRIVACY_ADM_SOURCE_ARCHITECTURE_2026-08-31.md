# Manual 28 — AI Privacy & Automated Decision Governance — Source / Architecture Gate

Status: active downstream prebuild. Publication remains sequential behind Manual 27.

## Current source boundary

- NIST Privacy Framework 1.0 remains the published NIST privacy framework baseline; PF 1.1 remains draft/change-watch until final publication.
- NIST AI RMF 1.0 remains a published voluntary AI risk-management baseline and is itself under revision; any future final revision requires release-time revalidation.
- Jurisdiction-specific automated-decision, profiling, privacy, consumer-protection, employment, credit, insurance, biometric, children’s-data, and sector rules remain separate legal layers. No single automated-decision rule is treated as universal.
- Existing Manual 01 EU AI Act, Manual 03 NIST AI RMF, Manual 11 GDPR, Manual 12 CCPA/CPRA, and Manual 27 Data Governance/Privacy Engineering may be mapped but are not treated as interchangeable requirements.

## Controlled 32-chapter architecture

1. Purpose, scope, and non-legal-advice boundary
2. Source hierarchy, jurisdiction, and change watch
3. AI/ADM system inventory and ownership
4. Decision taxonomy: assistive, recommendatory, automated, consequential
5. Data-flow and model-flow lineage
6. Purpose specification and use limitation
7. Training/evaluation data governance
8. Sensitive and inferred-data governance
9. Privacy risk and harms assessment
10. DPIA / AI-impact-assessment interfaces
11. Automated-decision applicability analysis
12. Profiling and personalization governance
13. Transparency and notice architecture
14. Explainability and reason-code governance
15. Contestability and appeal mechanisms
16. Human oversight and intervention design
17. Consent/preference/legal-basis interfaces
18. Data minimization and feature governance
19. Retention, deletion, and model-memory controls
20. De-identification, pseudonymization, and PETs
21. Fairness/bias interfaces without false legal equivalence
22. Access, identity, and privileged administration
23. Third-party models, APIs, and data providers
24. Cross-border processing and deployment
25. Logging, traceability, and decision records
26. Monitoring for drift, privacy harm, and misuse
27. Incident, complaint, and rights-request coordination
28. Change management and material-model updates
29. Metrics, KRIs/KPIs, and management reporting
30. Assurance, testing, and evidence inspection
31. Localization, accessibility, and source control
32. Release roadmap, provenance, checksums, and sequential publication

## Evidence schema

Every implementation chapter will identify source layer, jurisdiction/applicability, accountable owner, procedure, evidence object/location, test/review method, exception/remediation path, and reassessment trigger.

## Next parallel work

Build the controlled English master; maintain es-419 and pt-BR terminology maps; prepare jurisdiction-overlay tables that preserve non-equivalence; define reproducible DOCX/PDF candidate rules; and revalidate source versions immediately before candidate freeze.