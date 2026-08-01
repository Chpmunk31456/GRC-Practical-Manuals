#!/usr/bin/env python3
"""Reconstruct ISO PT-BR sections 17-21 from approved structure.

This bounded repair restores content and Markdown tables that were flattened in the
Portuguese source. It uses original paraphrases and does not reproduce normative ISO
text. The script fails closed unless all expected section boundaries are present.
"""
from pathlib import Path
import re

P = Path('02-management-systems/ISO_IEC_27001_27002/Portugues_BR/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md')
HEAD = re.compile(r'^#\s+(\d+)\.\s+.+$', re.M)

SECTIONS = {
17: '''# 17. Implementação de Controles com a ISO/IEC 27002

*Como transformar decisões de risco em controles adequados à organização.*

1. Comece pela decisão de tratamento de risco, pela obrigação aplicável e pelo resultado esperado — não por uma ferramenta.

2. Use as orientações da ISO/IEC 27002 e seus atributos relevantes para compreender a finalidade, as considerações de implementação e as relações entre controles.

3. Adapte o controle às pessoas, aos processos, à tecnologia, ao ambiente físico, às restrições legais e às operações do negócio.

4. Defina proprietário, escopo, gatilho, entradas, etapas, saídas, registros, frequência, dependências, exceções e escalonamento.

5. Avalie se o desenho do controle pode alcançar razoavelmente o resultado pretendido.

6. Implemente por meio de mudança controlada e treine as pessoas afetadas.

7. Meça a operação e a eficácia, investigue exceções e melhore o controle.

8. Atualize riscos, plano de tratamento, Declaração de Aplicabilidade, procedimentos e evidências quando o controle mudar.

| **Distinção importante:** A ISO/IEC 27002 fornece orientação. A organização continua responsável por selecionar e desenhar controles que tratem seus riscos e atendam aos requisitos aplicáveis. |
|---|
''',
18: '''# 18. Métricas e Testes de Controle

*Como verificar se o SGSI e seus controles funcionam.*

| **Área** | **População e amostra** | **Teste** | **Evidência** |
|---|---|---|---|
| Risco | Todos os riscos atuais; amostra de itens altos, alterados, aceitos e vencidos | Reexecutar a pontuação, rastrear o tratamento e confirmar aprovação e revisão pelo proprietário | Método, registro, aprovações, tratamento e risco residual |
| Acesso | Todas as identidades de funcionários, privilegiadas, de serviço e de terceiros | Testar necessidade, aprovação, MFA, revisão, alteração, inatividade e desligamento | Populações, exportações, tickets, configurações e logs |
| Vulnerabilidades | Todos os ativos e achados | Validar cobertura, priorização, exceções, prazos, correção e nova varredura | Inventário, varreduras, tickets, aprovações e retestes |
| Fornecedores | População completa de fornecedores; amostra de serviços críticos e alterados | Testar diligência, acordo, responsabilidades, monitoramento, incidente e saída | Inventário, avaliação, contrato, revisão e prova de encerramento |
| Incidentes | Todos os eventos e incidentes relatados | Testar classificação, resposta, evidências, comunicações, recuperação e aprendizado | Casos, cronologia, decisões, registro de evidências e lições |
| Continuidade | Processos críticos e TIC de suporte | Rastrear necessidades do negócio até o desenho de recuperação e os exercícios | BIA, planos, registros de testes, lacunas e retestes |
| Objetivos | Todos os objetivos e medidas do SGSI | Verificar definição, qualidade dos dados, tendência, meta, análise, decisão e ação | Definições de métricas, dados-fonte, painéis, atas e ações |

- Defina critérios, escopo, período, população, controle, proprietário, evidência e resultado esperado.
- Avalie o desenho antes de testar a operação.
- Obtenha a população completa e valide sua integridade e exatidão de forma independente.
- Selecione uma amostra baseada em risco que cubra datas, proprietários, locais, falhas, exceções e mudanças relevantes.
- Inspecione registros, observe o trabalho, entreviste pessoas, examine configurações e reexecute procedimentos quando viável.
- Documente exceções como fatos vinculados aos critérios; não exagere nem oculte limitações.
- Atribua correção, análise de causa raiz, proprietário, prazo, proteção provisória e escalonamento.
- Reteste e declare a conclusão final e qualquer limitação remanescente.
''',
19: '''# 19. Auditoria Interna

*Uma avaliação independente da conformidade e da implementação eficaz.*

Mantenha um programa de auditoria que considere importância dos processos, mudanças, riscos e resultados anteriores.

Defina objetivo, escopo, critérios, momento, método, amostragem, registros e comunicação para cada auditoria.

Selecione auditores competentes e suficientemente objetivos; auditores não devem auditar o próprio trabalho sem salvaguardas.

Use a norma licenciada, requisitos organizacionais, decisões de risco, Declaração de Aplicabilidade, políticas e obrigações aplicáveis como critérios.

Registre evidências e achados com clareza suficiente para que outra pessoa competente compreenda sua base.

Comunique os resultados à gestão relevante e acompanhe correções e ações corretivas até a verificação de eficácia.

| **Tipo de achado** | **Significado** | **Resposta exigida** |
|---|---|---|
| Conformidade | A evidência sustenta os critérios | Manter e monitorar |
| Oportunidade de melhoria | Sugestão útil que não encobre uma não conformidade | Avaliar voluntariamente e registrar a decisão |
| Não conformidade | Um ou mais requisitos não foram atendidos | Corrigir, analisar a causa, prevenir recorrência e verificar eficácia |
| Limitação da auditoria | Escopo, evidência, tempo, independência ou acesso restringiram a conclusão | Divulgar claramente e resolver quando possível |
''',
20: '''# 20. Análise Crítica pela Direção e Ação Corretiva

*Decisões de liderança que mantêm o SGSI adequado e eficaz.*

| **Entrada da análise crítica** | **Perguntas** |
|---|---|
| Ações anteriores | As decisões anteriores foram concluídas e eficazes? |
| Contexto e partes interessadas | O que mudou, incluindo relevância climática e necessidades das partes interessadas? |
| Desempenho | O que mostram métricas, objetivos, incidentes, auditorias e não conformidades? |
| Retorno das partes interessadas | O que relatam clientes, reguladores, trabalhadores, fornecedores e proprietários? |
| Risco e tratamento | Níveis de risco, aceitação, tratamento, recursos e Declaração de Aplicabilidade continuam adequados? |
| Oportunidades de melhoria | Quais mudanças a liderança deve aprovar? |

- Contenha ou corrija o problema imediato.
- Determine a extensão e se existem falhas semelhantes em outros locais.
- Analise a causa raiz com evidências, sem atribuição simplista de culpa.
- Planeje ações proporcionais ao efeito e ao risco de recorrência.
- Implemente mudanças com proprietário e prazo definidos.
- Verifique a eficácia com evidências definidas após tempo suficiente de operação.
- Atualize riscos, controles, documentos, treinamento, objetivos e Declaração de Aplicabilidade quando necessário.
''',
21: '''# 21. Preparação para Certificação

*O que a certificação faz, como normalmente ocorre e o que ela não garante.*

![A preparação é seguida pela avaliação de certificação e por atividades contínuas de supervisão e renovação.](media/image8.png)

Figura 8. Caminho para certificação

A certificação é opcional; organizações podem implementar a ISO/IEC 27001 sem buscar um certificado.

A ISO não realiza certificações. Um organismo de certificação independente conduz as auditorias de certificação.

A acreditação oferece confiança adicional na competência de um organismo de certificação; verifique o escopo relevante da acreditação e do certificado.

A Fase 1 normalmente avalia prontidão, escopo, sistema documentado e preparação para a auditoria de implementação.

A Fase 2 avalia implementação e eficácia em todo o escopo definido.

Atividades de supervisão e recertificação avaliam a conformidade contínua; confirme os detalhes com o organismo de certificação selecionado e as regras de acreditação.

Um certificado tem escopo e prazo definidos. Ele não prova que todo produto é seguro, que nenhum incidente ocorrerá ou que todos os sistemas da empresa estão incluídos.

| **Área de prontidão** | **Critério de aceitação** |
|---|---|
| Escopo | Claro, defensável e refletido nas operações reais e na intenção do certificado |
| Risco | Método usado de forma consistente; registro completo; proprietários aceitam o risco residual |
| Declaração de Aplicabilidade | Todos os controles do Anexo A abordados; seleções, exclusões e status sustentados |
| Controles | Implementados, operados por tempo suficiente para gerar evidência confiável e medidos |
| Auditoria interna | Programa e auditoria de escopo completo concluídos com evidência objetiva e acompanhamento |
| Análise crítica pela direção | Entradas exigidas consideradas e decisões registradas |
| Ação corretiva | Não conformidades corrigidas; causa e eficácia tratadas |
| Emenda | Relevância climática e requisitos das partes interessadas considerados e evidenciados |
'''
}

text = P.read_text(encoding='utf-8')
matches = list(HEAD.finditer(text))
for number in SECTIONS:
    if not any(int(m.group(1)) == number for m in matches):
        raise SystemExit(f'missing section {number}')

for number in sorted(SECTIONS, reverse=True):
    matches = list(HEAD.finditer(text))
    start_match = next(m for m in matches if int(m.group(1)) == number)
    end = next((m.start() for m in matches if m.start() > start_match.start()), len(text))
    text = text[:start_match.start()] + SECTIONS[number].rstrip() + '\n\n' + text[end:]

for number in SECTIONS:
    matches = list(HEAD.finditer(text))
    start_match = next(m for m in matches if int(m.group(1)) == number)
    end = next((m.start() for m in matches if m.start() > start_match.start()), len(text))
    chunk = text[start_match.start():end]
    if number in {18, 19, 20, 21} and sum(1 for line in chunk.splitlines() if line.startswith('|')) < 4:
        raise SystemExit(f'section {number} table validation failed')
    if number == 17 and 'Distinção importante' not in chunk:
        raise SystemExit('section 17 validation failed')

P.write_text(text, encoding='utf-8')
print('Regenerated ISO PT-BR sections 17-21')
