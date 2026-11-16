---
type: concept
title: "Escala tipográfica"
aliases: ["type scale", "escala de fontes", "escala de tamanho de fonte", "modular scale", "escala modular", "escala do Figma"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [ui, ui-design, tipografia, escala-tipografica, consistencia, design-tokens, style-guide]
skill: ux-ui-mentor
status: stub
---

# Escala tipográfica

Conjunto fechado de tamanhos de fonte que um projeto usa para títulos, subtítulos e corpo, em vez de escolher cada tamanho na hora. Parte da [[wiki/concepts/tipografia]]; é o equivalente textual da [[wiki/concepts/escala-de-espacamento]].

## Para que serve

Para [[wiki/concepts/consistencia-visual|consistência]]: a escala é "muito comum [...] em style guides" e responde à dúvida de quem começa, "quais são os tamanhos dos títulos, dos subtítulos" ([[wiki/sources/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma]]).

## Como montar (segundo a aula)

- **Partir da [[wiki/concepts/legibilidade-e-leiturabilidade|legibilidade]]:** corpo de texto entre 14 e 21 px como regra geral.
- **Tamanho versus espaço:** muito conteúdo puxa tudo para baixo (NYT: corpo de 14 px); pouco conteúdo permite exagerar (Framer: 106/32 px; Apple: 80/28 px).
- **Desktop e mobile:** uma escala para cada, como no style guide do [[wiki/entities/nubank]] em produção. Ver [[wiki/concepts/design-responsivo]].
- **Até 6 degraus, na prática 4:** espelhando h1–h6 do HTML. Ele usa h1 enorme no hero, h2 de 48, um título de 36, outro de 18 e corpo de 16.
- **Diferenças significativas:** os passos crescem com o tamanho (96 → 144 → 288 na escala do [[wiki/entities/figma]]), porque 144 e 160 lado a lado mal se distinguem. Ver [[wiki/concepts/contraste]].
- **A lista dele:** 14, 16, 18, 24, 36, 48, 52, 64, 72, 84, 96, misturando a escala do Figma com a [[wiki/concepts/grid-de-8-pontos|regra dos 8pt]].

## Escala modular

`[skill: ux-ui-mentor]` A versão sistemática é escolher uma razão e multiplicar: 1.125 (Major Second, compacta), 1.25 (Major Third, a mais comum em UI), 1.333 (Perfect Fourth, editorial), 1.5 (Perfect Fifth, display). Ferramenta: typescale.com. Para tipografia fluida, `clamp()` e utopia.fyi eliminam breakpoints por tamanho. A escala da aula não tem razão fixa: é escolhida à mão, como a escala híbrida de espaçamento.

## Olhar de dev

`[skill: ux-ui-mentor]` A escala vira token (`fontSize.sm = 0.875rem`, `base = 1rem`...) e o nível do heading (h1–h6) fica separado do estilo visual. `[external]` O MDN desaconselha usar headings para redimensionar texto: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements.

## Key Sources

- [[wiki/sources/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma]] — 14–21 px, tamanho vs. espaço, até 6 variações, escala do Figma + 8pt
