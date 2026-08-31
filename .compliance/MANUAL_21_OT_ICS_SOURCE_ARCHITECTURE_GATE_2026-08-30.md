# Manual 21 — OT/ICS Security Source and Architecture Gate

Status: downstream controlled build preparation only. Publication order is unchanged; Manual 21 cannot publish before Manual 20.

Verification date: 2026-08-30.

## Authoritative source state

1. NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security*, remains the current final NIST OT security guide. NIST published the final revision on 2023-09-28. Treat this as the principal public technical baseline for OT security architecture, OT-specific risk, threats, topologies, and safeguards.
2. ISA/IEC 62443 remains the principal consensus standards family for industrial automation and control systems security. ISA identifies the series as actively maintained and broadly applicable across industrial and critical-infrastructure sectors.
3. Current ISA/IEC 62443 source watch must include ANSI/ISA-62443-2-1-2024, which materially updates organization-wide IACS security-program requirements, and later series publications such as ISA-TR62443-2-2-2025. Release-time verification must recheck the exact current parts/editions relied upon.
4. CISA OT/ICS material is supporting public implementation guidance, not a substitute for NIST or ISA/IEC normative source boundaries. Current CISA guidance includes 2025 mitigations emphasizing removal of unintended public-internet exposure, credential hardening, and other baseline OT protections.

## Source-boundary controls

- Do not reproduce copyrighted ISA/IEC 62443 normative text beyond permissible quotation. Operationalize requirements in original language and preserve source citations.
- Distinguish NIST guidance, CISA recommendations, ISA/IEC requirements, sector rules, safety standards, and organization-specific engineering constraints.
- Never imply that applying this manual confers ISA/IEC certification, conformity assessment, regulatory compliance, or sector authorization.
- OT security decisions must preserve safety, availability, deterministic operation, environmental constraints, maintenance windows, vendor support, and process-engineering authority.
- Security controls that are routine in enterprise IT must not be transplanted into OT without engineering validation and change control.

## Controlled 32-chapter architecture

1. OT/ICS governance and operating model
2. Scope, system boundaries, and critical functions
3. Safety, reliability, and cybersecurity interaction
4. Asset inventory and authoritative configuration baseline
5. OT architecture and reference topologies
6. Zones, conduits, segmentation, and trust boundaries
7. Risk assessment and consequence analysis
8. Threat modeling and adversary pathways
9. Security levels and target-state design concepts
10. Identity, authentication, and privileged access
11. Remote access and vendor access
12. Engineering workstations and administrative systems
13. Network security and secure communications
14. Firewalling, gateways, proxies, and data diodes
15. Wireless, serial, fieldbus, and legacy protocol risk
16. PLC, DCS, SCADA, HMI, SIS, and controller security
17. Secure configuration and hardening
18. Vulnerability management and compensating controls
19. Patch, firmware, and change management
20. Malware defense and removable media
21. Backup, restore, golden images, and recovery
22. Logging, telemetry, time synchronization, and evidence
23. OT monitoring, detection, and anomaly analysis
24. Incident response and cyber-physical crisis coordination
25. Business continuity, resilience, and manual fallback
26. Secure procurement and supplier requirements
27. Product security lifecycle and component assurance
28. Maintenance, lifecycle, obsolescence, and end-of-support risk
29. Physical security and environmental interfaces
30. Workforce competency, roles, and exercises
31. Assessment, testing, metrics, exceptions, and assurance
32. Evidence package, implementation roadmap, and continuous improvement

## Evidence model

Each chapter should produce auditable evidence objects where applicable: scope decision; system/asset record; architecture diagram; zone/conduit record; risk decision; safety-interface decision; access record; configuration baseline; approved remote-access path; vulnerability disposition; patch/change record; backup/restore test; monitoring rule; incident record; supplier requirement; exception; corrective action; metric; and management approval.

Every evidence object must identify owner, system/scope, source requirement or guidance mapping, implementation state, date, reviewer where genuinely required, retention expectation, and change trigger.

## Localization architecture

Prepare es-419 and pt-BR terminology controls for OT, ICS, IACS, PLC, DCS, SCADA, HMI, SIS, zones/conduits, safety system, remote access, asset owner, system integrator, supplier, security level, compensating control, engineering workstation, historian, field device, and maintenance window. English remains controlling until exact-candidate semantic review is completed.

## Graphics and accessibility prebuild

Pre-stage accessible figures with text equivalents for: Purdue-style/reference architecture; zones and conduits; remote-access path; OT change-control workflow; vulnerability/patch decision tree; incident escalation; backup/recovery architecture; and supplier lifecycle. Final artifacts require heading, table, link, caption, language metadata, reading-order, contrast, bookmark, and rendered-page QA.

## Publication/pre-publication gates

Before Manual 21 can be represented as release-ready or published, require: release-time source recheck; controlled English master; controlled es-419 and pt-BR source sets; structure and parity QA; substantive technical/OT meaning review where required by repository controls; localization-semantic review where required; accessibility/visual review where required; reproducible DOCX/PDF generation; exact six-binary identity binding; SHA-256 manifest/provenance; durable staging; workflow-security QA; exact-head QA; catalog/release-registry reconciliation; and sequential clearance through Manual 20.

No review is recorded as complete by this gate, and no standing owner approval substitutes for any distinct substantive human review explicitly required by the repository control set.
