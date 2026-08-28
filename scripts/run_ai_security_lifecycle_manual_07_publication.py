#!/usr/bin/env python3
"""Safe runner for Manual 07 publication generation.

Repairs Manual 07 adapter bindings while preserving fail-closed publication,
semantic, accessibility, provenance, security, and human approval controls.
"""
from __future__ import annotations

import generate_ai_security_lifecycle_manual_07_publication as manual07


def find_localized_chapters(language: str):
    chapters: dict[int, str] = {}
    used: list[str] = []
    for path in sorted(manual07.source_dir(language).glob("*.md")):
        found = manual07.base.split_chapters(path.read_text(encoding="utf-8"))
        if not found:
            continue
        for number, body in found.items():
            if number in chapters and chapters[number] != body:
                raise ValueError(f"conflicting chapter {number} for {language}: {path}")
            chapters[number] = body
        used.append(str(path.relative_to(manual07.ROOT)))
    expected = set(range(1, 33))
    if set(chapters) != expected:
        raise ValueError(f"{language} chapter inventory invalid: {sorted(chapters)}")
    return "\n".join(chapters[n].rstrip() for n in range(1, 33)) + "\n", used


def inspect_pdf(path, render_dir):
    """Manual 07 PDF inspection with content-based checks and a realistic page floor.

    Manual 07 is intentionally more compact than Manual 03. Eight pages is the
    structural floor; chapter completeness is independently enforced in DOCX QA,
    and every PDF page must still contain meaningful extractable text and render.
    """
    pdf = manual07.core.fitz.open(path)
    if pdf.page_count < 8:
        raise ValueError(f"PDF page count unexpectedly small ({pdf.page_count}): {path}")
    render_dir.mkdir(parents=True, exist_ok=True)
    page_rows = []
    blank_pages = []
    for index, page in enumerate(pdf):
        text = page.get_text("text").strip()
        if len(text) < 20:
            blank_pages.append(index + 1)
        pix = page.get_pixmap(matrix=manual07.core.fitz.Matrix(1.35, 1.35), alpha=False)
        png = render_dir / f"page-{index + 1:03d}.png"
        pix.save(png)
        page_rows.append({
            "pdf": path.name,
            "page": index + 1,
            "width_pt": round(page.rect.width, 2),
            "height_pt": round(page.rect.height, 2),
            "text_chars": len(text),
            "render": str(png),
            "automated_status": "PASS" if len(text) >= 20 else "REVIEW",
        })
    if blank_pages:
        raise ValueError(f"possible blank PDF pages in {path.name}: {blank_pages}")
    result = {
        "file": path.name,
        "bytes": path.stat().st_size,
        "pages": pdf.page_count,
        "metadata": dict(pdf.metadata or {}),
        "sha256": manual07.core.sha256(path),
        "status": "PASS",
    }
    pdf.close()
    return result, page_rows


manual07.base.find_localized_chapters = find_localized_chapters
manual07.core.find_localized_chapters = find_localized_chapters
manual07.core.inspect_pdf = inspect_pdf

if __name__ == "__main__":
    raise SystemExit(manual07.core.main())
