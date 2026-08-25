#!/usr/bin/env python3
"""Generate exact localized ISO/IEC 42001 Manual 02 learning graphics.

The SVG files are editable controlled sources. PNG derivatives are generated
separately for Markdown, Word, and PDF compatibility. Meaning is conveyed by
ordered labels and arrows, never by color alone.
"""

from __future__ import annotations

import html
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "02-management-systems" / "ISO_IEC_42001_AIMS" / "assets"
WIDTH = 1657
HEIGHT = 871
# Every card color provides at least 4.5:1 contrast against white text.
COLORS = ["#17324d", "#2f75b5", "#11777d", "#5b3f91", "#9e5700", "#27815f"]


FIGURES = {
    "es-419": [
        ([('PLANIFICAR', 'Contexto + riesgo'), ('HACER', 'Operar controles'), ('VERIFICAR', 'Medir + auditar'), ('ACTUAR', 'Corregir + mejorar')], 'El SGIA es un sistema de gestión vivo, no un proyecto de certificación de una sola vez.'),
        ([('ORGANIZACIÓN', 'Entidad'), ('USO', 'Función de IA'), ('SISTEMA', 'Límite'), ('DATOS', 'Flujo'), ('PARTES', 'Necesidades'), ('ALCANCE', 'Declaración')], 'Un alcance defendible conecta el control organizacional con los sistemas de IA y las obligaciones reales.'),
        ([('CRITERIOS', 'Método'), ('IDENTIFICAR', 'Escenario'), ('ANALIZAR', 'Probabilidad + impacto'), ('EVALUAR', 'Decisión'), ('TRATAR', 'Control'), ('REVISAR', 'Cambio')], 'La evaluación de riesgos de IA debe ser consistente, repetible y estar vinculada con decisiones.'),
        ([('PROPÓSITO', 'Uso'), ('PERSONAS', 'Afectadas'), ('EFECTO', 'Beneficio + daño'), ('CONTROL', 'Mitigaciones'), ('DECISIÓN', 'Aceptar / escalar'), ('MONITOREAR', 'Cambio')], 'La evaluación de impacto examina efectos sobre personas, grupos y sociedad durante todo el ciclo de vida.'),
        ([('CRITERIOS', 'Cláusula'), ('MUESTRA', 'Basada en riesgo'), ('EVIDENCIA', 'Trazable'), ('PRUEBA', 'Diseño + operación'), ('HALLAZGO', 'No conformidad'), ('SEGUIMIENTO', 'Acción correctiva')], 'Las conclusiones de auditoría del SGIA requieren criterios, evidencia, juicio y seguimiento.'),
        ([('NECESIDAD', 'Justificar'), ('DISEÑO', 'Requisitos'), ('CONSTRUIR', 'Trazar'), ('VERIFICAR', 'Umbrales'), ('DESPLEGAR', 'Aprobar'), ('OPERAR', 'Monitorear')], 'Los objetivos de IA responsable se convierten en requisitos medibles y evidencia de liberación.'),
        ([('ADQUIRIR', 'Derechos'), ('CATALOGAR', 'Responsable'), ('PREPARAR', 'Transformar'), ('VALIDAR', 'Calidad'), ('USAR', 'Propósito'), ('CONSERVAR', 'Eliminar')], 'La evidencia de datos debe preservar fuente, transformaciones, calidad, autoridad y ciclo de vida.'),
        ([('USUARIO', 'Instrucciones'), ('AFECTADO', 'Aviso + reparación'), ('CLIENTE', 'Deberes'), ('REGULADOR', 'Evidencia'), ('PÚBLICO', 'Transparencia')], 'Cada parte interesada necesita información útil, oportuna y adaptada a su función.'),
        ([('SELECCIONAR', 'Debida diligencia'), ('CONTRATAR', 'Asignar'), ('CONFIGURAR', 'Contexto del cliente'), ('MONITOREAR', 'Cambio'), ('INCIDENTE', 'Cooperar'), ('SALIDA', 'Eliminar + exportar')], 'El riesgo de IA de terceros persiste desde la selección hasta una salida verificada.'),
        ([('APRENDER', 'Cláusulas'), ('MAPEAR', 'SGIA'), ('PROBAR', 'Control'), ('REDACTAR', 'Hallazgo'), ('CORREGIR', 'Volver a probar'), ('DEMOSTRAR', 'Portafolio')], 'Los analistas junior demuestran competencia mediante trabajo práctico y trazable del SGIA.'),
    ],
    "pt-BR": [
        ([('PLANEJAR', 'Contexto + risco'), ('FAZER', 'Operar controles'), ('VERIFICAR', 'Medir + auditar'), ('AGIR', 'Corrigir + melhorar')], 'O SGIA é um sistema de gestão vivo, não um projeto de certificação executado uma única vez.'),
        ([('ORGANIZAÇÃO', 'Entidade'), ('USO', 'Papel de IA'), ('SISTEMA', 'Limite'), ('DADOS', 'Fluxo'), ('PARTES', 'Necessidades'), ('ESCOPO', 'Declaração')], 'Um escopo defensável conecta o controle organizacional aos sistemas de IA e às obrigações reais.'),
        ([('CRITÉRIOS', 'Método'), ('IDENTIFICAR', 'Cenário'), ('ANALISAR', 'Probabilidade + impacto'), ('AVALIAR', 'Decisão'), ('TRATAR', 'Controle'), ('REVISAR', 'Mudança')], 'A avaliação de riscos de IA deve ser consistente, repetível e vinculada a decisões.'),
        ([('FINALIDADE', 'Uso'), ('PESSOAS', 'Afetadas'), ('EFEITO', 'Benefício + dano'), ('CONTROLE', 'Mitigações'), ('DECISÃO', 'Aceitar / escalonar'), ('MONITORAR', 'Mudança')], 'A avaliação de impacto examina efeitos sobre pessoas, grupos e sociedade durante todo o ciclo de vida.'),
        ([('CRITÉRIOS', 'Cláusula'), ('AMOSTRA', 'Baseada em risco'), ('EVIDÊNCIA', 'Rastreável'), ('TESTE', 'Desenho + operação'), ('CONSTATAÇÃO', 'Não conformidade'), ('ACOMPANHAR', 'Ação corretiva')], 'As conclusões de auditoria do SGIA exigem critérios, evidências, julgamento e acompanhamento.'),
        ([('NECESSIDADE', 'Justificar'), ('PROJETO', 'Requisitos'), ('CONSTRUIR', 'Rastrear'), ('VERIFICAR', 'Limites'), ('IMPLANTAR', 'Aprovar'), ('OPERAR', 'Monitorar')], 'Objetivos de IA responsável tornam-se requisitos mensuráveis e evidências de liberação.'),
        ([('ADQUIRIR', 'Direitos'), ('CATALOGAR', 'Responsável'), ('PREPARAR', 'Transformar'), ('VALIDAR', 'Qualidade'), ('USAR', 'Finalidade'), ('PRESERVAR', 'Excluir')], 'A evidência de dados deve preservar fonte, transformações, qualidade, autoridade e ciclo de vida.'),
        ([('USUÁRIO', 'Instruções'), ('AFETADO', 'Aviso + reparação'), ('CLIENTE', 'Deveres'), ('REGULADOR', 'Evidência'), ('PÚBLICO', 'Transparência')], 'Cada parte interessada precisa de informação útil, oportuna e adaptada ao seu papel.'),
        ([('SELECIONAR', 'Diligência prévia'), ('CONTRATAR', 'Alocar'), ('CONFIGURAR', 'Contexto do cliente'), ('MONITORAR', 'Mudança'), ('INCIDENTE', 'Cooperar'), ('SAÍDA', 'Excluir + exportar')], 'O risco de IA de terceiros persiste desde a seleção até uma saída verificada.'),
        ([('APRENDER', 'Cláusulas'), ('MAPEAR', 'SGIA'), ('TESTAR', 'Controle'), ('REDIGIR', 'Constatação'), ('CORRIGIR', 'Retestar'), ('DEMONSTRAR', 'Portfólio')], 'Analistas juniores demonstram competência por meio de trabalho prático e rastreável no SGIA.'),
    ],
}


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def svg_for(language: str, number: int, steps: list[tuple[str, str]], statement: str) -> str:
    count = len(steps)
    gap = 16
    margin = 80
    card_width = min(235, (WIDTH - 2 * margin - gap * (count - 1)) // count)
    total = card_width * count + gap * (count - 1)
    start_x = (WIDTH - total) // 2
    card_y = 250
    card_h = 195
    pieces = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{esc(statement)}</title>',
        f'<desc id="desc">{esc("; ".join(f"{i + 1}. {a}: {b}" for i, (a, b) in enumerate(steps)))}</desc>',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
    ]
    for index, (heading, subtitle) in enumerate(steps):
        x = start_x + index * (card_width + gap)
        color = COLORS[index % len(COLORS)]
        pieces.extend([
            f'<rect x="{x}" y="{card_y}" width="{card_width}" height="{card_h}" rx="16" fill="{color}" stroke="#10253b" stroke-width="3"/>',
            f'<circle cx="{x + 28}" cy="{card_y + 30}" r="18" fill="#ffffff" stroke="#10253b" stroke-width="2"/>',
            f'<text x="{x + 28}" y="{card_y + 37}" text-anchor="middle" font-family="DejaVu Sans, Arial, sans-serif" font-size="20" font-weight="700" fill="#10253b">{index + 1}</text>',
            f'<text x="{x + card_width / 2}" y="{card_y + 92}" text-anchor="middle" font-family="DejaVu Sans, Arial, sans-serif" font-size="25" font-weight="700" fill="#ffffff">{esc(heading)}</text>',
            f'<text x="{x + card_width / 2}" y="{card_y + 137}" text-anchor="middle" font-family="DejaVu Sans, Arial, sans-serif" font-size="19" fill="#ffffff">{esc(subtitle)}</text>',
        ])
        if index < count - 1:
            arrow_x = x + card_width + 3
            next_x = x + card_width + gap - 3
            pieces.extend([
                f'<line x1="{arrow_x}" y1="{card_y + card_h / 2}" x2="{next_x}" y2="{card_y + card_h / 2}" stroke="#10253b" stroke-width="4"/>',
                f'<polygon points="{next_x},{card_y + card_h / 2} {next_x - 11},{card_y + card_h / 2 - 8} {next_x - 11},{card_y + card_h / 2 + 8}" fill="#10253b"/>',
            ])
    statement_lines = textwrap.wrap(
        statement,
        width=82,
        break_long_words=False,
        break_on_hyphens=False,
    )
    statement_y = 570 if len(statement_lines) > 1 else 590
    statement_tspans = "".join(
        f'<tspan x="{WIDTH / 2}" dy="{0 if line_index == 0 else 40}">{esc(line)}</tspan>'
        for line_index, line in enumerate(statement_lines)
    )
    pieces.extend([
        f'<text x="{WIDTH / 2}" y="{statement_y}" text-anchor="middle" font-family="DejaVu Sans, Arial, sans-serif" font-size="29" font-weight="700" fill="#17324d">{statement_tspans}</text>',
        f'<text x="{WIDTH / 2}" y="790" text-anchor="middle" font-family="DejaVu Sans, Arial, sans-serif" font-size="16" fill="#526777">ISO/IEC 42001 Manual 02 · {esc(language)} · Figura {number}</text>',
        '</svg>',
    ])
    return "\n".join(pieces) + "\n"


def main() -> None:
    for language, figures in FIGURES.items():
        target = ASSETS / language / "media"
        target.mkdir(parents=True, exist_ok=True)
        for number, (steps, statement) in enumerate(figures, start=1):
            (target / f"image{number}.svg").write_text(
                svg_for(language, number, steps, statement), encoding="utf-8"
            )
    print("Generated 20 localized SVG source graphics")


if __name__ == "__main__":
    main()
