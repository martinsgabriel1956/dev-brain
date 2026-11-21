---
type: concept
title: "Easing (função de temporização)"
aliases: ["easing", "timing function", "função de temporização", "transition-timing-function", "animation-timing-function", "cubic-bezier", "ease-in", "ease-out", "transição entre estados"]
date_created: 2026-11-20
date_updated: 2026-11-21
source_count: 7
tags: [easing, timing-function, cubic-bezier, animacao, css, motion-design, frontend]
skill: tech-mentor-frontend
status: stub
---

# Easing (função de temporização)

Como a velocidade varia entre dois estados de uma animação. No mini curso de CSS Animations do [[wiki/entities/frontpush|FrontPUSH]], é a "transição entre N estados", terceiro princípio de [[wiki/concepts/motion-design]] ao lado da linha do tempo e dos [[wiki/concepts/keyframes-css|keyframes]]. Na aula 01, [[wiki/entities/nasser|Násser]] já definia motion como "transição entre estados com determinados níveis de velocidade diferentes" ([[wiki/sources/frontpush-introducao-motion-design-css-animations-grade-do-curso]]).

## O carro freando

Exemplo da aula 03 ([[wiki/sources/frontpush-principios-motion-linha-do-tempo-keyframes-transicao-entre-estados]]): o carro freando é "mais rápido [...] no começo" e vai devagar no fim. Com `linear`, "a mesma velocidade [...] no começo [...] e no final", "seria totalmente irreal". A curva certa é a que ele chama de "ease invertido": `ease-out`.

## As curvas do CSS

`[external]` Valores de `transition-timing-function` e `animation-timing-function` (confiança alta):

| Valor | Comportamento | `cubic-bezier` |
|---|---|---|
| `linear` | velocidade constante | `(0, 0, 1, 1)` |
| `ease` (padrão) | acelera pouco, desacelera bastante | `(0.25, 0.1, 0.25, 1)` |
| `ease-in` | começa devagar, termina rápido | `(0.42, 0, 1, 1)` |
| `ease-out` | começa rápido, termina devagar (frear) | `(0, 0, 0.58, 1)` |
| `ease-in-out` | devagar nas pontas | `(0.42, 0, 0.58, 1)` |

Além delas: `cubic-bezier()` personalizado (a "nossa própria transição" prometida na aula), `steps()` para movimento em degraus (sprites) e `linear()` com vários pontos, que permite simular mola e quique sem JavaScript (suporte amplo desde 2023). `[skill: tech-mentor-frontend]`

O gráfico de uma curva de easing é progresso × tempo, não velocidade: a velocidade é a inclinação. Uma curva `ease-out` sobe íngreme e achata no fim.

## Regras práticas

`[skill: tech-mentor-frontend]` Elemento entrando na tela: `ease-out` (chega rápido e assenta). Elemento saindo: `ease-in`. Movimento dentro da tela: `ease-in-out`. `linear` só para rotação contínua, loaders e progresso, como as órbitas de 0 a 360deg da aula 03. É o princípio *slow in and slow out* da animação tradicional.

## ease antes da explicação (FrontPUSH, básico CSS aula 02)

Em [[wiki/sources/frontpush-propriedade-transform-parte-2-transform-origin-transform-style-preserve-3d]]: "o modo da transição do modo ease. Não se preocupe que eu vou explicar ainda". `ease` = `cubic-bezier(0.25, 0.1, 0.25, 1)`, o padrão de `transition`.

## animation-timing-function (FrontPUSH, básico CSS aula 03)

Em [[wiki/sources/frontpush-propriedade-animation-parte-1-keyframes-from-to-duration-direction-fill-mode]], a timing function "é a forma, é a curva": quatro curvas-padrão e `cubic-bezier` para "criar sua própria curva", tema da aula seguinte. "Na maioria das vezes eu utilizo o ease." `[external]` Numa `animation` a curva se aplica a cada intervalo entre keyframes, não à linha do tempo inteira, e pode ser trocada dentro de um keyframe.

## Editor do Chrome e cubic-bezier.com (FrontPUSH, básico CSS aula 04)

Em [[wiki/sources/frontpush-propriedade-animation-parte-2-curvas-cubic-bezier-editor-chrome]], [[wiki/entities/nasser|Násser]] mostra as curvas no editor do [[wiki/entities/chrome-devtools]] (`ease-in-out`, `ease-out`, presets *out sine* e *out back*) e cria uma curva própria em [[wiki/entities/cubic-bezier-com]], copiando o `cubic-bezier()` "ao invés de colocar ease". Leitura do gráfico: horizontal é o tempo, vertical "a progressão". `[external]` A velocidade é a inclinação, não a distância da diagonal; os x dos pontos de controle ficam entre 0 e 1, os y podem sair da faixa, e é isso que faz a curva "ir e voltar" (*overshoot*). O carro freando volta como a noção que a curva tem de passar.

## ease trocado por cubic-bezier (FrontPUSH, básico CSS aula 05)

Em [[wiki/sources/frontpush-propriedade-animation-pratica-keyframes-parent-box-varias-animacoes]], a curva "muito rápido [...] e no final, muito devagar" (um `ease-out` forte) substitui o `ease` do shorthand; com 15 s a diferença some, com 2 s "ficou mais acentuada". `[external]` O giro `ease alternate` de 0 a 360 vira pêndulo; rotação contínua pede `linear`.

## A mesma Bézier no path (FrontPUSH, propriedades SVG aula 03)

Em [[wiki/sources/frontpush-estrutura-svg-viewport-viewbox-formas-basicas-path-defs]], o `C` do path aparece como letra desconhecida. `[external]` É a Bézier cúbica do `cubic-bezier()`: lá tempo × progresso, aqui posição no desenho ([[wiki/concepts/path-svg]]).

## Key sources

- [[wiki/sources/frontpush-principios-motion-linha-do-tempo-keyframes-transicao-entre-estados]]: FrontPUSH, mini curso de CSS Animations, aula 03: carro freando, linear × ease, "ease invertido"
- [[wiki/sources/frontpush-introducao-motion-design-css-animations-grade-do-curso]]: FrontPUSH, mini curso de CSS Animations, aula 01: "níveis de velocidade diferentes"
- [[wiki/sources/frontpush-propriedade-transform-parte-2-transform-origin-transform-style-preserve-3d]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 02: ease usado antes de explicado
- [[wiki/sources/frontpush-propriedade-animation-parte-1-keyframes-from-to-duration-direction-fill-mode]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 03: timing function por intervalo; ease como padrão dele
- [[wiki/sources/frontpush-propriedade-animation-parte-2-curvas-cubic-bezier-editor-chrome]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 04: editor do Chrome, cubic-bezier.com, curva própria, overshoot
- [[wiki/sources/frontpush-propriedade-animation-pratica-keyframes-parent-box-varias-animacoes]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 05: curva própria no lugar de ease; ease alternate em giro = pêndulo
- [[wiki/sources/frontpush-estrutura-svg-viewport-viewbox-formas-basicas-path-defs]]: FrontPUSH, mini curso de CSS Animations, propriedades SVG aula 03: C do path = Bézier cúbica
