# Capítulo 87 Envenenamento e Formação de Dados Risco de Dados

**Estado legal: **Mestre inglês corrigido para consolidação. Este arquivo controla a linguagem de rascunho do capítulo 87 anterior.

## Exigência

As organizações devem proteger os dados de treinamento, validação, teste, ajuste fino, recuperação e feedback contra alterações não autorizadas, contaminação maliciosa, falha de proveniência, degradação da qualidade e viés oculto que possam prejudicar a conformidade, segurança ou desempenho.

## Explicação em linguagem simples

O envenenamento de dados pode ser deliberado ou acidental. Uma pequena quantidade de dados manipulados pode criar comportamentos ocultos, resultados tendenciosos, precisão degradada ou fraquezas de segurança. Os controles devem cobrir fontes de dados, transformações, rótulos, acesso, linhagem, aprovações e ciclos de feedback pós-implante.

## Requisitos de controlo

Implementar conforme apropriado:

1. Controles de origem e proveniência aprovados;
2. controle de acesso, segregação de deveres e mudança de registro;
3. verificações de integridade, hashes, versionamento e dutos reprodutíveis;
4. Testes de anomalia, duplicação, outlier e qualidade de etiqueta;
5. análise de subgrupos e representatividade;
6. due diligence do fornecedor e do conjunto de dados de código aberto;
7. quarentena e revisão de feedback do usuário ou dados de produção antes da reutilização;
8. testes de backdoor, gatilho e envenenamento direcionado;
9. Reversão, reciclagem e identificação da versão afetada;
10. retenção de conjuntos de dados, decisões, transformações e evidências de validação.

## Exemplo GlobalWay

Antes de usar, a equipe valida a proveniência, detecta registros duplicados e manipulados, revisa a representação de grupos protegidos, separa o feedback da produção dos dados de reciclagem aprovados e bloqueia a entrada de dados não revisados no pipeline.

## Atividade de controlo

Nenhum conjunto de dados pode entrar em um treinamento de IA material ou pipeline de ajuste fino sem propriedade documentada, proveniência, integridade, qualidade, uso legal e aprovação de risco. Mudanças materiais exigem reteste e autorização de liberação vinculada à versão.

## Provas

- Registros de inventário e proveniência de conjuntos de dados;
- Registros de acesso e alteração;
- resultados de testes de integridade e qualidade;
- análise de subgrupos e representatividade;
- garantia do conjunto de dados do fornecedor;
- resultados de testes de envenenamento e backdoor;
- Registros de reciclagem e reversão;
- aprovação e liberação de evidências.

## Teste de auditoria

Verifique a proveniência aprovada, acesso controlado, transformações reprodutíveis, testes de integridade e envenenamento, limitações de qualidade documentadas e ligação entre a versão do conjunto de dados, a versão do modelo e a decisão de lançamento.

## Referências jurídicas primárias

- Regulamento (UE) 2024/1689, conforme alterado: dados e governança de dados aplicáveis, gerenciamento de riscos, precisão, robustez, segurança cibernética, documentação técnica e disposições pós-mercado.
- O texto consolidado atual do EUR-Lex controla os resumos mais antigos.
