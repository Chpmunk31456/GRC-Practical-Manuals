# Capítulo 76 – Risco de Dependência de Nuvem, API e Modelo

** Status legal: ** Corrigido o mestre inglês para consolidação. Este arquivo controla o conflito anterior Capítulo 76 linguagem de rascunho.

## Exigência

As organizações devem identificar e gerenciar dependências de nuvem material, API, modelo, dados, componentes de software e subprocessadores que afetam seus sistemas de IA. A Lei de IA da UE não cria um programa autônomo de risco de dependência para todos os operadores, mas o provedor, implantador, importador, distribuidor, fabricante de produtos, gerenciamento de qualidade, gerenciamento de riscos, segurança cibernética, monitoramento, incidente, documentação e deveres de cooperação aplicáveis exigem visibilidade e controle suficientes sobre as dependências relevantes.

## Explicação em linguagem simples

Um serviço de IA pode depender de vários componentes externos, mesmo quando aparece para os usuários como um único sistema. Uma mudança de provedor, interrupção, substituição de modelo, depreciação de API, mudança de roteamento regional, subprocessador indocumentado ou perda de logs pode alterar a classificação legal, segurança, precisão, acessibilidade, privacidade, segurança, supervisão humana ou continuidade. Contratar um componente não remove as próprias obrigações legais da organização.

## Requisitos de dependência-governança

Para cada dependência material, documento e avaliação:

1. componente, fornecedor, subprocessador, finalidade, proprietário e criticidade;
2. modelo, API, software, dados e versões de configuração;
3. locais de processamento e suporte, fluxos de dados, retenção e acordos de transferência;
4. disponibilidade, níveis de serviço, capacidade de recuperação, cotas e limites de taxa;
5. processos de notificação de mudança, liberação, depreciação e mudança de emergência;
6. segurança, acesso privilegiado, segredos, separação de inquilinos e gestão de vulnerabilidades;
7. registro, monitoramento, acesso a evidências e capacidade de notificação de incidentes;
8. concentração, lock-in, substituição e risco de ponto único de falha;
9. Reajuste testado, modo de segurança, apenas para humanos ou acordos de suspensão controlada;
10. gatilhos para reavaliação, revalidação, revisão de transparência ou análise de modificação substancial.

## Exemplo GlobalWay

O serviço de assistência ao viajante da GlobalWay depende de um modelo hospedado, plataforma em nuvem, API de tradução, provedor de identidade, banco de dados de recuperação e serviço de monitoramento. Depois de uma atualização não anunciada do modelo reduz a precisão multilíngue e omite restrições de acessibilidade, a GlobalWay restringe as funções afetadas, encaminha casos para consultores treinados, preserva a versão e as evidências de saída, exige a investigação do provedor e revalida o serviço antes da restauração.

## Atividade de controlo

Dependências materiais devem ser registradas na documentação de inventário e arquitetura de IA. Dependências altas ou críticas devem ser monitoradas para mudança e interrupção, testadas antes das mudanças na produção material e apoiadas por arranjos de continuidade e escalada aprovados. Dependências críticas desconhecidas ou evidências obrigatórias indisponíveis são bloqueadores de liberação ou operação contínua.

## Provas

- inventário de dependência e arquitetura;
- registros de provedores e subprocessadores;
- Histórico de versão e configuração;
- Contratos, níveis de serviço e avisos de alteração;
- avaliações de localização e transferência de dados;
- revisões de segurança e acesso;
- Resultados de teste, regressão e revalidação;
- monitoramento, interrupção e registros de incidentes;
- Exercícios de fallback e continuidade;
- aceitação de riscos e decisões de responsabilidade do proprietário.

## Teste de auditoria

Confirme se as dependências materiais são completas e atuais; versões, regiões, subprocessadores e proprietários são conhecidos; mudanças materiais desencadearam revisão e testes apropriados; arranjos de continuidade foram exercidos; evidências permaneceram acessíveis; e riscos de dependência não resolvidos foram escalados para tomadores de decisão autorizados.

## Referências jurídicas primárias

- Regulamento (UE) n.o 2024/1689, com a redação que lhe foi dada: artigos 9.o-17.o, 20.o-26.o, 72.o-74.o, 78.o-82.o e anexos conexos, consoante o papel e a classificação do sistema.
- Regulamento (UE) 2016/679 e outros requisitos aplicáveis em matéria de privacidade, cibersegurança, segurança dos produtos, proteção do consumidor e requisitos do setor.
- As práticas de gestão de dependências neste capítulo são métodos de governança e garantia usados para apoiar os deveres legais aplicáveis; eles não são um catálogo de controle estatutário autônomo.
- Textos oficiais consolidados atuais controlam resumos mais antigos.
