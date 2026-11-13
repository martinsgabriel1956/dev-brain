---
type: concept
title: "CSS (Cascading Style Sheets)"
aliases: ['CSS', 'folhas de estilo em cascata']
date_created: 2026-10-14
date_updated: 2026-11-13
source_count: 2
tags: [css, frontend, web, historia]
skill: tech-mentor-frontend
status: draft
---

# CSS (Cascading Style Sheets)

Linguagem **declarativa** que separa estilo de conteúdo: regras visuais aplicadas ao HTML, resolvidas em **cascata** (árvore de atributos de estilo). Surgiu ~1995–96; IE implementou melhor o primeiro CSS que a Netscape ([[wiki/concepts/guerra-dos-navegadores]]). CSS2/2.1: web fonts, i18n, posicionamento relativo/absoluto, migração de layouts de tabelas para elementos flutuantes; CSS3 (oficial em 2012 segundo o autor) trouxe media queries ([[wiki/concepts/design-responsivo]]). Pré-processadores: Sass/Less ([[wiki/concepts/transpilador]]); frameworks: [[wiki/entities/twitter-bootstrap]]. Ver [[wiki/concepts/cssom]], [[wiki/concepts/html-hipertexto]].

## CSS sobre SVG

Por ser código com tags, um [[wiki/concepts/formato-svg|SVG]] inline pode ter os caminhos estilizados e animados pelo CSS; para [[wiki/entities/nasser|Násser]], é daí que "a magia do Motion surgiu" ([[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]]). `[external]` Via `<img>` ou `background-image` o CSS da página não alcança os caminhos.

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
- [[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]] — SVG é código com tags, então o CSS manipula seus caminhos (base do motion)
