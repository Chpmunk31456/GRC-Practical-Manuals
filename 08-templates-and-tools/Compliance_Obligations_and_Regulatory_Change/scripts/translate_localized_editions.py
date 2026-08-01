#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path
from argostranslate import translate

ROOT = Path(__file__).resolve().parents[1]
EN = ROOT / 'English/Compliance_Obligations_and_Regulatory_Change_Toolkit_English_v1.0.md'
CONFIG = {
    'es-419': {
        'code': 'es',
        'title': 'Kit de Registro de Obligaciones de Cumplimiento y Gestion del Cambio Regulatorio',
        'file': 'Kit_Registro_Obligaciones_Cumplimiento_y_Cambio_Regulatorio_es-419_v1.0.md',
        'status': 'Candidato de publicacion con traduccion asistida por maquina',
    },
    'pt-BR': {
        'code': 'pt',
        'title': 'Kit de Registro de Obrigacoes de Conformidade e Gestao de Mudancas Regulatorias',
        'file': 'Kit_Registro_Obrigacoes_Conformidade_e_Mudancas_Regulatorias_pt-BR_v1.0.md',
        'status': 'Candidato a publicacao com traducao assistida por maquina',
    },
}
TOKEN_RE = re.compile(r'(`[^`]+`|https?://\S+|\b(?:ISO|NIST|GDPR|HIPAA|PCI DSS|EUR-Lex|SUIN-Juriscol)\b|\b\d{1,4}(?:[./-]\d{1,2}){1,2}\b)')


def protect(text: str):
    values = []
    def repl(m):
        values.append(m.group(0))
        return f'ZXQ{len(values)-1:04d}QXZ'
    return TOKEN_RE.sub(repl, text), values


def restore(text: str, values):
    for i, value in enumerate(values):
        text = text.replace(f'ZXQ{i:04d}QXZ', value)
    return text


def translate_line(line: str, target: str) -> str:
    if not line.strip() or line.strip() == '\\newpage' or line.startswith('---'):
        return line
    prefix = ''
    content = line
    m = re.match(r'^(#{1,6}\s+|>\s*|[-*]\s+|\d+\.\s+)', line)
    if m:
        prefix = m.group(1)
        content = line[len(prefix):]
    protected, values = protect(content)
    translated = translate.translate(protected, 'en', target)
    return prefix + restore(translated, values)


def body_without_yaml(text: str) -> str:
    if text.startswith('---\n'):
        _, rest = text.split('---\n', 1)
        _, body = rest.split('---\n', 1)
        return body.lstrip()
    return text


def main():
    if not EN.is_file():
        raise SystemExit(f'Missing committed English master: {EN}')
    english = EN.read_text(encoding='utf-8')
    body = body_without_yaml(english)
    for locale, cfg in CONFIG.items():
        outdir = ROOT / 'translations' / locale
        outdir.mkdir(parents=True, exist_ok=True)
        translated = '\n'.join(translate_line(line, cfg['code']) for line in body.splitlines()) + '\n'
        header = f'''---
title: "{cfg['title']}"
author: "Alberto Al Leiva"
date: "1 August 2026"
lang: {locale}
subject: "GRC, obligaciones de cumplimiento, cambio regulatorio, gobernanza y evidencia"
rights: "CC BY-NC-SA 4.0 salvo que un archivo indique lo contrario"
status: "{cfg['status']}"
---

'''
        output = outdir / cfg['file']
        output.write_text(header + translated, encoding='utf-8')
        print(output)


if __name__ == '__main__':
    main()
