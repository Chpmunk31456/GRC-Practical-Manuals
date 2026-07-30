# Chapter 77 — Open-Source and Component Governance

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 77 draft language.

## Requirement

Organizations must assess open-source AI models, systems, software, datasets, and components against the specific conditions of Regulation (EU) 2024/1689, as amended, rather than treating open-source status as a blanket exclusion. The assessment must consider actor role, commercialisation, downstream integration, high-risk use, GPAI treatment, cybersecurity, substantial modification, licensing, provenance, and supportability.

## Plain-English explanation

Open-source distribution can affect which obligations apply, but it does not automatically remove legal responsibility. Once an open component is integrated into a product, modified, placed on the market, used under an organisation's name, or deployed in a regulated context, different duties may arise.

## Governance requirements

Maintain controls for:

1. component and model provenance;
2. licence terms, restrictions, attribution, and compatibility;
3. maintainer identity, release history, and support status;
4. known vulnerabilities, incidents, and security advisories;
5. training-data, dataset, and documentation availability;
6. intended purpose, limitations, and prohibited or unsupported uses;
7. downstream modification and integration consequences;
8. provider-role and substantial-modification assessment;
9. high-risk, transparency, and GPAI classification;
10. version pinning, testing, monitoring, replacement, and exit.

## GlobalWay example

GlobalWay integrates an open-source language model into an internal travel-support workflow. Before production use, it records the model version and licence, reviews provenance and limitations, tests security and performance, assesses whether fine-tuning or own-brand deployment changes its legal role, and documents an exit path if the project becomes unsupported.

## Control activity

No open-source AI component may enter production without inventory registration, legal and security review, licence approval, version-specific testing, role and classification analysis, and an accountable maintenance owner. Material forks, fine-tuning, retraining, or repurposing must trigger reassessment.

## Evidence

- software and model bill of materials;
- licence and attribution record;
- provenance and maintainer review;
- vulnerability and security assessment;
- intended-purpose and limitation record;
- role and classification assessment;
- testing and approval evidence;
- monitoring and replacement plan.

## Audit test

Select open-source AI components in production. Confirm that the exact versions are inventoried, licence and provenance were reviewed, legal role and classification were assessed, vulnerabilities and limitations are monitored, and material modifications triggered reassessment.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: applicable scope, open-source, GPAI, provider-role, substantial-modification, cybersecurity, and high-risk provisions.
- Current consolidated EUR-Lex text controls over older summaries.
