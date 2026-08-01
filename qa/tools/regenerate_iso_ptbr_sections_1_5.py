#!/usr/bin/env python3
from pathlib import Path
import re

p = Path('02-management-systems/ISO_IEC_27001_27002/Portugues_BR/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md')
text = p.read_text(encoding='utf-8')

block = r'''# 1. Fundamentos da ISO/IEC 27001 e 27002

*Edições atuais, finalidade, relação e limitações importantes.*

![O contexto e o risco orientam o planejamento, a implementação, a avaliação e a melhoria.](media/image1.png)

Figura 1. Ciclo de melhoria contínua do SGSI

| **Documento** | **Função** | **Certificação** |
|---|---|---|
| ISO/IEC 27001:2022 | Requisitos normativos do SGSI, incluindo os controles de referência do Anexo A | Organizações podem obter certificação segundo essa norma |
| ISO/IEC 27001:2022/Amd 1:2024 | Alterações climáticas aplicáveis ao contexto e às partes interessadas | Aplicada em conjunto com a norma-base |
| ISO/IEC 27002:2022 | Orientação para implementação de controles de segurança da informação | Não é uma norma de certificação |
| ISO/IEC 27005:2022 | Orientação para gestão de riscos de segurança da informação | Orientação complementar, não a norma certificável ISO 27001 |

- As cláusulas 4–10 contêm requisitos que a organização deve tratar para demonstrar conformidade.

- O Anexo A apresenta 93 controles de referência em quatro temas: 37 organizacionais, 8 de pessoas, 14 físicos e 34 tecnológicos.

- A seleção de controles decorre do tratamento de riscos e das obrigações aplicáveis; o Anexo A não é uma lista universal em que todos os controles devam ser sempre implementados.

- A Declaração de Aplicabilidade registra os controles necessários, a justificativa, o estado de implementação e as exclusões justificadas do Anexo A.

# 2. Escopo do SGSI e partes interessadas

*Como definir um limite defensável para o sistema de gestão.*

- Identifique objetivos de negócio, produtos, serviços, processos, informações, entidades jurídicas, locais, pessoas, fornecedores, tecnologias e dependências.

- Compreenda questões internas relevantes, como estratégia, cultura, competências, arquitetura, governança e recursos.

- Compreenda questões externas relevantes, como ameaças, leis, contratos, mercados, fornecedores, condições físicas e mudanças tecnológicas.

- Determine as partes interessadas e seus requisitos relevantes, incluindo clientes, reguladores, trabalhadores, proprietários, fornecedores, comunidades e partes relacionadas à certificação.

- Considere se a mudança climática é relevante para a eficácia do SGSI e se as partes interessadas possuem requisitos relacionados ao clima; documente o raciocínio.

- Defina limites, interfaces, exclusões, dependências e justificativas do escopo em linguagem auditável.

- Mantenha o escopo alinhado aos inventários de ativos, processos, redes, nuvem, fornecedores e fluxos de dados.

| **Teste de escopo** | **Pergunta gerencial** | **Evidência** |
|---|---|---|
| Limite | Quais entidades, locais, serviços, processos e tecnologias estão incluídos? | Declaração de escopo aprovada e mapas |
| Interfaces | O que conecta o escopo a outras equipes, sistemas, fornecedores e locais? | Fluxos de dados, arquitetura, contratos e matriz de responsabilidades |
| Completude | Informações ou riscos importantes poderiam estar ocultos fora do limite declarado? | Inventários reconciliados e resultados de descoberta |
| Mudança | O que aciona uma revisão do escopo? | Registros de mudança, aquisições e marcos de produto |
| Relevância climática | Efeitos climáticos ou expectativas das partes interessadas podem afetar disponibilidade, fornecedores, instalações, pessoas ou obrigações? | Análise de contexto, decisão e ações quando pertinentes |

# 3. Avaliação e tratamento de riscos

*Um método repetível que conecta o risco de negócio às decisões de controle.*

![Os proprietários de risco avaliam cenários, tratamento e risco residual usando critérios definidos.](media/image2.png)

Figura 2. Fluxo de trabalho de risco de segurança da informação

Defina os critérios de risco antes da pontuação: método de identificação, escalas de probabilidade e consequência, regras de cálculo, limites de aceitação, tratamento exigido, escalonamento, frequência de revisão e autoridade do proprietário do risco. Aplique o método de forma suficientemente consistente para produzir resultados válidos e comparáveis.

| **Campo** | **Conteúdo de exemplo** |
|---|---|
| Ativo ou objetivo | Portal do cliente e disponibilidade exigida por contrato |
| Evento de ameaça | Roubo de credenciais seguido de acesso administrativo não autorizado |
| Vulnerabilidade ou condição | Cadastro fraco e ausência de MFA resistente a phishing |
| Consequências | Divulgação de dados, indisponibilidade, violação contratual e custo de resposta |
| Controles existentes | MFA, acesso condicional, registros e verificação de suporte |
| Risco inerente ou atual | Pontuação segundo critérios aprovados de probabilidade e consequência |
| Tratamento | Modificar o risco com autenticação mais forte e recuperação monitorada |
| Proprietário e data | Proprietário responsável e data-alvo definidos |
| Risco residual | Reavaliar após o tratamento e obter aprovação explícita do proprietário |

# 4. Declaração de Aplicabilidade

*A ponte entre o tratamento de riscos, o Anexo A, outros controles e a evidência de auditoria.*

![A Declaração de Aplicabilidade registra a seleção fundamentada de controles e o estado de implementação.](media/image3.png)

Figura 3. Fluxo de trabalho da Declaração de Aplicabilidade

- Liste os controles necessários para tratar os riscos identificados e atender a requisitos legais, regulatórios, contratuais e de negócio.

- Compare os controles selecionados com o Anexo A para assegurar que controles de referência necessários não tenham sido omitidos.

- Registre se cada controle do Anexo A é aplicável e justifique sua inclusão ou exclusão.

- Registre claramente o estado de implementação e mantenha-o coerente com o plano de tratamento e a evidência operacional.

- Inclua controles específicos da organização quando o Anexo A não tratar plenamente um risco.

- Controle a Declaração de Aplicabilidade como informação documentada e atualize-a após mudanças materiais de risco, escopo, requisitos legais, fornecedores, tecnologia ou controles.

| **Controle** | **Aplicável?** | **Justificativa** | **Estado** | **Proprietário / evidência** |
|---|---|---|---|---|
| Exemplo 8.15 — registros | Sim | Necessário para detecção, investigação e obrigações | Implementado com ações em aberto | Operações de Segurança / inventário de fontes e registros de revisão |
| Exemplo 7.9 — ativos fora das instalações | Sim | Pessoal remoto e em viagem utiliza dispositivos corporativos | Implementado | Operações de TI / inventário e comprovação de criptografia |
| Exemplo de controle organizacional | Sim | Risco específico de segurança de produto exige versões assinadas | Parcialmente implementado | Engenharia / registros do pipeline |
| Exemplo de exclusão | Não | A tecnologia ou o cenário descrito não existe no escopo controlado | Não aplicável | Evidência de escopo e arquitetura |

# 5. Documentação e evidência

*Como manter informação documentada útil sem criar burocracia.*

![A evidência deve sustentar o desenho, a operação, as exceções, a correção e o novo teste.](media/image4.png)

Figura 4. Cadeia de requisito para evidência

| **Documento ou registro** | **Finalidade** | **Verificações de controle** |
|---|---|---|
| Escopo do SGSI | Define limites e interfaces | Aprovado, atual e coerente com a realidade |
| Política | Estabelece direção e compromissos | Aprovada, comunicada e revisada |
| Método e registro de riscos | Demonstra avaliação e decisões repetíveis | Critérios aplicados de forma consistente; proprietários aprovam o risco residual |
| Plano de tratamento de riscos | Acompanha ações, proprietários, recursos e datas | Alinhado aos riscos e à Declaração de Aplicabilidade |
| Declaração de Aplicabilidade | Explica a seleção e o estado dos controles | Todos os controles do Anexo A tratados; justificativas sustentadas |
| Objetivos e métricas | Demonstra resultados planejados e avaliação | Mensuráveis, atribuídos, analisados e usados para ação |
| Registros de competência e conscientização | Sustentam capacidade e entendimento | Baseados em função, avaliados e atuais |
| Evidência operacional | Demonstra que os controles realmente operaram | Completa, autêntica, protegida e retida |
| Registros de auditoria e revisão | Sustentam supervisão e decisões | Objetivos, completos e acompanhados até a conclusão |
| Registros de ação corretiva | Demonstram causa raiz e correção eficaz | Causa tratada, recorrência considerada e eficácia verificada |

'''

new_text, count = re.subn(r'# 1\. Fundamentos da ISO/IEC 27001 e 27002\n.*?(?=# 6\. Cláusula 4)', block, text, flags=re.S)
if count != 1:
    raise SystemExit(f'Expected one sections 1-5 replacement; found {count}')
for marker in ('# 1. Fundamentos da ISO/IEC 27001 e 27002', '# 5. Documentação e evidência', '# 6. Cláusula 4'):
    if new_text.count(marker) != 1:
        raise SystemExit(f'Unexpected heading count for {marker!r}: {new_text.count(marker)}')
p.write_text(new_text, encoding='utf-8')
print('Regenerated ISO PT-BR sections 1-5')
