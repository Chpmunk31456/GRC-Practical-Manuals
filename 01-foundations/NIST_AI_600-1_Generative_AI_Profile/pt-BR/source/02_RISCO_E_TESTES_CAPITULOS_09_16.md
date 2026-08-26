# Manual 04 — Implementação do Perfil de IA Generativa NIST AI 600-1
## Fonte controlada em português brasileiro — Capítulos 09–16

> Tradução assistida por máquina para revisão controlada. Este material operacionaliza a linha de base do Manual 04 e não reproduz o texto do NIST. A aprovação semântica humana continua obrigatória antes da publicação.

## Capítulo 09 — Confabulação e confiabilidade das saídas

O risco de confabulação é gerenciado por avaliação específica do caso de uso, não por um único percentual de precisão. As equipes deveriam identificar quais afirmações precisam ser factuais, a taxa de erro aceitável, as consequências de falsa confiança e os controles usados quando o modelo não possui suporte confiável.

Controles úteis incluem recuperação fundamentada, exibição de fontes, geração restrita, comportamento de abstenção, validação humana, verificações determinísticas posteriores e restrições a ações autônomas de alta consequência. A evidência deveria incluir conjuntos de avaliação, limites de aceitação, falhas observadas, exemplos representativos, decisões de remediação e aprovação do risco residual.

## Capítulo 10 — Conteúdo nocivo, abusivo e perigoso

As organizações deveriam definir categorias de conteúdo proibido, restrito, dependente do contexto ou aceitável para o caso de uso. A política deve distinguir o tratamento de entradas do usuário do tratamento de saídas do modelo e tratar tentativas adversariais de contornar salvaguardas.

Os testes deveriam incluir uso esperado, uso indevido, condições de limite, manipulação de prompts, variação multilíngue quando relevante e comportamento de escalonamento. Um mecanismo de recusa que possa ser contornado trivialmente não deve ser tratado como controle efetivo.

## Capítulo 11 — Privacidade de dados e informações sensíveis

A revisão de privacidade deveria rastrear dados por prompts, armazenamentos de recuperação, logs, treinamento ou fine-tuning, APIs externas, plataformas de observabilidade, canais de suporte e histórico de conversas retido.

O conjunto mínimo de controles deveria abordar minimização, limitação de finalidade, acesso, retenção, exclusão, redação, tratamento de segredos, registro, processamento por terceiros e divulgação ao usuário quando aplicável. Os testes deveriam procurar memorização, vazamento de dados, sobre-exposição por recuperação, contaminação entre usuários e divulgação não autorizada por ferramentas ou conectores.

## Capítulo 12 — Viés prejudicial, homogeneização e impacto humano

A avaliação de viés deveria estar ligada às decisões, recomendações, classificações, conteúdos ou experiências produzidas pelo sistema. As equipes deveriam identificar populações ou partes interessadas que possam sofrer taxas de falha ou danos diferentes.

Controles podem incluir análise de dados, testes de resultados, avaliação por subgrupos, escalonamento humano, fluxos alternativos, monitoramento e restrições ao uso de conteúdo gerado em decisões consequenciais. Quando a medição for limitada por dados ou tamanho da amostra, essa incerteza deve ser documentada e não apresentada como evidência de equidade.

## Capítulo 13 — Configuração humano-IA e supervisão

A supervisão humana deve ser projetada, não presumida. A organização deveria determinar o que se espera que a pessoa perceba, que evidência está disponível, se há tempo e autoridade suficientes para intervir e como o viés de automação será reduzido.

Para usos consequenciais, defina decisões que o sistema pode tomar ou recomendar, decisões reservadas a humanos, gatilhos de escalonamento, autoridade de override, registro da revisão humana, requisitos de competência e procedimentos alternativos quando o sistema estiver indisponível ou não confiável.

## Capítulo 14 — Integridade da informação e proveniência

Controles de integridade deveriam ajudar usuários a distinguir informação gerada, recuperada, transformada e autoritativa. A proveniência deveria ser preservada quando afetar materialmente confiança, revisão, atribuição ou uso posterior.

A evidência pode incluir referências de fonte, metadados, artefatos assinados, histórico de transformações, identificadores de prompt/versão, registros de modelo e rastreabilidade da saída até material de suporte. Alegações de proveniência devem ser limitadas: metadados ou rótulos melhoram rastreabilidade, mas não provam por si só verdade ou autenticidade.

## Capítulo 15 — Segurança da informação e testes adversariais

Os testes de segurança de IA generativa deveriam cobrir toda a superfície de ataque: prompts, fontes de recuperação, bancos vetoriais, endpoints de modelo, plugins/ferramentas, identidades, segredos, APIs, interfaces, logs, camadas de orquestração e integrações com fornecedores.

Os testes deveriam incluir prompt injection direto e indireto, uso não autorizado de ferramentas, elevação de privilégios, extração de dados sensíveis, conteúdo malicioso de recuperação, divulgação do prompt do sistema, abuso de ações externas e cenários de negação ou degradação quando relevantes. Os achados devem ser vinculados a controles, responsáveis, remediação, evidência de reteste e decisões de risco residual.

## Capítulo 16 — Propriedade intelectual, cadeia de valor e integração de componentes

A organização deveria identificar componentes licenciados, proprietários, de terceiros, open source e hospedados externamente que influenciam o sistema. Quando relevante, termos do fornecedor, restrições de uso, direitos sobre saídas, termos de processamento de dados e dependências devem ser documentados.

A revisão da cadeia de valor deveria incluir fornecedores de modelos, hospedagem, conjuntos de dados, fontes de recuperação, plugins, APIs, serviços de segurança, monitoramento e subprocessadores. Um questionário de fornecedor isolado não constitui evidência suficiente para dependências de alto risco. Mudanças materiais de fornecedor ou componente devem acionar reavaliação quando puderem alterar capacidade, tratamento de dados, exposição contratual, segurança, disponibilidade ou comportamento das saídas.
