# NIST Cybersecurity Framework 2.0

## GRC prático, implementação, evidências e ferramentas de código aberto

*Manual de trabalho para gestores, analistas juniores, estudantes, profissionais em transição de carreira e equipes de cibersegurança*

**Alberto (Al) Leiva**

Primeira edição • Julho de 2026

| **Conteúdo:** Todos os 106 resultados do Núcleo do CSF • Perfis • Tiers • GRC • cadeia de suprimentos • evidências • teste de controles • ferramentas de código aberto • laboratórios • preparação profissional |
|---|

# Aviso de publicação e uso

Autor: Alberto (Al) Leiva

Edição: Primeira edição, julho de 2026

Objetivo: Oferecer educação gratuita e prática para gestores, analistas juniores, estudantes, profissionais em transição de carreira, profissionais de riscos e especialistas em cibersegurança.

## Aviso educacional

Este manual fornece informações educacionais gerais. Ele não constitui certificação, conformidade legal, opinião de auditoria nem garantia de segurança. Cada organização deve adaptar o NIST CSF à sua missão, aos seus riscos, às suas obrigações, ao seu apetite a risco, aos seus recursos, às suas tecnologias e às suas partes interessadas. Para decisões reais, utilize fontes oficiais atualizadas e orientação qualificada nas áreas jurídica, de riscos, privacidade, segurança física, auditoria e tecnologia.

## Uso ético e autorizado

Utilize ferramentas técnicas somente em sistemas, aplicações, redes, contas em nuvem e dados que sejam de sua propriedade ou para os quais você tenha autorização específica por escrito. Em atividades de treinamento, utilize dados fictícios, sintéticos ou aprovados. Capacidade técnica não constitui autorização.

# Prefácio

*Uma introdução acessível ao gerenciamento prático de riscos de cibersegurança.*

O trabalho de cibersegurança pode parecer uma coleção de produtos, alertas, políticas e tarefas técnicas. O NIST Cybersecurity Framework oferece uma linguagem comum para conectar essas atividades. Ele ajuda líderes a explicar quais resultados são importantes, gestores a definir prioridades e profissionais a relacionar o trabalho diário ao risco organizacional.

O CSF 2.0 é deliberadamente flexível. Ele não exige que todas as organizações comprem a mesma ferramenta, implementem o mesmo controle ou alcancem o mesmo Tier. Ele descreve resultados. Um hospital, uma indústria, uma escola, um banco, uma startup, um órgão governamental ou uma organização sem fins lucrativos podem utilizar o mesmo Núcleo e, ao mesmo tempo, escolher prioridades e implementações diferentes.

Este manual adota uma abordagem que começa pela metodologia. Uma planilha de framework só é útil quando o escopo é preciso. Um painel verde só é útil quando as evidências são confiáveis. O resultado de um scanner só é útil quando alguém o valida, prioriza, corrige e testa novamente. Os gestores continuam responsáveis pelas decisões; os analistas melhoram essas decisões ao reunir fatos completos e comunicá-los com clareza.

# Como utilizar este manual

Os gestores devem começar pelos capítulos 1–3 e 10–17, além dos modelos do capítulo 22.

Os analistas juniores devem estudar os seis capítulos dedicados às Funções, o método de verificação, as ferramentas, o laboratório e a preparação para entrevistas.

As equipes técnicas devem relacionar os achados a ativos, riscos, resultados do CSF, implementação, responsáveis, evidências e ações corretivas.

As equipes jurídica, de privacidade, segurança física, tecnologia operacional e negócios devem revisar as decisões que afetem suas responsabilidades.

| **Sumário real do Word:** O guia de capítulos inclui números de página específicos da edição após a renderização final. O documento também contém um campo nativo de sumário do Word. Depois de editar, clique com o botão direito no campo, selecione **Atualizar Campo** e depois **Atualizar o índice inteiro**. |
|---|

# 1. Fundamentos do NIST CSF 2.0

*O que é o framework, o que mudou e o que ele não afirma.*

<img src="media/image1.png" style="width:6.15in;height:3.39605in" alt="GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND e RECOVER funcionam como um sistema conectado." />

Figura 1. As seis Funções do NIST CSF 2.0

## 1.1 O que é o CSF 2.0

O NIST publicou o CSF 2.0 em 26 de fevereiro de 2024. Ele foi desenvolvido para organizações de qualquer porte, setor e nível de sofisticação técnica. Seus resultados são neutros em relação a país, setor e tecnologia. Uma organização pode adotá-lo voluntariamente ou porque uma política, um contrato, um regulador, um cliente ou uma norma interna assim o exige.

## 1.2 O que mudou em relação ao CSF 1.1

- **GOVERN** tornou-se a sexta Função, colocando liderança, política, risco empresarial e prestação de contas no centro do framework.
- A cibersegurança da cadeia de suprimentos recebeu maior ênfase.
- A linguagem foi ampliada para além da infraestrutura crítica, permitindo que o framework atenda claramente a todos os tipos de organização.
- Perfis, Tiers, Exemplos de Implementação, Referências Informativas e Guias de Início Rápido formam agora um portfólio mais amplo de recursos do CSF.
- Algumas numerações de Subcategorias contêm lacunas intencionais porque determinados conteúdos do CSF 1.1 foram realocados dentro do CSF 2.0.

## 1.3 O que o CSF 2.0 não é

- Não é, por si só, uma lei.
- Não é um catálogo único de controles nem uma lista obrigatória de tecnologias.
- Não fornece uma pontuação universal de aprovação ou reprovação.
- O NIST não certifica organizações, produtos, consultores nem avaliadores em relação ao CSF.
- Um Tier elevado não é automaticamente o objetivo correto para todos os escopos.
- Relacionar uma prática a um resultado do CSF não comprova que esse resultado tenha sido alcançado.

# 2. Núcleo, Perfis, Tiers e recursos de apoio

*Os componentes do CSF 2.0 e como eles se relacionam.*

<img src="media/image2.png" style="width:6.15in;height:2.6593in" alt="As Funções contêm Categorias, e as Categorias contêm Subcategorias específicas orientadas a resultados." />

Figura 2. Hierarquia do Núcleo do CSF

| **Componente** | **Objetivo** | **Uso prático** |
|---|---|---|
| Núcleo | Hierarquia de seis Funções, 22 Categorias e 106 Subcategorias | Descrever os resultados de cibersegurança desejados |
| Perfil Organizacional | Resultados atuais e/ou alvo para um escopo definido | Comparar a postura, priorizar lacunas e planejar o trabalho |
| Perfil da Comunidade | Linha de base compartilhada de resultados para um setor, tecnologia, ameaça ou caso de uso | Utilizá-la como insumo para o Perfil-Alvo de uma organização |
| Tiers | Contexto sobre o rigor das práticas de governança e gerenciamento de riscos | Caracterizar as condições do Perfil Atual e do Perfil-Alvo |
| Exemplos de Implementação | Ações orientativas que podem ajudar a alcançar resultados | Gerar ideias, adaptá-las e validá-las |
| Referências Informativas | Correspondências com normas, orientações, regulamentos e outras fontes | Selecionar práticas e controles mais detalhados |
| Guias de Início Rápido | Orientações breves e práticas sobre usos específicos do CSF | Iniciar trabalhos sobre Perfis, Tiers, ERM, cadeia de suprimentos e pequenas empresas |

| **Números importantes:** O CSF 2.0 contém 6 Funções, 22 Categorias e 106 Subcategorias. As Subcategorias descrevem resultados; elas não exigem produtos específicos nem implementações idênticas. |
|---|

# 3. Roteiro prático de implementação

*Uma forma repetível de passar da linguagem do framework para melhorias financiadas.*

- Designe um patrocinador executivo e um responsável pelo programa.
- Defina o escopo do Perfil: empresa, unidade de negócios, produto, serviço, sistema, região ou ecossistema de fornecedores.
- Reúna informações sobre a missão, as partes interessadas, as obrigações jurídicas e contratuais, os riscos, ativos, ameaças, incidentes, auditorias, força de trabalho e fornecedores.
- Selecione os resultados do CSF aplicáveis e crie um Perfil Atual utilizando evidências confiáveis.
- Defina um Perfil-Alvo baseado em risco, considerando os Perfis da Comunidade e as obrigações aplicáveis.
- Analise lacunas, dependências, custos, viabilidade e redução de risco.
- Crie um plano de ação aprovado com responsáveis, recursos, marcos, métricas e medidas de proteção provisórias.
- Implemente controles e procedimentos operacionais.
- Teste a eficácia do desenho e a eficácia operacional utilizando populações completas e amostras representativas.
- Relate riscos, decisões, exceções, progresso e limitações.
- Atualize os Perfis após mudanças relevantes, incidentes, exercícios, revisões ou alterações no risco.

| **Comece com um escopo pequeno sem perder a integridade:** Uma organização pequena pode começar por um serviço crítico ou processo de alto risco. Mantenha o escopo transparente, documente as exclusões e amplie-o de forma deliberada. |
|---|

---

**Status editorial:** Este bloco substitui o conteúdo defeituoso equivalente e foi revisado quanto à terminologia, ao significado, à estrutura Markdown e ao uso brasileiro. Ele deve ser integrado ao arquivo completo antes da regeneração dos arquivos DOCX/PDF.