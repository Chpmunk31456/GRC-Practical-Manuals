# Chapter 74 — Model Cards, System Cards, and Limitations

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 74 draft language.

## Requirement

Organizations should use model cards, system cards, and equivalent documentation as structured evidence about intended purpose, capabilities, limitations, evaluation, risks, and responsible use. These artifacts must not be treated as substitutes for statutory technical documentation, instructions for use, conformity records, or risk-management evidence where those are required.

## Plain-English explanation

A model card describes the model. A system card describes the wider deployed system, including integrations, prompts, data flows, safeguards, and human processes. Both are useful only when they are accurate, version-specific, and explicit about limitations.

## Required content

Document as applicable:

1. model and system identity, owner, provider, version, and release date;
2. intended and excluded uses;
3. training, tuning, evaluation, and relevant data information;
4. supported languages, populations, environments, and jurisdictions;
5. performance metrics, thresholds, uncertainty, and known failure modes;
6. bias, safety, privacy, security, robustness, and misuse risks;
7. human-oversight, fallback, escalation, and monitoring requirements;
8. dependencies, integrations, and downstream assumptions;
9. legal classification and applicable transparency or high-risk obligations;
10. change history and unresolved limitations.

## GlobalWay example

GlobalWay's travel-assistant system card documents the third-party GPAI model, retrieval sources, languages, booking integrations, prohibited autonomous actions, human escalation rules, hallucination risks, monitoring metrics, and the exact production configuration.

## Control activity

Product and Model Risk owners must approve version-controlled model and system cards before release and update them after material changes, significant incidents, new evaluation findings, or changed intended use. Limitations must be reflected in instructions, training, user interfaces, and monitoring.

## Evidence

- approved model and system cards;
- version mapping;
- evaluation reports;
- limitation and risk register;
- user instructions and training;
- change history;
- monitoring and incident records.

## Audit test

Select a deployed AI system and verify that its cards match the actual version and architecture, describe material limitations and dependencies, and are consistent with technical documentation, instructions, controls, and observed production performance.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: applicable technical-documentation, transparency, instructions, GPAI-information, risk-management, and post-market provisions.
- Model and system cards are supporting artifacts unless binding law or contract gives them a specific legal function.
