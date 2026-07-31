# Chapter 100 — Operational and Resilience Risk

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 100 draft language.

## Requirement

Organizations must identify and manage operational and resilience risks that could cause an AI system or dependent process to fail, degrade, produce unreliable outcomes, or become unavailable. Controls must support continuity, safe fallback, recovery, and evidence preservation.

## Plain-English explanation

An AI system can fail even without a cyberattack. Capacity limits, bad data feeds, model-provider outages, configuration drift, latency, dependency failures, or weak change control can disrupt operations or produce harmful decisions. Resilience requires tested alternatives and clear recovery priorities.

## Assessment requirements

Assess at minimum:

1. critical processes, service levels, and impact tolerances;
2. model, API, cloud, data, network, identity, and supplier dependencies;
3. capacity, latency, throughput, timeout, and rate-limit risks;
4. data-pipeline failure, stale data, schema change, and integrity degradation;
5. configuration, version, prompt, and retrieval-source drift;
6. monitoring coverage and alert thresholds;
7. manual workarounds, alternative channels, and safe degraded modes;
8. backup, restoration, rollback, failover, and recovery objectives;
9. operator readiness, communications, and decision authority;
10. evidence retention, incident coordination, and post-recovery validation.

## GlobalWay example

GlobalWay's AI travel-assistance service depends on a third-party model, booking APIs, identity services, and customer-profile data. GlobalWay defines a safe read-only mode, blocks automated booking changes during dependency failure, routes urgent requests to human agents, and tests recovery before restoring normal service.

## Control activity

Material AI services must have documented continuity and recovery plans aligned to business impact. Plans must include safe shutdown, fallback, dependency monitoring, recovery validation, and periodic exercises covering realistic AI-specific failure scenarios.

## Evidence

- business-impact and dependency assessment;
- service-level and impact-tolerance definitions;
- continuity, fallback, and recovery plans;
- backup, rollback, and failover test results;
- monitoring and capacity records;
- exercise reports and corrective actions;
- outage communications and recovery approvals;
- post-recovery validation evidence.

## Audit test

Select material AI services and review recent incidents or exercises. Confirm that critical dependencies are known, fallback processes are usable, recovery objectives are tested, restored versions and data are validated, and unresolved resilience gaps are escalated.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: applicable risk-management, accuracy, robustness, cybersecurity, human-oversight, monitoring, incident, and corrective-action provisions.
- Applicable operational-resilience, cybersecurity, product-safety, and sector requirements.
- Current consolidated official texts control over older summaries.
