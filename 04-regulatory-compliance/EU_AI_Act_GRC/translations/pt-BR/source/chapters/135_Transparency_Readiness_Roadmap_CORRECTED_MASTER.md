# Capítulo 135 Transparency Readiness Roteiro

**Estado legal: **Mestre inglês corrigido para consolidação. Este arquivo controla o conflito anterior Capítulo 135 linguagem de rascunho.

## Finalidade

Este capítulo fornece um roteiro prático para identificar, projetar, implementar, testar e manter obrigações de transparência para sistemas de IA e conteúdo gerado ou manipulado por IA.

A IA pode apoiar a tomada de decisões humanas, mas não deve remover a responsabilidade humana, julgamento ou responsabilidade.

## Exigência

As organizações devem identificar quais deveres de transparência se aplicam a cada sistema, ator, caso de uso, saída e contexto de implantação e, em seguida, implementar controles para que os avisos, divulgações, marcações e instruções exigidos sejam precisos, oportunos, acessíveis, compreensíveis, tecnicamente eficazes e consistentes com o comportamento real do sistema.

## Explicação em linguagem simples

Os deveres diferem por função e uso e podem incluir informar as pessoas de que estão interagindo com IA, fornecer informações e instruções para sistemas de alto risco, informar os trabalhadores ou pessoas afetadas quando necessário, marcar conteúdo gerado ou manipulado por IA, divulgar deepfakes ou determinado texto de interesse público e informar as pessoas expostas a sistemas de reconhecimento de emoções ou categorização biométrica.

## Fase 1: cenários de transparência de inventário

Identificar:

- sistemas que interagem diretamente com pessoas naturais;
- Sistemas de alto risco que requeiram instruções ou comunicações do deployer;
- Usos de reconhecimento de emoções ou de categorização biométrica;
- geração de áudio, imagem, vídeo e texto sintético;
- Cenários de deepfake e conteúdo manipulado;
- Texto de interesse público e cenários de responsabilidade editorial;
- empregado, candidato, viajante, cliente, fornecedor e interações públicas;
- canais, idiomas, jurisdições, características do público e necessidades de acessibilidade.

## Fase 2: determinar o gatilho legal e o ator responsável

Para cada caso de uso, documento:

1. a base jurídica ou política aplicável;
2. O fornecedor responsável, o despachante, o importador, o distribuidor, o fabricante do produto ou outro ator;
3. o destinatário pretendido ou o público afetado;
4. Quando as informações devem ser fornecidas;
5. conteúdo, formato e canal necessários;
6. exceções, exclusões e datas efetivas;
7. Requisitos de marcação técnica ou legível por máquina;
8. dependências de fornecedores e informações a jusante;
9. proprietário responsável, revisor legal e aprovador;
10. evidências necessárias, monitoramento e gatilhos de reavaliação.

## Fase 3: avisos de design, divulgações e instruções

As medidas de transparência devem ser:

- clara, concisa e factualmente precisa;
- distinguíveis de termos não relacionados e linguagem de marketing;
- apresentado cedo o suficiente para influenciar a compreensão ou a escolha da pessoa;
- adequado ao público e ao contexto operacional;
- acessível a pessoas com deficiência;
- disponíveis em línguas e canais relevantes;
- consistente entre interfaces, documentos e canais de suporte;
- alinhados com o propósito real, limitações, uso de dados, supervisão e rotas de reclamação;
- Apoiado por um contato humano significativo ou caminho de escalada, quando apropriado.

## Fase 4: implementar controles técnicos e de liberação

Implementar conforme aplicável:

- avisos de interação AI visíveis;
- Indicadores de divulgação persistentes ou facilmente acessíveis;
- marcação legível por máquina de conteúdo sintético quando legalmente exigido e tecnicamente viável;
- controles de metadados e proveniência;
- Etiquetas de conteúdo deepfake e manipulado;
- Comunicações entre pessoas afetadas e trabalhadores;
- opções de apoio humano e escalada;
- registro legal de apresentação de aviso e versão do sistema;
- portões de liberação que impedem a implantação sem controles de transparência aprovados.

## Fase 5: eficácia do teste

Teste:

- tempo, posicionamento e visibilidade;
- compreensão por audiências pretendidas;
- Acessibilidade e compatibilidade com tecnologia assistiva;
- qualidade da linguagem e precisão de localização;
- apresentação móvel, web, voz, documento e canal incorporado;
- Persistência de marcação técnica após processamento ou distribuição normais;
- capacidade do usuário de obter suporte humano ou desafio, quando aplicável;
- coerência entre o comportamento real do sistema e a divulgação aprovada;
- ligação entre avisos, marcações, instruções e a versão implantada.

## Fase 6: monitorar e manter

Reavaliar após:

- mudanças de modelo, interface, propósito ou fluxo de trabalho;
- novas funções de geração ou manipulação de conteúdo;
- expansão para novos países, populações ou idiomas;
- reclamações, defeitos de acessibilidade ou evidência de confusão do usuário;
- mudanças de fornecedor ou plataforma;
- alterações nos requisitos legais, atos de execução ou orientação autorizada;
- Reclassificação, modificação substancial ou novo uso de alto risco.

## Exemplo de GlobalWay Travel Services

O GlobalWay mapeia seu chatbot de viajante, ferramenta de recrutamento, conteúdo de marketing sintético e piloto de análise de emoções no centro de chamadas. O chatbot exibe um aviso de IA antes da primeira resposta e fornece uma rota visível para um consultor humano. Os avisos dos candidatos são revisados contra o fluxo de trabalho real de recrutamento. As imagens de destino geradas recebem os controles necessários de marcação e divulgação.

O teste de acessibilidade mostra que um aviso não é anunciado corretamente pelos leitores de tela. A liberação é pausada até que o defeito seja corrigido, retestado e vinculado à versão de produção aprovada. Um portão de mudança de fornecedor requer uma revisão renovada da transparência sempre que o modelo ou a interface subjacente mudar.

## Actividades de controlo

- Manter uma matriz de aplicabilidade de transparência e uma biblioteca de avisos.
- Distingue deveres específicos do ator e datas efetivas.
- Aprovar avisos, instruções e marcações técnicas antes do lançamento.
- Teste de tempo, compreensão, acessibilidade, localização e persistência técnica.
- Reconciliar divulgações com funções reais, limitações, uso de dados e supervisão.
- Manter a evidência do fornecedor e informações a jusante.
- Monitore reclamações, confusão e falhas de divulgação.
- Reavaliação do gatilho após mudança material.
- Preserve versões aprovadas, evidências de implementação e ações corretivas.

## Provas

- Matriz de aplicabilidade de transparência;
- Análise legal do papel e do caso de uso;
- Texto de aviso, divulgação e instrução aprovado;
- exemplos de interface de usuário, documento e conteúdo;
- Acessibilidade, compreensão e testes de linguagem;
- Marcação legível por máquina e resultados dos testes de proveniência;
- Fornecedor e documentação a jusante;
- registros de implantação, liberação e versão;
- resultados do teste de escalada humana;
- histórico de mudança e reavaliação;
- registros de reclamação, defeito e remediação.

## Testes de auditoria

1. Sistemas de IA selecionados e verificar a aplicabilidade da transparência foram avaliados usando o texto legal atual.
2. Confirmar o ator correto, destinatário, tempo, canal e data efetiva foram identificados.
3. Compare divulgações e instruções aprovadas com o comportamento e limitações reais do sistema.
4. Revisão de acessibilidade, linguagem, localização e testes de compreensão.
5. Teste a marcação de conteúdo sintético e a persistência da divulgação, quando aplicável.
6. Verifique se as funções de suporte humano ou de escalada operam como representadas.
7. Confirmar as mudanças de fornecedor e versão desencadear reavaliação e aprovação.
8. A verificação de orientações não vinculativas não é representada como um dever de transparência vinculativo.

## Métricas

- Sistemas que exijam medidas de transparência;
- avisos e instruções aprovados implementados;
- Acessibilidade, compreensão ou defeitos de linguagem;
- Falhas de divulgação ou marcação;
- Reclamações de usuários ou confusão documentada;
- sistemas alterados sem reavaliação da transparência;
- Remediação tardia;
- taxa de sucesso da escalada humana;
- mudanças do fornecedor aguardando revisão.

## Lista de verificação de gestão

- Todas as interações de IA aplicáveis e usos de conteúdo sintético foram identificados?
- O ator responsável e o gatilho legal são claros?
- Os avisos são oportunos, precisos, acessíveis, compreensíveis e localizados?
- As divulgações e instruções correspondem ao comportamento real do sistema?
- As marcações legíveis por máquina são implementadas e testadas quando necessário?
- Os usuários podem obter apoio humano significativo quando apropriado?
- Os controles de transparência são retestados após mudanças materiais?

## Especificação AI Transparency Readiness Journey

Crie uma jornada desde a identificação de casos de uso e análise de gatilhos legais até o mapeamento do ator, design de aviso e instrução, revisão de acessibilidade, marcação técnica, implementação, testes de produção, aprovação de liberação, feedback do usuário, revisão de mudanças e monitoramento contínuo.

**Alt text: **A jornada de prontidão de transparência da IA desde a identificação de interações e conteúdo relevantes através da análise do ator, avisos e instruções aprovados, marcações técnicas, testes de acessibilidade, implantação, feedback do usuário, revisão de mudanças e monitoramento contínuo.

## Referências jurídicas primárias

- Regulamento (UE) n.o 2024/1689, conforme alterado: direitos aplicáveis de transparência e informação, incluindo os artigos 13.o, 26.o e 50.o, juntamente com definições relevantes, exceções, datas efetivas e requisitos de documentação do anexo IV.
- Regulamento (UE) 2026/1744, se aplicável.
- Acessibilidade aplicável, proteção ao consumidor, emprego, privacidade, mídia e direito específico do setor.
- O texto consolidado atual do EUR-Lex controla os resumos mais antigos.
