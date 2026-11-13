---
type: concept
title: "Operações booleanas em formas"
aliases: ["boolean operations", "operações booleanas", "subtrair forma", "subtract", "modo de combinar", "union", "intersect", "exclude"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 2
tags: [ui, ui-design, figma, vetorial, formas, svg, ilustracoes]
skill: ux-ui-mentor
status: stub
---

# Operações booleanas em formas

Combinar duas ou mais formas vetoriais numa só: união, subtração, interseção e exclusão. É a base para desenhar ícones, ilustrações e mockups só com formas simples, que depois saem como caminhos de um [[wiki/concepts/formato-svg|SVG]].

## Na prática

[[wiki/entities/nasser|Násser]] recorta o notch de um mockup de iPhone no [[wiki/entities/figma]]: seleciona os dois retângulos com Shift e, "no modo de combinar", escolhe subtrair ("tem como subtrair, pegar interseção") ([[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]]). É o argumento da aula: se toda ilustração é um conjunto de formas, dá para construir a sua ([[wiki/concepts/ilustracoes-em-interfaces]]).

`[external]` No Figma (https://help.figma.com/hc/en-us/articles/360039957534-Boolean-operations):

| Operação | O que faz | Propriedades vêm de |
|---|---|---|
| Union | junta as camadas pelo contorno externo | — |
| Subtract | tira das de baixo as áreas das de cima (Alt Shift S) | camada de baixo |
| Intersect | mantém só a área onde todas se sobrepõem | — |
| Exclude | mantém só as áreas que não se sobrepõem (Alt Shift E) | camada de cima |

São **não destrutivas**: as camadas continuam editáveis dentro do grupo booleano. Não se aplicam a frames nem sections. O Shape builder é a alternativa destrutiva.

## Relacionado

- [[wiki/concepts/logica-booleana]] — a mesma álgebra (OU, E, E-NÃO, OU exclusivo) aplicada a áreas

## União no ícone de telefone

O fundo do "app telefone" de [[wiki/entities/nasser|Násser]] é "uma união de outros vetores"; o telefone em si não sai de formas simples e é traçado com a [[wiki/concepts/vetorizacao-com-pen-tool|Pen Tool]] ([[wiki/sources/imagens-e-ilustracoes-vetorizar-icones-figma-pen-tool-bend-tool]]).

## Key Sources

- [[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]] — subtração para recortar o notch do mockup de iPhone
- [[wiki/sources/imagens-e-ilustracoes-vetorizar-icones-figma-pen-tool-bend-tool]] — fundo do ícone como união de vetores; o que não sai de formas vai para a Pen Tool
