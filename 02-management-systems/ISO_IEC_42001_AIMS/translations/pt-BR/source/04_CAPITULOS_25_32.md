# 25. Anexo A.6: Ciclo de vida do sistema de IA

*O Anexo A.6 conecta objetivos de desenvolvimento responsável a requisitos, projeto, testes, implantação, operação, documentação e registro de eventos.*

<img src="../../../assets/pt-BR/media/image6.png" style="width:6.15in;height:3.23274in" alt="Cada marco do ciclo de vida deve produzir evidência rastreável e uma decisão com responsável." />

Figura 6. Ciclo de vida responsável do sistema de IA

> **Explicação acessível:** A figura mostra um fluxo de objetivos e requisitos para projeto, verificação/validação, implantação, operação, monitoramento, mudança e retirada. Cada etapa deve deixar versões, critérios, resultados, aprovações e decisões rastreáveis.

| **Área do ciclo de vida** | **Evidência de implementação** |
|---|---|
| Objetivos/processo responsável | Equidade, segurança funcional, privacidade, transparência, cibersegurança, robustez e outros objetivos mensuráveis relevantes; procedimento do ciclo de vida |
| Requisitos/especificação | Finalidade, critérios funcionais e não funcionais, pessoas afetadas, dados, modelo, supervisão humana, limites e obrigações |
| Registros de projeto/desenvolvimento | Arquitetura, decisões, alternativas, premissas, componentes, ameaças, interfaces, proveniência e revisões |
| Verificação/validação | Métodos, dados de avaliação, avaliadores, limites, falhas graves, testes de subgrupos/casos extremos/adversariais e limitações |
| Implantação | Aprovação de liberação, ambiente, configuração, informação ao usuário, migração, monitoramento e rollback |
| Operação/monitoramento | Desempenho, drift, segurança, segurança funcional, impacto, reclamações, mudanças, suporte, reparo e atualizações |
| Documentação técnica/logs | Instruções adequadas ao público mais eventos rastreáveis para auditoria, incidentes, decisões e melhoria |

## 25.1 Mudança e retirada

- Versione modelo, dados, prompts, recuperação, ferramentas, código, infraestrutura, políticas, avaliação, aprovações e monitoramento.
- Defina gatilhos de mudança material e escopo de regressão; implante gradualmente com rollback.
- Retire usuários, identidades, integrações, endpoints, modelos, conjuntos de dados, índices, logs, documentação, contratos e cópias de fornecedores conforme obrigações; preserve registros exigidos.

# 26. Anexo A.7: Dados para sistemas de IA

*O Anexo A.7 exige aquisição, qualidade, proveniência e preparação governadas de dados para desenvolvimento, melhoria e operação de IA.*

<img src="../../../assets/pt-BR/media/image7.png" style="width:6.15in;height:3.23274in" alt="A linhagem deve conectar fonte e autoridade a transformações, qualidade, uso, retenção e exclusão." />

Figura 7. Cadeia de evidências de dados de IA

> **Explicação acessível:** A cadeia de evidências acompanha os dados desde sua origem, autoridade e direitos, passando por aquisição, transformação, rotulagem, qualidade, versionamento e uso, até retenção ou exclusão. Deve permitir reproduzir quais dados sustentaram cada versão e decisão relevante.

## 26.1 Controles de dados

- Defina requisitos de gestão de dados para privacidade, segurança, representatividade, explicabilidade, proveniência, precisão, integridade, disponibilidade, retenção e exclusão conforme relevante.
- Documente aquisição/seleção: fonte, método, pessoas/população, direitos/licença, finalidade anterior, consentimento/autoridade quando aplicável, metadados, data, restrições e vieses conhecidos.
- Estabeleça critérios e limites de qualidade específicos do uso para precisão, completude, consistência, atualidade, unicidade, validade, representatividade, rótulos e cobertura de subgrupos.
- Preserve proveniência por criação, aquisição, transferência, transformação, rotulagem, aumento, filtragem, versionamento, validação, uso, compartilhamento, correção e exclusão.
- Documente métodos de preparação, código/ferramenta/versão, parâmetros, pessoas, verificações de qualidade, justificativa, saídas e reprodutibilidade.
- Separe e proteja conjuntos de treinamento, validação, teste, produção, monitoramento e incidentes; evite vazamento do conjunto de avaliação.

| **Evidência de dados** | **Teste** |
|---|---|
| Ficha de conjunto/dados | Rastrear finalidade, população, campos, fonte, direitos, qualidade, limitações e proprietário |
| Linhagem | Reproduzir transformações de fonte para atributo e versão |
| Resultado de qualidade | Verificar população/amostra, regras, falhas, correção e aprovação |
| Acesso/retenção | Amostrar concessões, revisões, remoções, uso, cópias e exclusão |
| Viés/representação | Verificar grupos relevantes, histórico, proxies, rótulos, lacunas e mitigação |

# 27. Anexo A.8: Informação para partes interessadas

*O Anexo A.8 exige informação útil para usuários e partes interessadas, além de reporte e comunicação de incidentes.*

<img src="../../../assets/pt-BR/media/image8.png" style="width:6.15in;height:3.23274in" alt="Transparência é comunicação específica ao público que permite uso seguro, responsabilização e reparação." />

Figura 8. Informação para partes interessadas

> **Explicação acessível:** A informação deve ser adaptada ao público. Usuários precisam de finalidade, capacidades e limites; pessoas afetadas precisam saber como a IA participa e como solicitar revisão ou reparação; clientes, reguladores e público recebem informação proporcional às suas responsabilidades e riscos.

## 27.1 Pacote de informação

- Usuários: finalidade pretendida, capacidades, limitações, entradas/saídas esperadas, uso proibido, verificação, supervisão humana, monitoramento, escalonamento e suporte.
- Pessoas afetadas: que IA é usada quando apropriado, papel na decisão, fatores/limitações importantes, dados e direitos, revisão humana, correção, recurso, reclamação e reparação.
- Clientes/parceiros: responsabilidades, configuração, dados, dependências de controle, evidências, incidentes, mudanças, suporte e saída.
- Reguladores/auditores: documentação controlada, escopo, avaliações, controles, resultados de testes, incidentes, mudanças, constatações e ação corretiva conforme exigido.
- Público: transparência proporcional, impactos significativos, governança, informações de segurança, contato e relatórios quando apropriado.

## 27.2 Reporte externo e incidentes

- Forneça canais acessíveis para relatar erros, danos, viés, preocupações de segurança/privacidade, uso indevido, problemas de acessibilidade ou efeitos inesperados.
- Defina triagem, gravidade, investigação, proteção, retorno, correção, reparação, escalonamento, retenção e análise de tendências.
- Predefina públicos do incidente, conteúdo, proprietário/porta-voz, revisão jurídica, tempo, canal, acessibilidade, coordenação, atualizações e encerramento.
- Não divulgue excessivamente informações sensíveis de segurança ou dados pessoais; tampouco esconda limitações materiais atrás de confidencialidade.

# 28. Anexos A.9 e A.10: Uso responsável, fornecedores e clientes

*O Anexo A.9 governa o uso responsável e a finalidade pretendida; o Anexo A.10 aloca deveres entre fornecedores, clientes e a cadeia de valor de IA.*

<img src="../../../assets/pt-BR/media/image9.png" style="width:6.15in;height:3.23274in" alt="A asseguração de fornecedores deve corresponder ao modelo, serviço, uso, fluxo de dados e configuração do cliente exatos." />

Figura 9. Ciclo de vida de IA de terceiros

> **Explicação acessível:** O controle de terceiros começa identificando atores e responsabilidades, segue com diligência prévia e contratos, monitora mudanças do fornecedor e termina com continuidade, portabilidade, exclusão e saída. Responsabilidade não pode ser transferida por linguagem contratual vaga.

## 28.1 Uso responsável

- Defina usos aprovados e proibidos, usuários, dados, saídas, decisões, autonomia, verificação, supervisão humana, logging, suporte, incidente e condições de interrupção.
- Estabeleça objetivos mensuráveis de uso responsável ligados a impactos e riscos relevantes.
- Treine usuários e supervisores; aplique por identidade, configuração, interfaces, política, monitoramento, revisão e consequências.
- Detecte expansão de escopo e exija reavaliação antes de reutilização, expansão, novas populações, maior impacto ou novas integrações/ferramentas.

## 28.2 Terceiros e clientes

- Mapeie desenvolvedor/fornecedor/implantador, fornecedores de dados/modelos/ferramentas/nuvem, integradores, serviços humanos, clientes, usuários e partes afetadas.
- Aloque responsabilidade por dados, requisitos, testes, configuração, transparência, supervisão humana, segurança, incidentes, monitoramento, mudança, evidências, direitos, exclusão e saída.
- Realize diligência prévia e contratação baseadas em risco; verifique documentação de modelo/sistema, avaliação, asseguração de segurança/privacidade, termos de dados, propriedade intelectual, suporte, vulnerabilidades, mudanças, subprocessadores, resiliência e portabilidade.
- Monitore mudanças de fornecedor em modelo/termos/treinamento/retenção/subprocessadores/incidentes/descontinuação e reavalie prontamente.
- Defina obrigações e suporte do cliente; não use responsabilidade do cliente como transferência vaga de deveres do fornecedor.

# 29. Certificação, ISO/IEC 42006:2025 e prontidão para auditoria

*A certificação avalia o SGIA em relação à ISO/IEC 42001 dentro de um escopo definido; a ISO/IEC 42006:2025 fortalece requisitos para organismos de certificação.*

## 29.1 Caminho de certificação

- Selecione organismo de certificação competente e verifique acreditação/status, esquema, geografia, competência, imparcialidade, capacidade de escopo e contrato.
- Solicitação e planejamento: organização, escopo do SGIA, papéis, locais, pessoas, sistemas, complexidade, processos terceirizados, normas e tempo de auditoria.
- Estágio 1: prontidão, escopo, sistema documentado, contexto, métodos de risco/impacto, Declaração de Aplicabilidade, auditoria interna, análise crítica pela direção e preparação para Estágio 2.
- Estágio 2: implementação e eficácia operacional por entrevistas, amostras, registros, observação e rastreamento.
- Resolva não conformidades com correção, causa, ação corretiva e evidência de eficácia conforme regras do esquema.
- Decisão de certificação, certificado, auditorias de supervisão, mudanças de escopo, recertificação, suspensão/retirada e melhoria contínua.

## 29.2 Importância da ISO/IEC 42006:2025

- Acrescenta requisitos específicos de SGIA para organismos que auditam e certificam em relação à ISO/IEC 42001 e se baseia na ISO/IEC 17021-1.
- Apoia competência apropriada, processos de auditoria consistentes, imparcialidade, tempo de auditoria e rigor para organizações que desenvolvem, fornecem ou usam sistemas de IA.
- A organização deve verificar que uma certificação alegada seja emitida sob esquema acreditado relevante e que escopo e status do certificado correspondam à alegação.

| **Pacote de evidências de auditoria** | **Exemplos** |
|---|---|
| Base | Escopo, contexto, partes, política, mapa de processos, papéis e inventário |
| Planejamento | Método/resultados de risco, tratamento, Declaração de Aplicabilidade, processo/resultados de impacto, objetivos e mudanças |
| Suporte/operação | Recursos, competência, comunicação, documentos, ciclo de vida, dados, uso, fornecedores e incidentes |
| Avaliação/melhoria | Métricas, auditoria interna, análise crítica pela direção, constatações, ações corretivas e eficácia |
| Amostras rastreáveis | Registros ponta a ponta de sistemas de IA representativos de risco alto/médio/baixo e mudanças materiais |

## 29.3 Prontidão para auditoria sem teatro

- Opere controles tempo suficiente para produzir evidências honestas; não crie registros depois do fato.
- Reconcilie escopo, inventário, risco, impacto, Declaração de Aplicabilidade, fornecedor, versões do sistema, métricas, auditoria e análise crítica pela direção.
- Prepare entrevistados para explicar o trabalho real e mostrar evidências, não memorizar respostas.
- Divulgue com precisão lacunas, riscos aceitos, limitações, incidentes e ações corretivas.

# 30. Ferramentas de código aberto para evidências do SGIA e asseguração de IA

*Ferramentas de código aberto podem apoiar rastreabilidade, avaliação, monitoramento, políticas, privacidade e constatações, mas não decidem conformidade com ISO.*

| **Ferramenta** | **Finalidade** |
|---|---|
| MLflow | Rastreamento de experimentos, registro de modelos, linhagem, aprovação e registros de implantação |
| DVC | Controle de versões para dados, modelos e pipelines |
| OpenLineage | Padrão aberto e ferramentas para eventos de linhagem de dados/trabalhos |
| OpenMetadata | Catálogo de dados, linhagem, propriedade, glossário e metadados de qualidade |
| Great Expectations | Expectativas automatizadas de qualidade de dados e resultados de validação |
| Evidently | Qualidade de dados, drift, desempenho de modelos e relatórios de monitoramento |
| Deepchecks | Testes de dados, modelos de ML e aplicações LLM |
| Giskard | Testes de IA e varredura de vulnerabilidades |
| Promptfoo | Avaliações de prompts, modelos, RAG e red teaming |
| Garak | Varredura e sondas de vulnerabilidades de LLM |
| PyRIT | Identificação de riscos e orquestração de red teaming para IA generativa |
| Inspect AI | Avaliações reproduzíveis de IA |
| Presidio | Detecção e desidentificação de informações pessoais |
| ModelScan | Varredura estática de arquivos de modelos serializados |
| CycloneDX | Formatos e ferramentas de lista de materiais de software, ML e IA |
| Open Policy Agent | Decisões de política como código |
| DefectDojo | Admissão, deduplicação, propriedade, remediação e reteste de constatações |
| Langfuse | Rastreamento de LLM, gestão de prompts e avaliação de código aberto |

| **Governança de ferramentas:** Use somente sistemas, modelos, contas, repositórios e dados autorizados. Comece com ambientes isolados e dados sintéticos. Proteja credenciais, prompts, saídas, rastros, informações pessoais e constatações. Registre versões e valide resultados automatizados. |
|---|

## 30.1 MLflow

**Finalidade:** Rastreamento de experimentos, registro de modelos, linhagem, aprovação e registros de implantação. Projeto oficial: [MLflow](https://mlflow.org/)

**Início seguro:** Crie projeto local; registre parâmetros, referência de conjunto de dados, métricas, artefatos, proprietário e aprovação; registre apenas modelo testado; restrinja mudanças no registro.

**Evidência do SGIA:** autoridade/escopo, versões de sistema/modelo/dados, identidade, ferramenta/versão/configuração, critérios/limites, data, população-fonte, resultado, validação humana, limitações, constatação, proprietário/ação, aprovação e reteste.

## 30.2 DVC

**Finalidade:** Controle de versões para dados, modelos e pipelines. Projeto oficial: [DVC](https://dvc.org/)

**Início seguro:** Use conjunto de dados sintético em repositório de treinamento; versione dados e etapas de pipeline; reproduza uma execução; proteja armazenamento remoto e credenciais.

**Evidência do SGIA:** autoridade/escopo, versões de sistema/modelo/dados, identidade, ferramenta/versão/configuração, critérios/limites, data, população-fonte, resultado, validação humana, limitações, constatação, proprietário/ação, aprovação e reteste.

## 30.3 OpenLineage

**Finalidade:** Padrão aberto e ferramentas para eventos de linhagem de dados/trabalhos. Projeto oficial: [OpenLineage](https://openlineage.io/)

**Início seguro:** Instrumente pequeno pipeline de laboratório; registre relações entre conjuntos de dados e trabalhos; verifique completude de eventos; proteja metadados sensíveis.

**Evidência do SGIA:** autoridade/escopo, versões de sistema/modelo/dados, identidade, ferramenta/versão/configuração, critérios/limites, data, população-fonte, resultado, validação humana, limitações, constatação, proprietário/ação, aprovação e reteste.

## 30.4 OpenMetadata

**Finalidade:** Catálogo de dados, linhagem, propriedade, glossário e metadados de qualidade. Projeto oficial: [OpenMetadata](https://open-metadata.org/)

**Início seguro:** Implante instância de laboratório; catalogue conjuntos sintéticos; atribua proprietários/classificação; documente linhagem e retenção; restrinja conectores.

**Evidência do SGIA:** autoridade/escopo, versões de sistema/modelo/dados, identidade, ferramenta/versão/configuração, critérios/limites, data, população-fonte, resultado, validação humana, limitações, constatação, proprietário/ação, aprovação e reteste.

## 30.5 Great Expectations

**Finalidade:** Expectativas automatizadas de qualidade de dados e resultados de validação. Projeto oficial: [Great Expectations](https://greatexpectations.io/)

**Início seguro:** Defina expectativas de precisão, completude, faixa e nulos para dados sintéticos; execute validação; preserve suite/versão/resultados e exceções.

**Evidência do SGIA:** autoridade/escopo, versões de sistema/modelo/dados, identidade, ferramenta/versão/configuração, critérios/limites, data, população-fonte, resultado, validação humana, limitações, constatação, proprietário/ação, aprovação e reteste.

## 30.6 Evidently

**Finalidade:** Qualidade de dados, drift, desempenho do modelo e relatórios de monitoramento. Projeto oficial: [Evidently](https://www.evidentlyai.com/)

**Início seguro:** Crie conjuntos sintéticos de referência e atuais; execute relatório; defina limites de ação; investigue antes de retreinar ou fazer rollback.

**Evidência do SGIA:** autoridade/escopo, versões de sistema/modelo/dados, identidade, ferramenta/versão/configuração, critérios/limites, data, população-fonte, resultado, validação humana, limitações, constatação, proprietário/ação, aprovação e reteste.

## 30.7 Deepchecks

**Finalidade:** Testes de dados, modelos de ML e aplicações LLM. Projeto oficial: [Deepchecks](https://github.com/deepchecks/deepchecks)

**Início seguro:** Execute suite focada sobre dados de laboratório aprovados; revise relevância e falsos positivos; registre exceções; repita após correção.

**Evidência do SGIA:** autoridade/escopo, versões de sistema/modelo/dados, identidade, ferramenta/versão/configuração, critérios/limites, data, população-fonte, resultado, validação humana, limitações, constatação, proprietário/ação, aprovação e reteste.

## 30.8 Giskard

**Finalidade:** Testes de IA e varredura de vulnerabilidades. Projeto oficial: [Giskard](https://github.com/Giskard-AI/giskard-oss)

**Início seguro:** Conecte apenas modelo e conjunto de teste aprovados; selecione testes relevantes; valide falhas manualmente; preserve relatório e reteste de remediação.

**Evidência do SGIA:** autoridade/escopo, versões de sistema/modelo/dados, identidade, ferramenta/versão/configuração, critérios/limites, data, população-fonte, resultado, validação humana, limitações, constatação, proprietário/ação, aprovação e reteste.

## 30.9 Promptfoo

**Finalidade:** Avaliações de prompts, modelos, RAG e red teaming. Projeto oficial: [Promptfoo](https://www.promptfoo.dev/)

**Início seguro:** Crie suite YAML versionada com casos sintéticos e comportamento esperado; execute localmente; revise falhas; preserve configuração e resultados.

**Evidência do SGIA:** autoridade/escopo, versões de sistema/modelo/dados, identidade, ferramenta/versão/configuração, critérios/limites, data, população-fonte, resultado, validação humana, limitações, constatação, proprietário/ação, aprovação e reteste.

## 30.10 Garak

**Finalidade:** Varredura e sondas de vulnerabilidades de LLM. Projeto oficial: [Garak](https://github.com/NVIDIA/garak)

**Início seguro:** Use modelo isolado de laboratório e conjunto limitado de sondas aprovadas; limite solicitações e custo; proteja saídas; valide cada constatação.

**Evidência do SGIA:** autoridade/escopo, versões de sistema/modelo/dados, identidade, ferramenta/versão/configuração, critérios/limites, data, população-fonte, resultado, validação humana, limitações, constatação, proprietário/ação, aprovação e reteste.

## 30.11 PyRIT

**Finalidade:** Identificação de riscos e orquestração de red teaming para IA generativa. Projeto oficial: [PyRIT](https://github.com/microsoft/PyRIT)

**Início seguro:** Defina regras de laboratório por escrito; use objetivos inofensivos e dados sintéticos; estabeleça limites de solicitações/tempo/custo; proteja transcrições e constatações.

**Evidência do SGIA:** autoridade/escopo, versões de sistema/modelo/dados, identidade, ferramenta/versão/configuração, critérios/limites, data, população-fonte, resultado, validação humana, limitações, constatação, proprietário/ação, aprovação e reteste.

## 30.12 Inspect AI

**Finalidade:** Avaliações reproduzíveis de IA. Projeto oficial: [Inspect AI](https://inspect.aisi.org.uk/)

**Início seguro:** Defina tarefa, conjunto de dados, solver, avaliador e regra de aceitação; fixe versões; execute modelo aprovado; preserve logs e limitações.

**Evidência do SGIA:** autoridade/escopo, versões de sistema/modelo/dados, identidade, ferramenta/versão/configuração, critérios/limites, data, população-fonte, resultado, validação humana, limitações, constatação, proprietário/ação, aprovação e reteste.

## 30.13 Presidio

**Finalidade:** Detecção e desidentificação de informações pessoais. Projeto oficial: [Presidio](https://presidio.dataprivacystack.org/)

**Início seguro:** Teste em exemplos sintéticos; configure reconhecedores para idioma/contexto; inspecione falsos positivos e perdas; proteja a saída do analisador.

**Evidência do SGIA:** autoridade/escopo, versões de sistema/modelo/dados, identidade, ferramenta/versão/configuração, critérios/limites, data, população-fonte, resultado, validação humana, limitações, constatação, proprietário/ação, aprovação e reteste.

## 30.14 ModelScan

**Finalidade:** Varredura estática de arquivos de modelos serializados. Projeto oficial: [ModelScan](https://github.com/protectai/modelscan)

**Início seguro:** Analise artefato em quarentena; verifique fonte e hash; investigue alertas; nunca carregue modelo não confiável somente para testá-lo.

**Evidência do SGIA:** autoridade/escopo, versões de sistema/modelo/dados, identidade, ferramenta/versão/configuração, critérios/limites, data, população-fonte, resultado, validação humana, limitações, constatação, proprietário/ação, aprovação e reteste.

## 30.15 CycloneDX

**Finalidade:** Formatos e ferramentas de lista de materiais de software, ML e IA. Projeto oficial: [CycloneDX](https://cyclonedx.org/)

**Início seguro:** Gere lista de materiais para repositório de laboratório; valide componentes e versões; vincule constatações a proprietários e registros de fornecedores.

**Evidência do SGIA:** autoridade/escopo, versões de sistema/modelo/dados, identidade, ferramenta/versão/configuração, critérios/limites, data, população-fonte, resultado, validação humana, limitações, constatação, proprietário/ação, aprovação e reteste.

## 30.16 Open Policy Agent

**Finalidade:** Decisões de política como código. Projeto oficial: [Open Policy Agent](https://www.openpolicyagent.org/)

**Início seguro:** Escreva pequena regra de laboratório para modelo/dados/uso aprovados; teste permitir, negar e casos sem dados; faça revisão por pares; preserve autoridade humana de exceção.

**Evidência do SGIA:** autoridade/escopo, versões de sistema/modelo/dados, identidade, ferramenta/versão/configuração, critérios/limites, data, população-fonte, resultado, validação humana, limitações, constatação, proprietário/ação, aprovação e reteste.

## 30.17 DefectDojo

**Finalidade:** Admissão, deduplicação, propriedade, remediação e reteste de constatações. Projeto oficial: [DefectDojo](https://www.defectdojo.org/)

**Início seguro:** Importe resultados seguros de laboratório; valide duplicatas e severidade; atribua proprietário/data; anexe evidências; encerre apenas após reteste.

**Evidência do SGIA:** autoridade/escopo, versões de sistema/modelo/dados, identidade, ferramenta/versão/configuração, critérios/limites, data, população-fonte, resultado, validação humana, limitações, constatação, proprietário/ação, aprovação e reteste.

## 30.18 Langfuse

**Finalidade:** Rastreamento de LLM, gestão de prompts e avaliação de código aberto. Projeto oficial: [Langfuse](https://langfuse.com/)

**Início seguro:** Use laboratório aprovado; oculte campos sensíveis; rastreie fluxo; restrinja acesso/retenção; conecte rastros a avaliação e registros de incidentes.

**Evidência do SGIA:** autoridade/escopo, versões de sistema/modelo/dados, identidade, ferramenta/versão/configuração, critérios/limites, data, população-fonte, resultado, validação humana, limitações, constatação, proprietário/ação, aprovação e reteste.

# 31. Guia de gestores e analistas juniores, laboratório e entrevistas

*Gestores mantêm o SGIA ligado a resultados reais; analistas juniores criam inventários, papéis de trabalho, constatações e evidências de melhoria confiáveis.*

<img src="../../../assets/pt-BR/media/image10.png" style="width:6.15in;height:3.23274in" alt="Trabalho prático e limitações declaradas com honestidade valem mais que números de cláusulas memorizados." />

Figura 10. Caminho do analista júnior de SGIA

> **Explicação acessível:** O caminho do analista júnior começa com compreensão de escopo e critérios, segue por inventários e evidências, testes e papéis de trabalho, redação objetiva de constatações, acompanhamento de ações e aprendizagem contínua, sem assumir autoridade de certificação ou auditoria que não corresponda.

## 31.1 Perguntas para gestores

| **Pergunta** | **Evidência forte** | **Sinal de alerta** |
|---|---|---|
| O que está no escopo? | Inventário reconciliado de IA e limites de organização/papel/sistema/dados/fornecedor | Escopo de marketing maior que o certificado |
| Quem pode decidir? | Autoridade nomeada de negócio, sistema, dados, impacto, risco, fornecedor, incidente e auditoria | Equipe de IA aceita sozinha risco jurídico/comercial |
| Que danos são possíveis? | Avaliações atuais de risco e impacto com pessoas afetadas e alternativas | Apenas precisão do modelo considerada |
| O que comprova prontidão? | Avaliação versionada e semelhante à produção, limites, falhas, supervisão e rollback | Apenas demonstração do fornecedor ou política |
| O que muda o risco? | Lista de gatilhos, monitoramento, aviso de fornecedor, regressão e reavaliação | Atualizações automáticas sem revisão |
| O SGIA está melhorando? | Objetivos, auditoria, reclamações/incidentes, causas-raiz e ações eficazes | Certificado é a única medida de sucesso |

## 31.2 Trabalho do analista júnior

- Mantenha inventário de IA, escopo, partes interessadas, obrigações, registros de risco/impacto, Declaração de Aplicabilidade, registros de fornecedores, objetivos, evidências e ações.
- Mapeie cláusulas/controles para processos e evidências reais do sistema; reconcilie populações e versões.
- Teste controle documental, competência, marcos do ciclo de vida, linhagem/qualidade de dados, avaliação, uso responsável, mudança de fornecedores, monitoramento, incidentes e ação corretiva.
- Redija constatações objetivas e resumos para gestores; acompanhe correção e reteste de eficácia.
- Apoie auditorias internas e análise crítica pela direção sem tomar decisões reservadas a proprietários ou auditores.

| **Regra do laboratório de portfólio:** Use organização fictícia, dados sintéticos e modelos locais ou de teste aprovados. Nunca alegue que o projeto é certificado, auditado por organismo acreditado ou baseado em evidências confidenciais de empregador. |
|---|

## 31.3 Laboratório fictício

- Crie empresa fictícia de 100 pessoas que desenvolve assistente RAG de suporte ao cliente e usa assistente adquirido para redação de RH que não pode tomar decisões de emprego.
- Defina contexto do SGIA, partes interessadas, papéis, escopo, política, mapa de processos, inventário de IA, obrigações e roteiro de implementação.
- Crie método de risco, seis cenários, plano de tratamento, Declaração de Aplicabilidade de 38 controles e duas avaliações de impacto usando conceitos da ISO/IEC 42005.
- Construa registros de recursos, conjuntos de dados, modelo/sistema, fornecedores, informação ao usuário, comunicação, competência e controle documental.
- Execute avaliações sintéticas com duas ferramentas de código aberto; preserve versões, limites, falhas, correção e reteste.
- Crie objetivos/painel, plano de auditoria interna e cinco papéis de trabalho, duas constatações, ações corretivas, pacote de análise crítica pela direção e relatório de prontidão para certificação.
- Publique apenas evidências fictícias sanitizadas e declaração honesta de limitações.

## 31.4 Plano de trinta dias

| **Dias** | **Foco** | **Entregável** |
|---|---|---|
| 1–3 | Norma, SGIA, PDCA | Mapa de cláusulas e glossário |
| 4–6 | Contexto, partes, escopo | Escopo e registro de partes interessadas |
| 7–9 | Liderança e planejamento | Política, RACI e objetivos |
| 10–12 | Risco e tratamento | Método, registro, plano e Declaração de Aplicabilidade |
| 13–15 | Avaliação de impacto | Dois papéis de trabalho de impacto |
| 16–18 | Suporte e documentos | Competência, comunicação e controles documentais |
| 19–21 | Ciclo de vida, dados, uso e fornecedores | Cinco papéis de trabalho de controles |
| 22–24 | Medição e ferramentas | Painel e evidências de avaliação |
| 25–27 | Auditoria e ação corretiva | Relatório de auditoria, constatações e plano de eficácia |
| 28–30 | Análise crítica pela direção e entrevista | Pacote de análise crítica, memorando de prontidão e histórias STAR |

## 31.5 O que é ISO/IEC 42001?

Uma norma certificável de sistema de gestão para organizações que desenvolvem, fornecem ou usam sistemas de IA. Estabelece requisitos para governança responsável, risco, impacto, operação, avaliação e melhoria.

## 31.6 O que é um SGIA?

As políticas, objetivos, processos, papéis, controles e registros inter-relacionados da organização para gerir IA responsavelmente dentro de um escopo definido.

## 31.7 Todos os controles do Anexo A são obrigatórios?

São controles de referência considerados por meio do tratamento de riscos. A organização documenta aplicabilidade e implementação na Declaração de Aplicabilidade e pode adicionar outros controles.

## 31.8 Avaliação de riscos versus avaliação de impacto?

A avaliação de riscos gerencia incerteza que afeta objetivos. A avaliação de impacto de sistemas de IA foca efeitos sobre indivíduos, grupos e sociedade. Elas trocam constatações, mas não são idênticas.

## 31.9 O que é a Declaração de Aplicabilidade?

Registro controlado que explica quais controles do Anexo A e adicionais se aplicam, por quê, como são implementados, seu status, evidências, lacunas e revisão.

## 31.10 Estágio 1 versus Estágio 2?

Estágio 1 avalia escopo, sistema documentado, prontidão e planejamento. Estágio 2 avalia implementação e eficácia operacional por evidências e amostragem.

## 31.11 O que é uma não conformidade?

Um requisito não é atendido. A constatação deve identificar critérios, evidência objetiva e lacuna sem prescrever a solução do auditado.

## 31.12 Como ferramentas comprovam conformidade?

Elas não comprovam. Ferramentas produzem evidências que devem ser delimitadas, validadas, interpretadas em relação aos requisitos, conectadas aos controles e revisadas por pessoas competentes.

## 31.13 Como testar uma ação corretiva?

Verifique correção, ação sobre causa-raiz, aplicação a condições semelhantes e evidência de que o risco de recorrência foi reduzido após operação suficiente.

## 31.14 O que caracteriza um bom analista júnior?

Escopo preciso, evidências cuidadosas, compreensão de cláusulas, redação clara, respeito às pessoas afetadas, incerteza honesta, uso seguro de ferramentas e acompanhamento confiável.

# 32. Modelos, glossário, índice e referências oficiais

*Estruturas reutilizáveis de trabalho e referências autoritativas apoiam implementação e auditoria consistentes do SGIA.*

## 32.1 Registro de escopo e contexto do SGIA

| **Campo** | **Entrada** |
|---|---|
| Organizações/unidades/locais | ________________________________________ |
| Papel de IA, produtos/serviços/processos | ________________________________________ |
| Sistemas/modelos/dados/ambientes de IA | ________________________________________ |
| Questões internas/externas | ________________________________________ |
| Partes interessadas e requisitos | ________________________________________ |
| Obrigações legais/contratuais | ________________________________________ |
| Limites, interfaces e dependências | ________________________________________ |
| Processos terceirizados/compartilhados | ________________________________________ |
| Exclusões e justificativa | ________________________________________ |
| Aprovação do escopo e gatilhos de revisão | ________________________________________ |

## 32.2 Registro de risco e tratamento de IA

| **Campo** | **Entrada** |
|---|---|
| Sistema/uso/versão/proprietário | ________________________________________ |
| Cenário, parte afetada, consequência | ________________________________________ |
| Probabilidade/impacto/incerteza/evidência | ________________________________________ |
| Controles existentes e eficácia | ________________________________________ |
| Avaliação/tolerância de risco | ________________________________________ |
| Opção de tratamento/controle | ________________________________________ |
| Mapeamento ao Anexo A/controle adicional | ________________________________________ |
| Proprietário/recurso/data/medida | ________________________________________ |
| Risco residual/aprovador/condições | ________________________________________ |
| Monitoramento/revisão/reteste | ________________________________________ |

## 32.3 Declaração de Aplicabilidade

| **Campo** | **Entrada** |
|---|---|
| Referência/título do controle | ________________________________________ |
| Aplicabilidade e justificativa | ________________________________________ |
| Risco/impacto/obrigação relacionada | ________________________________________ |
| Implementação e proprietário | ________________________________________ |
| Status e data-alvo | ________________________________________ |
| Evidência e resultado de teste | ________________________________________ |
| Dependências de fornecedor/cliente | ________________________________________ |
| Lacuna/exceção/risco residual | ________________________________________ |
| Última/próxima revisão | ________________________________________ |
| Histórico de mudanças/aprovação | ________________________________________ |

## 32.4 Avaliação de impacto de sistemas de IA

| **Campo** | **Entrada** |
|---|---|
| Finalidade, uso, pessoas afetadas, alternativas | ________________________________________ |
| Sistema/dados/modelo/fornecedor/contexto | ________________________________________ |
| Benefícios e impactos adversos | ________________________________________ |
| Efeitos individuais/de grupo/sociais | ________________________________________ |
| Probabilidade/gravidade/escala/duração | ________________________________________ |
| Reversibilidade/distribuição/incerteza | ________________________________________ |
| Participação de partes interessadas | ________________________________________ |
| Mitigação/supervisão/transparência/reparação | ________________________________________ |
| Decisão/autoridade/condições | ________________________________________ |
| Monitoramento/gatilhos/revisão | ________________________________________ |

## 32.5 Papel de trabalho de auditoria interna

| **Campo** | **Entrada** |
|---|---|
| Critérios/escopo/objetivo | ________________________________________ |
| Processo/sistema/versão/período | ________________________________________ |
| População/amostra/justificativa | ________________________________________ |
| Evidência/fonte/confiabilidade | ________________________________________ |
| Teste/resultado esperado | ________________________________________ |
| Resultado observado/exceções | ________________________________________ |
| Conclusão/não conformidade | ________________________________________ |
| Indicação de risco/impacto/causa | ________________________________________ |
| Correção/ação corretiva | ________________________________________ |
| Eficácia/acompanhamento/encerramento | ________________________________________ |

## 32.6 Registro de análise crítica pela direção

| **Campo** | **Entrada** |
|---|---|
| Status das ações anteriores | ________________________________________ |
| Mudanças de contexto/partes | ________________________________________ |
| Objetivos/tendências de desempenho | ________________________________________ |
| Risco/impacto/tratamento/Declaração de Aplicabilidade | ________________________________________ |
| Auditoria/não conformidade/ação corretiva | ________________________________________ |
| Incidentes/reclamações/preocupações/reparação | ________________________________________ |
| Mudanças de fornecedores/jurídicas/sistemas | ________________________________________ |
| Recursos/competência | ________________________________________ |
| Decisões/ações/proprietários/datas | ________________________________________ |
| Eficácia/acompanhamento | ________________________________________ |

## 32.7 Glossário

| **Termo** | **Significado** |
|---|---|
| SGIA | Sistema de gestão de inteligência artificial. |
| Avaliação de impacto de sistemas de IA | Avaliação estruturada de efeitos potenciais sobre indivíduos, grupos e sociedade. |
| Anexo A | Objetivos de controle e controles de referência da ISO/IEC 42001. |
| Anexo B | Orientação para implementação dos controles do Anexo A. |
| Certificação | Atestação de terceira parte de que o SGIA delimitado está conforme com requisitos especificados. |
| Conformidade | Atendimento de um requisito. |
| Controle | Medida que mantém ou modifica o risco. |
| Correção | Ação para eliminar uma não conformidade detectada. |
| Ação corretiva | Ação para eliminar causa e prevenir recorrência. |
| Informação documentada | Informação que a organização controla e mantém, além de seu meio. |
| Parte interessada | Pessoa ou organização que pode afetar, ser afetada ou perceber-se afetada por decisão/atividade. |
| Auditoria interna | Processo sistemático independente e objetivo para avaliar evidências em relação a critérios. |
| Não conformidade | Não atendimento de um requisito. |
| Objetivo | Resultado a ser alcançado. |
| Risco residual | Risco restante após tratamento. |
| Proprietário do risco | Pessoa/entidade com responsabilização e autoridade para gerenciar risco. |
| Declaração de Aplicabilidade (SoA) | Registro de aplicabilidade dos controles do SGIA. |
| Estágio 1 | Etapa de auditoria de prontidão para certificação e sistema documentado. |
| Estágio 2 | Etapa de auditoria de implementação e eficácia operacional para certificação. |
| Alta direção | Pessoa/grupo que dirige e controla a organização no nível mais alto dentro do escopo. |

## 32.8 Índice temático

| **Tema** | **Capítulo** |
|---|---:|
| Controles do Anexo A | 20–28 |
| Auditoria | 17, 29 |
| Certificação | 29 |
| Contexto/escopo | 3–4 |
| Ação corretiva | 19 |
| Dados | 23, 26 |
| Documentos | 13 |
| Avaliação de impacto | 9, 24 |
| Partes interessadas | 4, 27 |
| Liderança/política | 5, 21 |
| Ciclo de vida | 14–15, 25 |
| Gestor/analista júnior | 31 |
| Medição/análise crítica | 16–18 |
| Objetivos/mudança | 10 |
| Recursos/competência | 11–12, 23 |
| Risco/tratamento/Declaração de Aplicabilidade | 6–8 |
| Fornecedores/uso | 28 |
| Ferramentas | 30 |

## 32.9 Referências oficiais

- [Página oficial ISO/IEC 42001:2023](https://www.iso.org/standard/42001)
- [ISO 42001 explicada](https://www.iso.org/home/insights-news/resources/iso-42001-explained-what-it-is.html)
- [ISO/IEC 42001 Online Browsing Platform](https://www.iso.org/obp/ui/en/#iso:std:iso-iec:42001:ed-1:v1:en)
- [ISO/IEC 42005:2025 — avaliação de impacto de sistemas de IA](https://www.iso.org/standard/42005)
- [ISO/IEC 42006:2025 — organismos de certificação](https://www.iso.org/standard/42006)
- [ISO 19011:2026 — diretrizes de auditoria](https://www.iso.org/standard/19011)
- [ISO/IEC 23894:2023 — gestão de riscos de IA](https://www.iso.org/standard/77304.html)
- [ISO/IEC 22989:2022 — conceitos e terminologia de IA](https://www.iso.org/standard/74296.html)
- [ISO/IEC 23053:2022 — estrutura de sistemas de ML](https://www.iso.org/standard/74438.html)
- [ISO/IEC 38507:2022 — implicações de governança de IA](https://www.iso.org/standard/56641.html)
- [ISO/IEC 27001:2022 — requisitos de sistemas de gestão de segurança da informação](https://www.iso.org/standard/27001)
- [ISO/IEC 27001:2022/Amd 1:2024 — mudanças relativas à ação climática](https://www.iso.org/standard/88435.html)
- [ISO/IEC 17021-1:2015 — organismos de auditoria e certificação de sistemas de gestão](https://www.iso.org/standard/61651.html)
- [Catálogo ISO/IEC JTC 1/SC 42](https://committee.iso.org/committee/6794475/x/catalogue/)
- [Normas ISO de sistemas de gestão](https://www.iso.org/management-system-standards.html)
- [IAF CertSearch](https://www.iafcertsearch.org/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [Princípios de IA da OCDE](https://oecd.ai/en/ai-principles)
- [Página oficial de política do Regulamento de IA da UE](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

| **Lembrete final:** Use uma cópia autorizada da norma. Normas ISO, esquemas de certificação, acreditação, leis, sistemas de IA, fornecedores, riscos, ferramentas e orientações oficiais mudam. Verifique a fonte atual, edição exata, escopo/status do certificado, versão do sistema e fatos organizacionais antes de implementação, auditoria, certificação ou alegações públicas. |
|---|
