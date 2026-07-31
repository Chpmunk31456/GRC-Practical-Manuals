# Capítulo 42 Supervisão Humana

**Estado legal: **Mestre inglês corrigido para consolidação. Este arquivo controla o conflito anterior Capítulo 42 linguagem de rascunho.

## Exigência

Os sistemas de IA de alto risco devem ser projetados e desenvolvidos para que as pessoas naturais possam supervisioná-los efetivamente durante o uso. As medidas de supervisão devem ser proporcionais aos riscos, autonomia, contexto e consequências previsíveis do sistema.

## Explicação em linguagem simples

A supervisão humana não é satisfeita colocando uma pessoa perto do processo ou exigindo um clique final. A pessoa atribuída deve ter informações suficientes, competência, autoridade, tempo, acesso ao sistema e capacidade prática para detectar problemas, desafiar saídas, intervir, substituir, interromper o uso e aumentar as preocupações.

Os operadores não devem ser pressionados a aceitar uma saída de IA apenas porque o sistema a produziu ou porque rejeitá-la é inconveniente.

## Design de Supervisão

O plano de supervisão deve definir, conforme aplicável:

1. as decisões ou ações que exijam revisão humana;
2. quem executa a supervisão e quais qualificações são necessárias;
3. informações disponíveis para o revisor;
4. limiares, avisos, indicadores de confiança e limitações conhecidas;
5. intervenção, substituição, rejeição, suspensão e parar a autoridade;
6. caminhos de escalada e tempos de resposta;
7. Requisitos de revisão dupla ou de revisão especializada para casos graves;
8. carga de trabalho, pessoal e tempo necessário para uma revisão significativa;
9. controles contra viés de automação e carimbo de borracha;
10. registro de revisão, substituição, justificativa e escalada;
11. Testes periódicos de se a supervisão permanece eficaz.

## Salvaguarda biométrica especial

Quando a lei exigir a verificação por pelo menos duas pessoas singulares competentes para utilizações específicas de identificação biométrica, o manual deve preservar essa salvaguarda legal e qualquer exceção aplicável. Não deve ser generalizado para todos os sistemas biométricos ou omitido quando legalmente exigido.

## Exemplo GlobalWay

O sistema de recrutamento da GlobalWay pode classificar os pedidos, mas não pode rejeitar um candidato automaticamente. Um recrutador treinado revisa as evidências relevantes, pode desconsiderar a pontuação, registra o motivo da decisão e aumenta os resultados anômalos ou potencialmente discriminatórios para a conformidade com o RH.

## Atividade de controlo

O provedor deve projetar recursos de supervisão eficazes e documentá-los nas instruções de uso. O implantador deve atribuir revisores competentes, conceder-lhes autoridade, estabelecer procedimentos viáveis, monitorar padrões de substituição e escalada e suspender o uso onde a supervisão não pode ser realizada de forma eficaz.

## Provas

- Plano de Supervisão Humana;
- Requisitos de função e competência;
- Registros de treinamento e avaliação;
- Procedimentos do operador;
- interface de aviso e design de aviso;
- sobrepor e parar os controles;
- análise de carga de trabalho e pessoal;
- Registros de revisão e escalada;
- testes de automação-viés;
- Revisão periódica da eficácia.

## Teste de auditoria

Confirme que os revisores entendem as limitações do sistema, podem avaliar independentemente a saída, ter autoridade e tempo para intervir, usar mecanismos de substituição e escalada corretamente e produzir registros que mostrem uma supervisão significativa em vez de nominal.

## Referências jurídicas primárias

- Regulamento (UE) n.o 2024/1689, com a redação que lhe foi dada: Artigo 14.o e obrigações relacionadas com o deployer.
- O texto consolidado atual do EUR-Lex controla os resumos mais antigos.
