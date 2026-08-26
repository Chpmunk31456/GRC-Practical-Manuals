# Manual 04 — Implementação do Perfil de IA Generativa NIST AI 600-1
## Fonte controlada em português brasileiro — Capítulos 17–24

> Tradução assistida por máquina para revisão controlada. Este conjunto apoia governança de IA generativa baseada em evidência e não reproduz o texto do NIST. A aprovação semântica humana continua obrigatória antes da publicação.

## Capítulo 17 — Estratégia de avaliação

A avaliação começa com uma pergunta documentada: o que o sistema deve conseguir fazer, o que deve evitar, sob quais condições e com qual nível de confiança. A estratégia deveria definir objetivos, cenários, conjuntos de dados, avaliadores, métodos, limites, amostragem, limitações e regras de decisão.

A avaliação deveria incluir uso normal representativo e uso indevido plausível. Sistemas de alto impacto deveriam usar desafio independente ou separação entre construtores e responsáveis pela decisão final de liberação.

## Capítulo 18 — Governança de dados de teste e cenários

Os dados de teste deveriam ser rastreáveis ao propósito. As equipes deveriam registrar origem, cobertura, sensibilidade, transformação, representatividade, limitações conhecidas e se os dados podem ser retidos ou compartilhados.

Dados sintéticos podem melhorar cobertura, mas não devem ser presumidos representativos de populações reais ou comportamento adversarial. Quando usados, o registro de avaliação deveria explicar por que são apropriados e quais pontos cegos permanecem.

## Capítulo 19 — Limites de aceitação e critérios de decisão

Os limites deveriam ser definidos antes dos testes finais quando praticável e refletir consequências, não conveniência. Um assistente de redação de baixo impacto pode tolerar taxas de falha diferentes de um sistema que influencie decisões de segurança, finanças, saúde, emprego ou proteção.

A decisão de liberação deveria registrar se cada limite passou, falhou, foi aceito condicionalmente ou dispensado. Dispensas exigem justificativa, responsável, controle compensatório, data de expiração ou revisão e aprovação do risco residual.

## Capítulo 20 — Red teaming e avaliação adversarial

A avaliação adversarial deveria testar se controles permanecem efetivos quando usuários ou conteúdo externo tentam contorná-los intencionalmente. Casos de teste deveriam abordar manipulação direta de prompts, instruções indiretas, envenenamento de recuperação, abuso de ferramentas, falhas de identidade/permissão, extração de dados, divulgação do prompt do sistema e encadeamento inseguro de ações quando aplicável.

Resultados de red team devem ser tratados como evidência, não como espetáculo. Testes repetidos sem responsável de remediação ou reteste não devem ser representados como garantia.

## Capítulo 21 — Controles de proveniência de conteúdo

A proveniência deveria apoiar perguntas práticas: qual modelo e configuração produziu a saída, quais dados ou fontes influenciaram materialmente, quais transformações ocorreram e quem ou o que aprovou o uso posterior.

A organização deveria selecionar mecanismos proporcionais ao risco, como links de fonte, hashes de artefatos, identificadores de modelo/versão, versões de prompts ou políticas, logs de transformação, registros de aprovação humana ou metadados assinados. A proveniência melhora rastreabilidade, mas não prova sozinha precisão factual ou origem lícita.

## Capítulo 22 — Pacote de testes pré-implantação

Um pacote de evidência pré-implantação deveria reunir o necessário para uma decisão responsável. No mínimo, deveria incluir inventário do sistema/caso de uso, registro de riscos e impactos, plano e resultados de avaliação, resultados de testes de segurança/adversariais, revisão de privacidade/dados quando aplicável, evidência de fornecedores/componentes, achados e exceções abertos, limites de monitoramento, plano de parar/reverter e registro de aprovação.

O pacote deve ser versionado e vinculado ao candidato exato de liberação.

## Capítulo 23 — Preparação para divulgação e escalonamento de incidentes

Antes da implantação, a organização deveria definir quais eventos qualificam como incidentes de IA generativa, quem deve ser informado, que evidência deve ser preservada e quando notificação ou divulgação externa pode ser exigida.

Categorias podem incluir saída nociva, exposição de dados, ação não autorizada, contorno de controle, falha de fornecedor, desinformação material, autonomia inesperada, violação regulatória ou contratual ou repetida violação de limites. Critérios de escalonamento deveriam ser explícitos o suficiente para evitar improvisação durante um evento.

## Capítulo 24 — Suficiência de evidência e qualidade da revisão

A evidência deveria demonstrar que um controle operou para o sistema e período relevantes. Políticas, capturas de tela, alegações de fornecedor ou questionários podem apoiar a evidência, mas não devem ser automaticamente tratados como prova de efetividade.

Revisores deveriam considerar relevância, confiabilidade, completude, tempestividade e independência. Quando a evidência for fraca ou indisponível, o registro deve declarar essa limitação e o efeito resultante sobre risco residual ou confiança na liberação.
