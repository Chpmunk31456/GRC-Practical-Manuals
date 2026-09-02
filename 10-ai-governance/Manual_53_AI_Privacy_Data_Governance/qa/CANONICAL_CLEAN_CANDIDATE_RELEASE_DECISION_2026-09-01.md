# Manual 53 canonical clean-candidate release decision

Date: 1 September 2026

Decision: RELEASE FOR FINAL EXACT-BYTE PUBLICATION TRANSACTION.

Evidence:
- controlled candidate workflow run `33573114591`: SUCCESS;
- frozen artifact `9825670619`, `manual53-six-binary-candidate`;
- artifact digest `sha256:02eedc9e8ea53f693694da20ea38aa874cf0db1340c5f38c97fa4f11d8e187da`;
- candidate source head `e15050e25f8625480ee30d86daf67004b14ce71e`;
- deterministic EN/es-419/pt-BR DOCX/PDF build passed;
- PDF visible-text and first-page raster checks passed;
- PD-01 through PD-20 trilingual parity anchors passed;
- predecessor Manual 52 is published on `main`;
- no documented substantive, source-status, localization, packaging, integrity or rendering defect remains.

Frozen binary identities:
- EN DOCX: 40482 bytes, `c2933ec816b39d949ab6e1cd6323a2947ba7b4cd51669b532a4c31389823ab92`
- EN PDF: 66019 bytes, `33b1c8c69fbcc91ccc5585ea0bb0a62c5227a60d3879a06fc24eeb607f1c3885`
- es-419 DOCX: 40585 bytes, `2bb08e0fba506e80d35577cd42de561e4c34208e90f7eeecec516443b2bad3ed`
- es-419 PDF: 67340 bytes, `957a4df75bd1b734c0ff3b94a8d6179c471178c9d08a6c42a047f5bb89534bef`
- pt-BR DOCX: 40642 bytes, `f4a93ca8a7ed681a60be68ff975efd23578fb685eb0284871d016100abb8d896`
- pt-BR PDF: 68619 bytes, `a0a281f1adac54f3957b2fb2487d44773cab63f7c6fbda32501814493fe288d9`

The standing clean-candidate rule applies. This decision does not waive any retained final-head CI gate.