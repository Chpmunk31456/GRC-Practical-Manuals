# Chapter 86 — Prompt Injection and Model Manipulation

## Purpose

This chapter establishes governance and control requirements for direct prompt injection, indirect prompt injection, jailbreaks, instruction manipulation, malicious context, unsafe tool use, and other attempts to alter an AI system’s intended behaviour.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should treat prompts, retrieved content, tool instructions, system messages, memory, and external data as distinct trust domains. Untrusted content must not be permitted to override authorised instructions, expand permissions, disclose protected information, or trigger consequential actions without validated controls and human approval.

## Plain-language explanation

Prompt injection occurs when text or data causes an AI system to follow an attacker’s instructions instead of the organization’s approved rules. The malicious instruction may come directly from a user or indirectly from a webpage, document, email, supplier feed, attachment, or retrieved knowledge source.

## Threat scenarios

Consider attempts to:

- reveal system prompts, secrets, credentials, or personal data;
- bypass policies or safety constraints;
- manipulate classification, ranking, or recommendations;
- cause unauthorised tool calls;
- alter bookings, refunds, payments, or records;
- retrieve data outside the user’s entitlement;
- hide malicious activity from logs;
- persist hostile instructions in memory or retrieval stores;
- induce the system to trust fabricated evidence;
- exploit insecure output handling in downstream systems.

## Trust separation

Controls should distinguish:

- system and developer instructions;
- authorised business rules;
- user input;
- retrieved documents;
- external web content;
- tool results;
- memory and conversation history;
- model-generated output.

Untrusted data must be treated as data, not authority.

## Preventive controls

Use risk-appropriate combinations of:

- instruction hierarchy and immutable policy layers;
- content isolation and delimiters;
- retrieval filtering and source allowlists;
- least-privilege tool access;
- tool allowlists and parameter validation;
- transaction and rate limits;
- output encoding and sanitisation;
- secrets isolation;
- context minimisation;
- data-loss prevention;
- separate confirmation channels;
- human approval for consequential actions;
- secure defaults and fail-closed behaviour.

No single prompt or model instruction should be treated as a complete security control.

## Detection and monitoring

Monitor for:

- known injection patterns;
- policy-bypass attempts;
- unusual tool sequences;
- requests for hidden instructions or secrets;
- unexpected cross-tenant access;
- abnormal output or token volume;
- repeated denials and reformulations;
- suspicious retrieved content;
- changes in refusal or safety behaviour;
- unexplained increases in human overrides.

## Human oversight

For consequential use cases, the AI may propose an action, but a qualified human must review the underlying evidence, confirm the user’s authority, assess anomalies, and approve or reject the action.

The reviewer must not rely solely on the AI’s statement that content is safe or verified.

## Testing

Testing should include:

- direct and indirect injection;
- multilingual and encoded attacks;
- nested instructions;
- malicious documents and webpages;
- tool-call manipulation;
- memory poisoning;
- retrieval poisoning;
- long-context attacks;
- role confusion;
- output-injection into downstream applications;
- attempts to bypass human approval.

Tests should record the exact system version, prompts, context, tools, expected result, actual result, severity, remediation, and retest outcome.

## Stop and escalation conditions

Suspend or restrict operation when:

- protected data can be disclosed;
- unauthorised tools can be invoked;
- consequential actions bypass approval;
- attack attempts cannot be logged;
- hostile instructions persist across sessions;
- critical injection tests fail;
- vendor changes invalidate prior testing;
- controls depend only on model refusal.

## GlobalWay Travel Services example

A malicious hotel webpage contains hidden text instructing GlobalWay’s travel assistant to ignore policy, reveal traveller profiles, and issue a refund through a connected tool.

GlobalWay isolates webpage content, removes active instructions, restricts the assistant to approved retrieval fields, blocks direct refund execution, and requires a human agent to verify eligibility and approve any financial action. The event is logged and routed to security monitoring.

## Control activities

- Classify all context sources by trust level.
- Restrict tools and permissions.
- Require human approval for consequential actions.
- Test direct and indirect attacks before deployment and after material changes.
- Monitor attempted bypasses and anomalous tool use.
- Maintain emergency disablement and rollback procedures.

## Evidence

- trust-boundary design;
- prompt and tool-control standards;
- allowlists and permission records;
- injection test plans and results;
- monitoring rules and alerts;
- human-approval logs;
- incidents and remediation records;
- vendor assurance evidence;
- exception approvals.

## Audit tests

1. Verify that untrusted content cannot override protected instructions.
2. Test whether tool permissions exceed business need.
3. Review samples of consequential actions for human approval.
4. Confirm that injection attempts are logged and investigated.
5. Reperform selected adversarial tests.
6. Verify that failed controls trigger suspension or restriction.
7. Confirm vendor or model changes trigger retesting.

## Metrics

- injection attempts detected;
- successful bypass rate in testing;
- unauthorised tool-call attempts;
- consequential actions requiring approval;
- average time to contain critical findings;
- systems relying solely on prompt-based controls;
- material changes retested before release.

## Management checklist

- Are trusted instructions separated from untrusted content?
- Can external content trigger tools or disclose data?
- Are permissions least-privilege?
- Are consequential actions human-approved?
- Are direct and indirect attacks tested?
- Can the system be disabled quickly?

## Figure specification — Prompt-Injection Defence Layers

Create a layered defence diagram showing untrusted inputs, isolation and filtering, instruction hierarchy, model processing, tool gateway, human approval, output validation, monitoring, and incident response.

**Alt text:** Layered prompt-injection defence showing untrusted inputs passing through isolation, instruction controls, restricted model and tool access, human approval, output validation, monitoring, and incident response.
