---
type: concept
title: "Easing (função de temporização)"
aliases: ["easing", "timing function", "função de temporização", "transition-timing-function", "animation-timing-function", "cubic-bezier", "ease-in", "ease-out", "transição entre estados"]
date_created: 2026-11-20
date_updated: 2026-11-20
source_count: 2
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

## Key sources

- [[wiki/sources/frontpush-principios-motion-linha-do-tempo-keyframes-transicao-entre-estados]]: FrontPUSH, mini curso de CSS Animations, aula 03: carro freando, linear × ease, "ease invertido"
- [[wiki/sources/frontpush-introducao-motion-design-css-animations-grade-do-curso]]: FrontPUSH, mini curso de CSS Animations, aula 01: "níveis de velocidade diferentes"
