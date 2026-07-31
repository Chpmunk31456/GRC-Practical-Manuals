# 27. Laboratório fictício e portfólio

*Um exercício autorizado para demonstrar inventário, medição, correção e reteste sem expor dados reais.*

## 27.1 Cenário

Crie uma organização fictícia de 50 pessoas com laptops, servidores, serviços em nuvem, uma aplicação web, trabalho remoto e cinco prestadores de serviços. Use somente dados sintéticos, ativos de laboratório e sistemas para os quais exista autorização explícita.

## 27.2 Etapas do laboratório

1. Selecione o IG1 e documente três acréscimos baseados em risco provenientes do IG2 ou IG3.
2. Construa inventários de ativos empresariais, software, dados, contas, sistemas de autenticação, redes, prestadores de serviços, aplicações e fontes de logs.
3. Utilize Nmap e osquery em um ambiente isolado para reconciliar inventários de ativos e software.
4. Utilize OpenSCAP ou Lynis em um host de laboratório e registre achados de configuração, exceções, correções e nova avaliação.
5. Utilize Greenbone em alvos aprovados; valide cobertura, achados, remediação e nova varredura.
6. Utilize Wazuh ou Suricata para gerar e investigar um alerta de teste seguro.
7. Utilize Trivy ou ZAP em um repositório de treinamento ou aplicação de laboratório; registre correção e reteste.
8. Execute um teste documentado de restauração de backup e um exercício de mesa de resposta a incidentes.
9. Crie cinco papéis de trabalho alinhados à CIS Controls Assessment Specification, incluindo entradas, operações, medidas, métricas, exceções e conclusões.
10. Publique somente artefatos higienizados e declare claramente que o projeto é fictício e não constitui uma avaliação formal do CIS.

## 27.3 Artefatos de portfólio

| Artefato | Evidência demonstrada |
|---|---|
| Memorando de seleção do IG | Priorização, contexto e raciocínio de risco. |
| Inventários reconciliados | Completude, propriedade, fonte, data e exceções. |
| Papel de trabalho de Salvaguarda | Estrutura oficial de medição e conclusão sustentada. |
| Registro de achados | Severidade, responsável, prazo, correção e reteste. |
| Relatório de exercício | Cenário, decisões, lacunas e ações de melhoria. |
| Resumo executivo | Risco, cobertura, limitações e decisões necessárias. |

# 28. Plano de aprendizagem de trinta dias

*Uma sequência prática para compreender a estrutura, produzir evidências e explicar resultados.*

| Dias | Foco | Entregável |
|---|---|---|
| 1–4 | Estrutura dos 18 Controles, 153 Salvaguardas, IGs, classes de ativos e funções de segurança. | Mapa de conceitos e seleção preliminar de IG. |
| 5–8 | Inventários, escopo, responsáveis, exceções e dependências. | Inventários sintéticos e matriz RACI. |
| 9–12 | Configurações seguras, vulnerabilidades, identidades e proteção de dados. | Dois papéis de trabalho e um registro de achados. |
| 13–16 | Logs, monitoramento, malware, e-mail e segurança de rede. | Caso de alerta investigado e evidências de cobertura. |
| 17–20 | Backup, resposta a incidentes, prestadores e desenvolvimento seguro. | Teste de restauração e exercício de mesa. |
| 21–24 | CIS Controls Assessment Specification. | Cinco avaliações de Salvaguardas com medidas e métricas. |
| 25–27 | Correção, reteste, relatórios e comunicação executiva. | Plano de ação e resumo executivo. |
| 28–30 | Revisão técnica, portfólio e preparação para entrevistas. | Portfólio higienizado e respostas praticadas. |

# 29. Preparação para entrevistas

## 29.1 Como explicar os CIS Controls

Os CIS Controls são um conjunto priorizado de boas práticas de cibersegurança organizado em 18 Controles e 153 Salvaguardas. Eles ajudam a transformar objetivos defensivos em ações atribuíveis e mensuráveis, priorizadas pelos Grupos de Implementação.

## 29.2 O que é o IG1?

O IG1 contém 56 Salvaguardas e representa a higiene cibernética essencial. É o ponto de partida recomendado, mas a organização deve acrescentar Salvaguardas quando risco, obrigações, dados, serviços ou ameaças exigirem proteção adicional.

## 29.3 O IG1 atende a todos os requisitos?

Não. Um Grupo de Implementação é um mecanismo de priorização, não uma autorização para ignorar leis, contratos, requisitos setoriais ou riscos materiais.

## 29.4 Como medir uma Salvaguarda?

Defina a população aplicável, valide as entradas, execute operações repetíveis, produza medidas, calcule métricas, examine exceções e revise o procedimento. Preserve a evidência que sustenta a conclusão.

## 29.5 Qual é a diferença entre ferramenta e controle?

Uma ferramenta pode apoiar uma Salvaguarda, mas não substitui escopo, processo, responsáveis, configuração, tratamento de exceções, medição, revisão humana ou melhoria contínua.

## 29.6 Como tratar uma exceção?

Documente o ativo ou população afetada, justificativa, risco, controles compensatórios, responsável, aprovação, prazo e critério de revisão. Exceções não devem desaparecer dentro de uma porcentagem agregada.

## 29.7 Como apresentar um achado?

Explique o critério, a condição observada, a população afetada, o risco, a causa provável, a recomendação, o responsável, o prazo e o método de reteste.

## 29.8 Como evitar alegações excessivas?

Diferencie implementação, desenho, operação, teste e conformidade. Declare escopo, período, limitações, fontes e dependências. Um mapeamento ou uma ferramenta não comprova automaticamente conformidade.

## 29.9 Perguntas para fazer ao empregador

- Qual Grupo de Implementação foi selecionado e como a decisão é revista?
- Quais inventários são fontes oficiais e como a completude é conciliada?
- Como as exceções são aprovadas, monitoradas e encerradas?
- Quais Salvaguardas apresentam maior exposição residual?
- Como são realizados retestes e exercícios de recuperação?
- Como prestadores de serviços fornecem evidências e notificam incidentes?

# 30. Modelos, glossário, índice e referências

## 30.1 Modelo de papel de trabalho

| Campo | Conteúdo esperado |
|---|---|
| Salvaguarda | Número, título, IG, classe de ativo e função de segurança. |
| Escopo | Sistemas, unidades, locais, contas, dados e período. |
| Critério | Texto oficial e procedimento de avaliação aplicável. |
| Entradas | Populações, fontes, responsáveis, datas e validações. |
| Operações | Etapas executadas para produzir medidas. |
| Medidas e métricas | Contagens, listas, cobertura, exceções e interpretação. |
| Evidências | Arquivos, consultas, capturas, registros e aprovações. |
| Conclusão | Implementada, parcialmente implementada ou não implementada, com limitações. |
| Ações | Responsável, prioridade, prazo, correção e reteste. |

## 30.2 Registro de achados e retestes

| ID | Salvaguarda | Condição | Risco | Responsável | Prazo | Estado | Evidência de reteste |
|---|---|---|---|---|---|---|---|
| EX-001 | 7.7 | Exemplo sintético de vulnerabilidade fora do prazo. | Exposição elevada. | Responsável fictício. | AAAA-MM-DD | Aberto | Pendente. |

## 30.3 Glossário

| Termo | Definição prática |
|---|---|
| Classe de ativo | Categoria afetada por uma Salvaguarda, como dispositivos, software, dados, redes, usuários ou documentação. |
| CIS Benchmark | Recomendações de configuração segura para uma tecnologia específica. |
| Controle CIS | Uma das 18 áreas amplas de defesa. |
| Salvaguarda CIS | Ação específica e implementável dentro de um Controle. |
| Cobertura | Parte da população aplicável na qual a Salvaguarda está adequadamente implementada. |
| IG1 | Conjunto de 56 Salvaguardas de higiene cibernética essencial. |
| IG2 | IG1 acrescido de 74 Salvaguardas para maior complexidade e risco. |
| IG3 | Todas as 153 Salvaguardas, incluindo 23 adicionais para ambientes de maior risco. |
| Medida | Contagem, lista, data, configuração ou resultado produzido pelas operações de avaliação. |
| Métrica | Cálculo ou interpretação derivada de uma ou mais medidas. |
| Revisão de procedimento | Avaliação manual da existência e suficiência de um processo documentado. |
| Reteste | Nova avaliação realizada após a correção, utilizando critérios comparáveis e uma população atualizada. |

## 30.4 Índice de assuntos

- Avaliação e medição: capítulos 4 e 30.
- Configurações seguras: Controles 4 e 16.
- Dados: Controle 3.
- Evidências e métricas: capítulos 4, 27 e 30.
- Grupos de Implementação: capítulo 2.
- Identidades e acessos: Controles 5 e 6.
- Inventários: Controles 1, 2, 3, 5, 12 e 15.
- Monitoramento e logs: Controles 8 e 13.
- Prestadores de serviços: Controle 15.
- Recuperação e incidentes: Controles 11 e 17.
- Vulnerabilidades: Controle 7.

## 30.5 Referências oficiais

- CIS Controls v8.1: https://www.cisecurity.org/controls/v8-1
- Lista dos CIS Controls: https://www.cisecurity.org/controls/cis-controls-list
- Grupos de Implementação: https://www.cisecurity.org/controls/implementation-groups
- CIS Controls Assessment Specification: https://www.cisecurity.org/controls/cis-controls-assessment-specification

**Lembrete final:** Estruturas, mapeamentos, ferramentas, produtos, ameaças, leis, contratos e riscos organizacionais mudam. Confirme sempre os recursos oficiais atuais e as obrigações aplicáveis antes de implementar, avaliar ou publicar conclusões.
