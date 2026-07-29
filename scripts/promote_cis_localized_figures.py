from __future__ import annotations

import hashlib
import json
import re
import shutil
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "review/cis-controls-v8.1-localized-figures"
ES_MD = ROOT / "01-foundations/CIS_Controls_v8.1/Espanol/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md"
PT_MD = ROOT / "01-foundations/CIS_Controls_v8.1/Portugues_BR/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md"
ES_MEDIA = ES_MD.parent / "media"
PT_MEDIA = PT_MD.parent / "media"
INVENTORY = ROOT / "qa/images/LEGACY_IMAGE_PROVENANCE_INVENTORY.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def convert_img_tags(path: Path, expected: set[int]) -> None:
    text = path.read_text(encoding="utf-8")
    seen: set[int] = set()

    pattern = re.compile(
        r'<img\s+src="media/image(?P<num>\d+)\.png"[^>]*?alt="(?P<alt>[^"]*)"\s*/>',
        re.IGNORECASE,
    )

    def replace(match: re.Match[str]) -> str:
        number = int(match.group("num"))
        if number not in expected:
            return match.group(0)
        seen.add(number)
        alt = match.group("alt").strip() or f"CIS Controls figure {number}"
        return f"![{alt}](media/image{number}.png)"

    updated = pattern.sub(replace, text)
    missing = expected - seen
    if missing:
        raise SystemExit(f"{path}: missing expected HTML image tags {sorted(missing)}")
    path.write_text(updated, encoding="utf-8")


def main() -> None:
    manifest = json.loads((REVIEW / "manifest.json").read_text(encoding="utf-8"))
    dimensions = {int(k): tuple(v) for k, v in manifest["dimensions"].items()}

    ES_MEDIA.mkdir(parents=True, exist_ok=True)
    PT_MEDIA.mkdir(parents=True, exist_ok=True)

    mappings: list[tuple[str, int, Path, Path]] = [
        ("Latin American Spanish", 3, REVIEW / "es-LATAM-image3.png", ES_MEDIA / "image3.png")
    ]
    mappings.extend(
        ("Brazilian Portuguese", i, REVIEW / f"pt-BR-image{i}.png", PT_MEDIA / f"image{i}.png")
        for i in range(1, 11)
    )

    promoted: dict[tuple[str, int], dict[str, object]] = {}
    for language, number, source, destination in mappings:
        if not source.exists():
            raise SystemExit(f"Missing approved review image: {source}")
        shutil.copy2(source, destination)
        with Image.open(destination) as image:
            image.verify()
        with Image.open(destination) as image:
            if image.format != "PNG" or image.size != dimensions[number]:
                raise SystemExit(f"Invalid promoted image {destination}: {image.format} {image.size}")
            promoted[(language, number)] = {
                "path": destination.relative_to(ROOT).as_posix(),
                "sha256": sha256(destination),
                "width": image.width,
                "height": image.height,
            }

    convert_img_tags(ES_MD, {3})
    convert_img_tags(PT_MD, set(range(1, 11)))

    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    updated_count = 0
    for record in inventory["references"]:
        if record.get("manual_family") != "CIS Controls v8.1":
            continue
        key = (record.get("language"), int(record.get("figure_number")))
        if key not in promoted:
            continue
        info = promoted[key]
        record["localized_asset_exists"] = True
        record["localized_asset_path_checked"] = info["path"]
        if key[0] == "Latin American Spanish":
            record["spanish_localized_asset_exists"] = True
        if key[0] == "Brazilian Portuguese":
            record["brazilian_portuguese_localized_asset_exists"] = True
        record["primary_classification"] = "restored_localized"
        record["validation_status"] = "technical_validation_passed_owner_visual_review_approved"
        record["restored_destination"] = info["path"]
        record["localized_image_sha256"] = info["sha256"]
        record["localized_image_format"] = "PNG"
        record["localized_image_dimensions"] = {
            "width": info["width"],
            "height": info["height"],
        }
        record["owner_approval_evidence"] = "Conversation approval: Approve all CIS review images"
        updated_count += 1

    if updated_count != 11:
        raise SystemExit(f"Expected 11 CIS inventory updates, got {updated_count}")

    INVENTORY.write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Promoted 11 approved CIS localized figures and updated Markdown/provenance.")


if __name__ == "__main__":
    main()
