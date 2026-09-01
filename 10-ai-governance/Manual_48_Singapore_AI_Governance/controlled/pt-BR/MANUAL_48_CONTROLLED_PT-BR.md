# Manual 48 — Governança de IA de Singapura: MGF, GenAI, AI Verify e IA Agêntica

**Status:** DESENVOLVIMENTO CONTROLADO  
**Idioma:** Português do Brasil (`pt-BR`)  
**Linha de base de fontes:** 1 de setembro de 2026

## Objetivo

Converter o ecossistema prático de governança de IA de Singapura em um modelo operacional empresarial. O manual distingue orientação de governança, ferramentas de garantia/testes, exemplos de implementação, trabalhos de normalização propostos e obrigações legais de outras jurisdições. Alinhamento com um framework não é apresentado como certificação nem como conformidade legal automática.

## Módulo 1 — Ecossistema de governança de IA de Singapura

Distinguir as funções do Model AI Governance Framework, do framework para IA generativa, do AI Verify e do Model AI Governance Framework for Agentic AI. Para cada fonte registrar versão/data, status, finalidade e limitações.

**Evidência:** inventário de frameworks, registro de fontes/versões, nota de aplicabilidade e declaração de não equivalência.

## Módulo 2 — Governança organizacional e responsabilização

Estabelecer estrutura de governança, executivo responsável, proprietário do sistema, proprietários de controles, inventário de IA, critérios de risco e autoridades de decisão.

**Evidência:** carta de governança, RACI, política de IA, inventário de sistemas, decisões e exceções.

## Módulo 3 — Envolvimento humano significativo

O envolvimento humano deve corresponder ao impacto e permitir intervenção real. Avaliar autoridade, competência, informação disponível, tempo para intervir e risco de viés de automação.

**Evidência:** matriz de direitos de decisão, limites de aprovação, registros de override/rejeição e treinamento do revisor.

## Módulo 4 — Gestão operacional ao longo do ciclo de vida

Controlar dados, validação, robustez, monitoramento, mudanças, incidentes e retirada. Definir critérios de aceitação, gatilhos de revalidação e capacidade de recuperação.

**Evidência:** plano de ciclo de vida, linhagem/qualidade de dados, relatórios de teste, monitoramento, mudanças e incidentes.

## Módulo 5 — Interação e comunicação com partes interessadas

Comunicar o uso de IA, seu papel e limitações de forma compreensível. Manter canais de feedback quando apropriado e evitar declarações que excedam a evidência.

## Módulo 6 — Governança de IA generativa

Aplicar controles a dados, prompts, RAG, modelos/provedores, segurança, privacidade, procedência de conteúdo, testes e monitoramento. Avaliar alucinação/confabulação, vazamento de dados, conteúdo nocivo, robustez e mudanças do provedor.

**Perguntas-chave:**
- Quais fontes podem entrar no sistema?
- Como dados sensíveis são restringidos?
- Qual conjunto de avaliação demonstra desempenho aceitável?
- Como mudanças de modelo/provedor são detectadas?
- Qual saída exige transparência ou qualificação?

## Módulo 7 — AI Verify e garantia

AI Verify é usado como mecanismo de testes e garantia. Não deve ser interpretado como prova universal de segurança, ausência de viés, conformidade legal ou certificação.

**Fluxo:** definir alegações → selecionar verificações/testes → registrar condições e limitações → executar → analisar falhas → remediar → retestar após mudanças materiais.

## Módulo 8 — IA agêntica: avaliar e limitar riscos

Registrar finalidade, autonomia, ferramentas/APIs, dados, ações, comunicações externas, execução de código, transações, sistemas externos, interações multiagente e reversibilidade.

**Controles:** identidade separada, privilégio mínimo, listas de permissão/bloqueio, limites de transação/volume, segmentação e estado seguro diante de incerteza.

## Módulo 9 — IA agêntica: responsabilização humana

Definir pontos de controle humanos significativos antes de ações de alto impacto ou irreversíveis, por exemplo: entrada em produção, nova ferramenta privilegiada, pagamento, mudança de configuração crítica, exclusão irreversível ou exceção de segurança.

**Evidência:** catálogo de pontos de aprovação, identidade do aprovador, contexto, horário, ações rejeitadas e escalonamento.

## Módulo 10 — Controles técnicos e de processo para agentes

- identidade autenticada do agente/serviço;
- privilégio mínimo e credenciais limitadas;
- ferramentas/APIs explicitamente autorizadas;
- validação de entradas, saídas e ações;
- proteção dos limites prompt/ferramenta/dados;
- isolamento ou sandbox quando apropriado;
- registro completo e procedência das ações;
- monitoramento de anomalias;
- limites de taxa/recursos;
- mecanismo de parada e contenção;
- inventário de dependências;
- controle de terceiros;
- mudanças e revalidação.

## Módulo 11 — Sistemas multiagente

Documentar cadeias de delegação, permissões entre agentes, memória compartilhada, identidade, conflitos e responsabilização. Evitar propagação implícita de privilégios e preservar rastreabilidade ponta a ponta.

## Módulo 12 — Terceiros e cadeia de fornecimento

Avaliar modelos, agentes, ferramentas e provedores externos. Contratar controles de segurança/privacidade, mudanças, incidentes, evidências e saída. Revalidar quando capacidades, APIs, modelos ou políticas do provedor mudarem.

## Módulo 13 — Viés de automação

Medir situações em que usuários/revisores aceitam resultados sem julgamento independente. Analisar taxas de override/disagreement, criar verificações independentes e treinar quem exerce supervisão.

## Módulo 14 — Evidência e auditabilidade

Para cada controle manter:

**Conceito-fonte → interpretação organizacional → objetivo de controle → proprietário → implementação → evidência → método de teste → resultado → achado → remediação → risco residual.**

## Módulo 15 — Mapeamento entre frameworks sem falsa equivalência

Relacionar controles ao Manual 46, EU AI Act, ISO/IEC 42001 e NIST AI RMF apenas quando houver relação defensável. Classificar como direta, parcial, de apoio ou contextual e registrar diferenças de escopo, atores, status jurídico e evidência.

## Módulo 16 — Roteiro empresarial

### Primeiros 30 dias
- proprietário de governança e inventário;
- classificação de casos de uso;
- identificação dos agentes de maior risco;
- pontos humanos significativos;
- repositório de evidências.

### 60 dias
- controles do ciclo de vida;
- revisões de acesso e terceiros;
- programa de testes/garantia;
- resposta a incidentes/contenção;
- treinamento.

### 90 dias
- testes independentes conforme o risco;
- revisão de permissões de agentes;
- análise de viés de automação;
- fechamento de achados;
- painel de governança.

## Cenários práticos

1. assistente GenAI de atendimento com dados confidenciais;
2. agente financeiro com autoridade de pagamentos;
3. agente de recrutamento e viés de automação;
4. agente de programação de terceiro com acesso a repositórios/CI/CD;
5. operação de viagens multiagente;
6. chatbot público de orientação sem autoridade decisória;
7. exercício sobre alegações de AI Verify;
8. ampliação de capacidades após atualização de provedor;
9. revisão executiva de achados de agentes;
10. desafio de mapeamento entre frameworks.

## Domínios mínimos de controle

- governança e responsabilização;
- inventário e risco;
- envolvimento humano;
- ciclo de vida;
- dados/RAG;
- testes e garantia;
- identidade de agentes;
- autorização/privilégio mínimo;
- limites de ferramentas/APIs;
- procedência de ações;
- multiagente;
- terceiros;
- monitoramento;
- contenção/incidentes;
- mudanças/revalidação;
- transparência ao usuário;
- não equivalência entre frameworks.

## Critério de conclusão

A pessoa que concluir o Manual 48 deve conseguir transformar um conceito de governança de Singapura em um controle empresarial defensável, com proprietário, evidência, método de teste, tratamento de falhas e nota de limitação, sem afirmar certificação ou equivalência jurídica não sustentada.