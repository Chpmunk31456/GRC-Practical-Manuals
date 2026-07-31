# Capítulo 84 Ciclo de vida seguro para o desenvolvimento da IA

** Status legal: ** Corrigido o mestre inglês para consolidação. Este arquivo controla o conflito anterior do capítulo 84 da linguagem de rascunho.

## Exigência

Os fornecedores e organizações que desenvolvem, integram, configuram ou modificam materialmente os sistemas de IA devem incorporar segurança, segurança, privacidade, robustez, governança de dados, supervisão humana, documentação e controle de mudanças durante todo o ciclo de vida. Os controles devem ser proporcionais ao propósito pretendido do sistema, classificação de risco, uso indevido previsível, dependências da cadeia de valor e ambiente de produção.

## Explicação em linguagem simples

A revisão de segurança não pode ser adiada até o final do desenvolvimento. Ameaças específicas de IA podem entrar através de dados, modelos, prompts, ferramentas, APIs, integrações, logs, pipelines de implantação e uso a jusante. O ciclo de vida deve produzir evidências de que os controles foram projetados, testados, aprovados, monitorados e atualizados para a versão de produção real.

## Controles de ciclo de vida

O ciclo de vida seguro deve incluir:

1. Ingestão, finalidade pretendida, papel e classificação de risco;
2. Requisitos de segurança e caso de abuso;
3. arquitetura, fluxo de dados e revisão de confiança;
4. Procedência de dados, integridade, qualidade e controles de acesso;
5. Codificação segura, dependência, modelo e controles de infraestrutura;
6. Prompt, recuperação, agente, ferramenta e salvaguardas API;
7. privacidade, viés, segurança, robustez e testes de supervisão humana;
8. testes contraditórios e gestão de vulnerabilidades;
9. critérios de liberação, segregação de deveres, aprovações e reversão;
10. registro, monitoramento, resposta a incidentes e feedback pós-mercado;
11. Documentação vinculada à versão e retenção de evidências;
12. aposentadoria, exclusão de dados, eliminação de modelo e planejamento de continuidade.

## Exemplo GlobalWay

A GlobalWay desenvolve um assistente de política de viagens de IA que pode consultar sistemas de reservas e elaborar recomendações de viajantes. O ciclo de vida seguro limita as permissões da ferramenta, valida as fontes de recuperação, testa a injeção imediata e o vazamento de dados, requer aprovação humana para ações conseqentes, registra as versões de produção e bloqueia a liberação até que os portões de segurança e conformidade estejam completos.

## Atividade de controlo

A engenharia deve operar um ciclo de vida de IA seguro documentado com portões obrigatórios apropriados ao risco. Sistemas de alto risco ou materiais exigem aprovação independente de segurança, privacidade, legal e governança de IA. As exceções devem identificar o proprietário, a lógica, os controles compensadores, a data de validade e o risco residual.

## Provas

- padrão de ciclo de vida e portas de controle;
- modelo de ameaça e casos de abuso;
- Revisões de arquitetura e fluxo de dados;
- Registros de desenvolvimento seguro e dependência;
- Planos de teste e resultados;
- Registros de vulnerabilidade e remediação;
- aprovações e registros de exceções;
- Documentação técnica ligada à versão;
- Evidências de monitoramento e revisão pós-liberação;
- Registros de aposentadoria e descarte.

## Teste de auditoria

Selecione uma amostra de lançamentos de IA de produção. Trace cada lançamento através de entrada, design, desenvolvimento, teste, aprovação, implantação e monitoramento. Confirme que os portões necessários foram concluídos, as exceções foram autorizadas e vinculadas ao tempo e as evidências correspondem à versão implantada.

## Referências jurídicas primárias

- Regulamento (UE) n.o 2024/1689, alterado: artigos 9.o-15.o, 17.o, 20.o, 24.o-26.o, 55.o, 72.o-73.o e anexo IV, conforme aplicável.
- Regulamento (UE) 2016/679: artigos 25.o, 32.o, 35.o e disposições de responsabilidade conexas em que os dados pessoais são tratados.
- Textos EUR-Lex consolidados atuais controlam resumos e rascunhos anteriores.
