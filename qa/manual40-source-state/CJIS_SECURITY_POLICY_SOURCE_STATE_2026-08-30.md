# Manual 40 — CJIS Security Policy Authoritative Source State

**Manual:** 40 — CJIS Security Policy Controlled Implementation  
**State:** downstream authoritative-source gate only; publication state unchanged  
**Verified:** 2026-08-30/31 UTC against current FBI CJIS materials

## Controlled baseline

The current FBI baseline verified for this gate is **CJIS Security Policy Version 6.1, dated June 25, 2026**. Manual 40 must use that version as the active policy baseline unless a later official FBI revision supersedes it before candidate freeze or release.

The CJIS Security Policy represents the shared responsibility for lawful use and appropriate protection of Criminal Justice Information (CJI). The manual must preserve distinctions among the FBI CJIS Security Policy, federal/state laws and regulations, CJIS Advisory Policy Board decisions, Compact Council rules, state CJIS Systems Agency requirements, agency-specific procedures, contractual obligations, and organization-specific implementation controls.

## Source-layer boundaries

Manual 40 must separately identify:

1. current FBI CJIS Security Policy requirements;
2. applicable federal statutes, regulations, directives and Compact Council requirements;
3. state CJIS Systems Agency / State Identification Bureau implementation requirements;
4. FBI requirements companion materials, mappings, use cases and model policies;
5. outsourcing standards and contractor requirements where applicable;
6. agency-specific policies, technical standards, risk decisions, contracts and evidence.

Companion documents, mappings and examples must not be represented as substitutes for the controlling policy text.

## Implementation boundaries

The controlled manual must correctly scope at least: CJI handling and dissemination; access control and identity/authentication; personnel security; security awareness and training; incident response; audit/accountability; configuration and change control; media protection; physical protection; encryption and transmission protection; mobile/remote access; cloud/service-provider controls; vulnerability and patch management; continuous monitoring; outsourcing/contractor controls; and evidence required to demonstrate agency compliance.

No blanket claim may be made that every organization handling law-enforcement-related information is directly subject to the same CJIS obligations. Applicability must be established through the relevant CJIS relationship, agency agreement, state/federal requirement, contract, or other authoritative source.

## Current-version boundary

Older versions such as 5.9.x remain historical context only. They must not be used as the current control baseline where Version 6.1 has superseded them. Any implementation crosswalk from older versions must clearly identify changed, added, renumbered or removed requirements.

## Primary official sources used for this gate

- FBI Law Enforcement Enterprise Portal — CJIS Security Policy v6.1, June 25, 2026: https://le.fbi.gov/file-repository/cjis_security_policy_v6-1_20260625.pdf/view
- FBI — CJIS overview and Security Policy Resource Center: https://www.fbi.gov/services/cjis
- FBI — Compact Council outsourcing standard for non-channeling, May 8, 2025: https://www.fbi.gov/file-repository/cjis/compact-council-security-and-management-control-outsourcing-standard-for-non-channeling.pdf/view
- FBI — CJIS Security Policy Use Cases: https://www.fbi.gov/file-repository/cjis/cjis-security-policy-use-cases.pdf/view

## Release controls

This source gate is not an FBI/CJIS compliance determination, certification, audit opinion, or legal advice. Before candidate freeze and again before release, reverify the current CJIS Security Policy version, current requirements companion materials, applicable Compact Council standards, state CJIS Systems Agency overlays, outsourcing requirements, and any implementation-specific agency agreements.

Controlled architecture, full controlled English master, exact English freeze, es-419 and pt-BR localization, deterministic six-binary generation, accessibility/visual QA, provenance/checksums, workflow security, exact-hash substantive human review where required, durable staging, predecessor publication, and catalog/release-registry reconciliation remain fail-closed.

Publication remains strictly sequential behind Manuals 18–39.
