# Chapter 86 — Prompt Injection and Model Manipulation

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 86 draft language.

## Requirement

AI systems that process instructions, retrieved content, tool outputs, files, web content, or user-supplied data must implement proportionate controls against prompt injection, instruction hijacking, jailbreaks, context manipulation, unsafe tool execution, and related model-manipulation attacks.

## Plain-English explanation

An AI system may treat hostile content as trusted instructions. Controls must prevent untrusted input from changing the system's intended purpose, overriding safeguards, exposing confidential information, or causing unauthorized actions.

## Control requirements

Implement as appropriate:

1. separation of system, developer, user, retrieved, and tool-generated content;
2. least-privilege tool and data access;
3. allowlists, policy enforcement, and action confirmation;
4. content provenance and trust labeling;
5. input and output filtering with known limitations documented;
6. isolation or sandboxing of untrusted content;
7. human approval for consequential or irreversible actions;
8. anomaly detection, logging, rate limits, and session controls;
9. adversarial testing for direct and indirect injection;
10. safe failure, rollback, incident response, and vendor escalation.

## GlobalWay example

GlobalWay's travel assistant reads external hotel descriptions and emails. A malicious page contains hidden instructions asking the agent to reveal traveler data and change a booking. The system treats external content as untrusted, blocks access to unrelated data, requires user confirmation for booking changes, and logs the attempted manipulation.

## Control activity

Prompt-enabled systems must pass documented injection and manipulation testing before release and after material model, prompt, tool, retrieval, or integration changes. Unresolved high-impact paths must block production use.

## Evidence

- prompt and tool architecture;
- trust-boundary and privilege design;
- test cases and adversarial results;
- policy and filtering configuration;
- action-confirmation records;
- attack logs and incident records;
- remediation and retest evidence.

## Audit test

Select prompt-enabled systems and verify that direct and indirect injection scenarios were tested, privileges are constrained, consequential actions require appropriate authorization, attack attempts are detectable, and remediation was validated.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: applicable risk-management, human-oversight, accuracy, robustness, cybersecurity, logging, monitoring, and incident provisions.
- Current consolidated EUR-Lex text controls over older summaries.