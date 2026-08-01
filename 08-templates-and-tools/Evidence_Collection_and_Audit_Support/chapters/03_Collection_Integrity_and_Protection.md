# 3. Collection, Integrity, and Protection

## 3.1 Collect from authoritative sources

Identify the system of record, record owner, extraction method, date and time, query or filter parameters, population size, and person performing the extraction. Preserve raw source files when practical and create working copies for review.

## 3.2 System exports

A system export should include enough context to interpret the data:

- system and environment name;
- report or query name;
- extraction timestamp and time zone;
- reporting period;
- filters and exclusions;
- field definitions when unclear;
- total population and row count;
- user or service account that produced the export; and
- known limitations.

When an export is manually transformed, retain the original, record each transformation, and reconcile totals before and after processing.

## 3.3 Screenshots

Screenshots are useful for point-in-time configuration, workflow, and interface evidence, but they are easily incomplete. Capture:

- application and environment;
- visible system date or a documented capture timestamp;
- relevant URL, object, tenant, account, or record identifier without exposing unnecessary secrets;
- the full setting and surrounding context;
- pagination, filters, and scope; and
- the operator and capture method.

Do not crop away context that affects interpretation. Redaction should use an approved method and must not alter the substantive evidence.

## 3.4 Documents and records

Confirm approval status, owner, version, effective date, review date, change history, and applicability. A policy proves documented intent; it does not by itself prove implementation or operation.

## 3.5 Interviews and observations

Document participant roles, date, questions, key statements, observed activities, limitations, and corroborating records. Provide the interviewee an opportunity to correct factual misunderstandings where appropriate. Interviews should not be presented as independent proof when stronger operational evidence should exist.

## 3.6 Reperformance and testing

Record the procedure, inputs, tools, tester, date, environment, expected result, actual result, exceptions, and retained output. Testing must be authorized and designed to avoid operational harm, privacy violations, or unauthorized access.

## 3.7 Authenticity and integrity

Use proportionate controls such as:

- read-only retrieval;
- restricted evidence repositories;
- file hashes;
- digital signatures or trusted timestamps;
- immutable or versioned storage;
- access and download logs;
- source-system reconciliation;
- independent confirmation; and
- documented chain of custody.

A hash helps detect file changes after hashing; it does not prove the original content was accurate or complete.

## 3.8 Chain of custody

For high-risk, investigative, legal, or forensic material, record every transfer, handler, time, location, purpose, action, and integrity check. Use sealed or access-controlled storage and preserve originals. Escalate immediately if custody or integrity is uncertain.

## 3.9 Confidentiality and minimization

Collect the minimum evidence necessary. Redact or tokenize personal data, secrets, credentials, private keys, health information, payment data, legal advice, and unrelated employee information when the assessment objective does not require disclosure. Never email unrestricted credentials or place sensitive evidence in personal storage.

## 3.10 Cross-border and third-party evidence

Confirm contractual rights, data residency, transfer restrictions, confidentiality obligations, regulator requirements, and third-party consent before collection or disclosure. Record any limitation that prevents direct access and the alternative assurance obtained.
