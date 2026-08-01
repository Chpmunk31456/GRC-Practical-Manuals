> **Status da revisão:** Edição de revisão controlada. Requer validação humana de terminologia, significado, links, formatação, acessibilidade e atualidade técnica antes da publicação final.

**SÉRIE PRÁTICA DE CIBERSEGURANÇA, PRIVACIDADE E CONFORMIDADE**

**CIS Critical Security Controls v8.1**

**Implementação prática, medição, evidências e ferramentas de código aberto**

*Manual de trabalho para gestores, analistas juniores, estudantes, profissionais em transição de carreira, avaliadores e equipes de segurança*

**Alberto (Al) Leiva**

Primeira edição • Julho de 2026

| **Conteúdo:** 18 Controles • 153 Salvaguardas • IG1, IG2 e IG3 • medição • evidências • ferramentas • guia para gestores • laboratórios • preparação profissional |
|---|

# Aviso de publicação e uso

Autor: Alberto (Al) Leiva

Edição: Primeira edição, julho de 2026

Este manual educacional independente não é uma publicação, certificação, acreditação, relatório de auditoria, opinião jurídica ou garantia de segurança ou conformidade emitida pelo Center for Internet Security. CIS Controls e CIS Benchmarks são marcas do Center for Internet Security. Consulte os recursos oficiais do CIS para obter o conteúdo exato e a orientação vigente.

Os CIS Controls representam boas práticas de cibersegurança. Eles não substituem leis, regulamentos, contratos, requisitos setoriais, avaliações de risco ou responsabilidades de gestão aplicáveis. Um mapeamento demonstra relações entre estruturas; não comprova automaticamente a conformidade com outra estrutura.

## Uso ético e autorizado

Utilize ferramentas técnicas somente em ativos, redes, aplicações, contas de nuvem, repositórios e dados que você possui ou para os quais recebeu autorização específica por escrito. Em laboratórios, utilize informações sintéticas e sistemas isolados.

# Prefácio

*Introdução prática à defesa cibernética priorizada e à medição baseada em evidências.*

Os CIS Controls transformam necessidades defensivas comuns em Salvaguardas específicas. Sua principal força é a priorização prática: conhecer os ativos, controlar software e dados, proteger configurações e identidades, gerenciar vulnerabilidades e registros, preparar-se para interrupções e ataques e testar se as defesas funcionam.

A versão 8.1 é uma atualização iterativa da versão 8. Ela realinhou os mapeamentos ao NIST CSF 2.0, ampliou definições de termos reservados, revisou classes de ativos e mapeamentos de Salvaguardas, corrigiu questões menores, esclareceu determinadas Salvaguardas e incorporou a função Governar aos mapeamentos. Os 18 Controles e as 153 Salvaguardas permanecem como estrutura central.

A instalação de uma ferramenta não equivale à implementação de um controle. Uma implementação efetiva exige escopo definido, populações completas, configuração segura, evidência operacional, responsáveis capacitados, tratamento de exceções, medição, correção e novos testes. Gestores definem prioridades e recursos; analistas tornam essas decisões confiáveis por meio de inventários e evidências precisos.

# Como usar este manual

- Gestores devem começar pelos capítulos 1–5 e 24–25.
- Analistas juniores devem estudar os 18 capítulos de Controles, o método de medição, as ferramentas, o laboratório e o capítulo de entrevistas.
- Equipes técnicas devem relacionar cada Salvaguarda a ativos, dados, responsáveis, procedimentos, configurações, monitoramento, exceções e evidências.
- Avaliadores devem utilizar a especificação oficial de avaliação dos CIS Controls para confirmar entradas, operações, medidas, métricas, premissas e revisões de procedimentos.

| **Sumário no Word:** O arquivo DOCX pode conter um campo nativo de sumário. Após qualquer edição, atualize o campo e selecione a opção para atualizar a tabela inteira. |
|---|

# Sumário

1. Fundamentos dos CIS Controls v8.1  
2. Grupos de Implementação e priorização  
3. Governança, escopo e responsabilidades  
4. Medição com a especificação de avaliação do CIS  
5. Roteiro de implementação  
6–23. Os 18 CIS Controls  
24. Ferramentas de código aberto  
25. Guia dos CIS Controls para gestores  
26. Guia profissional para analistas juniores  
27. Laboratório fictício e portfólio  
28. Plano de aprendizagem de trinta dias  
29. Preparação para entrevistas  
30. Modelos, glossário, índice e referências

# 1. Fundamentos dos CIS Controls v8.1

*A versão atual, sua estrutura, finalidade e limitações.*

<img src="media/image1.png" style="width:6.15in;height:3.94164in" alt="Os Controles organizam 153 Salvaguardas em um programa defensivo prático." />

Figura 1. Os 18 CIS Critical Security Controls

- Os CIS Controls v8.1 foram publicados em junho de 2024.
- Os Controles são boas práticas priorizadas para defender sistemas e redes contra ataques prevalentes.
- A estrutura contém 18 Controles e 153 Salvaguardas.
- As Salvaguardas são relacionadas a classes de ativos, funções de segurança e Grupos de Implementação.
- A versão 8.1 alinha o mapeamento ao NIST CSF 2.0 e inclui a função Governar.
- Existem mapeamentos oficiais para várias estruturas, mas cada requisito aplicável deve ser verificado separadamente.

| Camada | Finalidade |
|---|---|
| Controle | Resultado defensivo amplo, como inventário de ativos ou resposta a incidentes. |
| Salvaguarda | Ação específica que pode ser atribuída, implementada e medida. |
| Classe de ativo | Tipo de elemento afetado, como dispositivos, software, dados, redes, usuários ou documentação. |
| Função de segurança | Mapeamento para Governar, Identificar, Proteger, Detectar, Responder ou Recuperar. |
| Grupo de Implementação | Priorização recomendada de acordo com o perfil de risco e os recursos. |
| Medida de avaliação | Entradas, operações, medidas, métricas e revisão de procedimentos usadas para avaliar uma Salvaguarda. |

# 2. Grupos de Implementação e priorização

*Como IG1, IG2 e IG3 ajudam organizações a escolher um ponto de partida realista.*

<img src="media/image2.png" style="width:6.15in;height:3.39605in" alt="Cada Grupo de Implementação se apoia no grupo anterior; o IG3 contém todas as Salvaguardas." />

Figura 2. Progressão dos Grupos de Implementação

| Grupo | Salvaguardas | Situação típica | Objetivo |
|---|---:|---|---|
| IG1 | 56 | Recursos e experiência de segurança limitados; menor sensibilidade; necessidade elevada de continuidade básica. | Higiene cibernética essencial contra ataques comuns. |
| IG2 | IG1 + 74 | Vários departamentos, maior complexidade, informações sensíveis e maior dependência operacional. | Gerenciar riscos e complexidade operacional crescentes. |
| IG3 | IG1 + IG2 + 23 = 153 | Especialistas em segurança, dados sensíveis ou regulamentados, serviços críticos e ameaças sofisticadas. | Reduzir o impacto de ataques direcionados e avançados. |

- Toda organização deve considerar o IG1 como ponto de partida, conforme a orientação do CIS.
- A seleção do grupo deve considerar sensibilidade dos dados, serviços críticos, exposição a ameaças, obrigações legais e contratuais, tolerância do negócio, tecnologia, pessoal e experiência.
- Um Grupo de Implementação é um mecanismo de priorização; não autoriza ignorar riscos materiais ou requisitos obrigatórios.
- Documente acréscimos, sequência, exceções, aceitação de risco, responsáveis e datas.
- Utilize o CIS Controls Navigator oficial para filtrar as Salvaguardas v8.1 e consultar os mapeamentos.

# 3. Governança, escopo e responsabilidades

*A base de gestão necessária para operar as Salvaguardas de maneira consistente.*

- Defina objetivos de negócio, serviços críticos, dados sensíveis, obrigações legais e contratuais, perfil de ameaças, tolerância ao risco e Grupo de Implementação selecionado.
- Mantenha inventários completos de ativos empresariais, software, dados, contas, sistemas de autenticação, infraestrutura de rede, registros, fornecedores, aplicações e recursos de recuperação.
- Designe um responsável principal para cada Salvaguarda e responsáveis operacionais para cada plataforma ou processo afetado.
- Defina escopo, aplicabilidade, dependências, responsabilidades de prestadores de serviços, exceções permitidas, autoridade de aprovação e gatilhos de revisão.
- Planeje orçamento, pessoas, competências, tecnologia, tempo e gestão de mudanças.
- Defina métricas e relatórios antes da implementação para tornar visíveis a cobertura e as falhas.
- Opere um ciclo de governança: priorizar, implementar, medir, corrigir, testar novamente e melhorar.

| Função | Decisão ou responsabilidade |
|---|---|
| Patrocinador executivo | Direção, tolerância ao risco, orçamento, escalonamento e responsabilidade final. |
| Responsável pelo Controle | Desenho da Salvaguarda, escopo, procedimento, medição, exceções e melhoria. |
| Responsável pelo ativo ou serviço | Inventário preciso, uso aprovado, configuração, impacto de negócio e remediação. |
| Operações de segurança | Monitoramento, alertas, investigação, resposta e evidências. |
| TI e engenharia | Implementação, gestão de mudanças, correções, configuração e recuperação. |
| GRC ou analista | Mapeamento, evidências, medição, achados, acompanhamento de ações e relatórios. |
| Auditoria interna ou avaliador | Critérios objetivos, testes, limitações e conclusões. |
| Prestador de serviços | Controles contratados, evidências, incidentes, mudanças e apoio à saída. |

# 4. Medição com a especificação de avaliação do CIS

*Um método repetível para determinar se as Salvaguardas estão implementadas.*

<img src="media/image3.png" style="width:6.15in;height:2.87986in" alt="A especificação oficial avança de entradas definidas para operações, medidas, métricas e revisão de procedimentos." />

Figura 3. Estrutura de medição das Salvaguardas CIS

| Elemento | Pergunta |
|---|---|
| Metadados da Salvaguarda | Qual é a Salvaguarda exata, a classe de ativo, a função de segurança e o IG? |
| Dependências | Quais outras Salvaguardas ou populações devem existir primeiro? |
| Premissas | Qual condição aceita afeta a medição? |
| Entradas | Quais dados completos e confiáveis são necessários? |
| Operações | Qual análise deve ser realizada sobre as entradas? |
| Medidas | Quais contagens, listas, datas, configurações ou resultados são produzidos? |
| Métricas | Como as medidas são calculadas e interpretadas? |
| Revisão de procedimentos | Existe um processo documentado e ele contém os elementos necessários? |

- Defina com precisão a Salvaguarda e a população aplicável.
- Obtenha as entradas necessárias e valide completude, precisão, atualidade, propriedade e confiabilidade da fonte.
- Siga as operações oficiais de medição ou documente um método equivalente e confiável.
- Preserve os cálculos das medidas e a população de exceções subjacente, não apenas uma porcentagem.
- Avalie se a Salvaguarda está implementada e opera adequadamente.
- Atribua correções para cobertura ausente, configuração inadequada, revisão atrasada, exceções ou dados não confiáveis.
- Execute novos testes utilizando os mesmos critérios e a população atualizada.
- Relate escopo, resultado, exceções, limitações, responsável, ação e data.

# 5. Roteiro de implementação

*Uma sequência prática que começa com inventários e termina com resiliência testada.*

1. Selecione e documente o Grupo de Implementação inicial e os acréscimos necessários.
2. Construa e concilie as populações principais: ativos, software, dados, contas, sistemas de autenticação, redes, fornecedores, aplicações e registros.
3. Implemente as Salvaguardas do IG1 com responsáveis, procedimentos, métricas de cobertura, exceções e evidências.
4. Proteja identidades e configurações; gerencie vulnerabilidades, e-mail, navegadores, defesas contra malware, cópias de segurança e monitoramento essencial.
5. Exercite resposta a incidentes e recuperação antes de uma emergência real.
6. Meça cada Salvaguarda aplicável utilizando entradas confiáveis e operações repetíveis.
7. Corrija cobertura incompleta e falhas recorrentes; confirme as correções por meio de novos testes.
8. Expanda para IG2 ou IG3 conforme o risco, as obrigações, a maturidade e a exposição a ameaças.
9. Utilize mapeamentos oficiais para coordenar outras estruturas sem tratar o mapeamento como comprovação automática de conformidade.

**Princípio de implementação:** Um conjunto menor de Salvaguardas, com escopo completo, operação consistente, medição e melhoria contínua, é mais defensável do que uma lista extensa marcada como concluída sem evidências confiáveis.

