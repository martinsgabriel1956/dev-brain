---
type: concept
title: "Webfonts"
aliases: ["fontes web", "carregar fonte no CSS", "font-family", "@import de fonte", "link de fonte", "font-weight", "@font-face"]
date_created: 2026-11-15
date_updated: 2026-11-16
source_count: 4
tags: [frontend, css, tipografia, google-fonts, performance, font-family, font-weight]
skill: ux-ui-mentor
status: stub
---

# Webfonts

Como uma fonte escolhida no design chega ao site. Na aula de abertura de [[wiki/concepts/tipografia]], o último bloco do módulo é "tipografia CSS": "como a gente literalmente aplica lá no CSS quais são as propriedades", "como é que eu vinculo" uma fonte como a Lato ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]).

## O fluxo da aula

1. No [[wiki/entities/google-fonts]], escolher a família e os estilos: "light, que é a mais fininha", normal, bold. Cada peso marcado é um arquivo a mais para baixar.
2. Vincular no HTML com `<link>` ou no CSS com `@import`. "Eu já adianto que é esse link aqui, deixa mais performático o seu site."
3. Aplicar com `font-family` e as outras propriedades de texto. Ver [[wiki/concepts/css]].

## Por que `<link>` ganha

`[external]` Um `@import` dentro de uma folha de estilo só é descoberto quando essa folha termina de baixar, e encadeia as requisições. O `<link>` no `<head>`, com `<link rel="preconnect">` para fonts.gstatic.com, começa antes. `font-display: swap` mostra o texto com a fonte de reserva enquanto a webfont carrega (https://web.dev/articles/font-best-practices).

## Pesos e pilha de fontes

- `[external]` Em `font-weight`, 400 é `normal` e 700 é `bold`; 300 costuma ser light e 900 black (https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight). Por isso o "Open Sans Bold 400" lido no WhatFont é contraditório.
- A pilha "Open Sans, Arial, Helvetica, Sans Serif" vista na aula é a lista de reserva: se a primeira não carregar, o navegador tenta a seguinte, até a genérica `sans-serif`.
- `[skill: ux-ui-mentor]` Em design system a família vira token (`fontFamily.display`, `fontFamily.body`, `fontFamily.mono`) ao lado de `fontWeight` 400/500/600/700.

## O fluxo no código

Em [[wiki/sources/principais-propriedades-css-color-background-font]], o mesmo fluxo vira código: "select style" no [[wiki/entities/google-fonts]], marcar regular e bold, colar o `<link>` no index "como se fosse um CSS" e aplicar `font-family` só no H1. "Download family" baixa o zip para instalar no computador, que não é o caminho do site. `[skill: tech-mentor-frontend]` Faltou `font-display` (`swap` ou `optional`) e `preconnect`, que evitam texto invisível e reduzem CLS.

## Na NLW #1 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] copia o `<link>` do embed do Google Fonts (Roboto 300 e 700) e junta a Ubuntu 700 no mesmo link para evitar "duas chamadas lá no servidor do Google". Um link errado (`family=Roboto` onde devia ser Ubuntu) fez os títulos caírem na fonte de reserva. `-webkit-font-smoothing: antialiased` no body; `[external]` só faz efeito no macOS (https://developer.mozilla.org/en-US/docs/Web/CSS/font-smooth).

## Na NLW #2, dia 1 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]], a Poppins vem por `<link>` do Google Fonts, mas "não é ainda o suficiente": falta a regra `font` no CSS, aplicada também a `input`, `button` e `textarea`.

## Key Sources

- [[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]: Google Fonts, pesos, `<link>` x `@import`, `font-family`
- [[wiki/sources/principais-propriedades-css-color-background-font]]: link no index, font-family no H1; download family só para instalar
- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: um `<link>` para duas famílias; smoothing
- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: NLW #2, dia 1: link não basta, falta a regra
