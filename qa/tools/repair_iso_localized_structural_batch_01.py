#!/usr/bin/env python3
"""Apply exact, high-confidence structural repairs to ISO ES and PT-BR sources.

This batch intentionally avoids broad stylistic rewriting. Every exact replacement must
match once unless explicitly configured as a global token cleanup.
"""
from pathlib import Path
import re

ROOT = Path("02-management-systems/ISO_IEC_27001_27002")
ES = ROOT / "Espanol/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md"
PT = ROOT / "Portugues_BR/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected one exact match, found {count}")
    return text.replace(old, new, 1)


def repair_es(text: str) -> str:
    exact = [
        (
            'لimg src="media/image1.png" style="width:6.15in;height:3.39605in" alt="Context and risk drive planning, implementation, evaluation, and improvement." /',
            '![El contexto y el riesgo impulsan la planificación, la implementación, la evaluación y la mejora.](media/image1.png)',
            'ES image1 markup',
        ),
        (
            'El estilo "png"="width:6.15in;height:3.39605in" alt="Los dueños de Risk evalúan escenarios, tratamiento y riesgo residual utilizando criterios definidos".',
            '![Los propietarios de riesgos evalúan escenarios, tratamientos y riesgo residual mediante criterios definidos.](media/image2.png)',
            'ES image2 markup',
        ),
        ('# Publication and Use Notice', '# Aviso de publicación y uso', 'ES publication heading'),
        ('2. ISMS Scope and Interested Parties', '# 2. Alcance del SGSI y partes interesadas', 'ES section 2 heading'),
        ('# 1. ISO/IEC 27001 y 27002 Foundations', '# 1. Fundamentos de ISO/IEC 27001 y 27002', 'ES section 1 heading'),
        ('Contenido de la palabra:** Este documento contiene un campo de mesa de contenido de Word nativo y una guía de capítulo verificada. Después de editar, haga clic con el botón derecho en el contenido y elija el campo de actualización, luego actualice la tabla completa.',
         '| **Tabla de contenido de Word:** Este documento contiene un campo nativo de tabla de contenido de Word y una guía de capítulos verificada. Después de editar, haga clic con el botón derecho en la tabla de contenido, seleccione **Actualizar campo** y luego **Actualizar toda la tabla**. |',
         'ES Word TOC instruction'),
        ('- En el anexo A se enumeran 93 controles de referencia en cuatro temas: 37 orgánicos, 8 personas, 14 físicos y 34 tecnológicos.',
         '- En el Anexo A se enumeran 93 controles de referencia en cuatro temas: 37 organizativos, 8 relacionados con personas, 14 físicos y 34 tecnológicos.',
         'ES Annex A counts'),
        ('- Considerar si el cambio climático es relevante para la eficacia del SIV y si las partes interesadas tienen requisitos relacionados con el clima; documentar el razonamiento.',
         '- Considerar si el cambio climático es relevante para la eficacia del SGSI y si las partes interesadas tienen requisitos relacionados con el clima; documentar el razonamiento.',
         'ES SGSI climate line'),
    ]
    for old, new, label in exact:
        text = replace_once(text, old, new, label)

    text = re.sub(r'^\|\. \|\s*$', '', text, flags=re.MULTILINE)
    text = text.replace('Silencioso ', '').replace(' Silencioso', '')
    text = text.replace('tención ', '')
    text = text.replace('La vida eterna', '')
    return text


def repair_pt(text: str) -> str:
    exact = [
        ('2. Âmbito de aplicação do ISMS e partes interessadas', '# 2. Escopo do SGSI e partes interessadas', 'PT section 2 heading'),
        ('# 1. ISO/IEC 27001 e 27002 Fundações', '# 1. Fundamentos da ISO/IEC 27001 e 27002', 'PT section 1 heading'),
        ('[Quadro de conteúdos [4](#table-of-contents)](#table-of-contents)', '[Sumário [4](#table-of-contents)](#table-of-contents)', 'PT TOC label'),
        ('[28.2 Papel de ensaio de controlo [42](#control-test-workpaper)](#control-test-workpaper)', '[28.2 Papel de trabalho para teste de controle [42](#control-test-workpaper)](#control-test-workpaper)', 'PT workpaper label'),
        ('ISO/IEC 27001:2022/Amd 1:2024 □ Alterações da ação climática que afetam o contexto e a consideração de partes interessadas',
         'ISO/IEC 27001:2022/Amd 1:2024 □ Consideração das mudanças climáticas no contexto da organização e nos requisitos das partes interessadas',
         'PT climate amendment row'),
        ('Alteração O que desencadeia uma revisão do escopo? Mudar registros, aquisição e portas do produto',
         'Mudança O que desencadeia uma revisão do escopo? Registros de mudanças, aquisições e marcos de aprovação do produto',
         'PT scope-change row'),
    ]
    for old, new, label in exact:
        text = replace_once(text, old, new, label)

    # High-confidence Brazilian Portuguese terminology normalization.
    substitutions = {
        r'\bcontrolos\b': 'controles',
        r'\bControlos\b': 'Controles',
        r'\bselecção\b': 'seleção',
        r'\bSelecção\b': 'Seleção',
        r'\bobjectivo\b': 'objetivo',
        r'\bObjectivo\b': 'Objetivo',
        r'\bactivo\b': 'ativo',
        r'\bActivo\b': 'Ativo',
        r'\bregisto\b': 'registro',
        r'\bRegisto\b': 'Registro',
        r'\bplaneamento\b': 'planejamento',
        r'\bPlaneamento\b': 'Planejamento',
        r'\butilização\b': 'uso',
        r'\bUtilização\b': 'Uso',
    }
    for pattern, replacement in substitutions.items():
        text = re.sub(pattern, replacement, text)
    return text


def main() -> None:
    es_before = ES.read_text(encoding='utf-8')
    pt_before = PT.read_text(encoding='utf-8')
    es_after = repair_es(es_before)
    pt_after = repair_pt(pt_before)
    if es_after == es_before or pt_after == pt_before:
        raise SystemExit('Both localized sources must change in this batch.')
    ES.write_text(es_after, encoding='utf-8')
    PT.write_text(pt_after, encoding='utf-8')
    print('Applied ISO localized structural repair batch 01.')


if __name__ == '__main__':
    main()
