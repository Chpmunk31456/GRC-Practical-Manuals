# Chapter 95 — Bias and Discrimination Risk

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 95 draft language.

## Requirement

Organizations must identify and mitigate risks that an AI system may produce unlawful discrimination, unjustified disadvantage, exclusion, inaccessible outcomes, or systematically poorer performance for protected or vulnerable groups. Assessment must reflect the applicable legal and factual context rather than rely on a single statistical metric.

## Plain-English explanation

Bias can arise from data, labels, sampling, proxies, objectives, model behavior, thresholds, user practices, accessibility barriers, feedback loops, or the surrounding decision process. Equal aggregate accuracy does not prove equal treatment, while a numerical disparity does not by itself determine legal unlawfulness.

## Assessment requirements

Assess at minimum:

1. protected and vulnerable groups relevant to the jurisdiction and use case;
2. representation, measurement, labeling, and historical-bias risks;
3. proxy variables and correlated features;
4. subgroup performance, error rates, calibration, and intersectional effects;
5. accessibility and reasonable-accommodation requirements;
6. threshold, ranking, and workflow consequences;
7. human-review quality and automation bias;
8. complaint, challenge, explanation, and remedy mechanisms;
9. feedback loops and post-deployment drift;
10. legal review of proposed metrics, mitigations, and residual disparities.

## GlobalWay example

GlobalWay tests a recruitment-ranking system across relevant applicant groups and job families. It reviews false-negative rates, proxy variables, disability-access barriers, ranking thresholds, human override patterns, and whether accommodations are available. A statistically improved result is not accepted until Legal and HR confirm that the process remains lawful and operationally fair.

## Control activity

High-impact systems must undergo documented pre-deployment and recurring subgroup testing using legally and technically appropriate methods. Material disparities require root-cause analysis, mitigation, validation, and approval. Severe unresolved discrimination risk must block or suspend use.

## Evidence

- protected-group and legal-context analysis;
- data and proxy-variable review;
- subgroup and intersectional testing;
- accessibility and accommodation assessment;
- mitigation and validation results;
- human-review and override analysis;
- complaints and monitoring trends;
- legal and management approvals.

## Audit test

Select systems affecting employment, education, credit, insurance, essential services, or other consequential decisions. Verify that relevant groups and legal requirements were identified, testing covered meaningful subgroups and outcomes, mitigations were validated, accessibility was addressed, and monitoring detects emerging disparity.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: applicable prohibited-practice, high-risk, data-governance, human-oversight, accuracy, monitoring, and fundamental-rights provisions.
- Charter of Fundamental Rights of the European Union.
- Applicable Union and Member State equality, employment, disability, consumer-protection, and sector law.