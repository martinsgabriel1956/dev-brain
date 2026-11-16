---
type: concept
title: "Estilos no Figma (color, text e effect styles)"
aliases: ["styles do Figma", "color styles", "text styles", "effect styles", "estilos de cor", "estilos de texto", "estilos de efeito", "create style", "edit style", "detach style"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [figma, style-guide, design-tokens, design-system, cor, tipografia, sombra, consistencia]
skill: ux-ui-mentor
status: stub
---

# Estilos no Figma (color, text e effect styles)

Um estilo guarda um valor com nome (uma cor, um conjunto de propriedades de texto, uma sombra) e o aplica a vários elementos. Editar o estilo muda todos os elementos de uma vez. É a forma de [[wiki/concepts/style-guide]] no [[wiki/entities/figma]] e o equivalente, no design, a uma variável de CSS.

## Por que usar

Sem estilo, mudar a cor de branding (`#F7931E`) obriga a "sair colando em tudo", e num "documento gigantesco" é "canseira". Com estilo, ganha-se **consistência**, "porque a gente está aplicando uma cor só", e facilidade de mudar "tanto de cor, como de tipografia, como de sombra" ([[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]]). Ver [[wiki/concepts/consistencia-visual]].

## Tipos e fluxo

| Tipo | O que guarda | Exemplo da aula |
|---|---|---|
| Color style | Fill ou stroke: sólido, linear, radial, angular, diamond, image | `Primary / Orange-1`, `-light`, `-dark` |
| Text style | Fonte, tamanho, peso, line-height | `Heads / H1` (Sora 48, line-height 110) |
| Effect style | Drop shadow, inner shadow, layer blur, background blur | `Shadow / Shadow purple 2` |

Fluxo: selecionar o elemento, ícone de estilos, "+", nome com grupo, **create style**. Depois: **edit style** muda o valor em todos os elementos; **add description** documenta o estilo; o ícone de "correntinha quebrando" desvincula (**detach**), e o elemento volta ao valor solto ([[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]]).

## Nomes: `Grupo / nome`

A barra cria o grupo. O padrão de [[wiki/entities/nasser]]: `Primary`, `Secondary` e `Black` com três tons cada (base, light, dark); `Heads` para títulos, com grupos desktop e mobile; `Shadow` para sombras. "Você pode criar os seus nomes do jeito que você quiser." Alternativas que ele cita: brand color, auxiliary color, white e black colors separados, neutral colors, gray colors ([[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]]). Ver [[wiki/concepts/cor-semantica]].

## Olhar de dev

- `[skill: ux-ui-mentor]` **Primitivo x semântico:** `Orange-1` descreve o valor; `brand-primary` descreve o papel. Separar as duas camadas (`brand-primary` aponta para `orange-500`) deixa trocar a cor sem renomear nada no código.
- `[skill: ux-ui-mentor]` **Pesos com nomes padrão:** 400 regular, 500 medium, 600 semibold, 700 bold. A aula chama 600 de "medium" ([[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]]), e o dev que lê o nome vai escrever 500.
- `[external]` **Variables:** desde 2023 o Figma tem variables com modos (light/dark) e aliases, mais próximas de design tokens que os color styles. Exportadas (por exemplo com Tokens Studio e Style Dictionary), viram CSS custom properties (https://help.figma.com/hc/en-us/articles/15339657135383, não reconsultado).

## Key Sources

- [[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]]: color, text e effect styles; grupos com barra; edit, description, detach
- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]]: cor de branding desconectada do estilo para mudar a opacidade
