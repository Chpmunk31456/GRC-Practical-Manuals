from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "01-foundations/NIST_AI_600-1_Generative_AI_Profile"
LOCALES = {
    "en": BASE / "English/source",
    "es-419": BASE / "es-419/source",
    "pt-BR": BASE / "pt-BR/source",
}
IMPLEMENTATION_FILES = {
    "en": BASE / "MANUAL_04_IMPLEMENTATION_PATHS.md",
    "es-419": BASE / "es-419/source/RUTAS_DE_IMPLEMENTACION_MANUAL_04.md",
    "pt-BR": BASE / "pt-BR/source/CAMINHOS_DE_IMPLEMENTACAO_MANUAL_04.md",
}

REQUIRED_CHAPTER_FILES = 4
REQUIRED_CHAPTERS = set(range(1, 33))
REQUIRED_TOKENS = ["NIST AI 600-1", "AI RMF", "GOVERN", "MAP", "MEASURE", "MANAGE"]
MIN_IMPLEMENTATION_CHARS = 9000

# Fail only on affirmative overclaims. Required negative disclaimers such as
# "does not create certification", "ni crea certificación", and
# "nem cria certificação" must not be treated as prohibited claims merely
# because the standard identifier and certification term appear together.
PROHIBITED_PATTERNS = [
    r"NIST AI 600-1\s+(?:is|es|é)\s+(?:mandatory|obligatorio|obrigatório)\b",
    r"NIST AI 600-1\s+(?:is|es|é)\s+(?:a\s+|una\s+|uma\s+)?(?:certification|certificación|certificação)\b",
    r"NIST AI 600-1\s+(?:provides|grants|otorga|concede|fornece)\s+(?:a\s+|una\s+|uma\s+)?(?:certification|certificación|certificação)\b",
]
HUMAN_REVIEW_TERMS = {
    "en": ["human review", "Final Human Release Approval"],
    "es-419": ["revisión humana", "Aprobación Humana Final de Liberación"],
    "pt-BR": ["revisão humana", "Aprovação Humana Final de Liberação"],
}
STOP_TERMS = {
    "en": ["stop", "rollback"],
    "es-419": ["detener", "revertir"],
    "pt-BR": ["parar", "reverter"],
}
DISCLAIMERS = {
    "en": ["does not reproduce", "does not create certification"],
    "es-419": ["no reproduce", "ni crea certificación"],
    "pt-BR": ["não reproduz", "nem cria certificação"],
}
IMPLEMENTATION_PATH_TERMS = {
    "en": ["Essential path", "Structured path", "Enhanced path", "Assurance statement"],
    "es-419": ["Ruta esencial", "Ruta estructurada", "Ruta mejorada", "Declaracion de aseguramiento"],
    "pt-BR": ["Caminho essencial", "Caminho estruturado", "Caminho aprimorado", "Declaracao de asseguracao"],
}
IMPLEMENTATION_BOUNDARIES = {
    "en": ["voluntary", "does not certify", "legal compliance", "audit opinion"],
    "es-419": ["voluntario", "no certifica", "cumplimiento legal", "opinion de auditoria"],
    "pt-BR": ["voluntarias", "nao certifica", "conformidade legal", "opiniao de auditoria"],
}


def chapter_inventory(locale: str, directory: Path):
    files = []
    chapters = set()
    if not directory.exists():
        return files, chapters, ""
    for path in sorted(directory.glob("*.md")):
        body = path.read_text(encoding="utf-8")
        if locale == "en":
            found = {int(x) for x in re.findall(r"^## Chapter (\d{2})", body, re.M)}
        else:
            found = {int(x) for x in re.findall(r"^## Cap[ií]tulo (\d{2})", body, re.M)}
        if found:
            files.append(path)
            chapters.update(found)
    text = "\n".join(p.read_text(encoding="utf-8") for p in files)
    return files, chapters, text


errors = []
summary = []

for locale, directory in LOCALES.items():
    files, chapters, text = chapter_inventory(locale, directory)
    if len(files) != REQUIRED_CHAPTER_FILES:
        errors.append(f"{locale}: expected {REQUIRED_CHAPTER_FILES} chapter source blocks, found {len(files)}")
    if chapters != REQUIRED_CHAPTERS:
        errors.append(f"{locale}: chapter coverage mismatch: {sorted(chapters)}")
    for token in REQUIRED_TOKENS:
        if token not in text:
            errors.append(f"{locale}: missing required token {token!r}")
    for term in HUMAN_REVIEW_TERMS[locale]:
        if term.lower() not in text.lower():
            errors.append(f"{locale}: missing human-review boundary term {term!r}")
    for term in STOP_TERMS[locale]:
        if term.lower() not in text.lower():
            errors.append(f"{locale}: missing stop/rollback term {term!r}")
    for term in DISCLAIMERS[locale]:
        if term.lower() not in text.lower():
            errors.append(f"{locale}: missing disclaimer fragment {term!r}")
    for pattern in PROHIBITED_PATTERNS:
        if re.search(pattern, text, re.I):
            errors.append(f"{locale}: prohibited affirmative implication matched {pattern!r}")

    implementation = IMPLEMENTATION_FILES[locale]
    if not implementation.is_file():
        errors.append(f"{locale}: implementation-path source is missing: {implementation.relative_to(ROOT)}")
        continue
    implementation_text = implementation.read_text(encoding="utf-8")
    if len(implementation_text.strip()) < MIN_IMPLEMENTATION_CHARS:
        errors.append(
            f"{locale}: implementation-path source is unexpectedly small "
            f"({len(implementation_text.strip())} chars; minimum {MIN_IMPLEMENTATION_CHARS})"
        )
    for term in IMPLEMENTATION_PATH_TERMS[locale]:
        if term.lower() not in implementation_text.lower():
            errors.append(f"{locale}: implementation paths missing required concept {term!r}")
    for term in IMPLEMENTATION_BOUNDARIES[locale]:
        if term.lower() not in implementation_text.lower():
            errors.append(f"{locale}: implementation paths missing assurance boundary {term!r}")
    for token in REQUIRED_TOKENS:
        if token not in implementation_text:
            errors.append(f"{locale}: implementation paths missing required token {token!r}")
    for pattern in PROHIBITED_PATTERNS:
        if re.search(pattern, implementation_text, re.I):
            errors.append(f"{locale}: implementation paths contain prohibited affirmative implication {pattern!r}")

    summary.append(
        f"{locale}: {len(files)} chapter blocks, 32 chapters, implementation paths present, required boundaries present"
    )

if not errors:
    print("Manual 04 localization fail-closed QA: PASS")
    for line in summary:
        print(f"- {line}")
    print("Automated parity/grammar checks do NOT constitute semantic approval.")
    sys.exit(0)

print("Manual 04 localization fail-closed QA: FAIL")
for err in errors:
    print(f"- {err}")
print("Localized publication remains blocked. Automated QA cannot substitute for semantic approval.")
sys.exit(1)
