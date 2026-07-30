# Capítulo 85 Modelagem de Ameaças

** Status legal: ** Corrigido o mestre inglês para consolidação. Este arquivo controla o conflito anterior do capítulo 85 da linguagem de rascunho.

## Exigência

As organizações devem realizar modelagem proporcional de ameaças para sistemas de IA e componentes de IA de uso geral, onde a segurança, segurança, resiliência, privacidade, direitos fundamentais ou riscos operacionais podem ser afetados materialmente por uso indevido malicioso ou acidental.

## Explicação em linguagem simples

A modelagem de ameaças de IA identifica como atacantes, insiders, usuários, dependências, pipelines de dados, prompts, modelos, ferramentas e interfaces podem causar resultados prejudiciais. Deve cobrir todo o ciclo de vida e ser atualizado quando o sistema, modelo, finalidade pretendida, dados, ambiente de implantação ou alterações no cenário de ameaças.

## m escopo de modelagem de ameaças

Avaliar no mínimo:

1. ativos, limites de confiança, atores e superfícies de ataque;
2. pipelines de treinamento, ajuste fino, recuperação, prompt e inferência;
3. Intoxicação de dados, injeção imediata, manipulação de modelo, extração e roubo;
4. uso de ferramentas não autorizadas, escalada de privilégios e abuso de agentes;
5. dependências de cadeia de suprimentos, API, plug-in, código aberto e nuvem;
6. vazamento de privacidade, memorização, exposição a informações confidenciais e inversão de modelo;
7. bypass de segurança, geração de conteúdo nocivo, evasão e uso indevido;
8. registro, monitoramento, detecção, contenção, reversão e recuperação;
9. Consequências pessoais, operacionais e regulatórias afetadas;
10. Risco residual, suposições e controles necessários.

## Exemplo GlobalWay

Antes de liberar um agente de assistência de viagem de IA que pode acessar sistemas de reserva, a GlobalWay mapeia as permissões de ferramenta do agente, canais de alerta, APIs externas, entradas de usuários, armazenamento de dados e caminhos de escalada. A revisão identifica injeção imediata, alterações não autorizadas de itinerário, vazamento de dados e substituição de modelo de fornecedor como cenários prioritários.

## Atividade de controlo

Os proprietários de sistemas e segurança devem completar um modelo de ameaça vinculado à versão antes do lançamento da produção e após a mudança material. As descobertas de alto risco devem ser atribuídas controles, proprietários, prazos, testes de validação e critérios de bloqueio de liberação.

## Provas

- Modelo de ameaça aprovado;
- Arquitetura e diagramas de fluxo de dados;
- inventário de ativos e de confiança;
- Casos de abuso e árvores de ataque;
- decisões de mapeamento de controle e risco residual;
- validação e resultados da equipe vermelha;
- Registros de reavaliação desencadeados por mudanças.

## Teste de auditoria

Selecione uma amostra de sistemas de IA material e verifique se os modelos de ameaça refletem a arquitetura implantada, as dependências atuais, cenários de uso indevido realistas, mitigações atribuídas, eficácia de controle testada e aceitação documentada de risco residual.

## Referências jurídicas primárias

- Regulamento (UE) n.o 2024/1689, conforme alterado: disposições aplicáveis em matéria de gestão de riscos, precisão, robustez, cibersegurança, pós-comercialização, incidentes e risco sistémico.
- O texto consolidado atual do EUR-Lex controla os resumos mais antigos.
- Estruturas e orientações de segurança reconhecidas não são vinculativas, a menos que sejam incorporadas por outro requisito vinculativo.
