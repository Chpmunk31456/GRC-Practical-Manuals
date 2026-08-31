# Manual 28 — AI Privacy & Automated Decision Governance — Source / Architecture Gate

Status: active publication-front build after Manual 27 publication.

## Release-time source boundary — 2026-08-31

- NIST Privacy Framework 1.0 remains the published NIST privacy framework baseline. Privacy Framework 1.1 remains an Initial Public Draft / change-watch item and is not treated as final.
- NIST AI RMF 1.0 remains the published voluntary AI risk-management baseline. NIST states that AI RMF 1.0 is being revised; any future final revision requires release-time revalidation.
- Jurisdiction-specific automated-decision, profiling, privacy, consumer-protection, employment, credit, insurance, biometric, children’s-data, and sector rules remain separate legal layers. No single automated-decision rule is treated as universal.
- Existing Manual 01 EU AI Act, Manual 03 NIST AI RMF, Manual 11 GDPR, Manual 12 CCPA/CPRA, and Manual 27 Data Governance & Privacy Engineering may be mapped for implementation but are not treated as interchangeable legal requirements.
- This manual operationalizes controls and evidence; it does not provide legal advice or claim that voluntary guidance creates a legal obligation by itself.

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

## Controlled evidence schema

Every implementation chapter identifies source layer, jurisdiction/applicability, accountable owner, procedure, evidence object/location, test/review method, exception/remediation path, and reassessment trigger.

## Release controls

The controlled English master is authoritative for this project. es-419 and pt-BR editions are unofficial project translations. Candidate DOCX/PDF generation must be reproducible, exact candidate binaries must be hash-bound and render-reviewed, staging must preserve exact bytes, and publication state may be reconciled only after predecessor Manual 27 is published and all objective gates are green.