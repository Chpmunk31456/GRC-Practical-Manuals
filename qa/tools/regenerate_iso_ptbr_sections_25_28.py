#!/usr/bin/env python3
from pathlib import Path
import re
P=Path('02-management-systems/ISO_IEC_27001_27002/Portugues_BR/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md')
HEAD=re.compile(r'^#\s+(\d+)\.\s+.+$',re.M)
S25='''# 25. Laboratório Fictício e Portfólio

*Um ambiente de prática segura com dados sintéticos e sistemas de laboratório autorizados.*

| **Regra do laboratório:** Use organização fictícia, dados sintéticos, sistemas isolados e apenas ferramentas que você está autorizado a operar. Não apresente um projeto de portfólio como certificação real ou auditoria de cliente. |
|---|

1. Crie uma empresa fictícia com dois produtos, um serviço em nuvem, força de trabalho remota e três fornecedores.
2. Produza análise de contexto, registro de partes interessadas, avaliação de relevância climática e declaração de escopo.
3. Defina critérios e um registro com dez cenários de risco, proprietários e decisões de tratamento.
4. Crie plano de tratamento e Declaração de Aplicabilidade cobrindo os 93 controles do Anexo A com justificativas e estado honesto.
5. Desenvolva políticas, procedimentos, objetivos, métricas, registros de ativos e fornecedores, treinamento, incidente e exercício de continuidade.
6. Use poucas ferramentas abertas em laboratório isolado e preserve escopo, configuração, resultados, validação, remediação e reteste.
7. Planeje e execute auditoria interna limitada contra cláusulas e controles selecionados.
8. Escreva duas não conformidades, análises de causa, ações corretivas e testes de eficácia.
9. Produza ata de análise crítica com entradas, decisões, responsáveis, recursos e prazos.
10. Publique apenas artefatos sanitizados e sintéticos, com declaração clara de limitações.

| **Artefato do portfólio** | **O que demonstra** |
|---|---|
| Contexto, partes e escopo | Raciocínio e limites da cláusula 4 |
| Método, registro e tratamento de risco | Cláusula 6 e propriedade do risco |
| Declaração de Aplicabilidade | Decisões de controle rastreáveis |
| Papel de trabalho de teste | Evidência, amostragem, exceção e conclusão |
| Pacote de auditoria interna | Programa, plano, critérios, relatório e acompanhamento |
| Ata de análise crítica | Avaliação e decisões da liderança |
| Registro de ação corretiva | Causa raiz e eficácia |
| Memorando de evidência técnica | Alfabetização técnica e limitações |
'''
S28='''# 28. Modelos, Glossário, Índice e Referências

*Estruturas reutilizáveis, termos importantes e pontos de partida autoritários.*

## 28.1 Registro mínimo de risco

| **Campo** | **Entrada** |
|---|---|
| ID do risco e proprietário | ____________________________ |
| Objetivo / ativo | ____________________________ |
| Evento de ameaça e condição | ____________________________ |
| Consequência | ____________________________ |
| Controles existentes | ____________________________ |
| Probabilidade e impacto | ____________________________ |
| Risco atual | ____________________________ |
| Tratamento e responsável pela ação | ____________________________ |
| Risco residual e aceitação | ____________________________ |
| Data de revisão | ____________________________ |

## 28.2 Papel de trabalho de teste de controle

| **Campo** | **Entrada** |
|---|---|
| Critérios e controle | ____________________________ |
| Escopo e período | ____________________________ |
| Proprietário e sistemas | ____________________________ |
| População e verificação de integridade | ____________________________ |
| Amostra e justificativa | ____________________________ |
| Procedimento executado | ____________________________ |
| Evidência inspecionada | ____________________________ |
| Exceções | ____________________________ |
| Conclusão e limitação | ____________________________ |
| Correção e reteste | ____________________________ |

## 28.3 Glossário

| **Termo** | **Significado** |
|---|---|
| Anexo A | Conjunto de referência de 93 controles de segurança da informação na ISO/IEC 27001:2022. |
| CIA | Confidencialidade, integridade e disponibilidade. |
| Conformidade | Atendimento a um requisito. |
| Controle | Medida que modifica ou mantém o risco. |
| Ação corretiva | Ação sobre a causa de uma não conformidade para evitar recorrência. |
| Informação documentada | Informação que a organização deve controlar, manter ou reter. |
| Parte interessada | Pessoa ou organização que pode afetar, ser afetada ou perceber-se afetada por decisão ou atividade. |
| SGSI | Sistema de gestão de segurança da informação. |
| Não conformidade | Falha no atendimento a um requisito. |
| Risco residual | Risco remanescente após o tratamento. |
| Proprietário do risco | Pessoa ou entidade responsável e autorizada a gerir um risco. |
| SoA | Declaração de Aplicabilidade. |
| Alta direção | Pessoa ou grupo que dirige e controla a organização no nível mais alto dentro do escopo. |

## 28.4 Índice de assuntos

| **Assunto** | **Capítulo** |
|---|---|
| Controles do Anexo A | 13–16 |
| Auditoria | 19 |
| Certificação | 21 |
| Emenda climática | 1, 2, 6, 21 |
| Ação corretiva | 12, 20 |
| Evidência | 5, 18 |
| Partes interessadas | 2, 6 |
| Analista júnior | 24–27 |
| Análise crítica pela direção | 11, 20 |
| Métricas | 11, 18 |
| Ferramentas abertas | 22 |
| Avaliação e tratamento de risco | 3, 8, 10 |
| Escopo | 2, 6 |
| Declaração de Aplicabilidade | 4 |
| Fornecedores | 13, 18, 23 |

## 28.5 Referências oficiais

[ISO/IEC 27001:2022 — visão geral](https://www.iso.org/standard/27001)

[ISO/IEC 27001:2022/Amd 1:2024](https://www.iso.org/standard/88435.html)

[ISO/IEC 27002:2022 — visão geral](https://www.iso.org/standard/75652.html)

[Comunicado ISO/IAF sobre mudança climática](https://iaf.nu/iaf_system/uploads/documents/Joint_ISO-IAF_Communique_re_Climate_Change_Amds_to_ISO_MSS_Feb_2024_Final.pdf)

[Visão geral de certificação da ISO](https://www.iso.org/certification.html)

[Família ISO/IEC 27000](https://www.iso.org/standard/iso-iec-27000-family)

| **Lembrete final:** Adquira ou acesse legalmente as normas oficiais antes da implementação ou avaliação. Confirme edições, emendas, acreditação, escopo de certificação, requisitos legais, contratos, tecnologia, ameaças e mudanças organizacionais. |
|---|
'''
text=P.read_text(encoding='utf-8')
for n,s in ((28,S28),(25,S25)):
 m=list(HEAD.finditer(text)); start=next((x for x in m if int(x.group(1))==n),None)
 if not start: raise SystemExit(f'missing section {n}')
 end=next((x.start() for x in m if x.start()>start.start()),len(text))
 text=text[:start.start()]+s.rstrip()+'\n\n'+text[end:]
for n in (25,28):
 m=list(HEAD.finditer(text)); start=next(x for x in m if int(x.group(1))==n); end=next((x.start() for x in m if x.start()>start.start()),len(text)); c=text[start.start():end]
 if sum(1 for line in c.splitlines() if line.count('|')>=2)<4: raise SystemExit(f'section {n} table validation failed')
P.write_text(text,encoding='utf-8')
print('Regenerated ISO PT-BR sections 25 and 28')
