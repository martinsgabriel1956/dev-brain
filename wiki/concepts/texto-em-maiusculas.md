---
type: concept
title: "Texto em maiúsculas"
aliases: ["maiúsculas", "caixa alta", "uppercase", "all caps", "text-transform"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [ui, ui-design, tipografia, maiusculas, hierarquia-visual, botoes, acessibilidade]
skill: ux-ui-mentor
status: stub
---

# Texto em maiúsculas

Texto todo em caixa alta como recurso de [[wiki/concepts/hierarquia-visual]] e de [[wiki/concepts/contraste]]. Parte de [[wiki/concepts/tipografia]].

## Sobe a hierarquia sem mudar o tamanho

Em [[wiki/sources/tipografia-negrito-italico-tracking-kerning-maiusculas]], [[wiki/entities/nasser|Násser]] põe o mesmo texto em 16 px, normal e em maiúsculas, no [[wiki/entities/figma]]: a versão em maiúsculas "já causa uma hierarquia maior". Uso: [[wiki/concepts/botoes-em-interfaces|botões]], call to action e links, quase sempre com [[wiki/concepts/tracking]] aberto "para poder melhorar a legibilidade e definir estilo".

`[external]` O efeito vem da altura: toda letra maiúscula ocupa a altura das capitulares, maior que a altura-x das minúsculas.

## Cuidados

`[skill: ux-ui-mentor]` Caixa alta é para labels e categorias curtas, com tracking aberto; em blocos longos cansa a leitura. `[external]` Escrever normal no HTML e usar `text-transform: uppercase` no CSS mantém o texto original para leitores de tela e buscas (confiança média).

## Key Sources

- [[wiki/sources/tipografia-negrito-italico-tracking-kerning-maiusculas]] — mesmo tamanho, mais hierarquia; botões, CTAs e links; junto com tracking
