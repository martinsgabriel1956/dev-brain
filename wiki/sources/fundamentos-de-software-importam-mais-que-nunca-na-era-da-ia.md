---
type: source
title: "Fundamentos de Software Importam Mais que Nunca na Era da IA"
aliases: ["software fundamentals matter more than ever", "code is not cheap", "palestra matt pocock ia"]
date_created: 2026-07-09
date_updated: 2026-07-10
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia.md
source_url: ""
author: "Matt Pocock (AI Hero)"
date_published: ""
date_ingested: 2026-07-09
source_count: 0
tags: [spec-driven-development, tdd, ddd, ubiquitous-language, deep-modules, philosophy-of-software-design, feedback-loop, prd, arquitetura, complexidade]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Palestra de Matt Pocock (aihero.dev) argumentando que **código não é barato** — código ruim é o mais caro que já foi, porque uma base de código difícil de mudar impede a equipe de aproveitar o ganho que a IA oferece. A tese central: o movimento "specs to code" (editar só a especificação, nunca olhar o código, rodar o "compilador" de novo) degenera em vibe coding disfarçado — cada rodada produz código pior, um paralelo direto à entropia de software do Pragmatic Programmer. A solução não é abandonar fundamentos de engenharia por causa da IA — é dobrar a aposta neles: conceito de design compartilhado (Fred Brooks), linguagem ubíqua (DDD), TDD como forspringer de passos pequenos, e módulos profundos (Ousterhout) como pré-condição para todo o resto funcionar.

## Key Claims

**Claim:** O movimento "specs to code" degrada a qualidade do código a cada iteração, porque ignorar o código e só editar a especificação equivale a nunca investir no design do sistema.
**Evidence:** O autor relata ter testado o fluxo repetidamente: rodava, o código saía ruim, rodava de novo sobre o mesmo código ruim, e o resultado piorava a cada ciclo — "vibe coding por outro nome". Conecta isso à ideia de entropia de software do Pragmatic Programmer: mudanças feitas pensando só na mudança local (nunca no design do sistema como um todo) degradam a base de código progressivamente. Ver [[wiki/concepts/spec-driven-development]] e [[wiki/concepts/vibe-coding]].
**Confidence:** média — é relato de experiência pessoal do autor, não um estudo controlado, mas alinhado com o consenso já registrado na wiki sobre riscos do L2/vibe coding sem harness de qualidade.

**Claim:** "Código é barato" é uma crença falsa na era da IA — código ruim é o mais caro que já foi, porque impede a equipe de colher o ganho que a IA oferece em bases de código boas.
**Evidence:** Citando John Ousterhout (*A Philosophy of Software Design*): complexidade é "qualquer coisa relacionada à estrutura de um sistema que dificulta entender e modificar o sistema" — logo, base de código ruim é a que é difícil de mudar. A IA amplifica esse efeito: em uma boa base de código, a IA rende muito; em uma base ruim, cada rodada de geração piora a situação.
**Confidence:** alta — argumento coerente e consistente com [[wiki/concepts/complexidade-acidental]] já documentado na wiki.

**Claim:** IA e humano raramente compartilham um "conceito de design" (design concept, termo de Frederick P. Brooks em *The Design of Design*) — a solução é forçar uma fase de entrevista adversarial antes de qualquer plano ou PRD.
**Evidence:** O autor criou uma skill chamada "grill me": instrui a IA a entrevistar o usuário implacavelmente, percorrendo cada ramo da árvore de decisões de design até alcançar entendimento compartilhado — o repositório dessa skill teria ~13 mil estrelas no GitHub. O autor argumenta que isso é superior ao plan mode padrão do Claude Code, que segundo ele "está ansioso demais para criar um artefato" em vez de garantir alinhamento primeiro. Ver [[wiki/entities/fred-brooks]] e [[wiki/concepts/prd-product-requirements-document]].
**Confidence:** média — a existência e popularidade da skill não foi verificada de forma independente pela wiki; a comparação com o plan mode do Claude Code é opinião do autor, não um dado.

**Claim:** A verbosidade e desalinhamento entre dev e IA se resolvem com uma "linguagem ubíqua" (ubiquitous language, DDD) extraída automaticamente da base de código.
**Evidence:** O autor descreve uma skill que varre a codebase, extrai terminologia de domínio e gera um arquivo markdown com tabelas de termos, mantido aberto durante o planejamento. Segundo o relato, isso reduziu a verbosidade dos "thinking traces" da IA e aumentou o alinhamento entre plano e implementação. É a aplicação direta do pilar Ubiquitous Language do DDD (já documentado em [[wiki/concepts/ddd]]) ao contexto de desenvolvimento assistido por IA.
**Confidence:** média — efeito relatado subjetivamente ("unbelievably good"), sem métrica objetiva de verbosidade ou alinhamento.

**Claim:** LLMs "ultrapassam o alcance dos próprios faróis" (outrunning your headlights, termo do Pragmatic Programmer) — produzem lotes grandes de código antes de rodar qualquer feedback loop, o que TDD corrige forçando passos pequenos.
**Evidence:** Mesmo com type-checking, acesso ao browser e testes automatizados disponíveis como feedback loops, a LLM por padrão gera muito código de uma vez e só depois verifica type-check ou testes — o oposto do ciclo RED-GREEN-REFACTOR do TDD, que já força passos pequenos e deliberados. Consistente com o que a wiki já documenta em [[wiki/concepts/tdd]] sobre "gaming de testes por IA" e a necessidade de harness de qualidade.
**Confidence:** alta — bate com o padrão de falha já registrado em outras fontes da wiki sobre comportamento de agentes de IA sem guard rails.

**Claim:** Testabilidade de uma base de código depende de módulos profundos (deep modules) — poucos módulos grandes com interface simples escondendo complexidade — não de muitos módulos rasos (shallow modules) com interfaces complexas e funcionalidade mínima.
**Evidence:** Conceito de Ousterhout (*A Philosophy of Software Design*): módulos profundos permitem tratar o interior como "caixa cinza" — você projeta e revisa a interface, mas pode delegar a implementação à IA. Módulos rasos são o padrão que a IA tende a produzir por padrão, e são precisamente o que a torna incapaz de localizar e entender dependências ao explorar a base de código. O autor descreve uma skill de refatoração ("improve codebase architecture") para migrar de um padrão para o outro.
**Confidence:** alta — este é o argumento central e mais bem fundamentado da palestra, apoiado numa fonte primária citada (Ousterhout).

**Claim:** "Design the interface, delegate the implementation" só é seguro quando a interface do módulo é bem verificada por fora (testável) e o módulo não é crítico (ex: não é lógica financeira) — cita Kent Beck: "invista no design do sistema todos os dias".
**Evidence:** O autor relata que tratar módulos profundos como caixa cinza (sem revisar a implementação linha a linha) "salvou seu cérebro" da fadiga cognitiva de acompanhar tanto o próprio raciocínio quanto o da IA. A citação de Kent Beck é usada para argumentar que "specs to code" desinveste no design do sistema, o oposto do que a disciplina recomenda.
**Confidence:** média — a citação de Kent Beck não foi verificada quanto à fonte exata (não indicada na palestra); o "salvou meu cérebro" é relato subjetivo de fadiga.

## Entities & Concepts Touched

- [[wiki/entities/matt-pocock]]
- [[wiki/entities/fred-brooks]]
- [[wiki/entities/john-ousterhout]]
- [[wiki/entities/kent-beck]]
- [[wiki/concepts/spec-driven-development]]
- [[wiki/concepts/vibe-coding]]
- [[wiki/concepts/tdd]]
- [[wiki/concepts/ddd]]
- [[wiki/concepts/modulo-profundo]]
- [[wiki/concepts/complexidade-acidental]]
- [[wiki/concepts/arquitetura-de-software]]
- [[wiki/concepts/entendimento-de-dominio]]
- [[wiki/concepts/prd-product-requirements-document]]
- [[wiki/concepts/tech-spec]]

**Nota de atualização (2026-07-10):** [[wiki/sources/filosofia-do-design-de-software-introducao]] ingeriu o capítulo introdutório do próprio livro de Ousterhout citado aqui de segunda mão — traz a fonte primária que confirma a definição de complexidade citada nesta palestra e adiciona o contexto que faltava aqui: as duas estratégias gerais do livro (eliminar vs. encapsular via módulos profundos) e por que design é processo contínuo, nunca uma fase única.

## Open Questions

- A skill "grill me" citada pelo autor (repositório "Mac PCO skills") não foi verificada nesta ingestão — não há como confirmar a contagem de estrelas nem examinar o código da skill sem acesso à URL.
- A citação atribuída a Kent Beck ("invest in the design of the system every day") não tem fonte primária indicada na palestra — vale checar contra *Tidy First?* ou outra obra de Beck em uma ingestão futura.
- Como a prática de "design the interface, delegate the implementation" se relaciona com — ou generaliza — a distinção já registrada em [[wiki/concepts/entendimento-de-dominio]] entre modelagem de domínio e decoreba de design patterns?

## Raw Quotes

> "Bad code is the most expensive it's ever been."

> "Code is not cheap. In fact bad code is the most expensive it's ever been."

> "No one knows exactly what they want — is that you and the AI, there is a communication barrier there."

> "Design the interface, delegate the implementation."

> "Invest in the design of the system every day." — atribuída a Kent Beck
