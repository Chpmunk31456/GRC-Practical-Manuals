# NIST CSF 2.0 — Bloco revisado em português do Brasil

## Capítulo 10. Perfis Organizacionais

*Como descrever a postura atual, definir um objetivo e criar um plano de ação priorizado.*

<img src="media/image3_ptbr.png" style="width:6.15in;height:3.39605in" alt="Um Perfil-Alvo é útil quando suas lacunas se transformam em ações baseadas em risco, com responsáveis e recursos definidos." />

**Figura 3. Do Perfil Atual ao plano de ação**

### 10.1 Declaração de escopo do Perfil

- Objetivo empresarial ou de missão.
- Sistemas, serviços, dados, instalações, pessoas, fornecedores e localidades incluídos.
- Período avaliado e data da evidência.
- Partes interessadas e autoridade para decisão.
- Obrigações legais, contratuais e de política, além dos Perfis da Comunidade utilizados como referência.
- Premissas, exclusões, dependências e limitações.

### 10.2 Status dos resultados

| **Status** | **Significado** | **Suporte necessário** |
|---|---|---|
| Alcançado | O resultado, dentro do escopo definido, está implementado e opera conforme o esperado. | Responsável, população completa, desenho, evidência operacional, teste e conclusão. |
| Parcialmente alcançado | Parte do escopo está ausente ou a operação é incompleta ou inconsistente. | Lacuna exata, risco afetado, ação provisória, responsável e prazo. |
| Não alcançado | O resultado é aplicável, mas não está em operação. | Decisão de risco, tratamento, recursos e cronograma. |
| Não aplicável | O resultado não se aplica ao escopo definido. | Justificativa documentada e aprovação. |
| Não avaliado | A evidência é insuficiente para uma conclusão. | Solicitação de evidência, responsável e prazo. |

### 10.3 Priorização de lacunas

Priorize as lacunas considerando impacto na missão, probabilidade de ameaça, criticidade dos ativos, obrigações legais e contratuais, exposição, dependências, segurança física, privacidade, controles atuais, tempo estimado para exploração, esforço de correção e recursos disponíveis. Não classifique lacunas apenas pela severidade indicada por uma ferramenta de varredura.

# Capítulo 11. Níveis do CSF

*Como utilizar Parcial, Informado pelo Risco, Repetível e Adaptativo sem transformá-los em uma pontuação.*

<img src="media/image4_ptbr.png" style="width:6.15in;height:3.35755in" alt="Os Níveis do CSF oferecem contexto sobre o rigor da governança e das práticas de gestão de riscos." />

**Figura 4. Níveis do CSF**

| **Nível** | **Significado prático** | **Evidência útil** |
|---|---|---|
| Nível 1 — Parcial | As práticas são principalmente informais, irregulares e nem sempre orientadas por objetivos ou ameaças. | Decisões caso a caso e ausência de processos consistentes em toda a organização. |
| Nível 2 — Informado pelo Risco | A direção aprova práticas de risco, mas elas não estão estabelecidas de forma consistente em toda a organização. | Práticas aprovadas, implementação local e conhecimento parcial de riscos e fornecedores. |
| Nível 3 — Repetível | Políticas e práticas repetíveis estão definidas, implementadas, revisadas e atualizadas em toda a organização. | Políticas aprovadas, execução consistente, funções qualificadas, compartilhamento periódico de informações e ações sobre fornecedores. |
| Nível 4 — Adaptativo | A gestão de riscos faz parte da cultura e se adapta por meio de lições aprendidas, informações preditivas e percepção quase em tempo real. | Decisões integradas à gestão de riscos corporativos, controles adaptativos, melhoria contínua e resposta oportuna ao risco de fornecedores. |

- Selecione o Nível para um escopo de Perfil definido, e não como um rótulo genérico para toda a empresa.
- Use risco, missão, obrigações, custo e benefício para definir o Nível-Alvo.
- Não faça média dos números dos Níveis para criar uma pontuação enganosa.
- Documente a evidência e as diferenças entre Funções.
- Reavalie quando houver mudanças relevantes em risco, missão, fornecedores ou tecnologia.

# Capítulo 12. Risco corporativo, apetite a risco e comunicação

*Como conectar a cibersegurança às decisões executivas e do órgão de governança.*

| **Conceito** | **Significado prático** | **Exemplo** |
|---|---|---|
| Apetite a risco | Quantidade e tipo geral de risco que a organização está disposta a assumir ou reter. | Apetite muito baixo para interrupção de serviços de emergência. |
| Tolerância a risco | Variação específica aceitável em torno de um objetivo. | No máximo quatro horas de indisponibilidade para um serviço crítico definido. |
| Risco inerente | Risco antes de considerar os controles. | Serviço exposto à Internet com dados valiosos e ameaças ativas. |
| Risco residual | Risco que permanece após a aplicação dos controles. | Risco remanescente de indisponibilidade ou violação após MFA, segmentação, monitoramento e recuperação. |
| Resposta ao risco | Aceitar, evitar, mitigar, transferir ou compartilhar o risco, ou aproveitar uma oportunidade. | Retirar software sem suporte, reduzir exposição e segurar parte do risco residual. |
| Risco positivo | Oportunidade que pode melhorar o alcance dos objetivos. | Automação segura que reduz erros e melhora a velocidade de detecção. |

## 12.1 Declaração executiva de risco

> **Modelo:** Como [ameaça] pode explorar [vulnerabilidade] e afetar [ativo ou objetivo], a organização pode sofrer [impacto empresarial]. Os controles existentes [resumo] deixam [exposição residual]. A direção deve [resposta] até [data], sob responsabilidade de [função], e monitorar [medida].

## 12.2 Perguntas para o órgão de governança

- Quais objetivos de missão e serviços críticos enfrentam o maior risco cibernético?
- Quais riscos excedem o apetite ou a tolerância aprovados?
- Quais decisões exigem financiamento ou aceitação explícita do risco?
- Quão confiável é a evidência que sustenta o status informado?
- Onde existem concentrações de fornecedores ou pontos únicos de falha?
- O que incidentes, exercícios, auditorias e quase incidentes nos ensinaram?
- As capacidades de recuperação foram comprovadas para os serviços mais importantes?

# Capítulo 13. Risco de cibersegurança na cadeia de suprimentos

*Como gerenciar fornecedores, produtos, serviços e dependências ao longo de todo o ciclo de vida.*

<img src="media/image5_ptbr.png" style="width:6.15in;height:3.21373in" alt="Planejar, selecionar, contratar, monitorar e encerrar relações com responsabilidades de segurança claramente definidas." />

**Figura 5. Ciclo de vida da cibersegurança na cadeia de suprimentos**

1. Mantenha um inventário de fornecedores, subcontratados, produtos, serviços, fluxos de dados, acessos, localidades e dependências.
2. Classifique as relações por criticidade, sensibilidade, acesso, possibilidade de substituição, concentração, segurança física e impacto operacional.
3. Realize diligência prévia proporcional antes da compra ou renovação.
4. Inclua nos contratos obrigações mensuráveis sobre cibersegurança, incidentes, notificação, evidência, subcontratados, resiliência, devolução e destruição de dados.
5. Monitore mudanças, achados, incidentes, saúde financeira, desempenho do serviço e dependências materiais de quartas partes.
6. Inclua terceiros críticos em exercícios, resposta, recuperação e comunicação.
7. No encerramento, remova acessos, recupere ativos, devolva ou destrua dados, transfira conhecimento, preserve registros obrigatórios e valide a conclusão.

> **Alerta contratual:** Um questionário ou uma cláusula contratual, por si só, não comprova que os controles do fornecedor funcionam. Combine direitos contratuais com evidência baseada em risco, monitoramento, informações sobre incidentes e acompanhamento de ações corretivas.

# Capítulo 14. Métricas, evidências e relatórios

*Medidas que apoiam decisões, em vez de produzir painéis meramente decorativos.*

| **Tipo de medida** | **Pergunta respondida** | **Exemplo** |
|---|---|---|
| Medida de implementação | A salvaguarda foi implantada? | Percentual de contas privilegiadas no escopo que usam MFA resistente a phishing. |
| Medida operacional | Está funcionando de forma consistente? | Percentual de contas de pessoas desligadas desabilitadas dentro do prazo aprovado. |
| Indicador de risco | A exposição está aumentando? | Vulnerabilidades críticas vencidas em ativos expostos à Internet. |
| Medida de resultado | O resultado desejado está ocorrendo? | Redução de eventos de acesso não autorizado para o serviço avaliado. |
| Medida de resiliência | A organização consegue continuar e se recuperar? | Percentual de restaurações de serviços críticos que atendem aos objetivos de recuperação. |
| Medida de qualidade da evidência | O status informado é confiável? | Percentual de conclusões sustentadas por populações completas e testes independentes. |

<img src="media/image6_ptbr.png" style="width:6.15in;height:2.73265in" alt="Um mapeamento se torna confiável quando os controles e as evidências operacionais são testados." />

**Figura 6. Cadeia do resultado à evidência**

## 14.1 Qualidade da evidência

| **Qualidade** | **Exemplo** | **Resposta do analista** |
|---|---|---|
| Fraca | Declaração verbal, captura de tela sem data, exportação parcial ou resumo sem suporte. | Solicitar fonte, data, escopo, população, responsável, revisor e identidade do sistema. |
| Útil | Relatório datado do sistema, vinculado ao escopo e período corretos. | Confirmar configuração, completude, acesso, interpretação e exceções. |
| Forte | Dados do sistema somados a revisão independente, decisões, ação corretiva e novo teste. | Rastrear toda a cadeia de evidência e declarar as limitações. |

# Capítulo 15. Verificação de conformidade e testes de controles

*Como determinar se um resultado do CSF, dentro de um escopo definido, foi realmente alcançado.*

> **Distinção importante:** Alinhamento ao CSF não equivale automaticamente a conformidade legal, certificação ou opinião de auditoria. Teste as obrigações e os controles realmente aplicáveis à organização e use os resultados do CSF para organizar e comunicar as conclusões.

1. Defina o resultado do CSF, risco, controle, responsável, sistemas, localidades, população, período, frequência e evidência esperada.
2. Avalie o desenho do controle: se executado conforme descrito, ele alcançaria razoavelmente o resultado pretendido?
3. Obtenha a população completa e teste sua completude e exatidão contra uma fonte independente.
4. Selecione uma amostra baseada em risco que cubra datas, sistemas, responsáveis, localidades, itens incomuns e falhas relevantes.
5. Inspecione a evidência e, quando possível, refaça ou confirme de forma independente o resultado do controle.
6. Registre exceções com critérios, fatos, duração, ativos afetados, causa, probabilidade, impacto e proteções existentes.
7. Defina ação corretiva, proteção provisória, responsável, recursos, prazo e escalonamento.
8. Refaça o teste sobre a população afetada e redija uma conclusão clara, incluindo limitações.

## 15.1 Testes práticos de verificação

| **Área de controle** | **População e amostra** | **Procedimento de teste** | **Evidência** |
|---|---|---|---|
| Inventário de ativos | Todos os ativos no escopo; incluir na amostra ativos críticos, novos, em nuvem, remotos, gerenciados por fornecedores e desativados. | Conciliar o inventário com fontes de identidade, rede, nuvem, compras, vulnerabilidades e endpoints. | Exportações, conciliação, propriedade, lacunas, correção e novo teste. |
| Ciclo de vida do acesso | Todas as admissões, mudanças, desligamentos, contas de serviço e contas privilegiadas. | Comparar aprovações e necessidade da função com prazos de provisionamento, revisão, alteração e remoção. | Populações de RH e IAM, aprovações, revisões, chamados, logs e exceções. |
| Gestão de vulnerabilidades | Todos os ativos e achados; incluir críticos, altos, antigos, aceitos e encerrados. | Validar cobertura e credenciais; confirmar achado, prazo, correção, exceção e nova varredura. | Inventário, configuração de varredura, relatório, chamados, aprovações e nova varredura. |
| Logs e detecção | Todas as fontes de log exigidas, alertas, revisões e incidentes. | Testar cobertura de fontes, horário, regra, geração de alerta, revisão, escalonamento e retenção. | Lista de fontes, configuração, alerta, chamado, revisão e encerramento. |
| Backup e recuperação | Todos os trabalhos de backup e testes exigidos; incluir sucessos, falhas e serviços críticos. | Examinar proteção, resposta a falhas, restauração, integridade, objetivos de recuperação e lições aprendidas. | Trabalhos, alertas, resultados de restauração, exercícios, correções e novo teste. |
| Supervisão de fornecedores | Todos os fornecedores; incluir críticos, novos, alterados, envolvidos em incidentes e relações encerradas. | Testar classificação, diligência prévia, contrato, monitoramento, obrigações de incidente, ação corretiva e saída. | Inventário, avaliação, contrato, achados, monitoramento e evidência de remoção de acesso. |
| Resposta a incidentes | População completa conciliada com alertas, service desk, privacidade, jurídico e operações. | Testar declaração, triagem, análise, evidência, notificação, contenção, erradicação, recuperação e lições aprendidas. | Linha do tempo, chamados, registro de evidências, mensagens, recuperação e melhoria. |
| Desenvolvimento seguro | Todos os repositórios, versões, dependências, exceções e achados no escopo. | Testar requisitos, revisão, análise, segredos, dependências, aprovação, implantação, correção e novo teste. | Logs do pipeline, revisão, análise, chamado, versão e validação. |

## 15.2 Linguagem de conclusão

> **Exemplo:** Para o serviço e o período de revisão definidos, o controle foi adequadamente desenhado e operou conforme o esperado em 37 de 40 eventos da amostra. Três remoções de acesso ocorreram fora da tolerância aprovada. A direção definiu uma ação corretiva, adicionou escalonamento automatizado e o novo teste confirmou a remoção tempestiva na população completa subsequente. A conclusão não abrange sistemas excluídos do escopo declarado.
