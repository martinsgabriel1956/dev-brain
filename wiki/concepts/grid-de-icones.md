---
type: concept
title: "Grid de ícones"
aliases: ["icon grid", "keyline", "keyline shapes", "grid de construção de ícones", "área útil do ícone", "live area", "grid-icon"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 5
tags: [ui, ui-design, icones, iconografia, grid, figma, consistencia, material-design]
skill: ux-ui-mentor
status: stub
---

# Grid de ícones

Formas-guia desenhadas dentro do frame do ícone (área útil, quadrado, círculo, X, círculo central) para que todos os ícones de uma [[wiki/concepts/familia-de-icones|família]] tenham o mesmo tamanho visual, a mesma margem e o mesmo centro. É a [[wiki/concepts/consistencia-visual]] e a [[wiki/concepts/simetria-visual]] aplicadas a [[wiki/concepts/icones-em-interfaces|ícones]].

## Material Design

`[external]` Frame de 24dp; conteúdo dentro da live area de 20dp×20dp, com 2dp de padding (pode invadir o padding "if additional visual weight is needed"); keyline shapes: quadrado 18dp, círculo 20dp, retângulo vertical 16×20, horizontal 20×16; ícones "on pixel" (https://m3.material.io/styles/icons/designing-icons). Ver [[wiki/entities/material-design]].

## O grid de Násser

Em [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]]:

1. Frame de 24×24 com retângulo de 20×20 (área útil) e linhas guia.
2. Quadrado com stroke em cinza, círculo (18×18, mais folgado que o Material, que ele acha "muito apertado"), X e um quadrado ou círculo no meio, "formas de a gente concentrar o ponto focal".
3. Desenhar dentro do círculo; ícone "em pé" (microfone) pode sobrar um pouco para cima e para baixo, mas centrado.
4. No [[wiki/entities/figma]]: Ctrl G, opacidade de 20–30%, travar o grupo; depois esconder o "grid-icon" e criar o componente.

## Regras que o grid sustenta

- Tamanhos pares, para centralizar sem meio pixel.
- Margem: não encostar o desenho na borda ([[wiki/concepts/espaco-em-branco]]).
- O centro "da matemática" nem sempre é o do olho: ver [[wiki/concepts/centralizacao-optica]].

## Mesma proporção entre ícones

Em [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]]: ao repetir a estrutura com outro ícone, "certifique-se que você está aumentando ele na mesma proporção que você aumentou o ícone passado". É o papel do grid feito à mão.

## Key Sources

- [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]] — área útil 20×20, grid com quadrado, círculo e X, travado no Figma
- [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]] — ícones do FrontPUSH seguem "à risca" o tamanho com relação ao grid
- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] — o mesmo princípio de réguas no layout: [[wiki/concepts/grid-de-colunas]]
- [[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia]] — alinhamento: cards homogeneízam ícones de proporções diferentes
- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]] — mesma escala entre ícones dentro dos círculos
