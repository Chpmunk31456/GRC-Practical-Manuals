# ISO/IEC 42001:2023

# SISTEMA DE GESTÃO DE INTELIGÊNCIA ARTIFICIAL

Manual prático para gestores do SGIA e analistas juniores

| **O que este manual faz:** Explica como estabelecer, implementar, operar, auditar, preparar para certificação e melhorar um sistema de gestão de inteligência artificial. Detalha as Cláusulas 4–10, os nove grupos de controles do Anexo A, avaliação de riscos e impactos, a Declaração de Aplicabilidade, certificação, evidências, ferramentas, decisões gerenciais e o trabalho do analista júnior. |
|---|

**Alberto (Al) Leiva**

Primeira edição • julho de 2026

> **Status da localização:** Fonte localizada em português do Brasil (`pt-BR`). Esta parte cobre os elementos preliminares e os Capítulos 1–8 do mestre controlado em inglês. Deve ser utilizada com as demais partes localizadas até a geração do mestre consolidado e dos artefatos DOCX/PDF. Não constitui tradução oficial da ISO.

# Prefácio

A ISO/IEC 42001 ajuda organizações a governar a inteligência artificial por meio de um sistema de gestão em toda a organização. Ela não certifica que toda saída esteja correta nem que todo sistema de IA seja seguro. Exige liderança, contexto, planejamento baseado em riscos, recursos, controles operacionais, avaliação de desempenho, ação corretiva e melhoria contínua em torno do desenvolvimento, fornecimento ou uso responsável de sistemas de IA.

Este manual explica conceitos em redação original e não reproduz a norma protegida por direitos autorais. Obtenha uma cópia autorizada da ISO/IEC 42001:2023 e de quaisquer normas utilizadas na implementação ou auditoria. Certificação, leis, deveres setoriais, contratos e riscos técnicos devem ser avaliados em relação ao escopo e aos fatos reais da organização.

| **Nota de informação atual:** Verificado em 14 de julho de 2026. A ISO/IEC 42001:2023 continua sendo a norma publicada de requisitos para SGIA. A ISO/IEC 42005:2025 fornece orientação sobre avaliação de impacto de sistemas de IA. A ISO/IEC 42006:2025 acrescenta requisitos para organismos que auditam e certificam SGIA. A ISO 19011:2026 é a orientação atual para auditoria de sistemas de gestão. ISO/IEC 42003 e 42007 continuam em desenvolvimento e não são tratadas aqui como requisitos. |
|---|

## Como utilizar este manual

- Líderes e gestores do SGIA: comecem pelos Capítulos 1–10, 16–20 e 29–31.
- Implementadores e equipes de GRC: estudem em ordem e utilizem todos os modelos do Capítulo 32.
- Equipes de IA, dados, produto, segurança, privacidade e jurídico: concentrem-se nos Capítulos 6–15 e 20–28.
- Auditores internos: concentrem-se nos Capítulos 16–20 e 29 e depois pratiquem o laboratório do Capítulo 31.
- Analistas juniores: aprendam a intenção das cláusulas, produzam evidências, redijam constatações e nunca aleguem certificação ou autoridade de auditor que não possuam.

# Sumário

O arquivo-fonte em Word contém um sumário nativo e um guia permanente de capítulos com páginas. Nesta edição Markdown localizada, o guia preserva a ordem do mestre controlado.

# Guia de capítulos

| **Capítulo** | **Título** | **Página inicial no mestre inglês** |
|---:|---|---:|
| 1 | ISO/IEC 42001 e o sistema de gestão de inteligência artificial | 5 |
| 2 | Arquitetura do SGIA e ciclo Planejar-Fazer-Verificar-Agir | 6 |
| 3 | Aplicabilidade, papéis organizacionais e roteiro de implementação | 7 |
| 4 | Cláusula 4: Contexto da organização | 9 |
| 5 | Cláusula 5: Liderança | 10 |
| 6 | Cláusula 6.1: Ações para abordar riscos e oportunidades | 11 |
| 7 | Cláusula 6.1.2: Avaliação de riscos de IA | 12 |
| 8 | Cláusula 6.1.3: Tratamento de riscos de IA e Declaração de Aplicabilidade | 14 |
| 9 | Cláusula 6.1.4: Avaliação de impacto de sistemas de IA | 15 |
| 10 | Cláusulas 6.2 e 6.3: Objetivos e planejamento de mudanças | 17 |
| 11 | Cláusula 7.1: Recursos | 18 |
| 12 | Cláusulas 7.2–7.4: Competência, conscientização e comunicação | 19 |
| 13 | Cláusula 7.5: Informação documentada | 20 |
| 14 | Cláusula 8.1: Planejamento e controle operacional | 21 |
| 15 | Cláusulas 8.2–8.4: Risco operacional, tratamento e avaliação de impacto | 22 |
| 16 | Cláusula 9.1: Monitoramento, medição, análise e avaliação | 23 |
| 17 | Cláusula 9.2: Auditoria interna | 24 |
| 18 | Cláusula 9.3: Análise crítica pela direção | 26 |
| 19 | Cláusula 10: Não conformidade, ação corretiva e melhoria contínua | 27 |
| 20 | Anexos A–D e a Declaração de Aplicabilidade | 28 |
| 21 | Anexo A.2: Políticas relacionadas à IA | 29 |
| 22 | Anexo A.3: Organização interna | 30 |
| 23 | Anexo A.4: Recursos para sistemas de IA | 31 |
| 24 | Anexo A.5 e ISO/IEC 42005: Avaliação de impacto de sistemas de IA | 32 |
| 25 | Anexo A.6: Ciclo de vida do sistema de IA | 33 |
| 26 | Anexo A.7: Dados para sistemas de IA | 34 |
| 27 | Anexo A.8: Informação para partes interessadas | 36 |
| 28 | Anexos A.9 e A.10: Uso responsável, fornecedores e clientes | 38 |
| 29 | Certificação, ISO/IEC 42006:2025 e prontidão para auditoria | 40 |
| 30 | Ferramentas de código aberto para evidências do SGIA e asseguração de IA | 42 |
| 31 | Guia de gestores e analistas juniores, laboratório e entrevistas | 47 |
| 32 | Modelos, glossário, índice e referências oficiais | 51 |

# 1. ISO/IEC 42001 e o sistema de gestão de inteligência artificial

*A ISO/IEC 42001 especifica requisitos para que uma organização estabeleça, implemente, mantenha e melhore continuamente um sistema de gestão de inteligência artificial.*

| **Conceito** | **Significado simples** | **Pergunta de evidência** |
|---|---|---|
| SGIA | Políticas, objetivos, processos, papéis, controles e registros inter-relacionados para IA responsável | O sistema opera em todo o escopo definido? |
| Papel da organização | Desenvolvedor/fornecedor, implantador/usuário, fornecedor, cliente ou vários papéis | Quais responsabilidades estão controladas? |
| Sistema de IA | Pessoas, dados, modelos, software, infraestrutura, processos e interfaces utilizados para um resultado de IA | Qual é o limite completo? |
| Conformidade | Requisitos são atendidos dentro do escopo certificado | Que cláusula, implementação, evidência e resultado sustentam a alegação? |
| Certificação | Avaliação independente por terceira parte do SGIA em relação à ISO/IEC 42001 | Qual entidade, escopo, norma, organismo, datas e status estão certificados? |

## 1.1 O que a certificação não comprova

- Não garante que toda saída de IA seja precisa, imparcial, segura, legal, confiável ou explicável.
- Não certifica produtos de IA individualmente, salvo quando o escopo do SGIA certificado e o esquema sustentarem explicitamente essa alegação.
- Não substitui testes de produto, análise jurídica, avaliação de impacto, controles de privacidade/segurança, validação de domínio ou supervisão humana.
- Não transfere a responsabilização da organização para o organismo de certificação ou fornecedor.

# 2. Arquitetura do SGIA e ciclo Planejar-Fazer-Verificar-Agir

*O SGIA segue a estrutura harmonizada dos sistemas de gestão e um ciclo contínuo Planejar-Fazer-Verificar-Agir (PDCA).* 

<img src="../../../assets/English/media/image1.png" style="width:6.15in;height:3.23274in" alt="As cláusulas interagem continuamente; a norma não é uma lista de verificação linear concluída uma única vez." />

Figura 1. Ciclo PDCA do SGIA

> **Explicação acessível:** A figura mostra que o SGIA funciona como um ciclo. A organização planeja contexto, riscos, impactos e objetivos; executa controles e processos; verifica o desempenho por medição, auditoria interna e análise crítica pela direção; e age sobre não conformidades e oportunidades de melhoria antes de reiniciar o ciclo.

| **Etapa PDCA** | **Trabalho da ISO/IEC 42001** | **Saída típica** |
|---|---|---|
| Planejar | Contexto, liderança, risco/oportunidade, avaliação, tratamento, objetivos e recursos | Escopo, política, métodos, registro de riscos, processo de impacto, Declaração de Aplicabilidade e objetivos |
| Fazer | Competência, comunicação, documentação, controles operacionais e avaliações | Procedimentos, registros do sistema, aprovações e evidências de fornecedores e ciclo de vida |
| Verificar | Monitoramento, medição, análise, auditoria interna e análise crítica pela direção | Métricas, avaliação, relatório de auditoria e decisões de análise crítica |
| Agir | Não conformidade, correção, causa-raiz, ação corretiva e melhoria | Registros de ações, testes de eficácia e riscos/controles/objetivos atualizados |

## 2.1 Integração com sistemas existentes

- Reutilize processos de governança, controle documental, risco, auditoria, ação corretiva, fornecedores, segurança, privacidade, qualidade e continuidade quando seu escopo e controles forem adequados ao risco de IA.
- Crie complementos específicos de IA para avaliação de impacto, ciclo de vida de modelos/dados, uso responsável, transparência, supervisão humana e responsabilidades da cadeia de valor.
- Mantenha uma única fonte de verdade e mapeie-a para ISO 27001, ISO 9001, privacidade, obrigações legais, NIST AI RMF e deveres setoriais em vez de duplicar registros.

# 3. Aplicabilidade, papéis organizacionais e roteiro de implementação

*Uma implementação útil começa com controle organizacional, inventário preciso de IA, papéis responsáveis e um roteiro por etapas.*

<img src="../../../assets/English/media/image2.png" style="width:6.15in;height:3.23274in" alt="O escopo deve descrever honestamente limites organizacionais, papéis de IA, sistemas, dados, fornecedores e exclusões." />

Figura 2. Cadeia de construção do escopo

> **Explicação acessível:** A figura representa a construção do escopo desde a organização e seus papéis de IA até sistemas, dados, fornecedores, interfaces e exclusões. Cada limite deve ter justificativa que não evite requisitos aplicáveis.

| **Papel** | **Responsabilidade principal** |
|---|---|
| Órgão de governança / executivos | Supervisão, direção, recursos, apetite a risco e decisões materiais |
| Líder do SGIA | Coordenar sistema de gestão, desempenho, auditorias e melhoria |
| Proprietário de negócio/sistema de IA | Finalidade, resultado, processo afetado, risco, aprovação e monitoramento |
| Modelo/dados/produto/engenharia | Requisitos, projeto, dados, avaliação, implantação e mudança |
| Segurança/privacidade/jurídico/compliance/segurança funcional | Requisitos especializados, revisão, contestação e incidentes |
| Compras/gestor de fornecedores | Due diligence, alocação, contratos, evidências, monitoramento e saída |
| Auditoria interna | Avaliação independente e objetiva sem ser proprietária dos controles |

## 3.1 Roteiro de implementação

- Autorize o programa e obtenha as normas; defina finalidade, patrocinador, recursos e governança.
- Inventarie sistemas e papéis de IA; realize análise de contexto e partes interessadas; redija escopo e política.
- Defina processos de risco, impacto, tratamento, Declaração de Aplicabilidade, objetivos, documentos, competência, comunicação e operação.
- Implemente controles do Anexo A e controles adicionais conforme o risco; colete evidências durante a operação real.
- Meça o desempenho; conclua auditoria interna e análise crítica pela direção; corrija não conformidades e verifique eficácia.
- Selecione um organismo de certificação competente; conclua Estágio 1 e Estágio 2; mantenha supervisão e melhoria.

# 4. Cláusula 4: Contexto da organização

*A Cláusula 4 estabelece por que o SGIA existe, quem importa, o que ele abrange e como seus processos interagem.*

## 4.1 Questões internas e externas

- Estratégia, cultura, governança, apetite a risco, recursos, competência, maturidade de dados, arquitetura tecnológica, sistemas de gestão existentes e mudança organizacional.
- Lei, regulamentação, expectativas setoriais, contratos, requisitos de clientes, normas, confiança pública, preocupações sociais, mercados, fornecedores, ameaças, mudança de tecnologia/modelo e questões climáticas quando relevantes aos resultados pretendidos do SGIA.
- Registre por que cada questão é relevante, responsável, efeito sobre o SGIA, resposta e gatilho de revisão.

## 4.2 Partes interessadas e requisitos

- Identifique pessoas e grupos afetados pela IA, mesmo que não sejam usuários ou clientes diretos.
- Inclua reguladores, clientes, trabalhadores, usuários, titulares de dados, fornecedores, parceiros, comunidades, acionistas, auditores, seguradoras e público, conforme relevante.
- Separe necessidades/expectativas de obrigações de compliance vinculantes; registre autoridade/fonte, sistema/processo, responsável, evidência e monitoramento de mudanças.
- Determine quais requisitos a organização abordará por meio do SGIA.

## 4.3 Declaração de escopo

| **Elemento do escopo** | **Clareza necessária** |
|---|---|
| Organização | Entidades legais, unidades de negócio, locais e funções |
| Papel de IA | Desenvolvedor/fornecedor, implantador/usuário, serviço/fornecedor ou combinação |
| Produtos/serviços/processos | Ofertas habilitadas por IA e usos internos |
| Tecnologia e dados | Sistemas, modelos, ambientes, interfaces e conjuntos de dados principais |
| Limites/dependências | Serviços compartilhados, fornecedores, clientes e exclusões |
| Justificativa | Por que os limites são válidos e não evitam requisitos aplicáveis |

## 4.4 Processos do SGIA

- Defina finalidade do processo, entradas, saídas, sequência, interação, proprietário, critérios, controles, recursos, registros, medidas, riscos e melhoria.
- Um mapa de processos deve conectar inventário, risco, impacto, tratamento, objetivos, ciclo de vida, dados, fornecedores, uso, monitoramento, incidentes, auditoria, análise crítica e ação corretiva.

# 5. Cláusula 5: Liderança

*A alta direção deve assumir o SGIA, a política, a integração, os recursos, a comunicação, o desempenho e os papéis responsáveis.*

## 5.1 Demonstração de liderança

- Torne os objetivos do SGIA compatíveis com a estratégia e os compromissos de IA responsável.
- Integre requisitos do SGIA aos processos de negócio, produto, compras, dados, tecnologia, pessoas, risco e mudança.
- Forneça pessoas competentes, tempo, ferramentas, dados, infraestrutura, orçamento, contestação independente e autoridade.
- Comunique que a gestão eficaz de IA e a conformidade importam, inclusive quando a pressão por entrega conflita com controles.
- Analise o desempenho e apoie pessoas que contribuem para melhoria ou levantam preocupações.
- Assegure que os resultados pretendidos sejam alcançados, em vez de tratar certificação como único resultado.

## 5.2 Política de IA

- Declare finalidade, princípios, compromissos com requisitos aplicáveis, IA responsável baseada em riscos, objetivos e melhoria contínua.
- Adeque a política aos papéis de IA, contexto, cultura, impacto, lei, produtos e apetite a risco da organização.
- Alinhe segurança, privacidade, qualidade, dados, ética, RH, compras, produto, registros, segurança funcional e incidentes.
- Aprove no nível adequado, comunique às pessoas relevantes, disponibilize conforme apropriado e revise em intervalos planejados e após mudanças materiais.

## 5.3 Papéis, responsabilidades e autoridades

- Defina responsabilização pelo SGIA e por reportar desempenho à alta direção.
- Atribua proprietários para cada sistema de IA, risco, impacto, fonte de dados, modelo, fornecedor, controle, métrica, incidente, mudança e ação corretiva.
- Defina autoridade de aprovação e escalonamento; evite conflitos em que a mesma equipe cria, valida, aceita e audita risco de alto impacto sem contestação adequada.

# 6. Cláusula 6.1: Ações para abordar riscos e oportunidades

*O planejamento transforma contexto em riscos, oportunidades, controles, objetivos e mudanças gerenciadas.*

## 6.1 Entradas de planejamento

- Contexto e requisitos de partes interessadas; escopo e processos do SGIA.
- Inventário de IA, papéis do sistema, etapa do ciclo de vida, pessoas afetadas, dados, modelos, fornecedores, integrações e condições de uso.
- Benefícios e oportunidades estratégicas, juntamente com ameaças, falhas, danos, incerteza e uso indevido razoavelmente previsível.
- Obrigações legais, regulatórias, contratuais, de segurança, privacidade, segurança funcional, qualidade, registros, acessibilidade, trabalho, propriedade intelectual, consumidor e setor aplicáveis.

## 6.1.1 Ações sobre riscos e oportunidades

- Planeje ações proporcionais ao efeito sobre resultados do SGIA; integre-as aos processos em vez de manter apenas um registro separado.
- Defina ação, proprietário, recurso, data, medida, evidência, dependência, decisão residual e avaliação de eficácia.
- Oportunidades podem incluir melhor supervisão, qualidade de dados, transparência, avaliação, competência, eficiência, confiança de partes interessadas e inovação.
- Evite que controles pretendidos criem novos riscos, como monitoramento excessivo, avisos inacessíveis ou sobrecarga de revisão.

# 7. Cláusula 6.1.2: Avaliação de riscos de IA

*O processo de avaliação de riscos de IA deve usar critérios definidos e repetíveis para identificar, analisar, avaliar e priorizar riscos.*

<img src="../../../assets/English/media/image3.png" style="width:6.15in;height:3.23274in" alt="Registre evidências e incerteza para que diferentes avaliadores possam chegar a conclusões comparáveis." />

Figura 3. Fluxo de avaliação de riscos de IA

> **Explicação acessível:** A avaliação parte de um cenário de risco definido, analisa contexto, probabilidade, consequências, incerteza e controles existentes, compara o resultado com critérios estabelecidos, seleciona tratamento e preserva evidências para decisão residual autorizada e futura reavaliação.

## 7.1 Método de risco

- Defina escopo, unidade de análise, categorias de risco, dimensões de impacto, probabilidade, gravidade, escala, duração, reversibilidade, grupos afetados, incerteza, agregação, tolerância e autoridade de decisão.
- Identifique cenários de risco em uso pretendido, uso indevido previsível, falha, ataque, dados, modelo, comportamento humano, fornecedores, ambiente, lei e efeito social.
- Analise risco inerente e controles existentes com evidências; diferencie risco atual, alvo e residual.
- Avalie em relação aos critérios; priorize tratamento segundo consequências para pessoas e negócio, não por uma única pontuação técnica.
- Assegure resultados consistentes, válidos e comparáveis e preserve a avaliação como informação documentada.
- Reavalie em intervalos planejados e após mudanças materiais, incidentes, novos grupos afetados, atualizações de modelo/fornecedor, drift, mudança legal ou falha de controle.

| **Registro de risco** | **Detalhe mínimo** |
|---|---|
| Cenário | Causa/ator, condição vulnerável, evento/ação, comportamento do sistema, parte afetada e consequência |
| Contexto | Uso, pessoas, geografia, escala, dados, modelo/versão, ferramentas, fornecedor e premissas |
| Análise | Probabilidade, dimensões de impacto, incerteza, evidências e eficácia dos controles existentes |
| Tratamento | Evitar/reduzir/compartilhar/aceitar, controles, proprietário, data, medida e risco residual |
| Decisão | Aprovador autorizado, justificativa, condições, validade, monitoramento e gatilho de revisão |

# 8. Cláusula 6.1.3: Tratamento de riscos de IA e Declaração de Aplicabilidade

*O tratamento de riscos seleciona controles, compara-os ao Anexo A, produz a Declaração de Aplicabilidade e obtém aprovação do risco residual.*

## 8.1 Processo de tratamento

- Escolha opções de tratamento: evitar, alterar/reduzir, compartilhar/transferir, aceitar dentro da autoridade ou conduzir piloto estritamente limitado para reduzir incerteza.
- Determine controles necessários a partir de requisitos legais e contratuais, resultados de risco e impacto de IA, arquitetura, partes interessadas e objetivos.
- Compare controles selecionados com o Anexo A para verificar que nenhum controle de referência relevante foi ignorado.
- Acrescente controles além do Anexo A quando necessários para segurança, privacidade, segurança funcional, qualidade, avaliação técnica, acessibilidade, resiliência ou obrigações setoriais.
- Crie e aprove plano de tratamento e obtenha autorização para o risco residual.
- Preserve resultados e mudanças do tratamento como informação documentada controlada.

## 8.2 Campos da Declaração de Aplicabilidade

| **Campo** | **Finalidade** |
|---|---|
| Referência/título do controle | Identidade do controle do Anexo A ou adicional |
| Aplicável? | Incluído ou excluído para o escopo definido do SGIA |
| Justificativa | Risco, obrigação, objetivo, arquitetura ou razão de exclusão |
| Implementação | Política/processo/sistema e proprietário responsável |
| Status | Implementado, parcial, planejado ou não aplicável |
| Evidência/teste | Evidência atual e resultado de eficácia operacional |
| Dependências/lacunas | Controles compartilhados de fornecedor/cliente e constatações |
| Revisão | Última/próxima revisão e gatilhos de mudança |

| **Alerta sobre a Declaração de Aplicabilidade:** Ela não é uma lista copiada. Deve concordar com o escopo atual, avaliações de risco e impacto, plano de tratamento, implementação real, evidências e decisões de risco. |
|---|
