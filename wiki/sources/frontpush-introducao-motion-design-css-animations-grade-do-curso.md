---
type: source
title: "Introdução ao Motion Design: o que é e a grade do mini curso de CSS Animations (FrontPUSH)"
aliases: ["FrontPUSH motion aula 01", "Introdução ao Motion Design", "mini curso Patch CA", "CSS Animations, aula 01"]
date_created: 2026-11-20
date_updated: 2026-11-20
source_count: 0
tags: [motion-design, animacao, css, svg, transicao, estado, biblioteca-vs-css-puro, gsap, curso, frontend]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-introducao-motion-design-css-animations-grade-do-curso.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-20
---

# Introdução ao Motion Design: o que é e a grade do mini curso de CSS Animations (FrontPUSH)

## TL;DR

Aula 01 de um mini curso de animação do [[wiki/entities/frontpush|FrontPUSH]], cerca de 6 minutos, só com slides. [[wiki/entities/nasser|Násser]] diz o nome. A legenda chama o curso de "Patch CA" e explica a sigla como "CSS Animations ou Curse Animations".

- **Definição:** [[wiki/concepts/motion-design]] é "o gráfico em movimento no espaço da tela e no tempo". O recorte é motion *para web*: HTML, CSS e JavaScript, "mais otimizado para poder executar no browser".
- **A mecânica:** motion é "transição entre estados com determinados níveis de velocidade diferentes entre eles" ([[wiki/concepts/transition-e-transform-css]]).
- **Método:** "baseado muito em exemplo". Há princípios, mas "não é uma regrinha"; o objetivo é ter "uma biblioteca de exemplos na sua cabeça" ([[wiki/concepts/repertorio]]).
- **Grade:** princípios de motion → propriedades de [[wiki/concepts/css]] voltadas ao motion → propriedades do [[wiki/concepts/formato-svg|SVG]] → animações na prática → bibliotecas JavaScript e o debate "biblioteca ou CSS puro" ([[wiki/entities/gsap]]) → módulo só de exemplos → bônus.
- **CSS primeiro:** retoma as "três partes" do CSS, estilização, layout e animação, que fecharam o módulo de CSS ([[wiki/sources/frontpush-conclusao-modulo-css-estilo-layout-animacao-documentacao]]).

## Key Claims

### O que é motion design

- "Um conceito bem simples aqui é o gráfico em movimento no espaço da tela e no tempo." "Design" é "o gráfico, [...] algum tipo de desenho, algum tipo de forma"; "Motion, movimento". Ver [[wiki/concepts/motion-design]].
- O curso trabalha "Motion Design para web", "utilizando as tecnologias que o browser entende, que é HTML, CSS e JavaScript" ([[wiki/concepts/html-hipertexto]], [[wiki/entities/javascript]]). Repete a fala da aula de ambiente ([[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]): o navegador entende três coisas.
- Motion "praticamente eu posso colocar como transição entre estados com determinados níveis de velocidade diferentes entre eles". Evidência: é a definição de trabalho para a parte de "princípio de Motion" e de "linha do tempo". Ver [[wiki/concepts/transition-e-transform-css]].

### Método: exemplos, não regras

- "Tem vários skills e vários jeitos de a gente aplicar o Motion, não é uma regrinha. Lógico que tem alguns princípios, mas [...] se dá muito pelo pleno entendimento de vários exemplos, de você literalmente ter uma biblioteca de exemplos na sua cabeça." Ver [[wiki/concepts/repertorio]].
- Motivo de dar o curso: "ao estudar, ao tentar passar o conhecimento, a gente aprende muito no processo". Objetivo: "elevar o nível das nossas interfaces web".

### CSS como base

- "O CSS3 trouxe vários recursos." "O curso inteiro, eu batendo na tecla CSS, CSS, CSS [...] porque pouca gente conhece o poder que essa tecnologia traz."
- "E aí tem três partes, lembra? A parte de estilização, a parte de layout e a parte de animação." Uma propriedade "pode muito bem interferir na outra", mas algumas são "mais voltadas" ao motion. Ver [[wiki/concepts/css]].
- Erro de fala: chama o CSS de "linguagem de marcação". Ver Precisões.

### SVG

- "A grande e esmagadora maioria das animações que eu faço no meu site [...] eu utilizo de SVGs, que são animações vetorizadas, se é que eu posso colocar assim."
- "Ele no fundo é tags HTML, então se é uma tag HTML, eu posso manipular ele com o CSS." Por isso conhecer as propriedades do SVG é "muito importante" para o resultado. Ver [[wiki/concepts/formato-svg]].

### Bibliotecas e exemplos

- Depois de CSS e SVG, "começar a executar de forma mais ordenada as bibliotecas JavaScript" e "discutir um pouco também sobre essa grande dualidade aqui, utilizar uma biblioteca ou CSS puro". Um módulo inteiro trata de bibliotecas JavaScript ([[wiki/entities/gsap]] é a que ele já usou no curso).
- Um módulo "só para a gente tratar dos mais exemplos possíveis" e um módulo de bônus para "tudo aquilo que não cabe em algum outro módulo".

### O slide

O slide da aula lista: Introdução; O que é motion design? ("É o gráfico em movimento no espaço da tela e no tempo"); Grade do curso; Princípios Motion; Baseado em exemplos; Vantagens e boas práticas motion (com estrela); Biblioteca vs. CSS puro; e, à parte, "Motion Design pra web" (com estrela). O slide usa um logo triangular com um "A", diferente do logo do FrontPUSH. "Vantagens e boas práticas" está no slide, mas não aparece na fala.

## Entities

- [[wiki/entities/nasser]]: instrutor; diz o nome ("Aqui é o Násser").
- [[wiki/entities/frontpush]]: curso; a legenda está na pasta "FrontPush".
- [[wiki/entities/gsap]]: biblioteca JavaScript de animação já usada no curso; centro provável do módulo de bibliotecas (inferência).
- [[wiki/entities/javascript]]: uma das três tecnologias do motion para web.

## Concepts

- [[wiki/concepts/motion-design]]: definição e recorte web (página criada nesta ingestão).
- [[wiki/concepts/transition-e-transform-css]]: transição entre estados com velocidades diferentes.
- [[wiki/concepts/css]]: estilização, layout e animação.
- [[wiki/concepts/formato-svg]]: SVG como tags que o CSS manipula.
- [[wiki/concepts/repertorio]]: "biblioteca de exemplos na sua cabeça".
- [[wiki/concepts/html-hipertexto]]: HTML como uma das tecnologias que o browser entende.
- [[wiki/concepts/acessibilidade]]: ausente na grade; ver Precisões.

## Precisões e tensões com a wiki

- **CSS não é linguagem de marcação.** É uma linguagem de folhas de estilo; marcação é o HTML (e o SVG, que é XML). A própria wiki já registra "Cascading Style Sheets, ou seja, folhas de estilo" ([[wiki/concepts/css]]) e, no fim do módulo de CSS, "HTML é uma linguagem de marcação" ([[wiki/sources/frontpush-conclusao-modulo-css-estilo-layout-animacao-documentacao]]). Provável lapso de fala. Confiança alta.
- **"CSS3" é rótulo, não versão.** O mesmo ponto já está em [[wiki/concepts/css]]. `[external]` Transitions, Animations e Transforms são módulos separados da especificação, cada um com seu nível: https://www.w3.org/Style/CSS/specs.en.html. Confiança alta.
- **SVG não é HTML.** SVG é XML com namespace próprio. Embutido inline no HTML, vira nós do DOM, e o CSS da página alcança `fill`, `stroke`, `stroke-dasharray`, `transform` etc. Carregado por `<img>` ou `background-image`, o CSS da página não entra (já anotado em [[wiki/concepts/formato-svg]]). A frase "no fundo é tags HTML" vale como intuição para o SVG inline. `[external]` sem fetch; confiança alta.
- **"Níveis de velocidade diferentes" é easing.** O nome técnico da variação de velocidade ao longo da transição é a função de temporização (`transition-timing-function`, `animation-timing-function`: `ease`, `cubic-bezier()`, `steps()`, `linear()`). `[skill: tech-mentor-frontend]` Confiança alta.
- **Que "princípios de Motion"?** A aula não diz quais. As listas mais citadas são os 12 princípios da animação da Disney (Thomas e Johnston, *The Illusion of Life*, 1981) e os guias de motion de design systems (Material Design). Isso é inferência; conferir na aula 02. `[external]` sem fetch; confiança média.
- **Biblioteca × CSS puro: o que pesa.** Na aula 07 de otimização ([[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]]) a wiki registrou que animação CSS (ou Web Animations API) de `transform`/`opacity` roda no compositor, e que o [[wiki/entities/gsap|GSAP]] roda na thread principal. `[skill: tech-mentor-frontend]` Bibliotecas ganham em timelines, sequências e scroll storytelling; o CSS moderno encurtou a distância (scroll-driven animations, `@starting-style`, View Transitions API). Esses recursos são posteriores à provável data da gravação.
- **Falta acessibilidade na grade.** Nenhum tópico fala em `prefers-reduced-motion`, que a wiki já cobrou na aula 07 de otimização. `[external]` WCAG 2.2.2 (Pause, Stop, Hide, nível A) e 2.3.3 (Animation from Interactions, AAA). Pode estar em "Vantagens e boas práticas", que está no slide e não na fala (inferência). Ver [[wiki/concepts/acessibilidade]].

## Open Questions

- **Nome do curso.** "Patch CA" é a legenda; pela família de marcas (FrontPUSH, [[wiki/entities/axlepush|AxlePUSH]], [[wiki/entities/creatorpush|CreatorPUSH]]), o nome provável é "PUSH CA" ou "PushCA". Confiança média; deixado literal no raw. "Curse Animations" talvez seja "Course Animations". O logo triangular do slide também não é o do FrontPUSH.
- **Data.** Fica antes ou depois do módulo de otimização? A aula 07 de otimização já usa GSAP e timeline; aqui as bibliotecas são prometidas.
- "As aulas introdutórias": quais? Talvez as aulas de motion do módulo de UI ou um vídeo de apresentação do mini curso.
- "Nesses dois módulos aqui": provavelmente CSS e SVG.
- "A gente vê mesmo cedo do inglês": provável "sendo do inglês"; deixado literal.

## Continuação

O tópico "Vantagens e boas práticas" virou a aula 02 ([[wiki/sources/frontpush-como-usar-o-motion-vantagens-boas-praticas-pontos-de-atencao]]): pontos de atenção, [[wiki/concepts/microinteracao]], "não coloque motion em tudo" e o preço em desempenho. `prefers-reduced-motion` também não aparece lá.


Os "princípios de Motion" vieram na aula 03 ([[wiki/sources/frontpush-principios-motion-linha-do-tempo-keyframes-transicao-entre-estados]]): linha do tempo, [[wiki/concepts/keyframes-css]] e [[wiki/concepts/easing]], não os 12 princípios da Disney inferidos acima.

A "grande dualidade" biblioteca × CSS puro virou a aula 04 ([[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]]): "depende", otimização × facilidade ([[wiki/concepts/css-puro-vs-biblioteca-de-animacao]]).

## Raw quotes

- "o gráfico em movimento no espaço da tela e no tempo"
- "transição entre estados com determinados níveis de velocidade diferentes entre eles"
- "uma biblioteca de exemplos na sua cabeça"
- "utilizar uma biblioteca ou CSS puro"
