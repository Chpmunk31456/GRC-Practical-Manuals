# Chapter 49 — Post-Market Monitoring

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 49 draft language.

## Requirement

Providers of high-risk AI systems must establish and document a proportionate post-market monitoring system that actively and systematically collects, documents, and analyses relevant performance and risk data throughout the system lifetime. The system must be based on a post-market monitoring plan that forms part of the technical documentation.

## Plain-English explanation

Compliance does not end when the system is released. Providers must continue checking whether the system performs as intended, remains compliant, interacts safely with other systems, and creates new or changed risks in real use.

## Monitoring design

The plan should define:

1. scope, owners, and system versions;
2. data sources, including deployer feedback, complaints, incidents, overrides, drift, and technical telemetry;
3. performance, safety, bias, robustness, cybersecurity, and human-oversight indicators;
4. thresholds and escalation criteria;
5. review frequency and sampling;
6. methods for trend, subgroup, and interaction analysis;
7. corrective-action and notification triggers;
8. links to risk management, technical documentation, serious-incident reporting, and change control;
9. retention, confidentiality, and evidence requirements.

Where sector legislation already requires a post-market system, the provider may integrate the AI Act elements into that system where the statutory conditions are met and equivalent protection is preserved.

## GlobalWay example

GlobalWay's provider monitors the production recruitment system for selection-rate disparities, false-positive and false-negative trends, override rates, user complaints, model drift, security events, and deviations from the intended purpose. Quarterly reviews are supplemented by immediate escalation when thresholds are exceeded.

## Control activity

The provider must approve a version-linked post-market monitoring plan before release, operate the plan throughout the system lifetime, document findings, and feed relevant results into risk management, corrective action, incident reporting, and technical-documentation updates.

## Evidence

- approved monitoring plan;
- metric definitions and thresholds;
- monitoring data and dashboards;
- deployer feedback and complaints;
- trend and subgroup analysis;
- escalation and corrective-action records;
- technical-documentation updates;
- management review minutes.

## Audit test

Select a sample of high-risk AI systems and verify that monitoring is active rather than purely reactive, covers the deployed lifetime and actual production version, uses defined thresholds, analyses relevant data, and triggers documented risk, incident, and corrective-action processes.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: Article 72 and Annex IV.
- Current consolidated EUR-Lex text controls over older summaries.
