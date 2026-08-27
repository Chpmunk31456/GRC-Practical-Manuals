# Manual 07 — Segurança de IA e Controles do Ciclo de Vida
## Fonte controlada em português brasileiro — Capítulos 01–08

> Tradução de trabalho sujeita à revisão semântica humana. Esta orientação original de implementação de segurança operacionaliza a linha de base controlada sem reproduzir texto de normas. Ela não garante segurança, segurança operacional, conformidade ou ausência de vulnerabilidades exploráveis.

## Capítulo 01 — Objetivo de segurança e limite do ciclo de vida

A segurança de IA deve abranger todo o ciclo de vida do sistema, e não apenas o endpoint do modelo. O limite controlado inclui definição do caso de uso, aquisição de dados e modelos, projeto, desenvolvimento, avaliação, implantação, operação, monitoramento, resposta a incidentes, mudanças e desativação.

Cada sistema deve ter um objetivo de segurança documentado ligado aos seus dados, ações, usuários, autonomia, conectividade externa e consequências de falha.

## Capítulo 02 — Inventário de ativos de IA

O inventário deve identificar modelos, conjuntos de dados, prompts, fontes de recuperação, bancos vetoriais, ferramentas, agentes, APIs, contas de serviço, segredos, guardrails, componentes de monitoramento, ambientes de hospedagem, fornecedores e sistemas críticos a jusante.

Os registros de inventário devem incluir responsável, versão, localização, classificação de dados, limite de autenticação, fornecedor, exposição, autoridade de mudança e status de desativação. Componentes desconhecidos criam superfície de ataque não gerenciada.

## Capítulo 03 — Modelagem de ameaças

A modelagem de ameaças deve identificar ativos, limites de confiança, atores, pontos de entrada, privilégios, dependências e caminhos plausíveis de abuso. Ameaças específicas de IA devem ser avaliadas junto com ameaças convencionais de aplicação, nuvem, identidade, dados e cadeia de suprimentos.

Os cenários devem incluir usuários maliciosos, conteúdo de recuperação comprometido, agentes com privilégios excessivos, segredos expostos, APIs inseguras, execução insegura de ferramentas, dados envenenados, divulgação de modelo ou prompt, comprometimento de fornecedor e comportamento autônomo não intencional quando relevante.

## Capítulo 04 — Desenvolvimento seguro e controle de mudanças

Componentes de IA devem ser desenvolvidos e alterados por meio de repositórios controlados, revisão, testes, gestão de dependências, controle de acesso e processos de liberação. Mudanças em prompts, políticas, recuperação, ferramentas e guardrails podem ser relevantes para segurança e não devem contornar controles de mudança apenas por não serem código tradicional.

Mudanças materiais exigem reavaliação das evidências de segurança anteriores e podem reabrir a aprovação de liberação.

## Capítulo 05 — Proveniência de dados e modelos

As equipes de segurança devem conseguir identificar a origem de modelos, conjuntos de dados, pesos, adaptadores, pacotes, prompts e componentes externos, além de quem aprovou seu uso.

Os registros de proveniência devem incluir origem, versão, evidência de integridade quando disponível, limites de licença ou uso, fornecedor, aprovação, histórico de transformação e limitações conhecidas. A proveniência apoia decisões de confiança, mas não prova que um componente seja seguro.

## Capítulo 06 — Identidade, privilégio mínimo e autorização de ferramentas

Sistemas de IA que invoquem ferramentas ou ações externas devem usar identidades explícitas e permissões de privilégio mínimo. O modelo não deve receber credenciais amplas apenas porque a aplicação precisa acessar múltiplas funções.

Sempre que possível, a autorização deve ser aplicada fora do modelo. Ações de alto impacto devem usar verificações de política, credenciais com escopo restrito, limites de transação, aprovação humana ou outros controles determinísticos adequados ao risco.

## Capítulo 07 — Injeção de prompts e conteúdo não confiável

A injeção direta e indireta de prompts deve ser tratada como ameaça de segurança quando entradas não confiáveis puderem influenciar comportamento privilegiado, expor informações sensíveis, alterar instruções do sistema ou causar uso inseguro de ferramentas.

Os controles podem incluir isolamento de conteúdo, limites de permissão, filtragem de recuperação, validação de saída, listas permitidas de ferramentas, separação de contexto, privilégios reduzidos, etapas de confirmação e monitoramento. Nenhum prompt ou classificador isolado deve ser tratado como defesa completa.

## Capítulo 08 — Gate de liberação de segurança fail-closed

A liberação deve falhar de forma fechada quando faltar evidência crítica de segurança, achados materiais permanecerem sem tratamento aprovado, testes adversariais obrigatórios não tiverem sido concluídos, rollback ou contenção forem necessários mas não testados, ou revisão humana obrigatória estiver incompleta.

Um workflow automatizado verde apoia a decisão de liberação, mas não garante que o sistema seja seguro. A aprovação final permanece um gate controlado por humanos, e mudanças materiais após a revisão reabrem a análise de segurança afetada.
