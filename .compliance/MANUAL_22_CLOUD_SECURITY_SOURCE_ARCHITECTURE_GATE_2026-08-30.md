# Manual 22 — Cloud Security Source and Architecture Gate

Status: downstream controlled build preparation only. Publication order is unchanged; Manual 22 cannot publish before Manual 21.

Verification date: 2026-08-30.

## Authoritative source state

1. Cloud Security Alliance Cloud Controls Matrix (CCM) v4.1 is the current CSA CCM release as of this verification. CSA released CCM v4.1 / CAIQ v4.1 on 2026-01-27; the framework contains 207 controls across 17 domains.
2. CSA has an active v4.1 transition plan. CSA states that CCM v4.1 succeeded v4.0.13 and that v4.0.x remains accepted during the transition window, with withdrawal planned for January 2028. Manual 22 should therefore build against v4.1 while preserving migration notes for organizations still on v4.0.x.
3. CSA Implementation Guidelines v2.0 remain relevant implementation guidance for the shared security responsibility model, but they were originally aligned to CCM v4.0.12. Any mapping reused from that guidance must be revalidated against CCM v4.1 rather than assumed current.
4. Provider-native guidance from AWS, Azure, Google Cloud or other CSPs may support implementation examples, but provider documentation is not a normative substitute for CSA controls, applicable law, or independent standards.

## Source-boundary controls

- Distinguish CSA control requirements and assurance program material from provider implementation guidance, architectural patterns, and organization-specific configuration.
- Do not imply CSA STAR registration, attestation, certification, or provider certification merely from implementing this manual.
- Crosswalks to ISO, NIST, PCI DSS, SOC 2, DORA, NIS2 or provider frameworks are mappings, not legal or control equivalence.
- Preserve shared-responsibility boundaries by service model, deployment model, contract, provider capability, and customer configuration.
- Reverify CCM/CAIQ version, transition dates, mappings, and STAR program dependencies at release time.

## Controlled 32-chapter architecture

1. Cloud governance and operating model
2. Scope, tenancy, accounts, subscriptions, projects, and landing zones
3. Shared responsibility and contractual allocation
4. Cloud risk assessment and architecture decision records
5. Identity federation, authentication, and privileged access
6. Workload identity and machine/service principals
7. Network architecture, segmentation, ingress, and egress
8. Zero Trust patterns and service-to-service trust
9. Data classification, residency, sovereignty, and lifecycle
10. Encryption, key management, HSMs, and secrets
11. Logging, telemetry, audit trails, and time integrity
12. Detection engineering, threat monitoring, and CSP-native security services
13. Configuration baselines and policy-as-code
14. Infrastructure as code governance and drift control
15. Vulnerability, patch, image, and dependency management
16. Container, Kubernetes, and orchestration security
17. Serverless, PaaS, managed-service, and API security
18. SaaS security and tenant configuration assurance
19. DevSecOps, CI/CD, signing, and build integrity
20. Backup, recovery, immutability, and ransomware resilience
21. Availability, regional resilience, and failure-domain design
22. Incident response, forensics, and cloud evidence preservation
23. Asset inventory, discovery, ownership, and tagging
24. Third-party, marketplace, and managed-service risk
25. Cloud supplier assurance and contractual evidence
26. Privacy, records, retention, and deletion controls
27. Cost, capacity, abuse, and resource-governance security interfaces
28. Multi-cloud and hybrid-cloud control consistency
29. Metrics, control health, continuous monitoring, and exceptions
30. Assessment, assurance, testing, and evidence sampling
31. Migration, modernization, exit, portability, and decommissioning
32. Evidence package, roadmap, and continuous improvement

## Evidence model

Evidence objects should include where applicable: account/subscription/project inventory; responsibility matrix; architecture decision record; identity policy; privileged-access record; network-policy record; key/secrets record; data-location record; configuration baseline; policy-as-code result; IaC review; image/SBOM record; vulnerability disposition; backup/restore result; logging/detection evidence; incident record; supplier assurance record; exception; metric; and management decision.

Each object must identify owner, cloud/service scope, control mapping, implementation state, date, retention expectation, material change trigger, and reviewer where genuine human judgment is required.

## Localization architecture

Prepare es-419 and pt-BR terminology controls for cloud service provider, shared responsibility, tenant, account/subscription/project, landing zone, workload identity, service principal, managed service, PaaS, SaaS, serverless, container, cluster, key vault/KMS, HSM, secret, infrastructure as code, policy as code, drift, data residency, sovereignty, region, availability zone, immutable backup, and exit/portability. English remains controlling until exact-candidate semantic review is completed.

## Graphics and accessibility prebuild

Pre-stage accessible figures with text equivalents for: shared-responsibility model; landing-zone architecture; identity trust flow; cloud data lifecycle; network segmentation; CI/CD security flow; logging/detection pipeline; multi-region resilience; backup/recovery; and exit/portability workflow. Final artifacts require heading, table, link, caption, language metadata, reading-order, contrast, bookmark, and rendered-page QA.

## Publication/pre-publication gates

Before Manual 22 can be represented as release-ready or published, require: release-time source recheck; controlled English master; controlled es-419 and pt-BR source sets; structure and parity QA; substantive cloud-security meaning review where required by repository controls; localization-semantic review where required; accessibility/visual review where required; reproducible DOCX/PDF generation; exact six-binary identity binding; SHA-256 manifest/provenance; durable staging; workflow-security QA; exact-head QA; catalog/release-registry reconciliation; and sequential clearance through Manual 21.

No review is recorded as complete by this gate, and no standing owner approval substitutes for any distinct substantive human review explicitly required by the repository control set.
