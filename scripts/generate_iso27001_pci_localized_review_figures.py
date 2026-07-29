#!/usr/bin/env python3
"""Generate review-only Brazilian Portuguese reconstructions for ISO 27001 and PCI DSS figures."""

from __future__ import annotations

import hashlib
import json
import re
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "qa/images/LEGACY_IMAGE_PROVENANCE_INVENTORY.json"
OUTPUT = ROOT / "review/iso27001-pci-dss-localized-figures"
FAMILIES = ("ISO/IEC 27001/27002", "PCI DSS v4.0.1")
EXPECTED_TOTAL = 18


def get_font(size: int, bold: bool = False):
    choices = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for choice in choices:
        if Path(choice).exists():
            return ImageFont.truetype(choice, size=size)
    return ImageFont.load_default()


def wrap(draw, text: str, max_width: int, font) -> list[str]:
    lines, current = [], ""
    for word in text.split():
        candidate = f"{current} {word}".strip()
        if draw.textbbox((0, 0), candidate, font=font)[2] <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def source_size(record: dict) -> tuple[int, int]:
    evidence = record["english_source_evidence"]
    with ZipFile(ROOT / evidence["container"]) as archive:
        raw = archive.read(evidence["internal_path"])
    with Image.open(BytesIO(raw)) as image:
        return image.size


def concept_segments(text: str) -> list[str]:
    cleaned = re.sub(r"\s+", " ", text).strip()
    parts = [p.strip(" .") for p in re.split(r"[;:]|,\s+", cleaned) if p.strip(" .")]
    if len(parts) < 3:
        words = cleaned.split()
        chunk = max(1, len(words) // 4)
        parts = [" ".join(words[i:i + chunk]) for i in range(0, len(words), chunk)]
    return parts[:5]


def draw_candidate(record: dict, destination: Path) -> dict:
    width, height = source_size(record)
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    margin = max(30, width // 30)
    title_font = get_font(max(27, width // 38), True)
    body_font = get_font(max(19, width // 62))
    number_font = get_font(max(22, width // 52), True)

    caption = record.get("caption") or f"Figura {record.get('figure_number', '')}"
    meaning = record.get("alt_text") or ""
    header_h = max(110, height // 7)
    draw.rounded_rectangle((margin, margin, width - margin, margin + header_h), radius=22, fill="#EEF3F8", outline="#37474F", width=3)

    y = margin + 18
    for line in wrap(draw, caption, width - 4 * margin, title_font)[:2]:
        box = draw.textbbox((0, 0), line, font=title_font)
        draw.text(((width - (box[2] - box[0])) / 2, y), line, font=title_font, fill="#17202A")
        y += box[3] - box[1] + 8

    items = concept_segments(meaning)
    count = len(items)
    gap = max(16, width // 90)
    content_top = margin + header_h + max(24, height // 35)
    footer_h = max(65, height // 11)
    box_h = min(max(150, height * 0.38), height - content_top - footer_h - margin)
    box_y = content_top + max(10, (height - content_top - footer_h - box_h) / 2)
    box_w = (width - 2 * margin - gap * (count - 1)) / count

    for idx, item in enumerate(items):
        x1 = margin + idx * (box_w + gap)
        x2 = x1 + box_w
        draw.rounded_rectangle((x1, box_y, x2, box_y + box_h), radius=20, fill="#FAFCFD", outline="#546E7A", width=3)
        cx = (x1 + x2) / 2
        circle_r = max(18, width // 82)
        cy = box_y + circle_r + 15
        draw.ellipse((cx - circle_r, cy - circle_r, cx + circle_r, cy + circle_r), fill="#DCE6EE", outline="#37474F", width=2)
        number = str(idx + 1)
        nbox = draw.textbbox((0, 0), number, font=number_font)
        draw.text((cx - (nbox[2] - nbox[0]) / 2, cy - (nbox[3] - nbox[1]) / 2 - 2), number, font=number_font, fill="#17202A")

        ty = cy + circle_r + 16
        for line in wrap(draw, item, int(box_w - 30), body_font)[:6]:
            tbox = draw.textbbox((0, 0), line, font=body_font)
            draw.text((cx - (tbox[2] - tbox[0]) / 2, ty), line, font=body_font, fill="#263238")
            ty += tbox[3] - tbox[1] + 6

        if idx < count - 1:
            ay = box_y + box_h / 2
            start, end = x2 + 3, x2 + gap - 3
            draw.line((start, ay, end, ay), fill="#455A64", width=4)
            draw.polygon([(end, ay), (end - 12, ay - 8), (end - 12, ay + 8)], fill="#455A64")

    footer = f"Reconstrução localizada programática para revisão — {record['manual_family']}"
    fbox = draw.textbbox((0, 0), footer, font=body_font)
    draw.text(((width - (fbox[2] - fbox[0])) / 2, height - footer_h + 15), footer, font=body_font, fill="#455A64")

    destination.parent.mkdir(parents=True, exist_ok=True)
    image.save(destination, "PNG", optimize=True)
    return {
        "inventory_id": record["id"],
        "manual_family": record["manual_family"],
        "figure_number": record.get("figure_number"),
        "caption": caption,
        "alt_text": meaning,
        "review_file": destination.relative_to(ROOT).as_posix(),
        "width": width,
        "height": height,
        "sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
        "status": "review_only_pending_owner_approval",
        "description": "Programmatic localized reconstruction; not an exact visual reproduction.",
    }


def main() -> None:
    data = json.loads(INVENTORY.read_text(encoding="utf-8"))
    records = [r for r in data["references"] if r.get("manual_family") in FAMILIES and r.get("primary_classification") == "requires_localization"]
    if len(records) != EXPECTED_TOTAL:
        raise SystemExit(f"Expected {EXPECTED_TOTAL} records, found {len(records)}")

    manifest = []
    for record in records:
        family_slug = "iso27001" if record["manual_family"].startswith("ISO/") else "pci-dss"
        destination = OUTPUT / f"pt-BR-{family_slug}-image{record['exact_image_path'].split('image')[-1]}"
        manifest.append(draw_candidate(record, destination))

    (OUTPUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Generated {len(manifest)} review-only localized figures in {OUTPUT}")


if __name__ == "__main__":
    main()
