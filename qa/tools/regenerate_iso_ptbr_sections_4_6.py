#!/usr/bin/env python3
from pathlib import Path
import re
P=Path('02-management-systems/ISO_IEC_27001_27002/Portugues_BR/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md')
text=P.read_text(encoding='utf-8')
HEAD=re.compile(r'^#\s+(\d+)\.\s+.+$',re.M)
def replace_section(src,n,new):
    ms=list(HEAD.finditer(src)); start=next((m.start() for m in ms if int(m.group(1))==n),None)
    if start is None: raise SystemExit(f'missing section {n}')
    end=next((m.start() for m in ms if m.start()>start),len(src))
    return src[:start]+new.rstrip()+'\n\n'+src[end:]

s4='''# 4. Declaração de Aplicabilidade

*A ponte entre o tratamento de riscos, o Anexo A, outros controles e as evidências de auditoria.*

<img src="media/image3.png" style="width:6.15in;height:3.39605in" alt="A Declaração de Aplicabilidade registra a seleção fundamentada de controles e o status de implementação." />

Figura 3. Fluxo de trabalho da Declaração de Aplicabilidade

- Listar os controles necessários para tratar os riscos de segurança da informação identificados e atender aos requisitos legais, regulatórios, contratuais e de negócio.

- Comparar os controles selecionados com o Anexo A para verificar se controles de referência necessários não foram ignorados.

- Registrar se cada controle do Anexo A é aplicável e justificar sua inclusão ou exclusão.

- Registrar claramente o status de implementação e mantê-lo coerente com o plano de tratamento de riscos e as evidências operacionais.

- Incluir controles específicos da organização quando o Anexo A não tratar completamente determinado risco.

- Controlar a Declaração de Aplicabilidade como informação documentada e atualizá-la após mudanças materiais em riscos, escopo, requisitos legais, fornecedores, tecnologia ou controles.

| **Controle** | **Aplicável?** | **Justificativa** | **Status** | **Responsável / evidência** |
|---|---|---|---|---|
| Exemplo 8.15 — registros de eventos | Sim | Necessário para detecção, investigação e obrigações aplicáveis | Implementado com ações em aberto | Operações de Segurança / inventário de fontes e registros de revisão |
| Exemplo 7.9 — ativos fora das instalações | Sim | Pessoas em trabalho remoto ou viagem utilizam dispositivos corporativos | Implementado | Operações de TI / inventário e evidência de criptografia |
| Exemplo de controle organizacional | Sim | Risco específico de segurança de produto exige versões assinadas | Parcialmente implementado | Engenharia / registros de pipeline |
| Exemplo de exclusão | Não | A tecnologia ou o cenário descrito não existe no escopo controlado | Não aplicável | Evidência de escopo e arquitetura |'''

s5='''# 5. Documentação e evidências

*Como manter informações documentadas úteis sem criar burocracia.*

<img src="media/image4.png" style="width:6.15in;height:3.29079in" alt="As evidências devem sustentar o desenho, a operação, as exceções, a correção e o reteste." />

Figura 4. Cadeia de requisitos até evidências

| **Documento ou registro** | **Finalidade** | **Verificações de controle** |
|---|---|---|
| Escopo do SGSI | Define limites e interfaces | Aprovado, atual e coerente com a realidade |
| Política | Estabelece direção e compromissos | Aprovada, comunicada e revisada |
| Método e registro de riscos | Demonstra avaliação e decisões repetíveis | Critérios aplicados de forma consistente; proprietários aprovam o risco residual |
| Plano de tratamento de riscos | Acompanha ações, responsáveis, recursos e datas | Alinhado aos riscos e à Declaração de Aplicabilidade |
| Declaração de Aplicabilidade | Explica a seleção e o status dos controles | Todos os controles do Anexo A tratados; justificativas sustentadas |
| Objetivos e métricas | Demonstra resultados planejados e avaliação | Mensuráveis, atribuídos, analisados e usados para ação |
| Registros de competência e conscientização | Sustentam capacidade e entendimento | Baseados em função, avaliados e atualizados |
| Evidência operacional | Demonstra que os controles realmente operaram | Completa, autêntica, protegida e retida |
| Registros de auditoria e revisão | Sustentam supervisão e decisões | Objetivos, completos e acompanhados até a conclusão |
| Registros de ação corretiva | Demonstram causa-raiz e correção eficaz | Causa tratada, recorrência considerada e eficácia verificada |'''

s6='''# 6. Cláusula 4 — Contexto da organização

*Requisitos em linguagem clara, foco de verificação e exemplos de evidências.*

| **Finalidade da cláusula:** Contexto da organização |
|---|

| **Cláusula** | **Significado em linguagem clara** | **Foco de verificação** | **Exemplo de evidência** |
|---|---|---|---|
| 4.1 | Compreender questões internas e externas que podem afetar o SGSI; considerar explicitamente se a mudança climática é relevante. | Confirmar responsabilidade, escopo, método, aprovação, evidência operacional, exceções, correção e registros retidos. | Políticas, registros, planos, atas, resultados, aprovações e evidências de acompanhamento. |
| 4.2 | Identificar as partes interessadas pertinentes, seus requisitos e se incluem expectativas relacionadas ao clima. | Confirmar responsabilidade, escopo, método, aprovação, evidência operacional, exceções, correção e registros retidos. | Políticas, registros, planos, atas, resultados, aprovações e evidências de acompanhamento. |
| 4.3 | Definir e manter o escopo do SGSI, incluindo limites, interfaces, dependências, localidades, tecnologia e exclusões. | Confirmar responsabilidade, escopo, método, aprovação, evidência operacional, exceções, correção e registros retidos. | Políticas, registros, planos, atas, resultados, aprovações e evidências de acompanhamento. |
| 4.4 | Estabelecer, operar, manter e melhorar continuamente o SGSI e seus processos obrigatórios. | Confirmar responsabilidade, escopo, método, aprovação, evidência operacional, exceções, correção e registros retidos. | Políticas, registros, planos, atas, resultados, aprovações e evidências de acompanhamento. |

Use o texto oficial licenciado da ISO/IEC 27001 para consultar os requisitos normativos exatos. Este manual apresenta paráfrases para fins educacionais e não substitui a norma.

| **Emenda de 2024:** Determinar explicitamente se a mudança climática é relevante para o contexto do SGSI e reconhecer que as partes interessadas pertinentes podem ter requisitos relacionados ao clima. Manter evidências do raciocínio e de qualquer ação resultante. |
|---|'''

for n,s in ((4,s4),(5,s5),(6,s6)):
    text=replace_section(text,n,s)
for marker in ('# 4. Declaração de Aplicabilidade','# 5. Documentação e evidências','# 6. Cláusula 4 — Contexto da organização'):
    if text.count(marker)!=1: raise SystemExit(f'heading validation failed: {marker}')
P.write_text(text,encoding='utf-8')
print('Regenerated ISO PT-BR sections 4-6')
