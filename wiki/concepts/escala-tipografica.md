---
type: concept
title: "Escala tipográfica"
aliases: ["escala de texto", "escala de fontes", "escala de tamanho de fonte", "type scale", "tamanho de fonte", "font-size", "modular scale", "escala modular", "escala do Figma"]
date_created: 2026-11-15
date_updated: 2026-11-19
source_count: 8
tags: [ui, ui-design, tipografia, escala-tipografica, font-size, hierarquia-visual, consistencia, design-tokens, style-guide]
skill: ux-ui-mentor
status: stub
---

# Escala tipográfica

Conjunto fechado de tamanhos de fonte que um projeto usa para títulos, subtítulos e corpo, em vez de escolher cada tamanho na hora. É a primeira das variáveis tipográficas: na aula de abertura de [[wiki/concepts/tipografia]], "literalmente escala é o tamanho, é o tamanho do texto", a resposta a "que tamanho eu coloco no título, [...] no subtítulo, [...] no corpo de texto" ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]).

No CSS é o `font-size`; o WhatFont mostra como "size" ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]). É o equivalente textual da [[wiki/concepts/escala-de-espacamento]]: poucos valores, escolhidos de antemão.

## O problema: inconsistência

O erro que [[wiki/entities/nasser|Násser]] diz ver em "muitas interfaces": elementos "da mesma hierarquia" com tamanhos diferentes, e destaques em cores diferentes que não batem com o tamanho. A escala existe para que o mesmo nível tenha sempre o mesmo tamanho ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]). Ver [[wiki/concepts/consistencia-visual]] e [[wiki/concepts/hierarquia-visual]].

A escala é "muito comum [...] em style guides" e responde à dúvida de quem começa, "quais são os tamanhos dos títulos, dos subtítulos" ([[wiki/sources/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma]]).

## Como montar (segundo a aula de escala)

Em [[wiki/sources/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma]]:

- **Partir da [[wiki/concepts/legibilidade-e-leiturabilidade|legibilidade]]:** corpo de texto entre 14 e 21 px como regra geral.
- **Tamanho versus espaço:** muito conteúdo puxa tudo para baixo (NYT: corpo de 14 px); pouco conteúdo permite exagerar (Framer: 106/32 px; Apple: 80/28 px).
- **Desktop e mobile:** uma escala para cada, como no style guide do [[wiki/entities/nubank]] em produção. Ver [[wiki/concepts/design-responsivo]].
- **Até 6 degraus, na prática 4:** espelhando h1–h6 do HTML. Ele usa h1 enorme no hero, h2 de 48, um título de 36, outro de 18 e corpo de 16.
- **Diferenças significativas:** os passos crescem com o tamanho (96 → 144 → 288 na escala do [[wiki/entities/figma]]), porque 144 e 160 lado a lado mal se distinguem. Ver [[wiki/concepts/contraste]].
- **A lista dele:** 14, 16, 18, 24, 36, 48, 52, 64, 72, 84, 96, misturando a escala do Figma com a [[wiki/concepts/grid-de-8-pontos|regra dos 8pt]].

## Escala modular

`[skill: ux-ui-mentor]` A versão sistemática é escolher uma razão e multiplicar em série: 1.125 (Major Second, compacta), 1.25 (Major Third, a mais comum em UI), 1.333 (Perfect Fourth, editorial), 1.5 (Perfect Fifth, display). Ferramentas: typescale.com e utopia.fyi. Para tipografia fluida, `clamp()` (por exemplo `clamp(2rem, 5vw, 4rem)`) e utopia.fyi eliminam breakpoints por tamanho.

A escala da aula não tem razão fixa: é escolhida à mão, como a escala híbrida de espaçamento.

## Aula x skill: o piso do corpo

`[skill: ux-ui-mentor]` Escala mínima de produto: 12 / 14 / 16 (corpo, nunca abaixo) / 18 / 20 / 24 / 30 / 36 / 48 px.

As duas divergem no piso: a aula aceita corpo a partir de 14 px (e cita o corpo de 14 px do NYT), enquanto a skill não desce o corpo abaixo de 16 px ([[wiki/sources/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma]]).

## Olhar de dev

`[skill: ux-ui-mentor]` A escala vira token (`fontSize.sm = 0.875rem`, `fontSize.base = 1rem`...) e o nível do heading (h1–h6) fica separado do estilo visual. `[external]` O MDN desaconselha usar headings para redimensionar texto: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements.

## h1–h6 não são a escala

Em [[wiki/sources/frontpush-o-que-e-html-linguagem-de-marcacao-tags-semantica]], [[wiki/entities/nasser|Násser]] chama `h1`–`h6` de "meio que [...] uma escala tipográfica" (`h1` o maior, `h6` o menor). `[external]` Os níveis marcam a hierarquia do documento; o tamanho vem da folha padrão do navegador e se ajusta no CSS. O MDN pede para não escolher o nível pelo tamanho: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements#usage_notes. A escala desta página se aplica com `font-size`, independente da tag.

## Escala em variáveis (FrontPUSH, Sass)

Em [[wiki/sources/frontpush-variaveis-sass]]: os tamanhos de H1–H3 e B1–B3 do style guide "são todos padronizados", então "eu consigo estabelecer isso mais facilmente por meio de variáveis".

## Escala por breakpoint (FrontPUSH, Sass aula 06)

Em [[wiki/sources/frontpush-mixin-e-content-sass]], "adeque o tamanho da tipografia ao tamanho da tela [...] um básico de UI Design alinhado à responsividade": `h1` 72/48/36 px e corpo 24/18/16 px. `[external]` Alternativa contínua: `font-size: clamp(2.25rem, 1.5rem + 3vw, 4.5rem)`, em `rem` para respeitar a fonte do usuário.

## Escala num mixin com @if (FrontPUSH, projeto Nubank)

Em [[wiki/sources/frontpush-if-else-sass]]: dois mixins (`typeface-1` para títulos em Sora, `typeface-2` para texto em Source Sans Pro) recebem tamanho `h1`–`h5` e dispositivo, e definem `font-size` e `line-height`. "Basta eu modificar alguma coisa aqui que automaticamente toda a minha estrutura textual vai ser modificada." `[skill: tech-mentor-frontend]` Um mapa de tokens faria o mesmo sem a cadeia de `@if`.

## Razão áurea numa função (FrontPUSH, Sass)

Em [[wiki/sources/frontpush-for-while-each-sass]], o exemplo da documentação: `scale-below($value, $base, $ratio: 1.618)` divide pela razão áurea até ficar abaixo da base; `scale-below(20px, 16px)` = 12.36px. Uma escala modular calculada pelo compilador.

## Mínimo de 16 px (FrontPUSH, otimização aula 05)

Em [[wiki/sources/frontpush-google-pagespeed-core-web-vitals-acessibilidade-meta-tags]]: "no mínimo 14 pixels", e "eu sempre coloco no mínimo de 16 pixels" no mobile. 16 px é o padrão do navegador e evita o zoom automático do iOS em inputs.

## Key Sources

- [[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]: escala = tamanho; inconsistência como erro comum; WhatFont
- [[wiki/sources/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma]]: 14–21 px, tamanho vs. espaço, até 6 variações, escala do Figma + 8pt
- [[wiki/sources/frontpush-o-que-e-html-linguagem-de-marcacao-tags-semantica]]: h1–h6 chamados de escala tipográfica (são hierarquia, não tamanho)
- [[wiki/sources/frontpush-variaveis-sass]]: H1–H3 e B1–B3 em variáveis
- [[wiki/sources/frontpush-mixin-e-content-sass]]: Sass aula 06: tamanhos por breakpoint × `clamp()`
- [[wiki/sources/frontpush-if-else-sass]]: escala h1–h5 × desktop/mobile num mixin
- [[wiki/sources/frontpush-for-while-each-sass]]: razão 1.618 numa `@function`
- [[wiki/sources/frontpush-google-pagespeed-core-web-vitals-acessibilidade-meta-tags]]: FrontPUSH, otimização aula 05: fonte mínima
