# Apêndice de evidência e testes para praticantes — Manual 13

## A. Planilha controle-risco
Para cada controle tecnológico financeiramente relevante registre risco de reporte financeiro, processo/conta/divulgação, asserção ou objetivo afetado, sistema ou dado dependente, dono do controle, executor, frequência, fonte de evidência, local de retenção, dependências, caminho de exceção e gatilho de reavaliação. Um revisor deve conseguir entender por que o controle está no escopo de ICFR e como uma falha pode afetar o reporte financeiro.

## B. Padrão de evidência de acesso
Para acessos de usuário preserve solicitação, aprovação, função ou privilégio concedido, data de implementação, administrador, registro do sistema, revisão periódica e remediação. Para acesso privilegiado inclua justificativa, limites, monitoramento e recertificação. Para desligamentos demonstre a população fonte e a tempestividade da remoção; capturas isoladas não comprovam completude.

## C. Padrão de gestão de mudanças
Para mudanças financeiramente relevantes preserve solicitação aprovada, avaliação de impacto, descrição/requisitos, testes, segregação, aprovação de migração, registro de implantação e validação posterior. Mudanças emergenciais exigem justificativa documentada e revisão retrospectiva. Em SaaS e low-code, mudanças de configuração, fluxos, fórmulas, permissões e integrações podem ser tão relevantes quanto alterações de código.

## D. Padrão de operações de TI
Para processamentos agendados identifique população esperada, monitoramento, critérios de falha, notificação, autoridade para reinício/reprocessamento, reconciliações e evidência de resolução. Um status de scheduler bem-sucedido pode ser insuficiente quando a completude financeira depende de contagens, totais de controle ou reconciliações posteriores.

## E. Interfaces e reconciliações
Documente origem/destino, frequência, população, mecanismo de transferência, controles automatizados, tratamento de rejeições, duplicidades, reconciliação, limites e responsáveis. Quando a reconciliação for manual, defina a precisão do revisor e o escalonamento; se automatizada, documente configuração/código, entradas, tratamento de erros e monitoramento.

## F. IPE e relatórios
Quando um controle depende de relatório, consulta, extração ou painel, documente nome, sistema, dono, parâmetros, período, filtros, fonte de dados, lógica e acesso. Para consultas ad hoc preserve script/consulta exata. Para planilhas registre fontes, fórmulas/macros, versão, acesso, revisão e reconciliação. Uma captura de tela não substitui evidência reproduzível da população.

## G. Organizações de serviço
Para cada prestador que afete ICFR documente serviço, processos/sistemas, relatório ou evidência revisada, período, controles complementares da entidade usuária, subservice organizations, exceções, período-ponte, incidentes e conclusão da administração. Receber um relatório SOC não significa confiar automaticamente em todos os controles relevantes.

## H. Mínimos do papel de trabalho de testes
Inclua ID do controle, objetivo, risco, descrição, dono, frequência, fonte da população, período, método, fundamento da amostra quando aplicável, itens testados, evidência, exceções, conclusão, revisor, data e acompanhamento. Separe desenho de eficácia operacional e assegure que outro revisor competente possa reproduzir a lógica da conclusão.

## I. Deficiência e remediação
Registre condição factual, objetivo afetado, processo/sistema, duração, população potencial, controles compensatórios, causa raiz, contenção, ação corretiva, dono, prazo, evidência de encerramento e plano de reteste. Mantenha os fatos separados da classificação final como deficiência significativa ou fraqueza material.

## J. Reavaliação por mudanças
Reavalie escopo e desenho após implementação relevante, migração ERP, aquisição, nuvem, mudança de identidade, terceirização, redesenho financeiro, nova interface, incidente material, exceção recorrente ou introdução de IA/automação financeiramente relevante. Registre evento, escopo afetado, riscos, controles alterados, evidência e testes requeridos.

## K. Cenário — acesso privilegiado
Um administrador financeiro mantém privilégios após uma janela emergencial. Identifique sistemas/capacidades afetadas, revise atividade, corrija o acesso, avalie monitoramento, registre a exceção e determine se os testes precisam ser ampliados. A classificação final exige julgamento competente.

## L. Cenário — parâmetro incorreto de relatório
Uma reconciliação mensal usa filtro de data incorreto por dois períodos. Reproduza populações corretas, avalie erros potencialmente não detectados, identifique controles alternativos, corrija procedimento/configuração, reteste e avalie a deficiência com critérios vigentes e fatos específicos.

## M. Cenário — mudança de configuração SaaS
Um prestador altera um fluxo financeiro configurável. Determine impacto em aprovações, acesso, cálculos, interfaces ou evidência; obtenha informações disponíveis, compare configuração, teste o fluxo, atualize documentação e reavalie a dependência do prestador.

## N. Cenário — processo financeiro assistido por IA
Uma ferramenta de IA propõe classificações contábeis. Controle uso aprovado, proveniência de entradas, revisão de saídas, mudanças, acesso, fallback, monitoramento, exceções e evidência. Pontuações de confiança do modelo não comprovam exatidão financeira; defina como a revisão humana valida resultados e escala anomalias.

## O. Lista de evidência de publicação
O pacote final deve vincular identidade exata da fonte controlada, verificação de fontes autoritativas, fontes trilíngues, DOCX/PDF, QA de páginas, revisão de acessibilidade/visual, hashes, manifesto, segurança de workflows, reconciliação de mudanças e decisões de revisão aplicáveis ligadas ao candidato exato. A autorização final permanente já está estabelecida separadamente.
