# Manual 50 — Clean Candidate Release Decision

**Date:** 1 September 2026  
**Candidate workflow run:** 33570204071  
**Artifact:** 9824656967 — `manual50-six-binary-candidate`  
**Artifact digest:** `sha256:0f9aeb68109367925203da09524d39b830b87ec1c4aaecd466bd9e7d90bf54c7`  
**Candidate source head:** `1e72997b45ade5eb2ef6205483519d5f1ef52a62`

## Release basis

The controlled Manual 50 candidate build completed successfully. Deterministic DOCX/PDF construction, PDF visible-text checks, first-page raster render checks, trilingual publication-source parity anchors, and candidate artifact upload all passed. The exact artifact was independently downloaded and its six publication binaries were SHA-256 verified without regeneration.

Frozen binary identities:

- EN DOCX — 41,952 bytes — `60950abfe278dc26dd36efef3d0395c3d5d99eca651b358fa3c3755229e4490f`
- EN PDF — 86,863 bytes — `bea5d32f6749328e24a846e7f48488d4694f54f5c664eee97bdffa6fd85108ae`
- es-419 DOCX — 41,287 bytes — `4e1d075be446461a3c274f5a2509a87f74607cf2ed3333028decb400d6196dc9`
- es-419 PDF — 70,125 bytes — `a1885b7b769625d6932193bd564bb68ec42ce5dfdb0c41ce15cf6aa77ffb6a54`
- pt-BR DOCX — 41,342 bytes — `cb4eb4261bd68d17ce1b24ce9d3baee3be248f1544d264c375fb7172b81a02b9`
- pt-BR PDF — 71,094 bytes — `1681b52b8dfdf25f1e3a463361e3a89665798d5cf7412fb5357ffd397c94be10`

The repository-owner canonical clean-candidate automatic release rule applies. No substantive, source-currentness, localization, integrity, packaging, rendering, provenance, or workflow-security defect is documented for the frozen candidate. This decision does not fabricate a human reviewer and does not waive retained repository checks on the final publication head.

## Decision

Proceed with exact-byte staging of the frozen candidate, publication-registry reconciliation, final-head retained checks, and publication merge. Standing owner/final approval is already granted.