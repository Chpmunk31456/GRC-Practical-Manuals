# Manual 04 — Implementação do Perfil de IA Generativa NIST AI 600-1
## Fonte controlada em português brasileiro — Capítulos 01–08

> Tradução assistida por máquina para revisão controlada. Orientação de implementação original baseada na linha de base controlada NIST AI 600-1 / AI RMF. Este texto não reproduz o texto da publicação do NIST nem cria certificação, conformidade legal ou opinião de auditoria. A aprovação semântica humana continua obrigatória antes da publicação.

## Capítulo 01 — Propósito, escopo e aplicabilidade

Este manual operacionaliza a gestão de riscos de IA generativa para organizações que projetam, adquirem, integram, implantam, operam ou desativam capacidades de IA generativa. O limite de implementação é deliberadamente baseado em risco: nem todo controle, teste, evidência ou prática operacional se aplica a todo caso de uso.

Cada implementação começa com uma decisão documentada de aplicabilidade cobrindo caso de uso, partes afetadas, contexto de implantação, dados tratados, autonomia, dependências externas e consequências de erro ou uso indevido. O registro de aplicabilidade torna-se evidência controlada e deve ser revisto quando sistema, modelo, dados, ferramentas, fornecedor ou contexto operacional mudarem materialmente.

Evidência mínima:
- descrição do caso de uso e responsável de negócio;
- referência ao inventário do sistema/modelo/componente;
- identificação das partes afetadas e partes interessadas;
- nível de risco ou classificação equivalente;
- justificativa de aplicabilidade;
- revisor e data de aprovação.

## Capítulo 02 — Relação com AI RMF 1.0

NIST AI 600-1 é tratado como perfil de IA generativa e recurso complementar ao AI RMF, não como checklist universal independente. O modelo operacional mantém GOVERN, MAP, MEASURE e MANAGE como ciclo de gestão, acrescentando famílias de risco específicas de IA generativa, expectativas de teste, considerações de proveniência e sinais de incidente.

As organizações deveriam mapear cada decisão de implementação à função relevante do AI RMF e preservar rastreabilidade da declaração de risco até evidência, decisão, ação e risco residual.

Comportamento de controle requerido:
- GOVERN define política, responsabilidade, autoridade e escalonamento;
- MAP define contexto, uso, atores, dependências e danos plausíveis;
- MEASURE avalia desempenho, segurança, cibersegurança, privacidade, integridade e incerteza;
- MANAGE seleciona tratamentos, aceita risco residual, monitora a operação e aciona parar/reverter quando limites são excedidos.

## Capítulo 03 — Caminhos de implementação

Três caminhos proporcionais são suportados.

### Essencial
Para usos de menor complexidade ou impacto. Requer inventário, responsáveis, triagem básica de risco, testes mínimos, supervisão humana, tratamento de incidentes e aprovação documentada.

### Estruturado
Para usos materiais de negócio, clientes, força de trabalho, segurança, privacidade, finanças ou operações. Requer registros formais de risco, matrizes de evidência, planos de teste, revisão de fornecedores, controles de mudança, limites de monitoramento, playbooks de incidente e reavaliação periódica.

### Reforçado
Para usos de alto impacto, alta autonomia, sensíveis à segurança, regulados, expostos externamente ou de outra forma consequenciais. Requer desafio independente, testes adversariais mais profundos, critérios formais de liberação, proveniência reforçada, autoridade explícita para parar/reverter, monitoramento reforçado e aceitação documentada do risco residual pela gestão responsável.

A seleção do caminho deve ser justificada e só pode ser reduzida mediante aprovação documentada.

## Capítulo 04 — Governança e responsabilização

Todo sistema de IA generativa deve ter responsáveis de negócio, técnicos, de segurança, privacidade/dados e risco adequados ao seu escopo. A responsabilidade não pode ser delegada apenas ao fornecedor do modelo ou implementador.

A governança deveria definir quem pode aprovar novo caso de uso, mudanças em modelo/prompt/recuperação/ferramentas/dados, quem responde por testes e evidência, quem pode suspender ou reverter implantação, quem aceita risco residual, quem recebe notificações de incidente e quem conduz revisão periódica.

Conflitos de interesse devem ser identificados quando a mesma pessoa projeta, testa e aprova sistema de alto impacto. Implementações reforçadas deveriam adicionar revisão ou desafio independente.

## Capítulo 05 — Inventário e decomposição do sistema

Trate a capacidade de IA generativa como sistema, não apenas modelo. O inventário deveria identificar modelo, hospedagem, camada de recuperação, armazenamento vetorial, prompts/instruções do sistema, ferramentas, APIs, fontes de dados, artefatos de fine-tuning, guardrails, monitoramento, serviços externos e pontos de decisão humana.

O inventário deveria registrar versão, responsável, fornecedor, localização, classificação de dados, limite de autenticação, autoridade de mudança e status de desativação. Dependências capazes de alterar materialmente saída ou comportamento devem ser rastreáveis separadamente.

Uma mudança é material quando pode alterar risco, capacidade, exposição, qualidade de saída, segurança, cibersegurança, privacidade, postura de conformidade ou impacto sobre partes afetadas.

## Capítulo 06 — Modelo de famílias de risco de IA generativa

A linha de base controlada do Manual 04 preserva doze famílias de risco de IA generativa:

1. Informações ou capacidades CBRN
2. Confabulação
3. Conteúdo perigoso, violento ou de ódio
4. Privacidade de dados
5. Impactos ambientais
6. Viés prejudicial e homogeneização
7. Configuração humano-IA
8. Integridade da informação
9. Segurança da informação
10. Propriedade intelectual
11. Conteúdo obsceno, degradante e/ou abusivo
12. Integração da cadeia de valor e componentes

Essas famílias são categorias de triagem, não achados automáticos. Cada caso de uso deve determinar famílias aplicáveis, cenários plausíveis, controles existentes, evidência, risco residual e indicadores de monitoramento.

## Capítulo 07 — Declarações de risco e caminhos de impacto

Os registros de risco deveriam ser baseados em cenários. Uma estrutura útil é:

**Condição ou ameaça → comportamento do sistema → ativo/pessoa/processo afetado → consequência → controle/evidência → risco residual.**

Por exemplo, um assistente com recuperação pode ingerir conteúdo não confiável, seguir instruções maliciosas incorporadas, invocar ferramenta externa e expor informação restrita. A declaração deveria descrever o caminho completo e não apenas rotular o problema como “prompt injection”.

A análise de impacto deveria considerar efeitos diretos, indiretos, cumulativos e de uso indevido previsível. Quando os impactos forem incertos, a incerteza deve ser registrada em vez de convertida silenciosamente em conclusão de baixo risco.

## Capítulo 08 — Autoridade de liberação e gates fail-closed

Nenhum caso de uso de IA generativa deveria ir para produção apenas porque testes automatizados passaram. A liberação requer evidência documentada suficiente para o caminho escolhido, exceções não resolvidas dentro da tolerância aprovada, aprovação dos responsáveis e qualquer revisão humana exigida.

Um gate de liberação deve falhar fechado quando faltar evidência ou estiver desatualizada; testes obrigatórios estiverem incompletos ou falharem; achados críticos permanecerem abertos sem tratamento aprovado; revisão humana obrigatória estiver ausente, rejeitada ou invalidada por mudança material; aplicabilidade legal, de segurança, privacidade, proteção ou operação estiver sem solução; ou capacidade exigida de parar/reverter não estiver validada.

Mudança material após aprovação reabre os gates de revisão e liberação afetados.
