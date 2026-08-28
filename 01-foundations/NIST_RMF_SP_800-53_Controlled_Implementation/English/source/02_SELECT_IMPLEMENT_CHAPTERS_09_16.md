# Manual 10 — NIST RMF and SP 800-53 Controlled Implementation
## Controlled English Source — Chapters 09–16

> Original implementation guidance for SELECT and IMPLEMENT. Control selection and tailoring must remain risk-based, evidence-based, and traceable to organizational and system context.

## Chapter 09 — SELECT the initial control baseline

Choose an appropriate initial control baseline using applicable organizational policy and NIST guidance. Record the baseline source, system impact context, assumptions, inherited controls, common controls, overlays, and other requirements that influence the starting set.

The initial baseline is not the final control set. It is the structured starting point for tailoring and risk-based refinement.

## Chapter 10 — Tailoring and scoping decisions

Tailor controls transparently based on applicability, technology, mission, risk, environment, compensating safeguards, legal or contractual obligations, and organizational risk tolerance.

Every substantive tailoring decision should record rationale, authority, affected controls, assumptions, residual risk, dependencies, and review conditions. Tailoring must not become undocumented control deletion.

## Chapter 11 — Common, system-specific, and hybrid controls

Classify controls according to where responsibility and implementation reside. Identify common-control providers, inherited portions, system-specific responsibilities, hybrid boundaries, and evidence owners.

Inheritance claims must identify the actual provider, implementation scope, evidence source, applicability, status, and any system-specific parameters or residual responsibilities.

## Chapter 12 — Control parameterization and implementation statements

Translate selected controls into system-specific implementation statements, parameters, roles, technologies, procedures, and evidence expectations. Avoid generic restatement of control objectives without explaining how the system satisfies them.

Implementation statements should be testable, current, version-controlled, and traceable to architectures, configurations, procedures, logs, tickets, contracts, or other supporting evidence.

## Chapter 13 — System security, privacy, and C-SCRM planning

Maintain planning documentation that explains system context, selected controls, implementation approach, privacy considerations, supply-chain dependencies, risk assumptions, responsibilities, and evidence sources.

Use current NIST planning guidance to structure living records rather than static documents produced only for authorization events.

## Chapter 14 — IMPLEMENT controls in the operational environment

Implement selected controls in technology, process, people, facilities, contracts, and supplier relationships as applicable. Configuration, procedures, access boundaries, monitoring, training, recovery, and evidence collection should reflect the approved control design.

Implementation completion should be based on evidence, not on task status alone.

## Chapter 15 — Implementation evidence and provenance

For each material control implementation, preserve evidence sufficient to show what was implemented, where, by whom, when, under what configuration or version, and with what limitations.

Evidence should be relevant, current, attributable, tamper-resistant where appropriate, and linked to the exact system scope. Machine-generated evidence requires provenance and human interpretation where judgment is involved.

## Chapter 16 — SELECT/IMPLEMENT fail-closed gate

Do not treat the control set as implementation-ready when tailoring rationale is missing, inherited-control responsibility is ambiguous, implementation statements are not testable, critical parameters are undefined, or evidence cannot be traced to the actual system.

Automation may assist control mapping and evidence collection, but it cannot establish applicability, effective implementation, or acceptable residual risk by itself.
