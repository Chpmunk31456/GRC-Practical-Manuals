# Manual 35 — Implementação Controlada de Governança de IA e Privacidade de Singapura

**Idioma:** Português do Brasil (pt-BR)  
**Linha de base controlada:** PDPA/PDPC de Singapura mais os recursos atuais de governança para IA tradicional, IA generativa, AI Verify e IA agêntica, verificados em 31 de agosto de 2026.  
**Limite:** Lei/regulação vinculante, orientação e enforcement do regulador, frameworks voluntários de IA, overlays setoriais e práticas da organização permanecem distintos. Esta é uma tradução de projeto não oficial e não constitui aconselhamento jurídico, aprovação regulatória ou certificação.

## Chapter 01 — Objetivo, escopo e hierarquia controlada de fontes
Use a PDPA e os regulamentos aplicáveis como camada vinculante de privacidade. Classifique materiais da PDPC, IMDA, AI Verify, reguladores setoriais, contratos e procedimentos internos conforme seu verdadeiro status jurídico. Mantenha registro datado de fontes, responsáveis e mudanças materiais.

## Chapter 02 — Ecossistema regulatório e de governança de Singapura
Mapeie PDPC, IMDA, reguladores setoriais, contrapartes contratuais e órgãos internos. Identifique explicitamente se cada requisito decorre de lei, regulamento, orientação, contrato ou framework voluntário.

## Chapter 03 — Aplicabilidade da PDPA, exclusões e papéis organizacionais
Documente se a PDPA se aplica à organização, atividade, dados e relacionamento analisados. Preserve distinções relativas a indivíduos em caráter pessoal, agências públicas, dados de empregados, business contact information, data intermediaries e outras exceções aplicáveis.

## Chapter 04 — Accountability e governança do Data Protection Officer
Estabeleça governança de privacidade com DPO designado, supervisão executiva, responsabilidades claras, recursos, escalonamento e revisão gerencial. Preserve nomeações, charters, políticas, relatórios, issues e ações corretivas.

## Chapter 05 — Notification, consentimento e retirada de consentimento
Projete coleta, uso e disclosure para informar finalidades e obter consentimento quando exigido. Permita retirada com aviso razoável e documente exceções ou bases alternativas válidas.

## Chapter 06 — Purpose Limitation e raciocínio de finalidade apropriada
Avalie se cada coleta, uso ou disclosure serve a uma finalidade que uma pessoa razoável consideraria apropriada. Novos usos habilitados por IA não devem herdar automaticamente autorização da finalidade original.

## Chapter 07 — Accuracy e controles de impacto em decisões
Aplique controles proporcionais de exatidão e completude quando dados pessoais puderem afetar decisões ou ser divulgados. Para decisões apoiadas por IA, teste qualidade, atualidade, representatividade e caminhos de erro material.

## Chapter 08 — Protection Obligation e medidas razoáveis de segurança
Implemente salvaguardas administrativas, técnicas e físicas razoáveis conforme sensibilidade, volume, uso e ameaças. Inclua sistemas de IA em IAM, configuração segura, logging, vulnerability management, proteção de dados, resiliência e incident response.

## Chapter 09 — Retention Limitation e descarte defensável
Interrompa a retenção de dados pessoais quando eles deixarem de ser necessários para fins legais ou de negócio. Inclua training data, avaliações, prompts, logs, embeddings, backups, memórias de agentes e dados derivados nas regras de retenção.

## Chapter 10 — Transfer Limitation e transferências internacionais
Antes de transferir dados para fora de Singapura, determine o mecanismo aplicável e a proteção comparável exigida pela PDPA. Mantenha assessments, contratos, due diligence, data flows, exceções e reavaliação periódica.

## Chapter 11 — Operações de acesso e correção
Implemente intake, identity verification, busca, review, resposta, correção, exceções e escalonamento. Inclua cópias e dados derivados usados por IA quando aplicável.

## Chapter 12 — Avaliação e notificação obrigatória de data breaches
Avalie breaches segundo os critérios atuais de significant harm e/ou significant scale. Após determinar que o breach é notificável, notifique a PDPC assim que praticável e no máximo em três dias corridos após essa determinação, além de tratar a notificação aos indivíduos quando exigida.

## Chapter 13 — Data intermediaries e responsabilidades contratuais
Identifique papéis de data intermediary e distribua responsabilidades contratuais e operacionais. Cubra instruções, segurança, breach escalation, subprocessors, retenção, transferências, audit evidence e termination.

## Chapter 14 — Data Portability: change-watch e ativação
Trate Data Portability como não operacional até a entrada em vigor dos regulamentos necessários. Mantenha monitoramento formal, readiness assessment e ponto de decisão para futura ativação.

## Chapter 15 — Inventário de dados, classificação, lineage e processing records
Mantenha inventário de dados pessoais, sistemas, repositórios, modelos, agentes, fluxos, finalidades, owners, retenção, recipients e locais de transferência. A lineage deve mostrar como os dados entram, alimentam e saem de sistemas de IA.

## Chapter 16 — Privacy by Design e Data-Protection Impact Assessment
Integre privacidade aos ciclos de product, system, AI, procurement e change. Use impact assessment proporcional para high-risk processing, novas tecnologias, dados sensíveis, decisões automatizadas ou mudanças materiais.

## Chapter 17 — Intake de casos de uso de IA e classificação de risco
Registre cada caso material de IA antes de produção. Documente finalidade, usuários, pessoas afetadas, dados, modelo ou agente, terceiros, autonomia, impacto decisório, privacidade, segurança e overlays regulatórios.

## Chapter 18 — Implementação do framework de IA tradicional
Use o Model AI Governance Framework tradicional como orientação voluntária para governance interno, human involvement, operations management e stakeholder communication. Não o apresente como certificação legal ou regulatória.

## Chapter 19 — Implementação do framework de IA generativa
Aplique o framework de GenAI a accountability, data, trusted development/deployment, incident reporting, testing/assurance, security, provenance, safety/alignment e ecosystem considerations conforme o caso de uso.

## Chapter 20 — Implementação do framework de IA agêntica
Avalie e limite autonomia, acesso a tools/data, transaction authority, persistence e delegation. Defina human approval checkpoints, lifecycle controls, monitoring, transparency, training, third-party agents, multi-agent risk e safeguards contra automation bias.

## Chapter 21 — Accountability humana, checkpoints e meaningful oversight
Atribua humanos ou órgãos responsáveis pelos resultados de IA. O oversight deve ter informação, autoridade, competência, tempo e capacidade real de intervenção; revisão nominal não é controle significativo.

## Chapter 22 — AI data governance, provenance, quality e minimisation
Governe training, retrieval, evaluation, prompts, fine-tuning, telemetry e agent memory com provenance, permitted use, quality, minimisation, access, retention e transfer controls documentados.

## Chapter 23 — Fairness, bias, explainability, transparency e contestability
Identifique riscos de fairness e bias conforme o contexto, defina necessidades de explicação, comunique o uso de IA e forneça revisão ou contestability quando exigido por risco, lei, contrato ou compromissos internos.

## Chapter 24 — AI security, robustness, testing e lifecycle controls
Integre IA com secure development, change management, model/dependency governance, access control, secrets, logging, evaluation, robustness testing, incident response e retirement. Maior autonomia exige controles mais fortes.

## Chapter 25 — AI Verify e limites de assurance/testing
Use AI Verify como mecanismo voluntário de testing e evidência quando útil. Resultados devem permanecer vinculados ao sistema, versão, dados, configuração, benchmark e data; não são prova universal de segurança, legalidade ou aprovação regulatória.

## Chapter 26 — Third-party models, agents, processors e supply chain
Execute due diligence baseada em risco para providers, hosted AI, processors, agent platforms, plugins, tools e dependencies críticas. Cubra data handling, confidentiality, security, subprocessors, changes, incidents, retention, transfers, evidence e exit.

## Chapter 27 — Multi-agent systems, tool access e bounded authority
Documente interações permitidas, authority limits, handoffs, shared context, external services e approval boundaries. Cada agente deve receber apenas dados, tools, credentials e actions necessários à finalidade aprovada.

## Chapter 28 — Comunicações, notices, feedback e responsible use
Comunique participação material de IA, finalidade, limitações, responsabilidades e opções de escalonamento. Treine sobre over-reliance, confidentiality, data entry, approval duties e mandatory human review.

## Chapter 29 — Integração de incidentes, privacy breaches e AI harm
Integre incidentes de IA com cybersecurity, privacy, operational risk, legal, communications e executives. Distinga security event, personal-data breach, model defect, harmful output, control failure e regulatory trigger.

## Chapter 30 — Monitoring, métricas, enforcement learnings e melhoria contínua
Use métricas que demonstrem efetividade. Analise enforcement da PDPC e atualizações da IMDA para identificar implicações de controle sem transformar fatos específicos em regras universais.

## Chapter 31 — Arquitetura de evidência, auditability e crosswalk governance
Permita rastreabilidade de requirement ou commitment até owner, control, operation, test, exception e remediation. Crosswalks podem demonstrar relações, mas não equivalência jurídica ou de controles sem análise fundamentada.

## Chapter 32 — Change control legal/framework e roadmap de implementação
Antes do release, reverifique PDPA/PDPC, Data Portability, breach notification, frameworks Traditional/GenAI/Agentic AI, AI Verify e overlays setoriais. Mudanças materiais após o candidate freeze exigem impact assessment e, quando necessário, candidate substituto com nova provenance.
