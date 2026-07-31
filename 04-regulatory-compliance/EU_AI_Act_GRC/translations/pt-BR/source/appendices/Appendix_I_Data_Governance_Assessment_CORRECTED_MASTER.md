# Apêndice I Avaliação da Governança de Dados

**Estado legal: **Mestre inglês corrigido. Este arquivo distingue as funções do Artigo 10 para provedores de sistemas de IA de alto risco de controles mais amplos de governança de dados organizacionais, privacidade, segurança, qualidade, propriedade intelectual e gerenciamento de registros.

## Finalidade

Use esta avaliação para avaliar se os dados usados para treinar, ajustar, validar, testar, recuperar, operar, monitorar ou melhorar um sistema de IA são adequados, legais, seguros, representativos, rastreáveis e regidos para o propósito pretendido documentado e a população afetada.

A avaliação deve ser vinculada à versão e repetida quando a fonte, população, finalidade, modelo, característica, rótulo, transformação, fornecedor, jurisdição ou condições legais mudarem.

## 1. Aplicabilidade e escopo

| Campo | Resposta |
|---|---|
| Sistema/modelo |  |
| ID do inventário |  |
| Versão/configuração |  |
| Pessoa jurídica e papel de ator |  |
| Classificação de alto risco e base legal |  |
| Dataset/nome da fonte e versão |  |
| Proprietário e administrador de dados |  |
| Finalidade prevista e utilização do ciclo de vida |  |
| Pessoas e populações afectadas |  |
| Competências |  |
| Aplica-se o artigo 10? |  |
| Avaliação relacionada DPIA/FRIA/segurança |  |
| Fonte legal atual e data de aplicação |  |
| Proprietário/data da avaliação |  |

## 2. Dataset e uso do ciclo de vida

Registre cada uso separadamente.

| Utilização dos dados | Dataset/versão | Finalidade | População/contexto | Proprietário | localização da evidência |
|---|---|---|---|---|---|
| Formação |  |  |  |  |  |
| Validação |  |  |  |  |  |
| Testes |  |  |  |  |  |
| Fine-afinação |  |  |  |  |  |
| Retrieval/grounding |  |  |  |  |  |
| Entrada operacional |  |  |  |  |  |
| Feedback/aprendizagem contínua |  |  |  |  |  |
| Monitorização |  |  |  |  |  |
| Dados sintéticos ou aumentados |  |  |  |  |  |

## 3. Finalidade e requisitos de dados

Documento:

- Uso pretendido e usos proibidos ou restritos;
- Estágio de ciclo de vida suportado;
- contribuição esperada para o comportamento e desempenho do sistema;
- Cobertura de população, geográfica, temporal, idioma, classe e eventos raros;
- ambiente operacional e contexto de decisão;
- populações afetadas e grupos vulneráveis;
- pressupostos sobre o que os dados medem ou representam;
- características exigidas de qualidade, quantidade, estatística e linhagem;
- limitações conhecidas e condições de uso aceitável.

## 4. Provenance, aquisição e direitos

| Pergunta | Resposta | Provas |
|---|---|---|
| A fonte é conhecida e documentada? |  |  |
| A coleta e aquisição são legais? |  |  |
| Licenças, permissões, contratos e direitos de propriedade intelectual são documentados? |  |  |
| A raspagem, reutilização, treinamento, ajuste fino, redistribuição e restrições a jusante são entendidas? |  |  |
| Os impactos dos dados, da comunidade, do cliente ou do fornecedor são compreendidos? |  |  |
| As representações dos fornecedores são verificadas independentemente onde proporcionalmente? |  |  |
| As lacunas de proveniência ou fontes não verificáveis são identificadas e escaladas? |  |  |

## 5. Artigo 10.o e critérios de governação

Avaliar, conforme aplicável:

- Opções de design relevantes;
- Processos de coleta de dados e origem;
- preparação, anotação, rotulagem, limpeza, enriquecimento e agregação;
- formulação de suposições sobre o que os dados medem e representam;
- avaliação prévia da disponibilidade, quantidade, adequação e características exigidas;
- exame de possíveis vieses que afetem a saúde, a segurança, os direitos fundamentais ou a discriminação proibida;
- Medidas para detectar, prevenir, reduzir e mitigar o viés;
- identificação de lacunas, deficiências e remediação;
- representatividade para a população e o contexto pretendidos;
- Propriedades estatísticas adequadas;
- configuração geográfica, contextual, comportamental, funcional, de idioma e acessibilidade;
- Versão, linhagem, integridade, segurança e reprodutibilidade.

## 6. Relevância e representatividade

Avaliar:

- relevância para o propósito pretendido;
- Cobertura de população e subgrupos;
- Cobertura geográfica e cultural;
- Moeda temporal;
- equilíbrio de classes e cobertura de eventos raros;
- representação interseccional;
- Diferenças entre treinamento, validação, teste e condições de produção;
- cobertura de falhas realistas, uso indevido e casos de borda;
- representatividade dos dados de feedback e monitoramento.

| Critério | Método | Resultado | Limitação | Acção |
|---|---|---|---|---|
| Cobertura da população |  |  |  |  |
| Cobertura geográfica/contextual |  |  |  |  |
| Moeda temporal |  |  |  |  |
| Classe/cobertura de eventos raros |  |  |  |  |
| Cobertura de subgrupo/interseccional |  |  |  |  |
| alinhamento da produção |  |  |  |  |

## 7. Avaliação da qualidade

| Dimensão da qualidade | Rating/result | Provas | Lim limiar | Remediação |
|---|---|---|---|---|
| Precisão |  |  |  |  |
| Completeness |  |  |  |  |
| Consistência |  |  |  |  |
| Timeliness |  |  |  |  |
| Validade |  |  |  |  |
| Unicidade/deduplicação |  |  |  |  |
| Qualidade do rótulo/anotação |  |  |  |  |
| Ruído e outliers |  |  |  |  |
| Desaparecimento |  |  |  |  |
| Integridade e corrupção |  |  |  |  |
| Reprodutibilidade |  |  |  |  |

## 8. Bias e risco de discriminação

Avaliar:

- viés histórico e estrutural;
- variáveis proxy e características correlacionadas;
- falta diferencial;
- viés de etiqueta e anotação;
- amostragem, seleção, sobrevivência e viés de medição;
- desempenho de subgrupos e interseccionais;
- linguagem, deficiência, idade e efeitos geográficos;
- ciclo de feedback e viés cumulativo;
- trade-offs de mitigação e consequências não intencionais;
- O monitoramento de dados pode detectar disparidades emergentes.

| Risco de viés | Grupo afectado | Método de detecção | Resultado | Mitigação | Limitação residual |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 9. Privacidade, sensibilidade e dados de categoria especial

Documento:

- Dados pessoais, de categoria especial, biométricos, infantis, confidenciais, proprietários ou regulamentados;
- Limitação e minimização de objetivos;
- Base de processamento legal;
- risco de desidentificação, pseudonimização e reidentificação;
- controles de acesso e segregação;
- Transferências internacionais e localização;
- retenção, exclusão, arquivamento e retenção legal;
- Restrições ao treinamento, uso secundário, melhoria do fornecedor ou divulgação posterior;
- Avisos de privacidade, manipulação de direitos e impactos sobre os dados.

Onde os dados pessoais da categoria especial são processados para monitoramento, detecção ou correção de viés, registre a base legal exata, necessidade estrita, limites de acesso, salvaguardas, pseudonimização, exclusão, documentação e privacidade / aprovação legal qualificada. Não trate o AI Act como uma permissão geral para processar dados confidenciais.

## 10. Preparação e transformação

Gravar:

- Limpeza e normalização;
- Engenharia de recursos e seleção;
- deduplicação;
- rotulagem e anotação;
- Aumento ou geração de dados sintéticos;
- filtragem, exclusões e tratamento atípico;
- Tratamento de dados em falta;
- limiares de qualidade e critérios de rejeição;
- código de transformação, aprovações e reprodutibilidade;
- controle de versão e reversão.

| Transformação | Método/ferramenta | Versão | Proprietário | Validação | Provas |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 11. Linhagem e rastreabilidade

| Elemento | Localização ou identificador |
|---|---|
| Fonte original |  |
| Registro de aquisição/licença |  |
| Registo de ingestão |  |
| pipeline transformação |  |
| Dataset version/checksum |  |
| Homologação |  |
| Treinamento/validação/teste |  |
| Sistema de produção/versão modelo |  |
| Local de retenção |  |
| Histórico de acessos |  |
| Registo de eliminação |  |

## 12. Segurança e integridade

Avaliar:

- autenticidade e integridade da fonte;
- alteração não autorizada, envenenamento, contaminação e vazamento;
- controle de acesso e segregação;
- encriptação e transferência segura;
- segurança do fornecedor e do gasoduto;
- backup, recuperação e disponibilidade;
- registro de auditoria e detecção de anomalias;
- Eliminação segura.

## 13. Decisão

- Aprovado para o uso documentado
- [ ] Aprovado com condições
- [ ] Uso limitado ou apenas piloto
- [ ] Remediação necessária antes do uso
- [ ] Proibido de uso
- [ ] Interpretação legal / de privacidade qualificada necessária

Motivo da decisão: **
** Limitações residuais:**
** Usos restritos ou proibidos: **
**Requisitos de monitorização: **

## 14. Plano de acção

| Acção | Proprietário | Data de vencimento | Estado | Método de validação | Evidência de encerramento |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 15. Acionadores da mudança e da reavaliação

Reavaliar após mudanças em:

- fonte, licença, fornecedor, subprocessador ou método de aquisição;
- propósito pretendido, população afetada, jurisdição ou setor;
- recurso, rótulo, anotação, transformação ou método de dados sintéticos;
- modelo, pronta, recuperação, feedback ou processo de aprendizagem contínua;
- qualidade, viés, desempenho, privacidade ou resultados de segurança;
- retenção, transferência, localização ou acesso a dados;
- base legal, consentimento, contrato, posição de autoridade ou lei aplicável.

## Exemplo de GlobalWay Travel Services

A GlobalWay avalia os dados de reserva, interrupção e perfil do viajante usados por um modelo de fraude. A avaliação encontra sub-representação de certos padrões de viagem regionais, rótulos inconsistentes e reutilização de fornecedores de dados do cliente para melhoria do modelo. A GlobalWay restringe o conjunto de dados, corrige rótulos, expande testes representativos, proíbe o treinamento do fornecedor sem autorização e vincula a versão aprovada do conjunto de dados ao modelo implantado e aos limiares de monitoramento.

## Homologação

| Papel | Nome | Decisão | Data |
|---|---|---|---|
| Proprietário/comandante de dados |  |  |  |
| Fornecedor/proprietário técnico |  |  |  |
| Privacidade/legal |  |  |  |
| Risco/conformidade |  |  |  |
| Segurança, quando aplicável |  |  |  |

**Referências de evidências:**
** Limitações residuais:**
**Condições/restrições:**
Próximo comentário trigger/date:**
**Versão de avaliação:**

## Referências jurídicas primárias

- Regulamento (UE) n.o 2024/1689, com as alterações que lhe foram introduzidas: Artigo 10.o e disposições aplicáveis em matéria de gestão de riscos, documentação técnica, exploração madeireira, monitorização, incidentes e de alto risco.
- Regulamento (UE) 2026/1744, se aplicável.
- Regulamento (UE) 2016/679 e propriedade intelectual aplicável, banco de dados, direitos autorais, confidencialidade, segurança cibernética, gerenciamento de registros, emprego, igualdade e direito do setor.
- Textos oficiais consolidados atuais controlam esse modelo.
