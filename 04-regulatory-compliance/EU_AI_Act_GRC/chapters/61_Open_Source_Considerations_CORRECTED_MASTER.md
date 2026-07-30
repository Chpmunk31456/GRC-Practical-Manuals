# Chapter 61 — Open-Source Considerations

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 61 draft language.

## Requirement

Open-source status does not create a blanket exemption from Regulation (EU) 2024/1689, as amended. Organizations must assess the exact statutory conditions, the actor’s role, the model or system category, whether monetisation or related services are involved, whether systemic risk applies, and which obligations remain applicable.

## Plain-English explanation

A public licence or downloadable model does not by itself determine legal treatment. The Act provides limited special treatment in specified circumstances, but important obligations may still apply, especially for systemic-risk GPAI models, prohibited practices, high-risk uses, transparency duties, and downstream providers that integrate, modify, rebrand, or deploy open components.

## Assessment questions

Document:

1. the licence and access conditions;
2. whether source code, architecture, weights, and usage information are genuinely available as required;
3. whether the provider receives monetary or other consideration, including platform, support, hosting, or data-related benefits;
4. whether the model presents systemic risk;
5. whether the organization modifies, fine-tunes, integrates, rebrands, or changes intended purpose;
6. whether the resulting system is prohibited, high-risk, or transparency-regulated;
7. which documentation, copyright, security, incident, and downstream-information duties remain;
8. how vulnerabilities, updates, provenance, and component dependencies are governed.

## GlobalWay example

GlobalWay downloads an openly licensed model and fine-tunes it for employee-screening support. The licence does not remove the need to assess high-risk classification, provider-role transfer, data governance, conformity, human oversight, security, and documentation obligations.

## Control activity

Open-source components must pass legal, security, provenance, licence, and role assessment before use. The inventory must record version, source, licence, maintainers, dependencies, modifications, intended purpose, known limitations, and reassessment triggers.

## Evidence

- licence and repository records;
- statutory open-source analysis;
- monetisation and service assessment;
- model and system classification;
- role and substantial-modification assessment;
- component inventory and provenance;
- vulnerability and update records;
- downstream documentation and approvals.

## Audit test

Select open-source AI components in production. Confirm that the organization did not rely on a blanket exemption, assessed the statutory conditions and remaining duties, tracked modifications and dependencies, and reassessed classification and role after material changes.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: relevant provisions concerning free and open-source AI systems and GPAI models, including Articles 2 and 53–55 as applicable.
- Current consolidated EUR-Lex text controls over older summaries.
- Applicable Commission and AI Office guidance must be identified as non-binding unless legally adopted.