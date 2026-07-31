# Capítulo 38 Governança de dados

**Estado legal: **Mestre inglês corrigido para consolidação. Este arquivo controla o conflito anterior Capítulo 38 linguagem de rascunho.

## Exigência

Caso um sistema de IA de alto risco utilize conjuntos de dados de treinamento, validação ou teste, o provedor deve aplicar os requisitos de governança de dados e dados do artigo 10.o do Regulamento (UE) 2024/1689, conforme alterado.

## Explicação em linguagem simples

O objetivo legal não é dados perfeitos. É disciplinado, governança de dados documentada apropriada para o propósito e risco pretendido. O provedor deve entender de onde os dados vieram, por que é adequado, como foi preparado, quais limitações ou erros existem, se os grupos afetados são adequadamente representados e se o sistema poderia criar ou reforçar viés.

O Artigo 10 não cria de forma independente uma base legal para processar dados pessoais ou dados de categoria especial. O GDPR e outros requisitos de privacidade aplicáveis devem ser avaliados separadamente.

## Áreas de governança necessárias

O provedor deve documentar, conforme aplicável:

1. escolhas de conceção de dados e processos de recolha;
2. origem dos dados, proveniência e finalidade original;
3. preparação, anotação, rotulagem, limpeza, enriquecimento e agregação de dados;
4. pressupostos sobre o que os dados medem ou representam;
5. disponibilidade, quantidade e adequação dos conjuntos de dados;
6. exame de possíveis vieses e seus efeitos na saúde, segurança ou direitos fundamentais;
7. Medidas para detectar, prevenir e mitigar o viés;
8. Relevância, representatividade, integridade e características de erro;
9. Propriedades estatísticas e adequação para as pessoas, grupos, geografia, contexto e condições de uso pretendido;
10. controles para lacunas de dados, deriva, vazamento, duplicação, contaminação e uso não autorizado;
11. a) Separação e governança de conjuntos de dados de treinamento, validação e teste, quando apropriado;
12. exceções documentadas, limitações e riscos residuais.

## Exemplo GlobalWay

A GlobalWay desenvolve um sistema de triagem de recrutamento usando dados históricos de aplicação e contratação. A revisão de governança de dados identifica sub-representação em certas famílias de trabalho, rótulos históricos inconsistentes, variáveis proxy para características protegidas e diferenças geográficas. A GlobalWay remove recursos inadequados, melhora a documentação, testa o desempenho de subgrupos, limita o uso pretendido e requer revisão humana.

## Atividade de controlo

O provedor deve aprovar um plano de governança de dados específico do sistema antes do desenvolvimento do modelo ou da reciclagem de material. Versões de conjunto de dados, transformações, verificações de qualidade, análises de viés, controles de acesso e aprovações devem ser rastreáveis para o modelo ou a versão do sistema liberada.

## Provas

- Plano de governança de dados;
- Registro de conjunto de dados e registros de proveniência;
- Procedimentos de processamento de dados e de anotação;
- análise de qualidade e representatividade dos dados;
- vies e testes de subgrupos;
- privacidade e avaliação de base legal;
- Histórico de versões do conjunto de dados;
- Registros de acesso e alteração;
- Limitações e registro de risco residual;
- registros de aprovação.

## Teste de auditoria

Confirme que a adequação, proveniência, qualidade, representatividade, viés, privacidade, transformações e limitações foram avaliadas e aprovadas antes do lançamento.Confirme que a adequação, proveniência, qualidade, representatividade, viés, privacidade, transformações e limitações foram avaliadas e aprovadas antes do lançamento.

## Referências jurídicas primárias

- Regulamento (UE) n.o 2024/1689, alterado: artigo 10.o
- O GDPR e a legislação aplicável do Estado-Membro ou setor permanecem aplicáveis de forma independente.
- O texto consolidado atual do EUR-Lex controla os resumos mais antigos.
