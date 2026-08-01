#!/usr/bin/env python3
"""Reconstruct ISO PT-BR sections 22-26 from approved structure.

This bounded repair restores flattened Markdown tables and damaged headings while
retaining practical, original Portuguese guidance. It does not reproduce normative
ISO text and fails closed unless all expected section boundaries are present.
"""
from pathlib import Path
import re

P = Path('02-management-systems/ISO_IEC_27001_27002/Portugues_BR/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md')
HEAD = re.compile(r'^#\s+(\d+)\.\s+.+$', re.M)

TOOLS = [
('CISO Assistant','https://intuitem.github.io/ciso-assistant-community/','SGSI, riscos, controles e evidências','Implante em laboratório isolado; configure escopo, riscos, tratamentos, proprietários e evidências.'),
('SimpleRisk Community','https://www.simplerisk.com/','Registro e tratamento de riscos','Defina critérios, registre riscos e proprietários, selecione tratamentos e acompanhe prazos.'),
('Wazuh','https://wazuh.com/','SIEM, monitoramento de endpoint e FIM','Instale gerente e agente em laboratório, gere evento autorizado e preserve configuração e alerta.'),
('osquery','https://www.osquery.io/','Inventário e consultas de endpoint','Execute consultas somente leitura em host de laboratório e documente cobertura e resultados.'),
('OpenSCAP','https://www.open-scap.org/','Avaliação de configuração Linux','Selecione perfil apropriado, examine sistema de laboratório, valide achados, corrija e repita.'),
('Greenbone Community Edition','https://greenbone.github.io/docs/latest/','Gestão de vulnerabilidades','Autorize alvos, atualize feeds, execute varredura autenticada, valide e reteste.'),
('Nmap','https://nmap.org/','Descoberta de ativos e serviços','Use apenas em faixas autorizadas; limite a varredura e compare com o inventário.'),
('Trivy','https://trivy.dev/','Código, imagem, dependência, segredo e configuração','Examine repositório ou imagem de teste, valide, corrija e reescaneie.'),
('OWASP ZAP','https://www.zaproxy.org/','Teste autorizado de aplicações web','Use aplicação de treinamento; mantenha varredura ativa sob aprovação escrita.'),
('Keycloak','https://www.keycloak.org/','Identidade, MFA, funções e logs','Crie ambiente de laboratório, usuários, grupos, menor privilégio e casos de entrada, mudança e saída.'),
('DefectDojo','https://www.defectdojo.org/','Ingestão e remediação de achados','Importe resultados seguros, deduplique, atribua responsáveis e encerre somente após reteste.'),
('AIDE','https://aide.github.io/','Monitoramento de integridade de arquivos','Crie linha de base, faça mudança autorizada, execute verificação e proteja a linha de base.'),
('Lynis','https://cisofy.com/lynis/','Auditoria de segurança Linux','Audite host de laboratório, avalie sugestões contra risco, corrija itens e execute novamente.'),
('Open Policy Agent','https://www.openpolicyagent.org/','Política como código','Escreva regra de laboratório, teste entradas permitidas e negadas e preserve resultados.'),
]

def tool_detail(i, row):
    name,url,purpose,start = row
    return f'''## 22.{i} {name}\n\n**Objetivo:** {purpose}. Projeto oficial: [{name}]({url})\n\n**Início rápido seguro:** {start}\n\n**Evidência:** escopo aprovado, configuração, versão, cobertura, resultados, revisão, exceção, remediação e reteste. Proteja credenciais, registros, relatórios e backups.\n'''

tool_rows='\n'.join(f'| {n} | {p} | {s} |' for n,_,p,s in TOOLS)
tool_details='\n'.join(tool_detail(i,r) for i,r in enumerate(TOOLS,1))

SECTIONS = {
22: f'''# 22. Ferramentas de Código Aberto\n\n*Links oficiais, inícios rápidos seguros, evidências e limitações.*\n\n| **Ferramenta** | **Finalidade** | **Possível apoio** |\n|---|---|---|\n{tool_rows}\n\n| **Limitação crítica:** Ferramentas apoiam controles e evidências; elas não selecionam tratamento de risco, determinam conformidade, substituem auditores competentes nem certificam uma organização. Valide cobertura, qualidade de dados, configuração, permissões, atualizações e revisão humana. |\n|---|\n\n{tool_details}''',
23: '''# 23. Manual do SGSI para Gestores\n\n*Perguntas, painel, propriedade e decisões que os gestores devem controlar.*\n\n- O escopo do SGSI continua alinhado à estratégia, aos serviços, locais, fornecedores, nuvem, pessoas e fluxos de dados?\n- O que mudou no contexto, nas partes interessadas, nas obrigações, ameaças, tecnologia ou relevância climática?\n- Os critérios de risco são confiáveis e os proprietários aprovam explicitamente tratamento e risco residual?\n- A Declaração de Aplicabilidade corresponde à implementação real dos controles e às ações abertas?\n- Objetivos e métricas geram decisões, em vez de painéis decorativos?\n- Incidentes, achados, exceções, ações vencidas e falhas recorrentes são escalonados?\n- Auditoria interna e análise crítica têm independência, competência, tempo e evidência suficientes?\n- Alegações de certificação, escopo, acreditação e declarações a clientes são exatas?\n\n| **Área** | **Pergunta de controle** | **Estado** |\n|---|---|---|\n| Contexto e escopo | Limites, dependências, partes e mudanças estão atuais? | Verde / Amarelo / Vermelho |\n| Risco | Critérios são consistentes e decisões dos proprietários são oportunas? | Verde / Amarelo / Vermelho |\n| SoA e controles | Seleção, estado e evidência estão alinhados? | Verde / Amarelo / Vermelho |\n| Desempenho | Objetivos, métricas, incidentes e tendências impulsionam ação? | Verde / Amarelo / Vermelho |\n| Fornecedores | Risco, responsabilidade, monitoramento, incidentes e saída são controlados? | Verde / Amarelo / Vermelho |\n| Auditoria | Auditorias são objetivas e achados são corrigidos com eficácia? | Verde / Amarelo / Vermelho |\n| Melhoria | Causas, recorrência e lições são tratadas? | Verde / Amarelo / Vermelho |\n| Certificação | Alegações são verificadas, atuais e sustentáveis? | Verde / Amarelo / Vermelho |\n''',
24: '''# 24. Guia de Carreira para Analista Júnior\n\n*Uma rota prática para trabalho com SGSI, GRC, risco, auditoria e conformidade.*\n\n![Aprenda o sistema, mapeie requisitos, teste evidências, comunique claramente e construa um portfólio honesto.](media/image9.png)\n\nFigura 9. Caminho do analista júnior de ISO 27001\n\nFunções iniciais comuns incluem analista júnior de GRC, analista de conformidade ISO 27001, analista de controles de segurança, coordenador de SGSI, analista de riscos, associado de auditoria interna, analista de risco de terceiros e analista de garantia de segurança.\n\n## 24.1 Trabalho júnior típico\n\n- Manter registros de escopo, ativos, obrigações, fornecedores, riscos, controles, SoA, evidências, achados e ações.\n- Coletar evidências sem alterar registros e validar sua integridade.\n- Mapear riscos e requisitos para controles, proprietários, procedimentos, sistemas e evidências.\n- Testar amostras de acesso, mudanças, vulnerabilidades, incidentes, backups, fornecedores, conscientização, controles físicos e continuidade.\n- Apoiar auditorias, análise crítica, métricas, ações corretivas e preparação para certificação.\n- Escrever conclusões factuais e divulgar limitações de amostragem, escopo e evidência.\n- Proteger informações confidenciais e permanecer dentro da autorização.\n\n## 24.2 Competências valorizadas\n\n| **Competência** | **Prova prática** |\n|---|---|\n| Conceitos de SGSI | Explicar cláusulas 4–10 e melhoria contínua |\n| Risco | Criar registro e plano de tratamento consistentes |\n| Declaração de Aplicabilidade | Justificar seleções, exclusões, estado e evidências |\n| Teste de evidência | Definir população, amostra, procedimento, exceção e reteste |\n| Alfabetização técnica | Interpretar identidade, nuvem, logs, vulnerabilidade, backup e configuração |\n| Comunicação | Escrever conclusões, ações e resumos gerenciais concisos |\n| Ética | Usar dados sintéticos, sistemas autorizados e alegações honestas |\n''',
25: '''# 25. Laboratório Fictício e Portfólio\n\n*Um ambiente de prática segura com dados sintéticos e sistemas de laboratório autorizados.*\n\n| **Regra do laboratório:** Use organização fictícia, dados sintéticos, sistemas isolados e apenas ferramentas que você está autorizado a operar. Não apresente um projeto de portfólio como certificação real ou auditoria de cliente. |\n|---|\n\nCrie uma organização fictícia com missão, serviços, locais, partes interessadas, ativos, fornecedores, obrigações e limites de SGSI claramente definidos. Registre hipóteses e mantenha todos os dados sem identificação real.\n\nConstrua um pacote mínimo de portfólio:\n\n1. declaração de escopo e diagrama simples de dependências;\n2. critérios de risco, registro de riscos e plano de tratamento;\n3. Declaração de Aplicabilidade vinculada a riscos e evidências;\n4. duas políticas e dois procedimentos controlados;\n5. inventário de ativos, identidades e fornecedores;\n6. plano de métricas e pequeno painel;\n7. papel de trabalho de teste de controle com população, amostra, evidência, exceção e reteste;\n8. relatório curto de auditoria interna;\n9. ata de análise crítica pela direção;\n10. registro de não conformidade, causa, correção, ação corretiva e verificação de eficácia.\n\nUse ferramentas somente para apoiar evidência. Preserve comandos, versões, configurações, capturas, resultados e limitações. Remova segredos e dados pessoais antes de publicar qualquer artefato.\n\nInclua uma nota de honestidade: o projeto demonstra método e capacidade de aprendizagem, não experiência de certificação, autoridade de auditoria nem conformidade de uma organização real.\n''',
26: '''# 26. Plano de Aprendizagem de Trinta Dias\n\n*Um cronograma focado para desenvolver capacidade útil de nível júnior.*\n\n| **Dias** | **Foco** | **Entrega** |\n|---|---|---|\n| 1–5 | SGSI, CIA, cláusulas, relação ISO 27001/27002 e escopo | Mapa do SGSI e declaração de escopo |\n| 6–10 | Critérios, cenários, avaliação, tratamento e aceitação de risco | Registro de riscos e plano de tratamento |\n| 11–14 | Temas do Anexo A e Declaração de Aplicabilidade | SoA preliminar vinculada a riscos |\n| 15–18 | Políticas, competência, comunicação, documentos e operação | Política e procedimento controlados |\n| 19–22 | Métricas, monitoramento, auditoria e análise crítica | Plano de métricas e programa de auditoria |\n| 23–25 | Não conformidade, causa raiz, ação corretiva e melhoria | Dois registros de achado e ação corretiva |\n| 26–28 | Laboratórios autorizados com ferramentas abertas | Dois memorandos de evidência e reteste |\n| 29–30 | Limpeza do portfólio e prática de entrevista | Pacote final e respostas ensaiadas |\n\nAo final de cada bloco, revise exatidão, rastreabilidade, confidencialidade, autorização e limitações. Corrija lacunas antes de adicionar complexidade.\n'''
}

text=P.read_text(encoding='utf-8')
for number in SECTIONS:
    if not re.search(rf'^#\s+{number}\.\s+', text, re.M):
        raise SystemExit(f'missing section {number}')
for number in sorted(SECTIONS, reverse=True):
    matches=list(HEAD.finditer(text))
    start=next(m for m in matches if int(m.group(1))==number)
    end=next((m.start() for m in matches if m.start()>start.start()),len(text))
    text=text[:start.start()]+SECTIONS[number].rstrip()+'\n\n'+text[end:]
for number in SECTIONS:
    matches=list(HEAD.finditer(text)); start=next(m for m in matches if int(m.group(1))==number)
    end=next((m.start() for m in matches if m.start()>start.start()),len(text)); chunk=text[start.start():end]
    if sum(1 for line in chunk.splitlines() if line.startswith('|'))<2:
        raise SystemExit(f'section {number} table validation failed')
P.write_text(text,encoding='utf-8')
print('Regenerated ISO PT-BR sections 22-26')
