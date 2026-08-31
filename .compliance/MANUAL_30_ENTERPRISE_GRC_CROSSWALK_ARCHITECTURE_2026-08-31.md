# Manual 30 — Enterprise GRC Integration & Crosswalks — Controlled Architecture Gate

Status: active downstream prebuild. Publication remains sequential behind Manual 29.

## Controlled source boundary

Manual 30 is an original integration layer over the controlled manual series, not a new normative standard. It must never claim that mapped clauses, controls, legal obligations, risks, or evidence requirements are equivalent merely because they share a topic. Each mapping must retain source, version, directionality, rationale, confidence, gaps, and non-equivalence notes.

## Controlled 32-chapter architecture

1. Purpose, scope, and non-equivalence principle
2. Source/version registry and change control
3. Enterprise obligation object model
4. Canonical control object model
5. Risk taxonomy and risk-object model
6. Policy and standard hierarchy
7. Procedure and operating-control relationships
8. Evidence-object architecture
9. Test and assurance-object architecture
10. Exception and risk-acceptance objects
11. Finding, issue, and remediation objects
12. Ownership, accountability, and RACI relationships
13. Entity, jurisdiction, product, and service applicability
14. Asset, process, data, supplier, and technology relationships
15. One-to-one, one-to-many, and many-to-many mappings
16. Directionality and asymmetric mappings
17. Confidence, rationale, and mapping limitations
18. Partial coverage and gap representation
19. Legal obligation vs guidance vs voluntary standard separation
20. Control inheritance and shared-control governance
21. Evidence reuse without false sufficiency claims
22. Testing reuse and assurance boundaries
23. Cross-framework issue normalization
24. Regulatory-change impact analysis
25. Framework/version migration management
26. Metrics, aggregation, and reporting semantics
27. Executive/board reporting and decision support
28. Audit/regulator/customer evidence packages
29. Data quality and reconciliation controls
30. Governance of crosswalk approvals and changes
31. Localization, accessibility, provenance, and audit trail
32. Release roadmap and series-wide maintenance model

## Required mapping record

Each crosswalk record must carry: source framework/law/manual and version; source object; target framework/law/manual and version; target object; mapping direction; rationale; confidence; coverage level; known gaps; non-equivalence statement; owner; reviewer/test method; evidence dependencies; and revalidation trigger.

## Next parallel work

Build the enterprise object schema and controlled crosswalk methodology; populate representative crosswalks only after source/version validation; design automated reconciliation tests; and prepare a series-wide change-impact process that can update mappings without silently altering published-source meaning.