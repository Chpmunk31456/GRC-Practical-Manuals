#!/usr/bin/env python3
"""Generate Batch 5 review-only Brazilian Portuguese reconstructions."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import generate_nist_rmf_incident_response_localized_review_figures as engine
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "qa/images/LEGACY_IMAGE_PROVENANCE_INVENTORY.json"
OUTPUT = ROOT / "review/cloud-third-party-localized-figures"
FAMILIES = (
    "Cloud Security and Compliance",
    "Third-Party Risk and Supply Chain Security",
)
EXPECTED_TOTAL = 20

REVIEW_TEXT = {
    "LEGACY-IMG-063": "Sempre confirme a documentação e o contrato exatos do serviço; diagramas são pontos de partida simplificados.",
    "LEGACY-IMG-064": "Hierarquia, identidade, redes, logs centralizados, políticas e separação de cargas de trabalho criam guardrails consistentes.",
    "LEGACY-IMG-065": "Comprovação de identidade robusta, MFA, privilégio mínimo, controle de sessão, revisão e revogação reduzem o risco do plano de controle.",
    "LEGACY-IMG-066": "Acompanhe os dados desde a descoberta e a finalidade até a exclusão controlada, incluindo réplicas, logs, backups e subprocessadores.",
    "LEGACY-IMG-067": "As evidências de segurança devem acompanhar o código desde o projeto até a compilação, implantação e execução.",
    "LEGACY-IMG-068": "Kubernetes gerenciado ainda requer controle do cliente sobre cargas, acesso, políticas, rede, dados e evidências.",
    "LEGACY-IMG-069": "Recursos de disponibilidade não comprovam que o serviço completo do cliente atende ao RTO e RPO.",
    "LEGACY-IMG-070": "Preserve com segurança os registros do provedor e de identidade antes que as evidências expirem ou as mudanças se propaguem.",
    "LEGACY-IMG-071": "Evidências automatizadas de configuração só se tornam garantia após avaliar escopo, confiabilidade, exceções e risco.",
    "LEGACY-IMG-072": "Laboratórios seguros e evidências rastreáveis transformam conceitos de nuvem em comprovação de portfólio.",
    "LEGACY-IMG-073": "O mesmo registro deve acompanhar o fornecedor desde a solicitação de negócio até a saída segura.",
    "LEGACY-IMG-074": "Use fatores documentados e permita escalonamento quando um fator for especialmente grave.",
    "LEGACY-IMG-075": "A pesquisa e as solicitações de evidências devem refletir a função e o risco reais do fornecedor.",
    "LEGACY-IMG-076": "As fontes de evidência se complementam; nenhum artefato responde a todas as perguntas.",
    "LEGACY-IMG-077": "Cláusulas contratuais só ajudam quando contatos e decisões são praticados.",
    "LEGACY-IMG-078": "Mapeie dependências materiais entre fornecedores, não apenas dentro de cada questionário.",
    "LEGACY-IMG-079": "Conecte o SBOM e as evidências de segurança à versão exata lançada e operada.",
    "LEGACY-IMG-080": "Comece pelo caso de uso permitido, dados, impacto, cadeia do modelo, avaliação e controle humano.",
    "LEGACY-IMG-081": "Toda conclusão deve ser rastreável desde os critérios exatos até o reteste.",
    "LEGACY-IMG-082": "Trabalho cuidadoso e limitações honestas constroem um portfólio e confiança profissional.",
}

engine.PALETTES.update(
    {
        "Cloud Security and Compliance": {
            "navy": "#123B5D",
            "accent": "#008D9F",
            "highlight": "#F2B134",
            "background": "#F3F8FB",
            "card_fills": ("#E2F3F5", "#E8EFF8", "#FFF3D6", "#E6F3EA", "#F2E8F6"),
            "text": "#172A3A",
        },
        "Third-Party Risk and Supply Chain Security": {
            "navy": "#3B2E5A",
            "accent": "#B4475A",
            "highlight": "#E99A3D",
            "background": "#FAF6F2",
            "card_fills": ("#F7E5E9", "#ECE8F6", "#FFF0D7", "#E7F2ED", "#E7EFF8"),
            "text": "#282038",
        },
    }
)


def main() -> None:
    data = json.loads(INVENTORY.read_text(encoding="utf-8"))
    records = [
        record
        for record in data["references"]
        if record.get("manual_family") in FAMILIES
        and record.get("primary_classification") == "requires_localization"
    ]
    if len(records) != EXPECTED_TOTAL:
        raise SystemExit(f"Expected {EXPECTED_TOTAL} records, found {len(records)}")

    records.sort(key=lambda item: (FAMILIES.index(item["manual_family"]), item["figure_number"]))
    manifest: list[dict] = []
    for record in records:
        slug = (
            "cloud-security"
            if record["manual_family"] == "Cloud Security and Compliance"
            else "third-party-risk"
        )
        destination = OUTPUT / f"pt-BR-{slug}-image{record['figure_number']}.png"
        localized_record = dict(record)
        localized_record["alt_text"] = REVIEW_TEXT[record["id"]]
        item = engine.draw_candidate(localized_record, destination)
        item["source_sha256"] = record["english_source_evidence"]["sha256"]
        item["source_container"] = record["english_source_evidence"]["container"]
        item["source_internal_path"] = record["english_source_evidence"]["internal_path"]
        item["markdown_file"] = record["markdown_file"]
        item["exact_image_path"] = record["exact_image_path"]
        item["localized_destination"] = record["localized_asset_path_checked"]
        item["language"] = record["language"]
        item["sha256"] = hashlib.sha256(destination.read_bytes()).hexdigest()
        manifest.append(item)

    if len({item["review_file"] for item in manifest}) != EXPECTED_TOTAL:
        raise SystemExit("Review paths are not unique")
    if len({item["localized_destination"] for item in manifest}) != EXPECTED_TOTAL:
        raise SystemExit("Localized destination paths are not unique")

    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    engine.create_review_sheet(
        manifest,
        "Cloud Security and Compliance",
        OUTPUT / "review-sheet-cloud-security.png",
    )
    engine.create_review_sheet(
        manifest,
        "Third-Party Risk and Supply Chain Security",
        OUTPUT / "review-sheet-third-party-risk.png",
    )

    for item in manifest:
        path = ROOT / item["review_file"]
        with Image.open(path) as image:
            image.verify()
        with Image.open(path) as image:
            if image.format != "PNG" or image.size != (item["width"], item["height"]):
                raise SystemExit(f"Review PNG validation failed: {path}")
    print(f"Generated and validated {len(manifest)} Batch 5 review-only figures.")


if __name__ == "__main__":
    main()
