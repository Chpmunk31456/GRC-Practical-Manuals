# Manual 39 — Implementação Controlada da COPPA

**Linha de base controlada:** Children's Online Privacy Protection Act, 15 U.S.C. §§ 6501–6506, e 16 CFR Part 312 vigente, incluindo as emendas finais da FTC de 2025.  
**Limite:** guidance, policy statements, materiais de safe harbor da FTC, leis estaduais de privacidade infantil, obrigações educacionais, contratos e práticas internas permanecem como camadas separadas.  
**Regra de release:** reverificar o 16 CFR Part 312, o estado das emendas e as datas de vigência no congelamento do candidato.

## Chapter 01 — Propósito, escopo e hierarquia controlada de fontes
Defina o escopo COPPA, a hierarquia de fontes, ownership e controle de mudanças. Mantenha registro de aplicabilidade, fontes, responsáveis, evidências e change watch.

## Chapter 02 — Aplicabilidade do operador e do serviço
Determine se a organização atua como operator ou está no escopo da COPPA. Documente propriedade do site/app, relações de serviço, fluxos de coleta e pressupostos jurisdicionais.

## Chapter 03 — Análise de serviços direcionados a crianças
Use fatores documentados para avaliar se site, app, feature ou audiência é child-directed. Preserve evidências de audiência, conteúdo, design, marketing, analytics e uso pretendido.

## Chapter 04 — Conhecimento real e audiências mistas
Defina como o actual knowledge sobre usuários menores de 13 anos é identificado, escalado e tratado. Para mixed audiences, documente age-screening, consequências e controles contra evasão.

## Chapter 05 — Inventário de informações pessoais
Inventarie identificadores, contatos, persistent identifiers, mídia, geolocalização, comportamento, dispositivo, conteúdo gerado por usuários e demais informações relevantes. Mapeie coleta, uso, disclosure, storage e deletion.

## Chapter 06 — Governança e accountability
Atribua funções legal/privacy, produto, security, engineering, marketing, data, procurement, support e executive. Mantenha RACI, approvals, exceptions e management-review evidence.

## Chapter 07 — Aviso direto aos pais
Defina quando e como o direct notice é entregue antes da coleta ou de mudanças materiais quando aplicável. Mantenha versões, evidência de entrega, timing, aprovação e accessibility records.

## Chapter 08 — Aviso de privacidade on-line
Mantenha privacy notice claro, completo e atual sobre operators cobertos, práticas de informação, direitos parentais, disclosures, retention e contatos aplicáveis.

## Chapter 09 — Estrutura de consentimento parental verificável
Estabeleça processo controlado para selecionar e operar métodos de verifiable parental consent adequados ao uso e risco. Preserve consent evidence, rationale, validação de identidade/autoridade e revogação.

## Chapter 10 — Exceções ao consentimento
Exija análise documentada antes de depender de coleta ou uso que possa ocorrer sem consentimento prévio. Registre base, escopo, propósito, dados, duração e controles contra expansão indevida.

## Chapter 11 — Minimização de dados
Limite a coleta às informações razoavelmente necessárias para a participação da criança na atividade ou serviço, conforme os requisitos aplicáveis. Mantenha necessity assessments e evidências de design.

## Chapter 12 — Limitação de finalidade e uso secundário
Defina usos permitidos para child data e impeça secondary uses incompatíveis, profiling, advertising ou reutilização sem a análise e o consentimento exigidos.

## Chapter 13 — Controles de publicidade e uso comercial
Governe targeted advertising, behavioral advertising, contextual advertising, measurement, attribution e monetization envolvendo child data. Separe requisitos regulatórios de políticas internas de risco.

## Chapter 14 — Persistent identifiers, cookies e SDKs
Inventarie cookies, pixels, SDKs, device identifiers, analytics, ad-tech e código incorporado. Documente propósito, fornecedor, fluxos, configuração, efeitos de consentimento e controles de desativação.

## Chapter 15 — Governança de disclosures a terceiros
Controle disclosures a service providers, platforms, ad-tech, analytics, processors e outros recipients. Mantenha inventário, propósito, necessidade, contratos, restrições downstream e monitoring.

## Chapter 16 — Ciclo de vida de vendors e service providers
Aplique due diligence de child data antes do onboarding. Avalie collection, use, disclosure, security, retention, subprocessors, incident support, deletion, audit rights e termination.

## Chapter 17 — Casos escolares e EdTech
Avalie usos autorizados por escolas sem presumir exceção COPPA universal. Documente papel do operator, autoridade escolar, comunicações parentais, uso de dados, restrições comerciais e overlays FERPA/estaduais separadamente.

## Chapter 18 — Acesso, revisão, exclusão e recusa parental
Implemente workflows para direitos aplicáveis dos pais de revisar informações, solicitar deletion e recusar collection/use futura. Mantenha validação, timing, search, response e closure evidence.

## Chapter 19 — Age-screening e design neutro
Projete age screens e audience controls sem induzir resposta específica. Mantenha testes, bypass monitoring, exception handling e product-change reviews.

## Chapter 20 — Salvaguardas de segurança
Implemente safeguards administrativos, técnicos e físicos razoáveis. Mantenha access controls, encryption decisions, secure configuration, logging, vulnerability management, monitoring e corrective actions.

## Chapter 21 — Retenção e exclusão
Retenha child personal information apenas pelo tempo razoavelmente necessário ao propósito e faça exclusão segura quando não for mais exigida, salvo exceções documentadas.

## Chapter 22 — Incident response e breach analysis
Integre incidentes de child data com incident response, revisão legal/privacy, evidence preservation, contratos, análise de leis estaduais e obrigações FTC/orders aplicáveis.

## Chapter 23 — Desenvolvimento de produto e privacy engineering
Integre COPPA a requirements, design, architecture, testing, release, experimentation e change management. Exija privacy review para novos dados, features, integrations e mudanças de monetização.

## Chapter 24 — AI, personalização e recursos automatizados
Avalie assistants, recommendations, moderation, profiling, inference, biometrics e generative features quanto a collection, secondary use, model training, disclosure, retention e transparency risks.

## Chapter 25 — Governança de safe harbor
Quando houver dependência de FTC-approved COPPA safe harbor, documente membership, requisitos, monitoring, assessments, corrective actions e a fronteira entre o programa e a regra subjacente.

## Chapter 26 — Overlays estaduais de privacidade infantil e setoriais
Mantenha análise separada para child/teen privacy, consumer privacy, education, biometrics, health, gaming e outros overlays. Não apresente deveres do overlay como requisitos COPPA.

## Chapter 27 — Gestão de registros e evidências
Preserve notices, consent records, age-screening decisions, vendor records, data inventories, disclosures, rights requests, retention/deletion evidence, incidents, training, testing e approvals sob retenção controlada.

## Chapter 28 — Treinamento e competência por função
Forneça training por função para product, engineering, design, marketing, data, privacy, legal, security, procurement, support e leadership. Registre completion, competency checks, remediation e refresh triggers.

## Chapter 29 — Assurance e testing
Teste notices, consent flows, age screens, SDK inventories, vendor controls, rights handling, retention/deletion, security controls e decisões child-directed. Mantenha samples, findings, remediation e retest evidence.

## Chapter 30 — Métricas e management review
Acompanhe consent failures, bypass rates, unauthorized SDKs, vendor findings, rights-request timing, retention exceptions, incidents, training completion e remediation aging.

## Chapter 31 — Localização exact-hash, provenance e evidência de release
Congele candidatos EN/es-419/pt-BR antes do review final. Vincule DOCX/PDF a SHA-256 e preserve evidências de localization, accessibility, rendered-page, workflow-security e release QA.

## Chapter 32 — Roadmap de implementação e reverificação no release
Implemente por fases: applicability; data inventory; notices/consent; product/vendor controls; rights; security; retention; assurance; metrics; continual improvement. Antes de publicar, reverifique texto FTC vigente, emendas, effective dates e overlays expressamente reivindicados. A publicação permanece sequencial após o Manual 38.
