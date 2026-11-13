---
type: concept
title: "Vetorização com a Pen Tool"
aliases: ["pen tool", "ferramenta caneta", "vetorizar imagem", "vetorização manual", "bend tool", "curvas de bézier", "bezier handles", "alças de bézier", "tracing"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 2
tags: [ui, ui-design, figma, vetorial, svg, pen-tool, bezier, icones, ilustracoes]
skill: ux-ui-mentor
status: stub
---

# Vetorização com a Pen Tool

Redesenhar à mão, como caminho vetorial, uma imagem raster (ícone, logo, objeto) colocada por baixo como referência. O resultado é um vetor editável e exportável em [[wiki/concepts/formato-svg|SVG]].

## Processo de Násser

Em [[wiki/sources/imagens-e-ilustracoes-vetorizar-icones-figma-pen-tool-bend-tool]], no [[wiki/entities/figma]]:

1. **Referência:** colar a imagem do ícone, com zoom alto.
2. **Pen Tool:** clicar onde o trecho reto termina e onde a curvatura muda; o mínimo de pontos possível, simétrico dos dois lados.
3. **Bend Tool:** com o caminho fechado, arredondar os pontos; baixar a opacidade para ver a referência.
4. **Refino:** duplo clique no elemento, clique no ponto, ajustar as duas alças até a curva ficar contínua ("você não perceber que ali tem um ponto de descontinuidade").
5. **Aplicar efeitos e exportar** em SVG.

Regra de ouro: "quanto menos pontos melhor"; com muito ponto, "dá muito trabalho".

O mesmo recurso serve para refazer logo de cliente recebido em baixa definição ([[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]]).

## Como funciona no Figma

`[external]` A Bend Tool adiciona alças de Bézier a um ponto ou trecho do caminho; as alças definem comprimento e inclinação da curva. Para entrar no modo de edição de vetor: selecionar a camada e Enter. O espelhamento das alças pode ser nenhum, só ângulo, ou ângulo e comprimento; com o ângulo espelhado a curva fica suave no ponto (https://help.figma.com/hc/en-us/articles/360039957634-Edit-vector-layers). Depois de traçado, "Simplify a vector path" reduz pontos (https://help.figma.com/hc/en-us/articles/33792593975575-Simplify-a-vector-path).

## Olhar de dev

`[external]` Menos pontos = `d` do `<path>` mais curto: SVG mais leve e mais fácil de animar (morph entre formas exige caminhos com estrutura parecida). Ver [[wiki/concepts/otimizacao-de-imagens]].

## Relacionado

- [[wiki/concepts/operacoes-booleanas-em-formas]] — a outra forma de construir: combinar formas simples
- [[wiki/concepts/icones-em-interfaces]], [[wiki/concepts/ilustracoes-em-interfaces]]
- [[wiki/concepts/simetria-visual]]

## Key Sources

- [[wiki/sources/imagens-e-ilustracoes-vetorizar-icones-figma-pen-tool-bend-tool]] — passo a passo com o ícone de telefone: Pen Tool, Bend Tool, alças
- [[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]] — vetorizar logo de cliente em baixa definição
