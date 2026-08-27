# Manual 07 — Localization & Semantic Review Gate

Status: LOCALIZATION DRAFTS COMPLETE / HUMAN REVIEW OPEN / FAIL-CLOSED

Languages: English controlled source, Spanish `es-419`, Brazilian Portuguese `pt-BR`.

The controlled Spanish and Brazilian Portuguese chapter drafts and localized implementation paths are complete. Completion of draft localization is not semantic approval and does not close this gate.

Required human semantic review covers AI lifecycle security, threat modeling, provenance, prompt injection, RAG/tool/agent authorization, secrets/data leakage, adversarial testing, red teaming, guardrails, monitoring, incident containment, rollback/stop, supplier/component and supply chain risk, and decommissioning.

Security terms must preserve authorization boundaries and must not weaken stop, rollback, least-privilege or evidence requirements in localization. Repository QA is not a guarantee of security and must never be presented as one.

The reviewer must also confirm that localized prose is natural, understandable, practitioner-oriented, and free of unnecessary machine-like or repetitive compliance wording. Technical correctness alone is insufficient when wording is materially difficult for a competent practitioner to understand.

Reviewer record must include reviewer, date, decision, evidence, findings and remediation. Material English or source-baseline changes reopen affected localized review. Automated translation/parity/readability checks are supporting evidence only and do not constitute technical, semantic, legal, accessibility, or human approval.