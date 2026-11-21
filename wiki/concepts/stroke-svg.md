---
type: concept
title: "Stroke em SVG (stroke-linecap, stroke-dasharray)"
aliases: ["stroke", "stroke-linecap", "stroke-dasharray", "stroke-dashoffset", "dash array", "contorno SVG"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 2
tags: [svg, stroke, stroke-dasharray, stroke-linecap, line-drawing, motion-design, frontend]
skill: tech-mentor-frontend
status: stub
---

# Stroke em SVG

O contorno de uma forma SVG. Além de `stroke` (cor) e `stroke-width`, tem propriedades sem equivalente direto na `border` do CSS, e quase todas podem ser escritas como atributo ou como propriedade CSS quando o SVG é inline.

| Propriedade | O que faz |
|---|---|
| `stroke-linecap` | Ponta de linha aberta: `butt` (padrão, corta reto), `round`, `square` |
| `stroke-linejoin` | Canto entre segmentos: `miter`, `round`, `bevel` |
| `stroke-dasharray` | Lista traço, vão, traço, vão... (`5 10`) |
| `stroke-dashoffset` | Desloca o início do tracejado; animável |
| `vector-effect: non-scaling-stroke` | Mantém a espessura quando o SVG escala |

## Na aula

[[wiki/entities/nasser|Násser]] mostra uma reta no [[wiki/entities/figma|Figma]]: "está vendo que ele é quadradinho", e há propriedades "para poder deixar ele redondo nas pontas"; depois o "dash array" com 5 10, 20 10 e 40 70, "porque como ele está round, você não enxerga direito". Dá "mais liberdade que as próprias propriedades do CSS" ([[wiki/sources/frontpush-propriedades-svg-introducao-o-que-e-por-que-usar]]).

## Precisões

`[external]` sem fetch (SVG 1.1/SVG 2, MDN):

- **Ponta `round` come o vão.** Cada traço ganha meia `stroke-width` em cada ponta; com traço grosso, `5 10` vira bolinhas encostadas. Para pontilhado redondo, traço `0` (ou quase) e vão maior que a espessura. Confiança alta.
- **Desenhar a linha (line drawing).** `stroke-dasharray` igual ao comprimento do caminho (`getTotalLength()` ou `pathLength="1"`) e `stroke-dashoffset` animado desse valor até 0. É a técnica do SVG "desenhado no scroll" da aula 02 do mini curso ([[wiki/sources/frontpush-como-usar-o-motion-vantagens-boas-praticas-pontos-de-atencao]]). Confiança alta.
- **Animar o dash repinta.** `stroke-dashoffset` não roda no compositor como `transform`/`opacity`; ver [[wiki/concepts/taxa-de-quadros-60fps]]. Confiança alta.
- **Pontilhado e cap round no Figma.** A aula prática de elementos de composição já usava "pontilhado 2, 10 e cap round" nas órbitas ([[wiki/sources/elementos-de-composicao-pratica-figma-orbitas-pontilhado-cometas-playstation]]): os mesmos controles, que o export leva para o SVG.

## Ver também

- [[wiki/concepts/formato-svg]]
- [[wiki/concepts/motion-design]]
- [[wiki/concepts/keyframes-css]]

## Lista do slide (FrontPUSH, propriedades SVG aula 03)

Em [[wiki/sources/frontpush-estrutura-svg-viewport-viewbox-formas-basicas-path-defs]], o slide de propriedades exclusivas lista `stroke`, `stroke-width`, `stroke-dasharray`, `stroke-linecap`, `stroke-dashoffset` e `stroke-opacity`; "enquanto no CSS é borda [...] aqui a gente trabalha mais com stroke", "um dos meus efeitos principais". As formas `line`/`polyline` do slide usam `stroke="#333" stroke-width="2"`.

## Key sources

- [[wiki/sources/frontpush-propriedades-svg-introducao-o-que-e-por-que-usar]]: FrontPUSH, mini curso de CSS Animations, propriedades SVG aula 01: pontas redondas e dash array
- [[wiki/sources/frontpush-estrutura-svg-viewport-viewbox-formas-basicas-path-defs]]: FrontPUSH, mini curso de CSS Animations, propriedades SVG aula 03: stroke-* no slide de propriedades exclusivas
