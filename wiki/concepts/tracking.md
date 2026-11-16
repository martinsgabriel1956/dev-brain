---
type: concept
title: "Tracking"
aliases: ["letter-spacing", "espaçamento entre letras", "entreletra"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [ui, ui-design, tipografia, tracking, letter-spacing, legibilidade, css]
skill: ux-ui-mentor
status: stub
---

# Tracking

Distância uniforme entre todas as letras de um trecho; no CSS, `letter-spacing`. Difere do [[wiki/concepts/kerning]], que ajusta um par específico. Parte de [[wiki/concepts/tipografia]].

## Abrir em maiúsculas, menus e botões

Em [[wiki/sources/tipografia-negrito-italico-tracking-kerning-maiusculas]], [[wiki/entities/nasser|Násser]]: tracking "define maior legibilidade e estilo dependendo da fonte"; não é para tudo, mas texto todo em [[wiki/concepts/texto-em-maiusculas|maiúsculas]] pede "uma maior distância". Aparece em itens de menu e em [[wiki/concepts/botoes-em-interfaces|botões]], sobretudo CTAs; nos botões do site dele (provavelmente o [[wiki/entities/frontpush]]), maiúsculas + letter-spacing "para poder chamar mais atenção".

## Figma e CSS

O tracking do [[wiki/entities/figma]] é o `letter-spacing` do [[wiki/concepts/css]]; o Inspect o mostra em `em`. A aula fala em "10% de 16 pixels". `[external]` `em` é relativo ao `font-size` do elemento, não fixo em 16 px; por isso o tracking em `em` acompanha o tamanho da fonte.

## Valores de referência

`[skill: ux-ui-mentor]`

| Uso | Valor |
|---|---|
| Corpo de texto | 0 |
| Títulos grandes (36 px+) | -0.02em a -0.04em |
| CAPS / labels | +0.05em a +0.1em |
| Badges, tags pequenas | +0.03em a +0.06em |

A aula só fala em abrir; apertar títulos grandes fica fora dela.

## Key Sources

- [[wiki/sources/tipografia-negrito-italico-tracking-kerning-maiusculas]] — definição; maiúsculas, menus e botões; letter-spacing em em
