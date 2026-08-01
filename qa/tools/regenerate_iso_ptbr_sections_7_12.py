#!/usr/bin/env python3
"""Regenerate ISO/IEC 27001/27002 PT-BR sections 7-12 from controlled source meaning."""
from pathlib import Path
import re

P = Path('02-management-systems/ISO_IEC_27001_27002/Portugues_BR/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md')
text = P.read_text(encoding='utf-8')
HEAD = re.compile(r'^#\s+(\d+)\.\s+.+$', re.M)


def replace_section(src: str, number: int, replacement: str) -> str:
    matches = list(HEAD.finditer(src))
    start = next((m.start() for m in matches if int(m.group(1)) == number), None)
    if start is None:
        raise SystemExit(f'missing section {number}')
    end = next((m.start() for m in matches if m.start() > start), len(src))
    return src[:start] + replacement.rstrip() + '\n\n' + src[end:]

COMMON_FOCUS = 'Confirmar responsabilidade, escopo, método, aprovação, evidência operacional, exceções, correção e registros retidos.'
COMMON_EVIDENCE = 'Políticas, registros, planos, atas, resultados, aprovações e evidências de acompanhamento.'

sections = {
7: f'''# 7. Cláusula 5 — Liderança

*Requisitos em linguagem clara, foco de verificação e exemplos de evidências.*

| **Finalidade da cláusula:** Liderança |
|---|

| **Cláusula** | **Significado em linguagem clara** | **Foco de verificação** | **Exemplo de evidência** |
|---|---|---|---|
| 5.1 | A alta direção demonstra comprometimento, integra o SGSI aos processos de negócio, fornece recursos e apoia a melhoria. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |
| 5.2 | Estabelecer, comunicar e manter uma política de segurança da informação adequada à organização. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |
| 5.3 | Atribuir e comunicar responsabilidades de segurança da informação e autoridade para reporte. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |

Use o texto oficial licenciado da ISO/IEC 27001 para consultar os requisitos normativos exatos. Este manual apresenta paráfrases para fins educacionais e não substitui a norma.''',
8: f'''# 8. Cláusula 6 — Planejamento

*Requisitos em linguagem clara, foco de verificação e exemplos de evidências.*

| **Finalidade da cláusula:** Planejamento |
|---|

| **Cláusula** | **Significado em linguagem clara** | **Foco de verificação** | **Exemplo de evidência** |
|---|---|---|---|
| 6.1.1 | Determinar riscos e oportunidades no nível do SGSI, planejar ações, integrá-las aos processos do SGSI e avaliar sua eficácia. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |
| 6.1.2 | Definir e aplicar critérios consistentes de risco de segurança da informação e métodos de avaliação; identificar responsáveis e analisar e avaliar os riscos. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |
| 6.1.3 | Escolher opções e controles de tratamento de riscos, compará-los ao Anexo A, produzir a Declaração de Aplicabilidade e o plano de tratamento e obter aprovação do responsável pelo risco. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |
| 6.2 | Definir objetivos mensuráveis de segurança com responsáveis, recursos, datas e métodos de avaliação. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |
| 6.3 | Planejar mudanças no SGSI considerando finalidade, consequências, recursos, responsabilidades e integridade do sistema. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |

Use o texto oficial licenciado da ISO/IEC 27001 para consultar os requisitos normativos exatos. Este manual apresenta paráfrases para fins educacionais e não substitui a norma.''',
9: f'''# 9. Cláusula 7 — Apoio

*Requisitos em linguagem clara, foco de verificação e exemplos de evidências.*

| **Finalidade da cláusula:** Apoio |
|---|

| **Cláusula** | **Significado em linguagem clara** | **Foco de verificação** | **Exemplo de evidência** |
|---|---|---|---|
| 7.1 | Fornecer pessoas, orçamento, tecnologia e outros recursos necessários ao SGSI. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |
| 7.2 | Definir necessidades de competência, tratar lacunas, avaliar resultados e manter evidências. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |
| 7.3 | Assegurar que as pessoas compreendam a política, sua contribuição e as consequências da não conformidade. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |
| 7.4 | Planejar o que, quando, com quem e como a organização se comunica interna e externamente. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |
| 7.5 | Criar, aprovar, identificar, proteger, distribuir, reter e controlar as informações documentadas necessárias. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |

Use o texto oficial licenciado da ISO/IEC 27001 para consultar os requisitos normativos exatos. Este manual apresenta paráfrases para fins educacionais e não substitui a norma.''',
10: f'''# 10. Cláusula 8 — Operação

*Requisitos em linguagem clara, foco de verificação e exemplos de evidências.*

| **Finalidade da cláusula:** Operação |
|---|

| **Cláusula** | **Significado em linguagem clara** | **Foco de verificação** | **Exemplo de evidência** |
|---|---|---|---|
| 8.1 | Planejar e controlar processos do SGSI, critérios, mudanças, trabalho terceirizado e evidências da operação adequada. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |
| 8.2 | Realizar avaliações de riscos de segurança da informação em intervalos planejados e quando ocorrerem mudanças significativas. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |
| 8.3 | Implementar o plano de tratamento de riscos e manter evidências dos resultados. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |

Use o texto oficial licenciado da ISO/IEC 27001 para consultar os requisitos normativos exatos. Este manual apresenta paráfrases para fins educacionais e não substitui a norma.''',
11: f'''# 11. Cláusula 9 — Avaliação de desempenho

*Requisitos em linguagem clara, foco de verificação e exemplos de evidências.*

| **Finalidade da cláusula:** Avaliação de desempenho |
|---|

| **Cláusula** | **Significado em linguagem clara** | **Foco de verificação** | **Exemplo de evidência** |
|---|---|---|---|
| 9.1 | Definir o que monitorar e medir, como e quando fazê-lo, quem avalia e como os resultados são retidos e analisados. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |
| 9.2.1 | Realizar auditorias internas em intervalos planejados para avaliar a conformidade com os requisitos organizacionais e da ISO/IEC 27001 e a eficácia da implementação. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |
| 9.2.2 | Manter um programa de auditoria com frequência, métodos, responsabilidades, planejamento, reporte, escopo, critérios, auditores objetivos, resultados retidos e ação corretiva tempestiva. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |
| 9.3.1 | A alta direção analisa o SGSI em intervalos planejados quanto à adequação, suficiência e eficácia contínuas. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |
| 9.3.2 | Analisar entradas obrigatórias, como ações anteriores, mudanças de contexto, necessidades das partes interessadas, desempenho, feedback, riscos, tratamento e oportunidades de melhoria. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |
| 9.3.3 | Registrar decisões da análise crítica da direção sobre melhorias e mudanças necessárias no SGSI. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |

Use o texto oficial licenciado da ISO/IEC 27001 para consultar os requisitos normativos exatos. Este manual apresenta paráfrases para fins educacionais e não substitui a norma.

<img src="media/image5.png" style="width:6.15in;height:3.32973in" alt="Um programa de auditoria considera riscos, independência, evidências, reporte e acompanhamento verificado." />

Figura 5. Fluxo de trabalho da auditoria interna''',
12: f'''# 12. Cláusula 10 — Melhoria

*Requisitos em linguagem clara, foco de verificação e exemplos de evidências.*

| **Finalidade da cláusula:** Melhoria |
|---|

| **Cláusula** | **Significado em linguagem clara** | **Foco de verificação** | **Exemplo de evidência** |
|---|---|---|---|
| 10.1 | Melhorar continuamente a adequação, suficiência e eficácia do SGSI. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |
| 10.2 | Reagir às não conformidades, corrigi-las, analisar causas, prevenir recorrência, verificar a eficácia e manter evidências. | {COMMON_FOCUS} | {COMMON_EVIDENCE} |

Use o texto oficial licenciado da ISO/IEC 27001 para consultar os requisitos normativos exatos. Este manual apresenta paráfrases para fins educacionais e não substitui a norma.

<img src="media/image6.png" style="width:6.15in;height:3.27166in" alt="Os 93 controles de referência estão agrupados em temas organizacionais, de pessoas, físicos e tecnológicos." />

Figura 6. Temas dos controles do Anexo A''',
}

for number, section in sections.items():
    text = replace_section(text, number, section)

for number in sections:
    if len(re.findall(rf'^# {number}\. ', text, re.M)) != 1:
        raise SystemExit(f'heading validation failed for section {number}')

P.write_text(text, encoding='utf-8')
print('Regenerated ISO PT-BR sections 7-12')
