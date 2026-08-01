#!/usr/bin/env python3
from pathlib import Path
import re
P=Path('02-management-systems/ISO_IEC_27001_27002/Portugues_BR/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md')
text=P.read_text(encoding='utf-8')
HEAD=re.compile(r'^#\s+(\d+)\.\s+.+$',re.M)

def replace_section(src,n,new):
    ms=list(HEAD.finditer(src))
    start=next((m.start() for m in ms if int(m.group(1))==n),None)
    if start is None: raise SystemExit(f'missing section {n}')
    end=next((m.start() for m in ms if m.start()>start),len(src))
    return src[:start]+new.rstrip()+'\n\n'+src[end:]

s1='''# 1. Fundamentos da ISO/IEC 27001 e da ISO/IEC 27002

*Edições atuais, finalidade, relação entre as normas e limitações importantes.*

<img src="media/image1.png" style="width:6.15in;height:3.39605in" alt="O contexto e o risco orientam o planejamento, a implementação, a avaliação e a melhoria." />

Figura 1. Ciclo de melhoria contínua do SGSI

| **Documento** | **Função** | **Certificação** |
|---|---|---|
| ISO/IEC 27001:2022 | Requisitos normativos do SGSI, incluindo os controles de referência do Anexo A | As organizações podem obter certificação com base nessa norma |
| ISO/IEC 27001:2022/Amd 1:2024 | Alterações relacionadas à ação climática que afetam o contexto e a consideração das partes interessadas | Aplicada em conjunto com a norma-base |
| ISO/IEC 27002:2022 | Orientações para a implementação de controles de segurança da informação | Não é uma norma de certificação |
| ISO/IEC 27005:2022 | Orientações para a gestão de riscos de segurança da informação | Orientação de apoio; não é a norma de certificação ISO/IEC 27001 |

- As cláusulas 4 a 10 contêm requisitos que a organização deve atender para demonstrar conformidade.

- O Anexo A apresenta 93 controles de referência em quatro temas: 37 organizacionais, 8 de pessoas, 14 físicos e 34 tecnológicos.

- A seleção de controles decorre do tratamento de riscos e das obrigações aplicáveis; o Anexo A não é uma lista universal em que todos os controles devam ser sempre implementados.

- A Declaração de Aplicabilidade registra os controles necessários, a justificativa, o status de implementação e as exclusões justificadas do Anexo A.'''

s2='''# 2. Escopo do SGSI e partes interessadas

*Como definir um limite defensável para o sistema de gestão.*

- Identificar objetivos de negócio, produtos, serviços, processos, informações, entidades jurídicas, localidades, pessoas, fornecedores, tecnologias e dependências.

- Compreender questões internas relevantes, como estratégia, cultura, competências, arquitetura, governança e recursos.

- Compreender questões externas relevantes, como ameaças, leis, contratos, mercados, fornecedores, condições físicas e mudanças tecnológicas.

- Determinar as partes interessadas e os requisitos pertinentes, incluindo clientes, reguladores, trabalhadores, proprietários, fornecedores, comunidades e partes relacionadas à certificação.

- Considerar se a mudança climática é relevante para a eficácia do SGSI e se as partes interessadas possuem requisitos relacionados ao clima; documentar o raciocínio.

- Definir limites, interfaces, exclusões, dependências e justificativas do escopo em linguagem auditável.

- Manter o escopo alinhado aos inventários de ativos, processos, redes, nuvem, fornecedores e fluxos de dados.

| **Teste de escopo** | **Pergunta gerencial** | **Evidência** |
|---|---|---|
| Limite | Quais entidades jurídicas, unidades, serviços, processos e tecnologias estão incluídos? | Declaração de escopo aprovada e mapas |
| Interfaces | O que conecta o escopo a outras equipes, sistemas, fornecedores e localidades? | Fluxos de dados, arquitetura, contratos e matriz de responsabilidades |
| Completude | Informações ou riscos importantes podem estar ocultos fora do limite declarado? | Inventários reconciliados e atividades de descoberta |
| Mudança | O que aciona uma revisão do escopo? | Registros de mudança, aquisições e pontos de controle de produtos |
| Relevância climática | Efeitos climáticos ou expectativas das partes interessadas podem afetar disponibilidade, fornecedores, instalações, pessoas ou obrigações? | Análise de contexto, decisão e ações quando aplicável |'''

s3='''# 3. Avaliação e tratamento de riscos

*Um método repetível que conecta o risco de negócio às decisões sobre controles.*

<img src="media/image2.png" style="width:6.15in;height:3.39605in" alt="Os proprietários de riscos avaliam cenários, tratamento e risco residual usando critérios definidos." />

Figura 2. Fluxo de trabalho de riscos de segurança da informação

Defina os critérios de risco antes da pontuação: método de identificação, escalas de probabilidade e consequência, regras de cálculo, limites de aceitação, tratamento obrigatório, escalonamento, frequência de revisão e autoridade do proprietário do risco. Aplique o método com consistência suficiente para produzir resultados válidos e comparáveis.

| **Campo** | **Conteúdo de exemplo** |
|---|---|
| Ativo ou objetivo | Portal do cliente e disponibilidade exigida contratualmente |
| Evento de ameaça | Roubo de credenciais seguido de acesso administrativo não autorizado |
| Vulnerabilidade ou condição | Cadastro fraco e ausência de MFA resistente a phishing |
| Consequências | Divulgação de dados, indisponibilidade, violação contratual e custo de resposta |
| Controles existentes | MFA, acesso condicional, registros e verificação pelo suporte |
| Risco inerente ou atual | Pontuação conforme critérios aprovados de probabilidade e consequência |
| Tratamento | Modificar o risco por meio de autenticação mais forte e recuperação monitorada |
| Proprietário e data | Proprietário responsável pelo risco e data-alvo designados |
| Risco residual | Reavaliar após o tratamento e obter aprovação explícita do proprietário |'''

for n,s in ((1,s1),(2,s2),(3,s3)):
    text=replace_section(text,n,s)
for marker in ('# 1. Fundamentos da ISO/IEC 27001 e da ISO/IEC 27002','# 2. Escopo do SGSI e partes interessadas','# 3. Avaliação e tratamento de riscos'):
    if text.count(marker)!=1: raise SystemExit(f'heading validation failed: {marker}')
P.write_text(text,encoding='utf-8')
print('Regenerated ISO PT-BR sections 1-3')
