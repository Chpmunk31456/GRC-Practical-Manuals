# Manual 07 — Segurança de IA e Controles do Ciclo de Vida
## Fonte controlada em português brasileiro — Capítulos 09–16

> Tradução de trabalho sujeita à revisão semântica humana. Esta orientação defensiva original não reproduz texto de normas nem garante segurança.

## Capítulo 09 — Segurança de recuperação e fontes de conhecimento

Fontes de recuperação devem ser tratadas como entradas influenciadas externamente. Os controles devem abordar admissão de fontes, autoridade de escrita, validação de conteúdo, controle de acesso, separação entre tenants, conteúdo desatualizado, exposição de dados sensíveis e remoção.

Bancos vetoriais e índices devem herdar controles apropriados de classificação de dados, acesso, retenção, logging e backup.

## Capítulo 10 — Tratamento de segredos e dados sensíveis

Segredos não devem ser incorporados em prompts, código-fonte, notebooks ou contexto do modelo quando existirem alternativas mais seguras. Credenciais de serviço devem ter escopo restrito, ser rotacionadas, monitoradas e armazenadas usando mecanismos aprovados de gestão de segredos.

Logs, traces, avaliações e artefatos de suporte também devem ser revisados para exposição não intencional de dados sensíveis.

## Capítulo 11 — Cadeia de suprimentos de modelos e componentes

A revisão de segurança deve incluir origem do modelo, pacotes, contêineres, adaptadores, conjuntos de dados, APIs, plugins, serviços de segurança e dependências de hospedagem. Os componentes devem ser versionados e rastreáveis para que as equipes de segurança possam avaliar o impacto de mudanças em fornecedor ou componente.

Mudanças materiais de fornecedores devem acionar reavaliação em vez de serem herdadas silenciosamente.

## Capítulo 12 — Avaliação e validação de segurança

A avaliação de segurança deve usar objetivos e resultados esperados baseados em risco. A validação deve cobrir se controles de acesso, limites de dados, permissões de ferramentas, controles de recuperação, tratamento de saídas, comportamento de dependências e restrições operacionais funcionam conforme esperado em condições representativas e de limite.

A evidência de teste deve registrar configuração, escopo, resultado, limitação e remediação.

## Capítulo 13 — Desafio independente

O desafio independente deve testar se premissas e limites de controle continuam válidos fora das condições normais de operação. A revisão deve ser autorizada, delimitada e orientada por evidências.

Atividade de desafio sem responsável pela remediação e sem validação de acompanhamento não deve ser apresentada como asseguração.

## Capítulo 14 — Guardrails e controles determinísticos

Guardrails podem reduzir risco, mas devem ser combinados com controles de segurança determinísticos quando as consequências forem significativas. Autorização, validação de entrada, validação de saída, listas permitidas, limites de transação, controles de rede e aprovação humana podem fornecer aplicação mais forte que o comportamento do modelo isoladamente.

## Capítulo 15 — Supervisão humana para ações sensíveis à segurança

A aprovação humana deve ser exigida quando ações automatizadas puderem criar impacto material de segurança ou negócio e o sistema não puder limitar o risco de forma confiável por meio de controles determinísticos.

Revisores precisam de contexto, tempo, competência e autoridade suficientes para rejeitar ou interromper a ação. Uma etapa nominal de aprovação sem informação significativa não constitui supervisão eficaz.

## Capítulo 16 — Pacote de segurança pré-implantação

Antes da liberação, reúna o modelo de ameaças atual, arquitetura, inventário de ativos, resultados de validação, achados em aberto, evidências de fornecedores, revisão de identidade/permissões, limites de monitoramento, plano de incidentes, plano de rollback/parada, exceções e aprovações.

O pacote deve corresponder ao candidato exato de liberação, e mudanças materiais devem reabrir as evidências afetadas.
