# Apêndice D Lista de verificação da prática proibida

**Estado legal: **Mestre inglês corrigido. Use o texto atual consolidado do artigo 5, o Regulamento (UE) 2026/1744, quando aplicável, e qualquer lei nacional aplicável. Cada **Sim** ou **Incerto** resposta requer revisão jurídica qualificada. Esta lista de verificação é uma ajuda operacional, não um substituto para o regulamento, texto oficial consolidado, interpretação da autoridade, direito nacional ou aconselhamento jurídico.

## Finalidade

Use esta lista de verificação antes da aprovação, aquisição, desenvolvimento, pilotagem, implantação, modificação material, reaproveitamento ou expansão geográfica para identificar práticas de IA que possam ser proibidas.

Não classifique um uso apenas a partir de um rótulo de tecnologia, descrição do fornecedor ou declaração de política. Teste todos os elementos legais relevantes, fato de implantação, exceção, salvaguarda, população afetada e rota razoavelmente previsível para evasão.

## Informações de avaliação

| Campo | Resposta |
|---|---|
| Sistema ou caso de uso |  |
| ID do inventário |  |
| proprietário do negócio |  |
| Proprietário técnico |  |
| Fornecedor/fornecedor |  |
| Papel ou papéis de ator |  |
| Entidades jurídicas |  |
| Competências |  |
| Propósito pretendido |  |
| Uso real e razoavelmente previsível |  |
| Pessoas afetadas e grupos vulneráveis |  |
| Versão, configuração, prompts, ferramentas e integrações |  |
| Contexto de implantação |  |
| Fonte legal oficial atual e data de aplicação |  |
| Assessor e Data |  |
| Repositório de evidências |  |

## Instruções

Para cada pergunta de triagem:

1. Resposta **Sim****, **Não****, ou **Incerto**;
2. Identificar o ponto exato do artigo 5.o e o elemento jurídico que está a ser testado;
3. Citar fatos e evidências;
4. registrar qualquer alegação de exceção, limitação, autorização e evidência de apoio;
5. identificar o revisor, a data, a decisão, a restrição e a ação de acompanhamento;
6. avaliar proxy, fluxo de trabalho, configuração e rotas de reaproveitamento previsíveis.

Uma resposta **Não** deve ser apoiada por fatos verificados. “Vendor diz que está em conformidade” não é evidência suficiente.

## A. Técnicas subliminares, propositadamente manipuladoras ou enganosas

| Pergunta | Sim/Não/Incerto | Evidência e racionalidade |
|---|---|---|
| O sistema usa técnicas subliminares além da consciência de uma pessoa, técnicas propositadamente manipuladoras ou técnicas enganosas? |  |  |
| A técnica tem o objetivo ou efeito de distorcer materialmente o comportamento? |  |  |
| Isso prejudica significativamente a capacidade de tomar uma decisão informada? |  |  |
| Isso poderia levar uma pessoa a tomar uma decisão que de outra forma não teria tomado? |  |  |
| O uso causa, ou é razoavelmente provável que cause, danos significativos? |  |  |
| A persuasão, a recomendação, a personalização, o design da interface e a manipulação enganosa foram distinguidos factualmente? |  |  |
| Os riscos de usuário vulnerável, acessibilidade, padrão escuro e design coercitivo foram testados? |  |  |

** Exemplos de evidências: ** registros de projeto, prompts, interfaces, testes comportamentais, análise de danos, pesquisa do usuário, revisão de acessibilidade, análise legal.

## B. Exploração de vulnerabilidades

| Pergunta | Sim/Não/Incerto | Evidência e racionalidade |
|---|---|---|
| O sistema explora a vulnerabilidade devido à idade, deficiência ou uma situação social ou econômica específica? |  |  |
| Qual recurso, mensagem, classificação, tempo, segmentação ou mecanismo de interação realiza a exploração? |  |  |
| O uso pode distorcer materialmente o comportamento? |  |  |
| O uso causa, ou é razoavelmente provável que cause, danos significativos? |  |  |
| A acessibilidade legítima, assistência, acomodação, proteção ou design adequado à idade foram distinguidos da exploração? |  |  |

** Exemplos de evidências: ** análise populacional, lógica de segmentação, regras de segmentação, revisão de acessibilidade, cenários de danos, salvaguardas, pesquisa de usuários.

## C. pontuação social

| Pergunta | Sim/Não/Incerto | Evidência e racionalidade |
|---|---|---|
| O sistema avalia ou classifica pessoas ou grupos naturais ao longo do tempo com base no comportamento social ou em características pessoais ou de personalidade conhecidas, inferidas ou previstas? |  |  |
| A pontuação leva a um tratamento prejudicial ou desfavorável? |  |  |
| O tratamento num contexto não está relacionado com o contexto em que os dados foram gerados ou recolhidos? |  |  |
| O tratamento é injustificado ou desproporcional ao comportamento social ou à sua gravidade? |  |  |
| A lealdade, a fraude, a segurança, a reputação, a elegibilidade ou as pontuações de risco são reutilizadas em todos os contextos? |  |  |
| As pessoas afetadas podem entender, desafiar e corrigir a pontuação ou os dados subjacentes? |  |  |

** Exemplos de evidências: ** inventário de recursos, lógica de pontuação, contexto de dados originais, mapa de uso a jusante, análise de proporcionalidade, testes de impacto adverso, registros de apelo.

## D. Previsão individual de risco de infração penal

| Pergunta | Sim/Não/Incerto | Evidência e racionalidade |
|---|---|---|
| O sistema é usado para avaliar ou prever o risco de uma pessoa natural cometer um crime? |  |  |
| A previsão baseia-se unicamente na definição de perfis ou avaliação de traços ou características de personalidade? |  |  |
| Se a IA apoia uma avaliação humana, essa avaliação já se baseia em fatos objetivos e verificáveis diretamente ligados à atividade criminosa? |  |  |
| A área, o grupo, o evento ou a análise operacional estão sendo usados como proxy para a previsão de risco criminal individual? |  |  |
| O papel da IA e da avaliação humana independente estão documentados nos registros de decisão? |  |  |

** Exemplos de evidências: ** características de entrada, propósito pretendido, registros de fatos objetivos, fluxo de trabalho humano, análise de perfil, registros de decisão.

## E. Rasting de imagem facial sem alvo

| Pergunta | Sim/Não/Incerto | Evidência e racionalidade |
|---|---|---|
| O sistema cria ou expande um banco de dados de reconhecimento facial? |  |  |
| As imagens faciais obtidas através de raspagem não direcionada da internet? |  |  |
| As imagens faciais obtidas através de raspagem não direcionada de imagens de televisão em circuito fechado? |  |  |
| O método de coleta, os critérios de segmentação, a escala, a fonte e a função do banco de dados são documentados? |  |  |
| A organização verificou independentemente as representações dos fornecedores sobre fontes de treinamento e imagem de referência? |  |  |

** Exemplos de evidências: ** registro de origem, método de aquisição, configuração do rastreador, evidência do fornecedor, testes técnicos, avaliação de dados biométricos.

## F. Reconhecimento de emoções nos locais de trabalho e instituições de ensino

| Pergunta | Sim/Não/Incerto | Evidência e racionalidade |
|---|---|---|
| O sistema infere emoções de pessoas naturais? |  |  |
| Está implantado em um local de trabalho? |  |  |
| Está implantado em uma instituição de ensino? |  |  |
| Uma exceção médica ou de segurança é reivindicada? |  |  |
| O propósito médico ou de segurança reivindicado é genuíno, necessário, proporcional, estreito e documentado? |  |  |
| Um sistema rotulado como sentimento, engajamento, fadiga, atenção, estresse ou análise comportamental poderia realizar inferência emocional na prática? |  |  |
| Se o uso não for proibido, as obrigações de alto risco, transparência, emprego, educação, privacidade, consulta e discriminação foram avaliadas? |  |  |

** Exemplos de evidências: ** descrição da capacidade, contexto de implantação, análise de exceção, avaliação de necessidade, consulta de trabalhador/estudante, controles de transparência.

## G. Categorização biométrica utilizando características protegidas ou sensíveis

| Pergunta | Sim/Não/Incerto | Evidência e racionalidade |
|---|---|---|
| O sistema categoriza as pessoas singulares individualmente com base em dados biométricos? |  |  |
| Deduz ou deduz uma característica protegida ou sensível listada no texto legal atual? |  |  |
| A verificação biométrica, a identificação e a categorização foram distinguidas? |  |  |
| Uma exceção é reivindicada para a rotulagem ou filtragem de conjuntos de dados biométricos legalmente adquiridos em um contexto de aplicação da lei aplicável? |  |  |
| O tratamento reivindicado é documentado de forma restrita, em vez de tratado como uma isenção geral? |  |  |
| Se não for proibido, a classificação de alto risco e as restrições de dados de categoria especial foram avaliadas? |  |  |

** Exemplos de evidências: ** fluxo de dados biométricos, lista de categorias inferidas, saídas, ações a jusante, análise de exceções, avaliação do GDPR, testes de justiça.

## H. Identificação biométrica remota em tempo real em espaços acessíveis ao público para aplicação da lei

| Pergunta | Sim/Não/Incerto | Evidência e racionalidade |
|---|---|---|
| O sistema realiza identificação biométrica remota? |  |  |
| A operação é em tempo real em vez de pós-evento? |  |  |
| É usado em um espaço acessível ao público? |  |  |
| É usado para fins de aplicação da lei? |  |  |
| Um dos objetivos estatutários estritamente permitidos é reivindicado? |  |  |
| A necessidade estrita é documentada? |  |  |
| A seriedade, a probabilidade e a escala de danos estão documentadas? |  |  |
| Os efeitos sobre os direitos e liberdades são avaliados? |  |  |
| Os limites temporais, geográficos e pessoais são definidos? |  |  |
| A autorização administrativa prévia ou independente está documentada, sujeita apenas à estrutura de emergência estreita? |  |  |
| O registro, a avaliação dos direitos fundamentais, as condições da legislação nacional, o registro e a revisão pós-uso estão completos? |  |  |

** Exemplos de evidências: ** conceito operacional, propósito, autorização, análise de necessidade e proporcionalidade, governança de lista de vigilância, testes de precisão, registros completos.

## I. Proibições adicionais introduzidas pelo Regulamento (UE) 2026/1744

** Controle de data de aplicação: ** Avalie a adoção e a aplicação separadamente. Use o texto alterado oficial e verifique a data **2 de dezembro de 2026** aplicável antes de confiar nesta lista de verificação.

| Pergunta | Sim/Não/Incerto | Evidência e racionalidade |
|---|---|---|
| O sistema gera conteúdo sexualmente explícito ou íntimo não consensual envolvendo uma pessoa identificável? |  |  |
| O sistema gera material de abuso sexual infantil dentro da redação estatutária alterada? |  |  |
| As duas categorias proibidas são analisadas separadamente? |  |  |
| O consentimento, a identidade, a idade, o material de origem, a finalidade de saída e o uso indevido previsível são documentados quando relevante? |  |  |
| O produto inclui controles técnicos, contratuais, de relatórios e de execução que impedem a geração proibida? |  |  |
| O uso é bloqueado em vez de apenas advertido quando a proibição legal é cumprida? |  |  |

**Exemplos de evidências:** controles de política de uso, testes de modelo e filtro, registros de consentimento quando relevante, controles de idade e identidade, registros de saída bloqueada, resposta a incidentes.

## J. Proxy, repurposing, e revisão de evasão

| Pergunta | Sim/Não/Incerto | Evidência e racionalidade |
|---|---|---|
| O projeto indiretamente alcança um resultado proibido por meio de proxies, recursos combinados, integração de fluxo de trabalho ou uso a jusante? |  |  |
| A configuração, ajuste fino, modelos rápidos, plugins, agentes ou instruções do usuário podem permitir uma prática proibida? |  |  |
| Poderia um piloto legal ser reaproveitado para um contexto de implantação proibido? |  |  |
| O fornecedor restringiu contratualmente usos proibidos e forneceu controles técnicos aplicáveis? |  |  |
| As tentativas de soluções alternativas são detectadas, registradas, investigadas e bloqueadas? |  |  |
| As restrições geográficas, de usuário, de dados ou de recursos podem ser tecnicamente aplicadas? |  |  |

## Evidências analisadas

- declaração para fins pretendidos;
- Avaliação de utilização real e razoavelmente previsível;
- documentação do sistema, modelo, prompt, ferramenta e agente;
- fontes de dados, linhagem e lista de recursos;
- interfaces de usuário, instruções, fluxos de trabalho e demonstrações;
- Documentação do fornecedor, direitos de teste, contratos e avisos de alteração;
- Testes independentes e comportamento observado;
- contexto de implantação e análise da população afetada;
- análise de direitos jurídicos e fundamentais;
- Exceções, autorizações, registros de necessidade e proporcionalidade;
- monitoramento, uso indevido, proxy, repurposing e controles de evasão.

## Decisão

- [ ] Nenhuma prática proibida identificada em fatos verificados
- [ ] Evidências adicionais necessárias
- [ ] Revisão legal qualificada necessária
- [ ] O uso deve ser redesenhado ou restrito
- [ ] Implantação proibida
- [ ] Implantação existente suspensa, retirada ou desativada

**Ponto de artigo e elementos exatos avaliados:**
Motivo da decisão: **
**Exceção, limitação ou autorização reivindicada:**
**Evidência de apoio:**
**Restrições ou redesenho obrigatório:**
**Incerteza residual:**

## gatilhos de escalada obrigatórios

Escalar e não aprovar quando:

- qualquer elemento estatutário não pode ser resolvido a partir de factos verificados;
- uma alegada exceção, limitação, autorização ou salvaguarda carece de provas;
- o fornecedor não divulgará funcionalidades relevantes, fontes de dados ou limitações observadas;
- descrições de marketing conflitam com a capacidade observada;
- crianças, trabalhadores, estudantes, migrantes, suspeitos de crimes ou outros grupos vulneráveis são afetados;
- A legislação nacional pode ser mais rigorosa ou impor condições separadas;
- O sistema pode ser reaproveitado para uma prática proibida;
- Restrições técnicas não podem bloquear de forma confiável o uso proibido;
- uma mudança material afeta o propósito, contexto, população, dados, geografia, capacidade, papel do ator ou uso da saída.

## Controlos obrigatórios

- Registre a base jurídica exata, as descobertas factuais e a fundamentação da decisão.
- Aplicar restrições técnicas, contratuais, organizacionais e de acesso.
- Bloqueie configurações proibidas, fluxos de trabalho, usuários, jurisdições e saídas.
- Impedir repurposing não autorizado e detectar tentativas de evasão.
- Treinar desenvolvedores, compras, usuários, aprovadores, suporte e pessoal de incidentes.
- Monitor para uso indevido, soluções alternativas, mudanças materiais e atualizações de fornecedores.
- Preservar rejeição, suspensão, retirada, descomissionamento, testes e evidências de incidentes.
- Reavaliar após alterações de propósito, dados, características, geografia, provedor, papel de ator, população afetada ou lei.

## Exemplo de GlobalWay Travel Services

A GlobalWay analisa uma ferramenta de “engajamento” de funcionários que afirma medir a fadiga e o sentimento de voz e vídeo. Testes mostram que ela infere estados emocionais em um contexto de local de trabalho. A GlobalWay suspende o piloto, preserva evidências de fornecedores e testes e aumenta para revisão legal qualificada. A garantia geral de conformidade do fornecedor é rejeitada como insuficiente porque a capacidade observada e os fatos de implantação controlam a análise.

## Homologação

| Papel | Nome | Decisão | Data |
|---|---|---|---|
| Revisor Jurídico Qualificado |  |  |  |
| Revisor de conformidade |  |  |  |
| Revisor técnico |  |  |  |
| proprietário do negócio |  |  |  |
| Revisor de privacidade/HR/Security, quando aplicável |  |  |  |

**Condições:**
**Ações e datas de vencimento:**
Próxima data de revisão ou gatilho: **
**Repositório de evidências:**
**Versão de avaliação:**

## Referências jurídicas primárias

- Regulamento (UE) n.o 2024/1689, com a redação que lhe foi dada: Artigo 5.o e todas as definições, exceções, salvaguardas, datas efetivas e condições de direito nacional aplicáveis.
- Regulamento (UE) 2026/1744, se aplicável.
- Regulamento (UE) 2016/679 e o emprego, a igualdade, a acessibilidade, o processo penal, a proteção do consumidor, a proteção da criança, a cibersegurança, a segurança dos produtos e o direito nacional aplicáveis.
- Os textos oficiais consolidados atuais controlam esta lista de verificação e todos os resumos anteriores.
