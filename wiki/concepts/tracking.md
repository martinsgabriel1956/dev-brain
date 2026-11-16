---
type: concept
title: "Tracking"
aliases: ["letter-spacing", "espaçamento entre letras", "entreletra"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 3
tags: [ui, ui-design, tipografia, tracking, letter-spacing, legibilidade, branding, css]
skill: ux-ui-mentor
status: stub
---

# Tracking

Distância uniforme entre todas as letras de um trecho; no CSS, `letter-spacing` (`[external]` https://developer.mozilla.org/en-US/docs/Web/CSS/letter-spacing). Difere do [[wiki/concepts/kerning]], que ajusta um par específico. Parte de [[wiki/concepts/tipografia]].

Na aula de abertura do módulo, o tracking aparece com o nome de kerning: "Kerning é literalmente o espaçamento entre as letras" ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]). A confusão está detalhada em [[wiki/concepts/kerning]].

## Abrir em maiúsculas, menus e botões

Em [[wiki/sources/tipografia-negrito-italico-tracking-kerning-maiusculas]], [[wiki/entities/nasser|Násser]]: tracking "define maior legibilidade e estilo dependendo da fonte"; não é para tudo, mas texto todo em [[wiki/concepts/texto-em-maiusculas|maiúsculas]] pede "uma maior distância". Aparece em itens de menu e em [[wiki/concepts/botoes-em-interfaces|botões]], sobretudo CTAs; nos botões do site dele (provavelmente o [[wiki/entities/frontpush]]), maiúsculas + letter-spacing "para poder chamar mais atenção".

## Espaçamento como identidade

- **Logo da Tesla:** na aula de abertura, o espaçamento entre letras (chamado ali de kerning) é um recurso "para criar branding, para criar coisa de logo", que "traz uma ideia também por trás"; o logo da Tesla é "bem espaçada" ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]).
- **Site de arquitetura:** na aula de formas de botões, o título vem "com maior espaçamento entre letras" junto de letras sem serifa, "buscando o minimalismo" ([[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]]).

Nos dois casos, tracking aberto como sinal de marca.

## Figma e CSS

O tracking do [[wiki/entities/figma]] é o `letter-spacing` do [[wiki/concepts/css]]; o Inspect o mostra em `em`. A aula fala em "10% de 16 pixels". `[external]` `em` é relativo ao `font-size` do elemento, não fixo em 16 px; por isso o tracking em `em` acompanha o tamanho da fonte.

## Valores de referência

`[skill: ux-ui-mentor]`

| Uso | Valor |
|---|---|
| Corpo de texto | 0 ("nunca mexa") |
| Títulos grandes (36 px+) | -0.02em a -0.04em |
| CAPS / labels | +0.05em a +0.1em |
| Badges, tags pequenas | +0.03em a +0.06em |

"Texto grande, apertar; texto pequeno em caps, abrir." As aulas só falam em abrir; apertar títulos grandes fica fora delas.

`[external]` A WCAG 1.4.12 exige que o conteúdo aguente `letter-spacing` de 0.12em sem quebrar (https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html).

## Key Sources

- [[wiki/sources/tipografia-negrito-italico-tracking-kerning-maiusculas]]: definição; maiúsculas, menus e botões; letter-spacing em em
- [[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]: espaçamento entre letras chamado de kerning; logo da Tesla
- [[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]]: título espaçado do site de arquitetura
