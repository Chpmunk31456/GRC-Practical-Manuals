# Capítulo 100 Risco Operacional e Resiliência

**Estado legal: **Mestre inglês corrigido para consolidação. Este arquivo controla o conflito anterior Capítulo 100 linguagem de rascunho.

## Exigência

As organizações devem identificar e gerenciar riscos operacionais e de resiliência que possam causar um sistema de IA ou processo dependente a falhar, degradar, produzir resultados não confiáveis ou tornar-se indisponíveis. Os controles devem apoiar a continuidade, a recuperação segura e a preservação de evidências.

## Explicação em linguagem simples

Um sistema de IA pode falhar mesmo sem um ataque cibernético. Limites de capacidade, feeds de dados ruins, interrupções no modelo, deriva de configuração, latência, falhas de dependência ou controle de mudanças fracas podem interromper as operações ou produzir decisões prejudiciais. A resiliência requer alternativas testadas e prioridades claras de recuperação.

## Requisitos de avaliação

Avaliar no mínimo:

1. processos críticos, níveis de serviço e tolerâncias de impacto;
2. modelo, API, nuvem, dados, rede, identidade e dependências de fornecedores;
3. riscos de capacidade, latência, taxa de transferência, tempo limite e limite de taxa;
4. Falha de pipeline de dados, dados obsoletos, mudança de esquema e degradação da integridade;
5. configuração, versão, prompt e deriva de fonte de recuperação;
6. Monitorização da cobertura e dos limiares de alerta;
7. soluções alternativas manuais, canais alternativos e modos degradados seguros;
8. backup, restauração, reversão, failover e objetivos de recuperação;
9. prontidão do operador, comunicações e autoridade de decisão;
10. retenção, coordenação de incidentes e validação pós-recuperação.

## Exemplo GlobalWay

O serviço de assistência em viagens de IA da GlobalWay depende de um modelo de terceiros, APIs de reservas, serviços de identidade e dados de perfil do cliente. A GlobalWay define um modo seguro de somente leitura, bloqueia alterações de reservas automatizadas durante falhas de dependência, encaminha solicitações urgentes para agentes humanos e testa a recuperação antes de restaurar o serviço normal.

## Atividade de controlo

Os serviços de IA de material devem ter documentado os planos de continuidade e recuperação alinhados ao impacto nos negócios. Os planos devem incluir desligamento seguro, fallback, monitoramento de dependência, validação de recuperação e exercícios periódicos que cobrem cenários de falha realistas específicos da IA.

## Provas

- Avaliação do impacto nos negócios e da dependência;
- Definições de nível de serviço e tolerância ao impacto;
- Planos de continuidade, recuo e recuperação;
- resultados dos testes de backup, reversão e failover;
- Registos de monitorização e capacidade;
- relatórios de exercícios e ações corretivas;
- Comunicações de interrupção e aprovações de recuperação;
- evidência de validação pós-recuperação.

## Teste de auditoria

Confirme se as dependências críticas são conhecidas, os processos de fallback são utilizáveis, os objetivos de recuperação são testados, as versões restauradas e os dados são validados e as lacunas de resiliência não resolvidas são escaladas.

## Referências jurídicas primárias

- Regulamento (UE) n.o 2024/1689, conforme alterado: disposições aplicáveis em matéria de gestão de riscos, precisão, robustez, cibersegurança, supervisão humana, monitorização, incidentes e medidas corretivas.
- Resiliência operacional aplicável, segurança cibernética, segurança do produto e requisitos do setor.
- Textos oficiais consolidados atuais controlam resumos mais antigos.
