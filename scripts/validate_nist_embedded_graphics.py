from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
NIST_DOCX_FILES = (
    ROOT
    / "01-foundations/NIST_CSF_2/Espanol/"
    "NIST_CSF_2_Practical_GRC_and_Junior_Analyst_Manual_Espanol_v1.0.docx",
    ROOT
    / "01-foundations/NIST_CSF_2/Portugues_BR/"
    "NIST_CSF_2_Practical_GRC_and_Junior_Analyst_Manual_Portugues_BR_v1.0.docx",
)
EXPECTED_FIGURES = 8


def embedded_media(docx: Path) -> list[str]:
    with ZipFile(docx) as archive:
        return [
            name
            for name in archive.namelist()
            if name.startswith("word/media/") and not name.endswith("/")
        ]


def main() -> None:
    for docx in NIST_DOCX_FILES:
        media = embedded_media(docx)
        if len(media) != EXPECTED_FIGURES:
            raise RuntimeError(
                f"{docx.relative_to(ROOT)} must contain exactly "
                f"{EXPECTED_FIGURES} embedded figures; found {len(media)}: {media}"
            )
        print(
            f"Embedded-figure check: {docx.relative_to(ROOT)} contains "
            f"exactly {EXPECTED_FIGURES} figures."
        )


if __name__ == "__main__":
    main()
