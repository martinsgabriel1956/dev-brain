---
type: concept
title: "transform-origin (ponto de ancoragem)"
aliases: ["transform-origin", "ponto de ancoragem", "origem da transformação", "eixo de rotação CSS", "transform-box"]
date_created: 2026-11-20
date_updated: 2026-11-20
source_count: 2
tags: [css, transform, transform-origin, svg, animacao, frontend]
skill: tech-mentor-frontend
status: stub
---

# transform-origin (ponto de ancoragem)

O ponto fixo em torno do qual `rotate`, `scale` e `skew` acontecem. `translate` não muda com ele. Padrão: o centro da caixa (`50% 50% 0`).

## Sintaxe

`[external]` (CSS Transforms Level 1, w3.org/TR/css-transforms-1; MDN; confiança alta)

- `transform-origin: x y z`. X: `left` | `center` | `right` | comprimento | %. Y: `top` | `center` | `bottom` | comprimento | %. Z: só comprimento.
- Um valor só vale para um eixo e põe o outro em `center` (`left` = `left center`).
- Com duas palavras-chave a ordem é livre (`top left` = `left top`); com números a ordem é X Y.
- Porcentagem é do próprio elemento. Valores negativos ou acima de 100% põem o eixo fora da caixa: um elemento que gira em torno de um ponto distante descreve uma órbita.

| Efeito | Origem |
|---|---|
| Ponteiro de relógio | `bottom center` |
| Porta abrindo | `left center` com `rotateY` |
| Barrinha que cresce da esquerda | `left` com `scaleX` |
| Menu que desce | `top` com `scaleY` |

## SVG

Em elementos SVG o padrão é `0 0` do sistema de coordenadas do SVG, não o centro do elemento: `rotate` gira em torno do canto. Para girar uma forma no lugar: `transform-box: fill-box; transform-origin: center`. ([[wiki/concepts/formato-svg]])

## No FrontPUSH (Násser)

Na [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva|parte 1 da aula de transform]], [[wiki/entities/nasser|Násser]] aponta que o `rotate` gira em torno do centro, "o seu ponto de ancoragem", e promete mudá-lo. Na [[wiki/sources/frontpush-propriedade-transform-parte-2-transform-origin-transform-style-preserve-3d|parte 2]], gira um quadrado 180° no hover com a origem em `center`, `0% 0%`, `50% 0%` e `100%`, e prefere porcentagem por ser "mais intuitivo". Na fala os eixos das palavras-chave saem trocados ("quando é Y, é left ou right"), mas o código funciona, porque o navegador reconhece `top`/`left` pelo nome. Ver [[wiki/concepts/transition-e-transform-css]].

## Key sources

- [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 01: o centro como "ponto de ancoragem"
- [[wiki/sources/frontpush-propriedade-transform-parte-2-transform-origin-transform-style-preserve-3d]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 02: demo com 0%, 50% e 100%; importância no SVG
