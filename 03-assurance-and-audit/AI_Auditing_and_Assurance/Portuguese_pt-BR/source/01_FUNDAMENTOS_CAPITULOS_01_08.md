# Manual 05 — Auditoria e Asseguração de IA
## Fonte localizada pt-BR — Capítulos 01–08

> Rascunho de localização para revisão semântica humana. Orientação original para implementação de auditoria. Este material utiliza a linha de base controlada de normas e a referência de prática profissional AAIA sem reproduzir conteúdo proprietário de normas, treinamento ou exames. Por si só, não constitui opinião de auditoria nem certificação.

## Capítulo 01 — Mandato e objetivo da auditoria

Toda auditoria de IA começa com um mandato documentado. O mandato identifica quem solicitou o trabalho, por que a auditoria está sendo realizada, qual decisão os resultados apoiarão, a autoridade da equipe de auditoria e quaisquer restrições de acesso ou reporte.

O objetivo da auditoria deve ser redigido como uma afirmação testável. “Revisar a governança de IA” é amplo demais; “determinar se os sistemas de IA em produção acima do limite de alto risco da organização possuem responsáveis aprovados, avaliações de risco atuais, evidências de liberação, monitoramento e aceitação documentada do risco residual” é auditável.

## Capítulo 02 — Critérios e limite de asseguração

Os critérios de auditoria devem ser identificados antes do trabalho de campo. Podem vir de leis, regulamentos, contratos, políticas internas, normas aprovadas, compromissos da administração, estruturas de controles ou requisitos operacionais definidos.

O registro de auditoria deve distinguir critérios obrigatórios de orientações e referências de prática profissional. A ISACA AAIA é utilizada aqui como referência de prática profissional para capacidade e cobertura dos domínios de auditoria; não é lei, regulamento, norma ISO, certificação organizacional nem opinião de auditoria.

## Capítulo 03 — Escopo e limite do sistema

O escopo deve identificar os sistemas de IA, processos de negócio, entidades jurídicas, locais, ambientes, período, fornecedores, conjuntos de dados, modelos, interfaces e etapas do ciclo de vida incluídos. Exclusões exigem justificativa.

Auditorias de IA devem decompor os sistemas em componentes relevantes: dados, modelo, prompts, recuperação, ferramentas, identidades, infraestrutura, monitoramento, revisão humana, fornecedores e processos de mudança. Um escopo limitado ao modelo pode deixar de identificar risco material na orquestração ou em ações subsequentes.

## Capítulo 04 — Independência, competência e conflitos

O líder da auditoria deve avaliar se a equipe possui independência e competência suficientes para o objetivo. Testes técnicos de alto impacto podem exigir especialistas em segurança, privacidade, ciência de dados, risco de modelos, assuntos jurídicos, acessibilidade, segurança operacional ou no domínio pertinente.

Conflitos devem ser divulgados quando auditores tenham projetado, implementado, aprovado ou operado materialmente o controle avaliado. Quando a independência organizacional plena não for possível, a limitação e a revisão compensatória devem ser documentadas.

## Capítulo 05 — Planejamento de auditoria e priorização de riscos

O planejamento deve priorizar áreas em que uma falha de controle possa causar dano material ou em que a qualidade da evidência seja incerta. As entradas podem incluir achados anteriores, incidentes, registros de riscos, obrigações regulatórias, criticidade do modelo, sensibilidade dos dados, autonomia, dependência de fornecedores e mudanças recentes.

O plano de auditoria deve indicar procedimentos, fontes de evidência, abordagem de amostragem, testes técnicos, entrevistas, auditores responsáveis, cronograma e entregáveis esperados.

## Capítulo 06 — Estratégia e suficiência da evidência

A evidência deve ser relevante ao critério de auditoria e confiável o suficiente para sustentar a conclusão. Políticas demonstram intenção de projeto; não comprovam operação. Capturas de tela mostram um ponto no tempo; podem não comprovar operação sustentada. Declarações de fornecedores podem apoiar uma conclusão, mas devem ser corroboradas quando o risco do fornecedor for material.

A evidência deve ser avaliada quanto à relevância, confiabilidade, completude, tempestividade, reprodutibilidade quando apropriado e independência em relação ao proprietário do controle.

## Capítulo 07 — Amostragem e definição da população

A amostragem começa pela definição da população. Exemplos incluem todos os sistemas de IA em produção, todos os casos de uso de alto risco, todas as liberações de modelos em um período, todos os fornecedores críticos ou todos os incidentes que atinjam um limite de severidade.

O método de amostragem deve refletir o objetivo da auditoria e o risco. A amostragem por julgamento pode direcionar itens de alto risco; técnicas estatísticas podem ser adequadas para populações homogêneas. As limitações da amostra e as partes não testadas da população devem ser divulgadas.

## Capítulo 08 — Ciclo de vida da auditoria e controles de qualidade fail-closed

O ciclo de vida controlado da auditoria é:
1. mandato e escopo;
2. critérios e plano de evidências;
3. trabalho de campo e testes;
4. achados e severidade;
5. resposta da administração;
6. validação da remediação;
7. encerramento e acompanhamento.

Os controles de qualidade falham de forma fechada quando a evidência requerida não está disponível, preocupações de independência permanecem sem solução, os testes estão incompletos, comentários do revisor permanecem abertos, mudanças materiais de escopo invalidam procedimentos ou falta uma aprovação humana obrigatória.

O QA automatizado do repositório apoia a consistência do pacote do manual; não substitui o julgamento do auditor nem a aprovação humana de publicação.