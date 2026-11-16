---
type: concept
title: "CSS (Cascading Style Sheets)"
aliases: ['CSS', 'folhas de estilo em cascata']
date_created: 2026-10-14
date_updated: 2026-11-15
source_count: 3
tags: [css, frontend, web, historia]
skill: tech-mentor-frontend
status: draft
---

# CSS (Cascading Style Sheets)

Linguagem **declarativa** que separa estilo de conteúdo: regras visuais aplicadas ao HTML, resolvidas em **cascata** (árvore de atributos de estilo). Surgiu ~1995–96; IE implementou melhor o primeiro CSS que a Netscape ([[wiki/concepts/guerra-dos-navegadores]]). CSS2/2.1: web fonts, i18n, posicionamento relativo/absoluto, migração de layouts de tabelas para elementos flutuantes; CSS3 (oficial em 2012 segundo o autor) trouxe media queries ([[wiki/concepts/design-responsivo]]). Pré-processadores: Sass/Less ([[wiki/concepts/transpilador]]); frameworks: [[wiki/entities/twitter-bootstrap]]. Ver [[wiki/concepts/cssom]], [[wiki/concepts/html-hipertexto]].

## CSS sobre SVG

Por ser código com tags, um [[wiki/concepts/formato-svg|SVG]] inline pode ter os caminhos estilizados e animados pelo CSS; para [[wiki/entities/nasser|Násser]], é daí que "a magia do Motion surgiu" ([[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]]). `[external]` Via `<img>` ou `background-image` o CSS da página não alcança os caminhos.

## CSS a partir do Figma

A aba inspect do [[wiki/entities/figma]] dá o CSS do elemento. background, box-shadow e border-radius servem; width, height, top e left dependem da arquitetura (flexbox, position). Os nomes do style guide seguem o CSS (`card-hover`), e a paleta vai para variáveis Sass ou CSS ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]). `[external]` A aula chama hover de pseudo-element; `:hover` é pseudo-classe (https://developer.mozilla.org/en-US/docs/Web/CSS/:hover).

## Tipografia no CSS

O módulo de tipografia do curso de UI fecha com as propriedades de texto no CSS: `font-family`, pesos (light, normal, bold), e o vínculo da fonte com `<link>` (preferido, "mais performático") ou `@import` ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]). Ver [[wiki/concepts/webfonts]].

## Propriedades tipográficas

Em [[wiki/sources/tipografia-negrito-italico-tracking-kerning-maiusculas]], o Inspect do [[wiki/entities/figma]] traduz o design em `letter-spacing` ([[wiki/concepts/tracking]]), `font-family`, `font-style` e `font-weight` ([[wiki/concepts/peso-tipografico]]). Peso usado no CSS sem ter sido carregado do Google Fonts ou Adobe Fonts vira estilo "falso".

## Alinhamento padrão

Em [[wiki/sources/alinhamento-e-espacamento-de-texto]], alinhar à esquerda é "o padrão do CSS": as tags de texto e de título já vêm assim. `[external]` Mais precisamente, o valor inicial de `text-align` é `start`, que segue a direção do idioma: https://developer.mozilla.org/en-US/docs/Web/CSS/text-align. Ver [[wiki/concepts/alinhamento-de-texto]].

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
- [[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]] — SVG é código com tags, então o CSS manipula seus caminhos (base do motion)
- [[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]] — CSS do inspect; nomes iguais ao CSS; hover é pseudo-classe
- [[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]] — tipografia: font-family, pesos, `<link>` x `@import`
- [[wiki/sources/tipografia-negrito-italico-tracking-kerning-maiusculas]] — letter-spacing, font-weight e estilo falso
- [[wiki/sources/alinhamento-e-espacamento-de-texto]] — text-align à esquerda como padrão (inicial `start`)
