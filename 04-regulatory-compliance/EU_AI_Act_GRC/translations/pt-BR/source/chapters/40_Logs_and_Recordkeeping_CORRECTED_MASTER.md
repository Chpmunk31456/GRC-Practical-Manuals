# Capítulo 40 Registos e manutenção de registos

** Status legal: ** Corrigido o mestre inglês para consolidação. Este arquivo controla o conflito anterior Capítulo 40 linguagem de rascunho.

## Exigência

Os sistemas de IA de alto risco devem ser projetados para permitir o registro automático de eventos ao longo da vida útil do sistema, na medida apropriada para o propósito pretendido. Os provedores e implantadores devem manter registros e registros relacionados pelos períodos exigidos pelo Regulamento (UE) 2024/1689, conforme alterado, e outras leis aplicáveis.

## Explicação em linguagem simples

Os registros são a trilha de evidências operacionais de como um sistema de IA de alto risco se comportou. Eles suportam monitoramento, investigação de incidentes, supervisão humana, avaliação de conformidade, ação corretiva e revisão regulatória. O registro deve ser útil, proporcional, seguro e vinculado à versão correta do sistema.

A Lei AI não cria um período de retenção universal para cada registro. A retenção deve ser determinada pelo papel do ator, tipo de registro, artigo aplicável, lei do setor, requisitos de proteção de dados, obrigações contratuais, períodos de limitação e litígios ou retenções regulatórias.

## Requisitos de registo

O projeto de registro deve abordar, conforme aplicável:

1. sistema e versão do modelo;
2. Data e hora da operação;
3. Fonte de entrada e contexto de processamento relevante;
4. produção, pontuação, recomendação ou decisão;
5. Informações de confiança ou de limiar, se relevante;
6. revisão humana, intervenção, superação ou escalada;
7. erros, anomalias, falhas nos controles e eventos de segurança;
8. configuração, pronta, recuperação e mudanças de dependência;
9. identidade ou papel dos operadores autorizados quando legal e necessário;
10. ligações a reclamações, incidentes, ações corretivas e registros de monitoramento.

## Controles de proteção e segurança de dados

A organização deve definir propósito legal, minimização de dados, restrições de acesso, proteção de integridade, retenção, exclusão e procedimentos de exportação seguros.

## Exemplo GlobalWay

O sistema de recrutamento de alto risco da GlobalWay registra a versão do modelo de produção, o carimbo de data e hora do processo do candidato, o resultado de pontuação relevante, o limiar aplicado, a identidade do revisor, a decisão do revisor, a razão de substituição e qualquer erro do sistema. O acesso é restrito ao RH autorizado, conformidade, auditoria e pessoal de segurança.

## Atividade de controlo

O provedor deve definir as capacidades de registro durante o projeto, e o deployer deve garantir que os registros sejam habilitados, protegidos, revisados e retidos de acordo com um cronograma aprovado. Qualquer lacuna de registro que impeça o monitoramento, a supervisão, a investigação ou a resposta regulatória efetiva deve bloquear a implantação ou desencadear ações corretivas.

## Provas

- Especificação de registo;
- dicionário de dados;
- registros de eventos de amostra;
- configuração de controle de acesso;
- cronograma de retenção;
- Procedimentos de supressão e de retenção legal;
- Controles de integridade e evidências de adulteração;
- Monitorização e revisão de registos;
- ligações de incidentes e ações corretivas;
- Avaliação da privacidade.

## Teste de auditoria

Selecione uma amostra de eventos do sistema de alto risco e confirme que os logs são gerados, completos, vinculados à versão, protegidos contra alterações não autorizadas, acessíveis a revisores autorizados, retidos sob um cronograma aprovado e usados em monitoramento e investigação de incidentes.

## Referências jurídicas primárias

- Regulamento (UE) n.o 2024/1689, com a redação que lhe foi dada: Artigo 12.o e obrigações aplicáveis do ator em matéria de retenção e acesso a registos.
- GDPR e regras de retenção específicas do setor em que dados pessoais ou registros regulamentados estão envolvidos.
- O texto consolidado atual do EUR-Lex controla os resumos mais antigos.
