#!/usr/bin/env python3
"""Generate Batch 4 review-only Brazilian Portuguese reconstructions."""

from __future__ import annotations

import json
import hashlib
from pathlib import Path

import generate_iso27001_pci_localized_review_figures as engine
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "review/nist-rmf-incident-response-localized-figures"
FAMILIES = ("NIST RMF / SP 800-53", "Incident Response / BCDR")
EXPECTED_TOTAL = 20
SHEET_WIDTH = 1500

PALETTES = {
    "NIST RMF / SP 800-53": {
        "navy": "#12355B",
        "accent": "#007C91",
        "highlight": "#F2B134",
        "background": "#F4F8FB",
        "card_fills": ("#E6F3F5", "#EDF1FA", "#FFF4D6", "#E9F5EC", "#F4EAF7"),
        "text": "#172A3A",
    },
    "Incident Response / BCDR": {
        "navy": "#25344F",
        "accent": "#C4473D",
        "highlight": "#E89B3C",
        "background": "#FAF7F2",
        "card_fills": ("#FCE8E6", "#E8EFF8", "#FFF1D8", "#E7F3ED", "#F2EAF7"),
        "text": "#202A3A",
    },
}


def get_font(size: int, bold: bool = False):
    names = (
        ("C:/Windows/Fonts/DejaVuSans-Bold.ttf", "C:/Windows/Fonts/DejaVuSans.ttf"),
        ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        ("/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf", "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"),
    )
    for bold_name, regular_name in names:
        path = Path(bold_name if bold else regular_name)
        if path.exists():
            return ImageFont.truetype(path, size=size)
    return ImageFont.load_default()


def draw_candidate(record: dict, destination: Path) -> dict:
    width, height = engine.source_size(record)
    palette = PALETTES[record["manual_family"]]
    image = Image.new("RGB", (width, height), palette["background"])
    draw = ImageDraw.Draw(image)
    margin = max(34, width // 28)
    title_font = get_font(max(30, width // 36), True)
    body_font = get_font(max(20, width // 60))
    number_font = get_font(max(23, width // 50), True)
    footer_font = get_font(max(16, width // 76))

    caption = record.get("caption") or f"Figura {record.get('figure_number', '')}"
    meaning = record.get("alt_text") or ""
    header_h = max(130, height // 6)
    draw.rounded_rectangle(
        (margin, margin, width - margin, margin + header_h),
        radius=26,
        fill=palette["navy"],
    )
    draw.rounded_rectangle(
        (margin, margin + header_h - 12, width - margin, margin + header_h),
        radius=6,
        fill=palette["highlight"],
    )

    y = margin + 24
    for line in engine.wrap(draw, caption, width - 4 * margin, title_font)[:2]:
        box = draw.textbbox((0, 0), line, font=title_font)
        draw.text(
            ((width - (box[2] - box[0])) / 2, y),
            line,
            font=title_font,
            fill="#FFFFFF",
        )
        y += box[3] - box[1] + 10

    items = engine.concept_segments(meaning)
    count = len(items)
    gap = max(18, width // 84)
    content_top = margin + header_h + max(28, height // 32)
    footer_h = max(72, height // 10)
    box_h = min(max(170, height * 0.40), height - content_top - footer_h - margin)
    box_y = content_top + max(8, (height - content_top - footer_h - box_h) / 2)
    box_w = (width - 2 * margin - gap * (count - 1)) / count

    for idx, item in enumerate(items):
        x1 = margin + idx * (box_w + gap)
        x2 = x1 + box_w
        fill = palette["card_fills"][idx % len(palette["card_fills"])]
        draw.rounded_rectangle(
            (x1 + 5, box_y + 7, x2 + 5, box_y + box_h + 7),
            radius=22,
            fill="#CDD6DF",
        )
        draw.rounded_rectangle(
            (x1, box_y, x2, box_y + box_h),
            radius=22,
            fill=fill,
            outline=palette["accent"],
            width=4,
        )
        cx = (x1 + x2) / 2
        circle_r = max(21, width // 76)
        cy = box_y + circle_r + 18
        draw.ellipse(
            (cx - circle_r, cy - circle_r, cx + circle_r, cy + circle_r),
            fill=palette["accent"],
            outline="#FFFFFF",
            width=3,
        )
        number = str(idx + 1)
        nbox = draw.textbbox((0, 0), number, font=number_font)
        draw.text(
            (cx - (nbox[2] - nbox[0]) / 2, cy - (nbox[3] - nbox[1]) / 2 - 2),
            number,
            font=number_font,
            fill="#FFFFFF",
        )

        ty = cy + circle_r + 18
        for line in engine.wrap(draw, item, int(box_w - 34), body_font)[:6]:
            tbox = draw.textbbox((0, 0), line, font=body_font)
            draw.text(
                (cx - (tbox[2] - tbox[0]) / 2, ty),
                line,
                font=body_font,
                fill=palette["text"],
            )
            ty += tbox[3] - tbox[1] + 7

        if idx < count - 1:
            ay = box_y + box_h / 2
            start, end = x2 + 4, x2 + gap - 4
            draw.line((start, ay, end, ay), fill=palette["accent"], width=5)
            draw.polygon(
                [(end, ay), (end - 13, ay - 9), (end - 13, ay + 9)],
                fill=palette["accent"],
            )

    footer = (
        f"Reconstrução localizada programática para revisão — "
        f"{record['manual_family']}"
    )
    fbox = draw.textbbox((0, 0), footer, font=footer_font)
    draw.text(
        ((width - (fbox[2] - fbox[0])) / 2, height - footer_h + 20),
        footer,
        font=footer_font,
        fill=palette["navy"],
    )

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


def create_review_sheet(records: list[dict], family: str, destination: Path) -> None:
    family_records = [item for item in records if item["manual_family"] == family]
    if len(family_records) != 10:
        raise SystemExit(f"Expected 10 review images for {family}")
    thumb_width = 700
    thumb_height = 386
    padding = 34
    label_height = 54
    sheet_height = padding + 5 * (thumb_height + label_height + padding)
    palette = PALETTES[family]
    sheet = Image.new("RGB", (SHEET_WIDTH, sheet_height), palette["background"])
    draw = ImageDraw.Draw(sheet)
    label_font = get_font(20, True)
    for idx, item in enumerate(family_records):
        row, col = divmod(idx, 2)
        x = padding + col * (thumb_width + padding)
        y = padding + row * (thumb_height + label_height + padding)
        with Image.open(ROOT / item["review_file"]) as source:
            thumb = source.convert("RGB")
            thumb.thumbnail((thumb_width, thumb_height), Image.Resampling.LANCZOS)
        sheet.paste(thumb, (x, y))
        label = f"{item['caption']} · {Path(item['review_file']).name}"
        label_y = y + thumb_height + 10
        for line in engine.wrap(draw, label, thumb_width, label_font)[:2]:
            draw.text((x, label_y), line, font=label_font, fill=palette["navy"])
            label_y += 23
    sheet.save(destination, "PNG", optimize=True)


def main() -> None:
    data = json.loads(engine.INVENTORY.read_text(encoding="utf-8"))
    records = [
        record
        for record in data["references"]
        if record.get("manual_family") in FAMILIES
        and record.get("primary_classification") == "requires_localization"
    ]
    if len(records) != EXPECTED_TOTAL:
        raise SystemExit(f"Expected {EXPECTED_TOTAL} records, found {len(records)}")

    manifest = []
    for record in records:
        family_slug = (
            "nist-rmf"
            if record["manual_family"] == "NIST RMF / SP 800-53"
            else "incident-response-bcdr"
        )
        suffix = record["exact_image_path"].split("image", 1)[-1]
        destination = OUTPUT / f"pt-BR-{family_slug}-image{suffix}"
        manifest.append(draw_candidate(record, destination))

    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    create_review_sheet(
        manifest,
        "NIST RMF / SP 800-53",
        OUTPUT / "review-sheet-nist-rmf.png",
    )
    create_review_sheet(
        manifest,
        "Incident Response / BCDR",
        OUTPUT / "review-sheet-incident-response-bcdr.png",
    )
    print(f"Generated {len(manifest)} review-only localized figures in {OUTPUT}")


if __name__ == "__main__":
    main()
