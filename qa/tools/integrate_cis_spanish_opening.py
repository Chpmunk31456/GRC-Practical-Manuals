from pathlib import Path

TARGET = Path("01-foundations/CIS_Controls_v8.1/Espanol/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md")
REWRITE = Path("qa/rewrite/CIS_CONTROLS_V8_1_ES_OPENING_REVIEWED.md")
START_BODY = "# 1. Fundamentos de CIS Controls v8.1"


def main() -> None:
    target_text = TARGET.read_text(encoding="utf-8")
    rewrite_text = REWRITE.read_text(encoding="utf-8").rstrip() + "\n\n"

    body_index = target_text.find(START_BODY)
    if body_index < 0:
        raise SystemExit(f"Required body marker not found: {START_BODY}")

    body = target_text[body_index:]
    updated = rewrite_text + body

    if updated == target_text:
        print("CIS Spanish opening already matches the reviewed rewrite.")
        return

    TARGET.write_text(updated, encoding="utf-8")
    print(f"Updated reviewed opening in {TARGET}")


if __name__ == "__main__":
    main()
