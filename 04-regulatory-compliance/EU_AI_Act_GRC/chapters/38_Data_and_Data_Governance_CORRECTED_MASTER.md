# Chapter 38 — Data and Data Governance

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 38 draft language.

## Requirement

Where a high-risk AI system uses training, validation, or testing datasets, the provider must apply the data and data-governance requirements of Article 10 of Regulation (EU) 2024/1689, as amended.

## Plain-English explanation

The legal objective is not perfect data. It is disciplined, documented data governance appropriate to the intended purpose and risk. The provider must understand where the data came from, why it is suitable, how it was prepared, what limitations or errors exist, whether affected groups are adequately represented, and whether the system could create or reinforce bias.

Article 10 does not independently create a lawful basis to process personal data or special-category data. GDPR and other applicable privacy requirements must be assessed separately.

## Required governance areas

The provider should document, as applicable:

1. data-design choices and collection processes;
2. data origin, provenance, and original purpose;
3. data preparation, annotation, labelling, cleaning, enrichment, and aggregation;
4. assumptions about what the data measures or represents;
5. availability, quantity, and suitability of datasets;
6. examination of possible bias and its effects on health, safety, or fundamental rights;
7. measures to detect, prevent, and mitigate bias;
8. relevance, representativeness, completeness, and error characteristics;
9. statistical properties and suitability for the persons, groups, geography, context, and conditions of intended use;
10. controls for data gaps, drift, leakage, duplication, contamination, and unauthorized use;
11. separation and governance of training, validation, and testing datasets where appropriate;
12. documented exceptions, limitations, and residual risks.

## GlobalWay example

GlobalWay develops a recruitment-screening system using historical application and hiring data. The data-governance review identifies underrepresentation in certain job families, inconsistent historical labels, proxy variables for protected characteristics, and geographic differences. GlobalWay removes inappropriate features, improves documentation, tests subgroup performance, limits the intended use, and requires human review.

## Control activity

The provider must approve a system-specific data-governance plan before model development or material retraining. Dataset versions, transformations, quality checks, bias analyses, access controls, and approvals must be traceable to the released model or system version.

## Evidence

- data-governance plan;
- dataset register and provenance records;
- data-processing and annotation procedures;
- data-quality and representativeness analysis;
- bias and subgroup testing;
- privacy and lawful-basis assessment;
- dataset version history;
- access and change logs;
- limitations and residual-risk record;
- approval records.

## Audit test

Select a released high-risk AI-system version and trace it to the exact training, validation, and testing datasets. Confirm that suitability, provenance, quality, representativeness, bias, privacy, transformations, and limitations were assessed and approved before release.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: Article 10.
- GDPR and applicable Member State or sector law remain independently applicable.
- Current consolidated EUR-Lex text controls over older summaries.