---
type: concept
title: "Viewport e viewBox do SVG"
aliases: ["viewbox", "viewBox", "viewport svg", "preserveAspectRatio", "sistema de coordenadas do svg"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 1
tags: [svg, viewbox, viewport, coordenadas, responsivo, frontend]
skill: tech-mentor-frontend
status: stub
---

# Viewport e viewBox do SVG

Dois tamanhos diferentes num `<svg>`:

- **Viewport:** a área que o `<svg>` ocupa na página (`width`/`height` do atributo ou do CSS). O que passa da borda é cortado.
- **`viewBox="min-x min-y largura altura"`:** o sistema de coordenadas do desenho. Diz qual retângulo do desenho é esticado para caber no viewport.

`<svg width="300" height="300" viewBox="0 0 150 150">` mostra só 150×150 unidades em 300×300 px: tudo sai em dobro (zoom in). `viewBox="0 0 600 600"` faz o contrário (zoom out). Mudar `min-x`/`min-y` desloca a janela (pan). Quando as proporções diferem, `preserveAspectRatio` decide o encaixe; o padrão `xMidYMid meet` centraliza e mostra tudo; `none` distorce; `slice` preenche e corta.

A origem `0 0` fica no canto superior esquerdo e o Y cresce para baixo, não o plano cartesiano da escola.

`[external]` sem fetch (SVG 1.1/SVG 2, MDN). Confiança alta.

## SVG responsivo

Mantém-se o `viewBox` e tira-se `width`/`height` fixos (ou usa-se `width: 100%; height: auto` no CSS). Sem `viewBox`, o SVG não escala: só corta ou sobra espaço. O SVG exportado do Figma traz os três; é por isso que "não está responsivo" ([[wiki/sources/frontpush-propriedades-svg-introducao-o-que-e-por-que-usar]]).

## Na aula do FrontPUSH

[[wiki/entities/nasser|Násser]] demonstra num `<svg>` de 300×300 com borda branca: um círculo de raio 70 em (50, 50) é cortado pela "janelinha"; o `viewBox` 150 dá "zoom in", o 600 "zoom out". Analogia do slide: "Viewport vs. ViewBox ~ Tela vs. Resolução" (23 polegadas em Full HD ou 2K). Na prática, "não gosto de modificar esses valores"; tira `width` e `height` e deixa o CSS dimensionar ([[wiki/sources/frontpush-estrutura-svg-viewport-viewbox-formas-basicas-path-defs]]).

Precisões: são quatro números, não "o tamanho da viewport multiplicado ou não"; o "só vai centralizar" vem do `preserveAspectRatio`.

## Ver também

- [[wiki/concepts/formato-svg]]
- [[wiki/concepts/path-svg]]
- [[wiki/concepts/unidades-de-viewport]]: o viewport da página, outra coisa
- [[wiki/concepts/design-responsivo]]

## Key sources

- [[wiki/sources/frontpush-estrutura-svg-viewport-viewbox-formas-basicas-path-defs]]: FrontPUSH, mini curso de CSS Animations, propriedades SVG aula 03: viewport × viewBox, tela × resolução
