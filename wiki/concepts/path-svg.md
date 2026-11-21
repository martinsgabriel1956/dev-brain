---
type: concept
title: "path do SVG (atributo d e comandos)"
aliases: ["path", "<path>", "atributo d", "comandos de path", "moveto", "lineto", "path morphing", "morph svg"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 1
tags: [svg, path, bezier, vetorial, morph, motion-design, frontend]
skill: tech-mentor-frontend
status: stub
---

# path do SVG

O elemento que desenha qualquer forma livre. O atributo `d` é uma lista de comandos, cada letra seguida de coordenadas X Y:

| Comando | Nome | Faz |
|---|---|---|
| `M x y` | moveto | Leva a caneta a um ponto sem desenhar |
| `L x y` | lineto | Reta até o ponto |
| `H x` / `V y` | horizontal / vertical | Reta só num eixo |
| `C x1 y1 x2 y2 x y` | curveto | Bézier cúbica: dois pontos de controle e o ponto final |
| `S x2 y2 x y` | smooth curveto | Cúbica que espelha o controle anterior |
| `Q x1 y1 x y` / `T x y` | quadrática | Bézier com um ponto de controle |
| `A rx ry rot large sweep x y` | arco | Arco de elipse |
| `Z` | closepath | Fecha voltando ao início |

Maiúscula = coordenada absoluta; minúscula = relativa ao ponto atual. Toda forma básica (`rect`, `circle`, `polygon`) pode ser escrita como path; a Pen Tool do Figma ([[wiki/concepts/vetorizacao-com-pen-tool]]) exporta quase tudo assim.

`[external]` sem fetch (SVG 1.1/SVG 2, MDN). Confiança alta.

## Bézier: a mesma curva do easing

O `C` é a mesma Bézier cúbica do `cubic-bezier()` das curvas de animação ([[wiki/concepts/easing]], [[wiki/entities/cubic-bezier-com]]): no easing, os pontos são tempo × progresso; no path, posição no desenho.

## Animar um path

- **Desenhar o traço:** `stroke-dasharray` + `stroke-dashoffset` ([[wiki/concepts/stroke-svg]]).
- **Morph (um desenho vira outro):** só interpola se os dois `d` tiverem o mesmo número e tipo de comandos. Vias: propriedade CSS `d: path("...")` em `transition`/`@keyframes` (Chromium e Firefox; Safari a conferir), SMIL `<animate attributeName="d">`, ou GSAP MorphSVG/flubber, que igualam os pontos. Confiança média-alta.

## Na aula do FrontPUSH

[[wiki/entities/nasser|Násser]]: o path é "um dos mais importantes", o que a Pen Tool desenha; `M` move to, `L` line to, `A` arcs, `Z` close path; "aqui tem um C" que ele precisa pesquisar, e "eu nunca entendi de fato [...] como se dá o caminho", porque faz pelo Figma. No exemplo do Spotify, pega o código de dois caminhos e "transita desse para esse" ([[wiki/sources/frontpush-estrutura-svg-viewport-viewbox-formas-basicas-path-defs]]).

Precisão: `M711 435` é **um** ponto (x, y), não "dois pontos [...] de tal ponto a tal ponto".

## Ver também

- [[wiki/concepts/formato-svg]]
- [[wiki/concepts/viewbox-svg]]
- [[wiki/concepts/motion-design]]

## Key sources

- [[wiki/sources/frontpush-estrutura-svg-viewport-viewbox-formas-basicas-path-defs]]: FrontPUSH, mini curso de CSS Animations, propriedades SVG aula 03: path, comandos M/L/A/Z, morph do Spotify
