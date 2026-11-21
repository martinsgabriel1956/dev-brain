---
type: concept
title: "Motion design"
aliases: ["Motion Design", "motion", "motion para web", "animação de interface", "CSS Animations"]
date_created: 2026-11-20
date_updated: 2026-11-20
source_count: 8
tags: [motion-design, animacao, css, svg, easing, ui-design, frontend]
skill: tech-mentor-frontend
status: stub
---

# Motion design

Design gráfico em movimento. Na definição de [[wiki/entities/nasser|Násser]], é "o gráfico em movimento no espaço da tela e no tempo" ([[wiki/sources/frontpush-introducao-motion-design-css-animations-grade-do-curso]]). Em interfaces, a definição de trabalho dele é mais estreita: motion é "transição entre estados com determinados níveis de velocidade diferentes entre eles".

## Motion para web

O recorte do mini curso do [[wiki/entities/frontpush|FrontPUSH]] é o motion feito com o que o navegador entende, [[wiki/concepts/html-hipertexto|HTML]], [[wiki/concepts/css]] e [[wiki/entities/javascript|JavaScript]], e "otimizado para poder executar no browser". Não é motion de vídeo (After Effects); é animação que roda na própria página.

As peças que a grade do curso promete:

- **Transição entre estados.** Um elemento sai de um estado (repouso) e vai a outro (hover, aberto, carregado). Em CSS, `transition` para dois estados e `@keyframes` para sequências ([[wiki/concepts/transition-e-transform-css]]).
- **Velocidade variável ([[wiki/concepts/easing|easing]]).** Os "níveis de velocidade diferentes" são a função de temporização: `ease`, `ease-in-out`, `cubic-bezier()`, `steps()`, `linear()`. `[skill: tech-mentor-frontend]`
- **SVG.** Cada caminho de um SVG inline é um nó do DOM que o CSS anima (`stroke-dasharray`, `fill`, `transform`). Quase todas as animações do site de Násser são SVG ([[wiki/concepts/formato-svg]]).
- **Bibliotecas JavaScript.** Para timelines e sequências, como o [[wiki/entities/gsap|GSAP]]. A pergunta do curso é "utilizar uma biblioteca ou CSS puro".

## Biblioteca ou CSS puro

O que a wiki já tem sobre o trade-off:

- **Desempenho.** Animação CSS (ou da Web Animations API) de `transform` e `opacity` pode rodar na thread do compositor e continua fluida com a thread principal ocupada. O GSAP atualiza estilos via `requestAnimationFrame`, na thread principal ([[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]], [[wiki/concepts/taxa-de-quadros-60fps]]).
- **Controle.** Bibliotecas ganham em timelines encadeadas, controle de reprodução e animação por rolagem (ScrollTrigger). `[skill: tech-mentor-frontend]` GSAP para scroll storytelling e animação de marketing; Framer Motion para interações de UI em React.
- **CSS moderno.** Scroll-driven animations (`animation-timeline`), `@starting-style` e a View Transitions API cobrem casos que antes pediam JavaScript. `[skill: tech-mentor-frontend]`

## Acessibilidade

Movimento pode causar enjoo e distração em pessoas com distúrbios vestibulares. Animações não essenciais devem respeitar `prefers-reduced-motion` ([[wiki/concepts/acessibilidade]]). `[external]` WCAG 2.2.2 (Pause, Stop, Hide, nível A) e 2.3.3 (Animation from Interactions, AAA). A grade do mini curso não cita o tema.

## Princípios

Na aula 01 o mini curso promete "princípios de Motion" sem dizer quais, e a wiki inferiu os 12 princípios da animação da Disney (confiança média). **A aula 03 corrigiu a inferência** ([[wiki/sources/frontpush-principios-motion-linha-do-tempo-keyframes-transicao-entre-estados]]): são três conceitos que [[wiki/entities/nasser|Násser]] trouxe do [[wiki/entities/after-effects|After Effects]]:

1. **Linha do tempo:** "o tempo transcorrido de uma determinada animação" (`animation-duration`).
2. **[[wiki/concepts/keyframes-css|Keyframes]]:** pontos na linha do tempo onde as propriedades mudam; "N estados" de 0% a 100%.
3. **Transição entre estados ([[wiki/concepts/easing]]):** como a velocidade varia entre os pontos; o carro freando não é `linear`.

Dos 12 da Disney, só o *slow in and slow out* (o easing) aparece. O método declarado é por exemplos: "uma biblioteca de exemplos na sua cabeça" ([[wiki/concepts/repertorio]]).

## Para que serve e quando não usar (aula 02)

Em [[wiki/sources/frontpush-como-usar-o-motion-vantagens-boas-praticas-pontos-de-atencao]]: motion cria **pontos de atenção** e guia o usuário na jornada; "não são puramente estéticas". Funciona por contraste: "se colocar motion em tudo, não tem contraste", como na [[wiki/concepts/hierarquia-visual]] do texto. Vantagens: diferencial "no mar de páginas estáticas", valor, "sentimento de descoberta". Preço: "o sistema pode ficar mais lento". Inclui as [[wiki/concepts/microinteracao]].

## Biblioteca ou CSS puro: a resposta (aula 04)

Em [[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]], a pergunta da aula 01 vira "depende", pela dualidade otimização × facilidade: CSS puro para o simples, biblioteca JS para 3D e casos complexos. Ver [[wiki/concepts/css-puro-vs-biblioteca-de-animacao]].

## As propriedades de motion começam pelo transform (básico CSS aula 01)

Em [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]] começa o módulo "Básico CSS" do mini curso: `transform`, `transition`, `opacity`, `position`, `animation`. A primeira aula fica com as funções de `transform` e a [[wiki/concepts/perspective-css|perspectiva]]; os exemplos dos sites dele (seta que transita entre pontos de translate com velocidades diferentes, links que sobem no hover) são `translate` com [[wiki/concepts/easing]].

## Ponto de ancoragem e 3D (básico CSS aula 02)

Em [[wiki/sources/frontpush-propriedade-transform-parte-2-transform-origin-transform-style-preserve-3d]]: [[wiki/concepts/transform-origin-css]] e `preserve-3d`, e o convite a "colocar transitando esses estados utilizando a animação".

## A propriedade animation (básico CSS aula 03)

Em [[wiki/sources/frontpush-propriedade-animation-parte-1-keyframes-from-to-duration-direction-fill-mode]], "a tão esperada e tão aclamada propriedade de animação": `@keyframes` com N estados e as subpropriedades de `animation` ([[wiki/concepts/keyframes-css]]); a linha do tempo e os keyframes da aula 03 de princípios viram código.

## A curva como identidade do movimento (básico CSS aula 04)

Em [[wiki/sources/frontpush-propriedade-animation-parte-2-curvas-cubic-bezier-editor-chrome]]: "eu quero um padrão que é só o meu": `cubic-bezier` próprio, e a curva do carro freando como a "noção" que a transição entre estados tem de passar ([[wiki/concepts/easing]]).

## Key sources

- [[wiki/sources/frontpush-introducao-motion-design-css-animations-grade-do-curso]]: FrontPUSH, mini curso de CSS Animations, aula 01: definição, motion para web, grade do curso
- [[wiki/sources/frontpush-como-usar-o-motion-vantagens-boas-praticas-pontos-de-atencao]]: FrontPUSH, mini curso de CSS Animations, aula 02: vantagens, cuidados, "não coloque motion em tudo"
- [[wiki/sources/frontpush-principios-motion-linha-do-tempo-keyframes-transicao-entre-estados]]: FrontPUSH, mini curso de CSS Animations, aula 03: linha do tempo, keyframes e easing; origem no After Effects
- [[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]]: FrontPUSH, mini curso de CSS Animations, aula 04: "depende": otimização × facilidade
- [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 01: módulo Básico CSS: transform e perspectiva
- [[wiki/sources/frontpush-propriedade-transform-parte-2-transform-origin-transform-style-preserve-3d]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 02: transform-origin e preserve-3d
- [[wiki/sources/frontpush-propriedade-animation-parte-1-keyframes-from-to-duration-direction-fill-mode]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 03: @keyframes e subpropriedades de animation
- [[wiki/sources/frontpush-propriedade-animation-parte-2-curvas-cubic-bezier-editor-chrome]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 04: curva própria com cubic-bezier
