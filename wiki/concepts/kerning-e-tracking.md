---
type: concept
title: "Kerning e tracking"
aliases: ["kerning", "tracking", "letter-spacing", "espaçamento entre letras", "font-kerning"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 2
tags: [ui, ui-design, tipografia, kerning, tracking, letter-spacing, branding, css]
skill: ux-ui-mentor
status: stub
---

# Kerning e tracking

Duas variáveis tipográficas sobre o espaço entre letras, listadas juntas no roteiro do módulo de [[wiki/concepts/tipografia]] ("Alinhamento, tracking e kerning").

## O que a aula diz

"Kerning é literalmente o espaçamento entre as letras." [[wiki/entities/nasser|Násser]] digita "teste" na ferramenta de texto, abre e fecha o espaçamento e cita o logo da Tesla, "bem espaçada". É um recurso "para criar branding, para criar coisa de logo", que "traz uma ideia também por trás" ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]).

## A distinção padrão

`[external]` **Tracking** é o espaçamento uniforme de um trecho inteiro, no CSS `letter-spacing` (https://developer.mozilla.org/en-US/docs/Web/CSS/letter-spacing). **Kerning** é o ajuste entre pares específicos de letras (AV, To, Wa), que vem nas tabelas da fonte e o CSS liga ou desliga com `font-kerning` (https://developer.mozilla.org/en-US/docs/Web/CSS/font-kerning). O que a aula descreve, e o logo da Tesla, é tracking. Confiança alta.

`[skill: ux-ui-mentor]` Valores de referência para tracking: corpo 0 ("nunca mexa"); títulos de 36 px ou mais, -0.02em a -0.04em; texto em CAPS e labels, +0.05em a +0.1em. "Texto grande, apertar; texto pequeno em caps, abrir."

## Espaçamento como identidade

Na aula de formas de botões, o site de arquitetura usa título "com maior espaçamento entre letras" junto de letras sem serifa, "buscando o minimalismo" ([[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]]). Mesmo uso do logo da Tesla: tracking aberto como sinal de marca.

`[external]` A WCAG 1.4.12 exige que o conteúdo aguente `letter-spacing` de 0.12em sem quebrar (https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html).

## Key Sources

- [[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]: "kerning é o espaçamento entre as letras"; logo da Tesla
- [[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]]: título espaçado do site de arquitetura
