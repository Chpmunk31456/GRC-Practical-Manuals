# Manual 28 — Implementação Controlada de Privacidade em IA e Governança de Decisões Automatizadas

Tradução não oficial do projeto para português do Brasil. A fonte controladora do projeto é a edição em inglês. Este manual operacionaliza controles de governança e evidência; não constitui aconselhamento jurídico nem transforma orientação voluntária em obrigação legal. Obrigações específicas de cada jurisdição devem ser validadas para cada implantação e caso de uso.

## 01. Propósito, escopo e limite de uso controlado
**Camada de fonte:** NIST Privacy Framework 1.0, NIST AI RMF 1.0, governança interna e camadas legais aplicáveis.
**Aplicabilidade:** Sistemas assistidos por IA, algorítmicos, de perfilamento e decisão automatizada que processem dados pessoais ou vinculáveis a pessoas, ou afetem materialmente indivíduos.
**Responsável:** Líder de governança de IA com privacidade/jurídico, segurança, produto e responsáveis de negócio.
**Procedimento:** Definir escopo, populações afetadas, papel da decisão, uso de dados pessoais, jurisdições, usos excluídos e objetivos de implementação antes da implantação.
**Evidência:** Registro de escopo aprovado, identificador do sistema, responsáveis, mapa jurisdicional e limite de liberação.
**Revisão/teste:** Confirmar que o escopo corresponde ao comportamento e aos fluxos de dados em produção.
**Remediação/reavaliação:** Corrigir lacunas e reavaliar após mudanças materiais de uso, jurisdição, modelo ou dados.

## 02. Hierarquia de fontes, jurisdição e monitoramento de mudanças
**Camada de fonte:** Lei/regulamento aplicável; orientação de reguladores; contratos; NIST PF/AI RMF; políticas e padrões internos.
**Aplicabilidade:** Todo sistema regido por este manual.
**Responsável:** Jurídico/privacidade com governança de IA e compliance.
**Procedimento:** Manter registro que diferencie obrigações vinculantes de orientação voluntária e separe material em rascunho ou desenvolvimento.
**Evidência:** Registro de fontes, versão/data, autoridade, justificativa de aplicabilidade e log de monitoramento.
**Revisão/teste:** Verificar o status das fontes imediatamente antes do congelamento do candidato e após mudanças regulatórias materiais.
**Remediação/reavaliação:** Atualizar mapeamentos e controles sem tratar retroativamente rascunhos como obrigatórios.

## 03. Inventário de sistemas de IA/decisão automatizada e propriedade
**Camada de fonte:** Conceitos de inventário e accountability do NIST e governança interna de ativos.
**Aplicabilidade:** Usos produtivos, pilotos, incorporados, adquiridos, baseados em API e não registrados.
**Responsável:** Proprietário de negócio do sistema e governança de IA.
**Procedimento:** Manter inventário autoritativo de propósito, modelo/provedor, domínios de dados, papel da decisão, ambientes, usuários, pessoas afetadas e responsáveis.
**Evidência:** Registro de inventário, estado do ciclo de vida, proprietário de negócio, técnico e de privacidade, e data de revisão.
**Revisão/teste:** Conciliar com compras, APIs, contas cloud, registros de modelos e plataformas de dados.
**Remediação/reavaliação:** Registrar sistemas não controlados e escalar usos não autorizados.

## 04. Taxonomia de decisões e classificação de consequências
**Camada de fonte:** Taxonomia interna informada por NIST e definições legais aplicáveis.
**Aplicabilidade:** Todo sistema que influencie decisão sobre uma pessoa.
**Responsável:** Proprietário de produto/negócio com privacidade/jurídico e risco de IA.
**Procedimento:** Classificar como assistivo, recomendatório, automatizado ou consequencial e documentar se uma pessoa pode alterar materialmente o resultado.
**Evidência:** Registro de taxonomia, nível de consequência, descrição do papel humano e cruzamento com definições legais quando aplicável.
**Revisão/teste:** Testar o fluxo real contra a classificação declarada.
**Remediação/reavaliação:** Reclassificar quando automação, dependência ou consequência mudar.

## 05. Linhagem de dados e fluxo do modelo
**Camada de fonte:** Orientação de engenharia de privacidade/governança de dados do NIST e controles internos de arquitetura.
**Aplicabilidade:** Fluxos de treinamento, avaliação, inferência, enriquecimento, feedback e decisão.
**Responsável:** Arquiteto/engenheiro de dados com privacidade e proprietário do modelo.
**Procedimento:** Mapear fontes, transformações, características, chamadas ao modelo, saídas, destinatários, armazenamentos, transferências e ciclos de feedback.
**Evidência:** Diagramas de fluxo, registros de linhagem, inventário de interfaces e mapa de transferências.
**Revisão/teste:** Rastrear registros representativos de ponta a ponta.
**Remediação/reavaliação:** Corrigir fluxos não documentados e reavaliar após mudanças de pipeline.

## 06. Especificação de finalidade e limitação de uso
**Camada de fonte:** Princípios de governança de privacidade, contratos, requisitos legais aplicáveis e política interna.
**Aplicabilidade:** Coleta, reutilização, inferência e processamento para decisões.
**Responsável:** Proprietário de negócio com privacidade/jurídico.
**Procedimento:** Registrar finalidades aprovadas, usos compatíveis, usos proibidos, gatilhos de revisão de uso secundário e limites de decisão.
**Evidência:** Registro de finalidade, casos aprovados, lista de usos proibidos e exceções.
**Revisão/teste:** Comparar características, prompts, análises e usos posteriores reais com finalidades aprovadas.
**Remediação/reavaliação:** Interromper ou corrigir usos incompatíveis e reavaliar antes da expansão.

## 07. Governança de dados de treinamento e avaliação
**Camada de fonte:** NIST AI RMF, controles de privacidade/dados, contratos e lei aplicável.
**Aplicabilidade:** Dados usados para treinar, ajustar, avaliar, calibrar ou comparar modelos.
**Responsável:** Proprietário do modelo/dados com privacidade, segurança e jurídico.
**Procedimento:** Documentar procedência, autorização, representatividade, sensibilidade, retenção, qualidade, exclusões e usos permitidos.
**Evidência:** Fichas de datasets, procedência, licenças/contratos, testes de qualidade, aprovações e obrigações de exclusão.
**Revisão/teste:** Amostrar registros de origem e verificar permissões e usos declarados.
**Remediação/reavaliação:** Remover ou substituir dados não conformes e retreinar/retestar quando o impacto for material.

## 08. Governança de dados sensíveis e inferidos
**Camada de fonte:** Lei de privacidade/setor aplicável, orientação regulatória e classificação interna.
**Aplicabilidade:** Identificadores sensíveis, saúde, finanças, biometria, localização precisa, dados de crianças, características protegidas onde reguladas e inferências sensíveis.
**Responsável:** Privacidade/jurídico com proprietário de dados e governança de IA.
**Procedimento:** Identificar entradas e inferências sensíveis, aplicar controles reforçados de acesso/minimização e documentar restrições jurisdicionais.
**Evidência:** Registro de dados sensíveis, inventário de inferências, regras de acesso, controles de mascaramento e análise de aplicabilidade.
**Revisão/teste:** Revisar características e saídas por inferências sensíveis não declaradas.
**Remediação/reavaliação:** Suprimir, restringir ou redesenhar o processamento e reavaliar base legal e risco.

## 09. Avaliação de risco e danos à privacidade
**Camada de fonte:** NIST Privacy Framework/engenharia de privacidade e deveres de avaliação aplicáveis.
**Aplicabilidade:** Sistemas com risco material de privacidade, autonomia, economia, reputação, segurança ou vigilância.
**Responsável:** Proprietário do risco de privacidade com governança de IA e negócio.
**Procedimento:** Identificar pessoas afetadas, ações de dados prejudiciais, probabilidade, severidade, escala, reversibilidade, mitigações e risco residual.
**Evidência:** Avaliação de risco, cenários de dano, plano de tratamento, aceitação residual e data de revisão.
**Revisão/teste:** Desafiar premissas com cenários representativos e perspectivas de populações afetadas quando viável.
**Remediação/reavaliação:** Implementar controles adicionais ou interromper o uso se o risco residual exceder a tolerância.

## 10. Interfaces de DPIA e avaliação de impacto de IA
**Camada de fonte:** Requisitos jurisdicionais aplicáveis e métodos internos de risco IA/privacidade.
**Aplicabilidade:** Usos que atinjam limiares legais ou internos para avaliação formal.
**Responsável:** Privacidade/jurídico e governança de IA.
**Procedimento:** Determinar se é necessária DPIA, avaliação de impacto de IA, algorítmica ou equivalente, sem presumir que uma avaliação satisfaça automaticamente outra jurisdição.
**Evidência:** Análise de limiar, avaliações concluídas, aprovações, consultas e decisões de risco residual.
**Revisão/teste:** Confirmar que a avaliação cobre sistema, dados, pessoas e contexto reais.
**Remediação/reavaliação:** Reabrir avaliações após mudanças materiais de modelo, finalidade, população, dados ou implantação.

## 11. Análise de aplicabilidade de decisões automatizadas
**Camada de fonte:** Lei e orientação específica por jurisdição sobre decisões automatizadas/perfilamento.
**Aplicabilidade:** Decisões realizadas ou materialmente influenciadas por processamento automatizado.
**Responsável:** Jurídico/privacidade com proprietário do processo de negócio.
**Procedimento:** Determinar definições, exclusões, limiares, avisos, direitos, revisão humana, testes e documentação aplicáveis por jurisdição/caso.
**Evidência:** Matriz de aplicabilidade, revisão jurídica, classificação do sistema e mapeamento de controles.
**Revisão/teste:** Comparar automação e discricionariedade humana reais com a análise.
**Remediação/reavaliação:** Atualizar controles quando a automação ou o escopo legal mudar.

## 12. Governança de perfilamento e personalização
**Camada de fonte:** Regras aplicáveis de privacidade/proteção do consumidor e governança interna de analytics.
**Aplicabilidade:** Predição comportamental, segmentação, ranking, recomendação, targeting e personalização de indivíduos.
**Responsável:** Proprietário de produto/negócio com privacidade e governança de dados.
**Procedimento:** Documentar finalidade, entradas, atributos inferidos, destinatários, nível de consequência, interfaces de direitos/opt-out quando aplicáveis e perfis proibidos.
**Evidência:** Registro de perfilamento, lista de características, definições de audiência, mapeamento de direitos e aprovações.
**Revisão/teste:** Testar perfilamento não declarado e reutilização incompatível.
**Remediação/reavaliação:** Restringir ou redesenhar e reavaliar avisos e direitos.

## 13. Arquitetura de transparência e avisos
**Camada de fonte:** Deveres aplicáveis de transparência/aviso, conceitos NIST e padrões internos de comunicação.
**Aplicabilidade:** Pessoas que interagem materialmente com ou são afetadas por IA/ADM.
**Responsável:** Produto/negócio com privacidade/jurídico e comunicações.
**Procedimento:** Fornecer avisos em camadas que descrevam corretamente papel do sistema, uso de dados, contexto da decisão, limitações materiais, direitos/opções quando aplicáveis e canais de escalonamento.
**Evidência:** Avisos aprovados, histórico de versão, evidência de entrega, controles de idioma/acessibilidade e log de mudanças.
**Revisão/teste:** Comparar afirmações com comportamento real.
**Remediação/reavaliação:** Corrigir avisos enganosos, obsoletos ou incompletos.

## 14. Governança de explicabilidade e códigos de razão
**Camada de fonte:** Deveres aplicáveis de explicação/razão, conceitos NIST AI RMF e padrões internos de risco de modelos.
**Aplicabilidade:** Decisões que exigem razão compreensível para usuários, revisores, auditores ou pessoas afetadas.
**Responsável:** Proprietário do modelo com negócio, jurídico/privacidade e risco de modelos.
**Procedimento:** Definir público, método, lógica de códigos de razão, requisitos de fidelidade, limitações e escalonamento para resultados não explicáveis.
**Evidência:** Especificação de explicação, catálogo de razões, validações e amostras de explicações.
**Revisão/teste:** Testar fidelidade e consistência contra os fatores reais de decisão.
**Remediação/reavaliação:** Corrigir explicações enganosas ou restringir o uso.

## 15. Mecanismos de contestação e recurso
**Camada de fonte:** Direitos aplicáveis e deveres de consumidor/emprego/setor, além de política interna.
**Aplicabilidade:** Resultados consequenciais ou recorríveis.
**Responsável:** Proprietário do processo com jurídico/privacidade e operações.
**Procedimento:** Fornecer caminho documentado para questionar, contestar, corrigir dados, apresentar contexto e obter revisão qualificada quando exigido ou adotado por política.
**Evidência:** Procedimento, registros, resultados, níveis de serviço e qualificação dos revisores.
**Revisão/teste:** Amostrar recursos por independência, tempestividade e reconsideração significativa.
**Remediação/reavaliação:** Corrigir falhas e alimentar problemas sistêmicos à melhoria de modelo/processo.

## 16. Desenho de supervisão e intervenção humana
**Camada de fonte:** NIST AI RMF, deveres aplicáveis de IA/ADM e desenho interno de controles.
**Aplicabilidade:** Sistemas em que pessoas supervisionam, aprovam, anulam ou revisam resultados.
**Responsável:** Proprietário do processo e governança de IA.
**Procedimento:** Definir autoridade, competência, informação disponível, capacidade de anulação, limites de carga, escalonamento e proteção contra aprovação mecânica.
**Evidência:** RACI, instruções, treinamento, registros de anulação, escalonamento e métricas de carga.
**Revisão/teste:** Observar decisões representativas e medir comportamento real de revisão/anulação.
**Remediação/reavaliação:** Redesenhar supervisão nominal ou ineficaz.

## 17. Interfaces de consentimento, preferências e base legal
**Camada de fonte:** Lei de privacidade aplicável e controles internos de preferências.
**Aplicabilidade:** Processamento baseado em consentimento, opt-in/opt-out ou outras bases jurídicas específicas.
**Responsável:** Privacidade/jurídico com produto e dados.
**Procedimento:** Registrar base ou permissão aplicável, propagar escolhas, suportar retirada quando cabível e separar consentimento de usos baseados validamente em outra base.
**Evidência:** Registro de base legal, estado de consentimento/preferência, versão de aviso, logs de propagação e exceções.
**Revisão/teste:** Rastrear mudanças de preferências por sistemas downstream.
**Remediação/reavaliação:** Corrigir estados obsoletos/conflitantes e cessar processamento não autorizado.

## 18. Minimização de dados e governança de características
**Camada de fonte:** Princípios de minimização, lei aplicável e governança de modelos.
**Aplicabilidade:** Características, prompts, embeddings, armazenamentos de contexto, logs e atributos de decisão.
**Responsável:** Proprietário de modelo/dados com privacidade e produto.
**Procedimento:** Exigir necessidade documentada para cada característica material e remover dados redundantes, excessivamente granulares ou injustificados.
**Evidência:** Registro de características, justificativa, testes de ablação quando apropriado e exceções aprovadas.
**Revisão/teste:** Desafiar periodicamente necessidade e sensibilidade.
**Remediação/reavaliação:** Remover/transformar dados e retestar desempenho/risco.

## 19. Retenção, exclusão e memória do modelo
**Camada de fonte:** Deveres aplicáveis de retenção/exclusão, política de registros e arquitetura.
**Aplicabilidade:** Dados de treinamento, prompts, históricos, embeddings, bases vetoriais, logs, cache, saídas e feedback.
**Responsável:** Proprietário de dados com privacidade, records e plataforma.
**Procedimento:** Definir prazos, legal hold, propagação de exclusão, limites de memória, backups e exceções.
**Evidência:** Tabela de retenção, jobs de exclusão, verificação, holds e exceções.
**Revisão/teste:** Testar exclusão de ponta a ponta em armazenamentos primários e derivados quando tecnicamente viável.
**Remediação/reavaliação:** Reparar rotas falhas e reavaliar arquitetura se a exclusão não for confiável.

## 20. Desidentificação, pseudonimização e PETs
**Camada de fonte:** Engenharia de privacidade, lei aplicável e padrões internos de segurança.
**Aplicabilidade:** Usos baseados em menor identificabilidade ou tecnologias de aprimoramento de privacidade.
**Responsável:** Engenharia de privacidade/segurança de dados.
**Procedimento:** Selecionar técnicas proporcionais, documentar modelo de ameaça e premissas de reidentificação e restringir chaves de ligação/reversão.
**Evidência:** Especificação técnica, controles de chaves, testes de reidentificação, parâmetros de privacidade e restrições.
**Revisão/teste:** Reavaliar frente a novos dados auxiliares e ataques.
**Remediação/reavaliação:** Reforçar transformação ou deixar de alegar desidentificação.

## 21. Interfaces de equidade e viés sem falsa equivalência legal
**Camada de fonte:** NIST AI RMF, lei antidiscriminação/setor aplicável e política de IA responsável.
**Aplicabilidade:** Sistemas com possíveis diferenças materiais entre grupos ou proxies relevantes.
**Responsável:** Risco de IA/modelos com jurídico e negócio.
**Procedimento:** Definir questões de equidade segundo contexto, categorias protegidas quando aplicáveis, risco de proxies, cortes de desempenho, limiares e critérios de escalonamento.
**Evidência:** Plano de testes, métricas por subgrupo, análise de proxies, revisão de aplicabilidade e decisões.
**Revisão/teste:** Testar disparidades adversas materiais e limitações de medição.
**Remediação/reavaliação:** Ajustar dados, características, limiares, processo ou caso e retestar.

## 22. Acesso, identidade e administração privilegiada
**Camada de fonte:** Padrões de segurança/IAM e requisitos de confidencialidade.
**Aplicabilidade:** Consoles, datasets, prompts, logs, feature stores, bases vetoriais, ferramentas de rotulagem e sistemas de decisão.
**Responsável:** Segurança/IAM e proprietário da plataforma.
**Procedimento:** Aplicar menor privilégio, autenticação forte, PAM, segregação, revisão periódica e revogação rápida.
**Evidência:** Matriz de acesso, aprovações, MFA/PAM, revisões e desligamentos.
**Revisão/teste:** Amostrar acessos privilegiados e a dados sensíveis.
**Remediação/reavaliação:** Revogar excessos e investigar uso não autorizado.

## 23. Modelos, APIs e provedores de dados terceiros
**Camada de fonte:** Contratos, risco de terceiros, privacidade, NIST AI RMF e cadeia de suprimentos.
**Aplicabilidade:** Modelos externos, APIs hospedadas, brokers, enriquecimento, avaliadores e subprocessadores.
**Responsável:** Compras/risco de terceiros com governança IA, privacidade, segurança e negócio.
**Procedimento:** Avaliar uso e reutilização de dados, retenção, subprocessadores, segurança, privacidade, mudanças de modelo, incidentes, auditoria, término e saída.
**Evidência:** Due diligence, cláusulas, termos de processamento, model cards, evidências e plano de saída.
**Revisão/teste:** Revalidar provedores de alto risco e mudanças materiais.
**Remediação/reavaliação:** Restringir dados, exigir mudanças ou sair do provedor.

## 24. Processamento e implantação transfronteiriços
**Camada de fonte:** Regras aplicáveis de transferência/localização, contratos e governança de privacidade.
**Aplicabilidade:** Dados, hospedagem de modelos, suporte, telemetria ou decisões que atravessem jurisdições relevantes.
**Responsável:** Privacidade/jurídico com proprietário cloud/plataforma.
**Procedimento:** Mapear rotas, mecanismos/restrições, acesso de suporte, subprocessadores e requisitos regionais sem presumir um mecanismo global único.
**Evidência:** Mapa de transferências, análise jurídica, mecanismo contratual, arquitetura regional e lista de subprocessadores.
**Revisão/teste:** Comparar hospedagem/suporte/telemetria reais com regiões aprovadas.
**Remediação/reavaliação:** Reconfigurar routing/hospedagem ou atualizar mecanismos legais.

## 25. Registro, rastreabilidade e registros de decisão
**Camada de fonte:** Conceitos de rastreabilidade NIST AI RMF, accountability de privacidade e padrões de logging.
**Aplicabilidade:** Decisões materiais e ações de suporte.
**Responsável:** Proprietário de plataforma/modelo com segurança e negócio.
**Procedimento:** Registrar versão, referências de entradas pertinentes, decisão/saída, razões quando cabível, ações humanas, anulações e estado de política, minimizando dados pessoais desnecessários.
**Evidência:** Logs, esquema de registro, retenção, controles de integridade e acessos.
**Revisão/teste:** Reconstruir decisões amostradas.
**Remediação/reavaliação:** Reparar lacunas e ajustar equilíbrio entre retenção e minimização.

## 26. Monitoramento de drift, dano à privacidade e abuso
**Camada de fonte:** Conceitos de monitoramento NIST AI RMF e controles internos de risco.
**Aplicabilidade:** Sistemas em produção durante sua operação.
**Responsável:** Proprietário do modelo, risco IA, privacidade e operações.
**Procedimento:** Monitorar drift, qualidade, reclamações, inferências sensíveis, violações de política, abuso, desempenho por grupo e uso inesperado.
**Evidência:** Dashboards, alertas, limiares, investigações e tendências.
**Revisão/teste:** Validar cobertura de alertas e amostrar resoluções.
**Remediação/reavaliação:** Ajustar, suspender, reverter ou redesenhar ao exceder limiares.

## 27. Coordenação de incidentes, reclamações e solicitações de direitos
**Camada de fonte:** Deveres aplicáveis de privacidade/incidentes/direitos e resposta interna.
**Aplicabilidade:** Eventos de segurança/privacidade, saídas danosas, reclamações, solicitações e contestações.
**Responsável:** Operações de incidentes/privacidade com governança IA e negócio.
**Procedimento:** Encaminhar ao processo correto, preservar evidências e cumprir prazos aplicáveis.
**Evidência:** Registros, triagem, notificações, respostas, contenção e lições aprendidas.
**Revisão/teste:** Exercitar cenários representativos de incidentes IA/privacidade.
**Remediação/reavaliação:** Corrigir falhas de encaminhamento, controle ou modelo e reavaliar risco.

## 28. Gestão de mudanças e atualizações materiais do modelo
**Camada de fonte:** Mudança interna, ciclo de vida NIST AI RMF, terceiros e deveres regulatórios aplicáveis.
**Aplicabilidade:** Mudanças de modelo/versão, prompt, recuperação, características, dados, limiar, provedor, finalidade ou implantação.
**Responsável:** Produto/modelo com governança IA, privacidade e segurança.
**Procedimento:** Classificar materialidade, identificar avaliações/avisos/contratos/testes afetados, aprovar e manter rollback.
**Evidência:** Ticket, análise de impacto, resultados, aprovações, release notes e plano de reversão.
**Revisão/teste:** Confirmar que produção corresponde à versão aprovada.
**Remediação/reavaliação:** Reverter mudanças não autorizadas ou insuficientemente avaliadas.

## 29. Métricas, KRI/KPI e reporte gerencial
**Camada de fonte:** Governança interna e conceitos de medição NIST.
**Aplicabilidade:** Governança de portfólio e sistema.
**Responsável:** Liderança de governança IA/privacidade.
**Procedimento:** Medir cobertura de inventário, avaliações, direitos/recursos, incidentes, drift, terceiros, exceções, remediação vencida e sinais materiais de disparidade/risco.
**Evidência:** Definições, dashboards, tendências, limiares e ações gerenciais.
**Revisão/teste:** Verificar linhagem das métricas e evitar agregação enganosa.
**Remediação/reavaliação:** Corrigir indicadores fracos e escalar violações sustentadas.

## 30. Asseguração, testes e inspeção de evidências
**Camada de fonte:** Auditoria/asseguração interna, avaliação NIST AI RMF e requisitos aplicáveis.
**Aplicabilidade:** Sistemas de alto risco e amostras de portfólio.
**Responsável:** Auditoria/asseguração independente com apoio especializado.
**Procedimento:** Testar desenho e efetividade operacional por evidência, amostragem, testes técnicos, entrevistas, solicitações/recursos e reconstrução de decisões.
**Evidência:** Plano, papéis de trabalho, achados, respostas, remediação e fechamento.
**Revisão/teste:** Manter independência proporcional ao risco e não depender apenas de autoatestação.
**Remediação/reavaliação:** Levar achados ao fechamento verificado e retestar correções materiais.

## 31. Localização, acessibilidade e gestão de fonte controlada
**Camada de fonte:** Controles de liberação do projeto e obrigações aplicáveis de acessibilidade/comunicação.
**Aplicabilidade:** Edições controladas em inglês, es-419 e pt-BR e seus artefatos.
**Responsável:** Documentação/release com revisão terminológica de privacidade/jurídico quando aplicável.
**Procedimento:** Preservar distinções de fontes, paridade de capítulos, terminologia, qualificadores legais, estrutura acessível, metadados de idioma e aviso de tradução não oficial.
**Evidência:** Fontes, resultados de paridade, controles de acessibilidade, notas terminológicas e histórico.
**Revisão/teste:** Comparar capítulos, cabeçalhos, qualificadores principais e renderização entre idiomas.
**Remediação/reavaliação:** Corrigir defeitos antes do congelamento do candidato.

## 32. Liberação, proveniência e roteiro de implementação
**Camada de fonte:** Política de liberação do repositório e procedimento controlled-build.
**Aplicabilidade:** Liberação final do Manual 28 e futuras revisões.
**Responsável:** Proprietário de liberação com governança IA/privacidade.
**Procedimento:** Revalidar fontes; congelar fontes; construir reprodutivelmente DOCX/PDF EN/es-419/pt-BR; vincular SHA-256; executar QA de pacote/acessibilidade/render; staging exato; verificar Manual 27 publicado; reconciliar catálogo e registro.
**Evidência:** Registro de fontes, workflow/artifact, manifesto, seis hashes, QA, commit de staging, checks exact-head e merge.
**Revisão/teste:** Falhar fechado diante de predecessor ausente, binário alterado, gate falho, defeito material ou premissa de fonte obsoleta.
**Remediação/reavaliação:** Regenerar somente quando defeito determinístico ou mudança material de fonte/controle exigir; caso contrário preservar bytes revisados.