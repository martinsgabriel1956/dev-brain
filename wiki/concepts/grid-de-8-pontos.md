---
type: concept
title: "Grid de 8 Pontos"
aliases: ["8pt grid", "8-point grid", "grid de oito pontos", "escala de espaçamento", "spacing scale"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 3
tags: [ui, ui-design, layout, espacamento, grid, consistencia, design-tokens]
skill: ux-ui-mentor
status: stub
---

# Grid de 8 Pontos

Escala de "bons números" múltiplos de 8 usada para espaçamentos e tamanhos (altura de botão, distância entre elementos, tamanho de logo). Serve ao princípio da [[wiki/concepts/consistencia-visual|consistência]]: escolher uma escala e usá-la em toda a interface ([[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]]).

## A escala da aula

- Fala: 16, 32, 40, 48, 56, 64, 72, 80, 88, 96 "e por aí vai".
- Slide: 2, 4, 8, 16, 18, 24, 28, 32, 36, 40, 48, 56, 64, 72, 80, 88, 96.
- **Bom senso acima da regra.** 18 vale como meio-termo entre 16 e 24; 28 e 36 também. "Eu não posso generalizar que eu só vou utilizar múltiplos de oito."

Exemplos aplicados no [[wiki/concepts/wireframe]] da aula: logo de 72 × 72; 4 a 8 px entre título e descrição (a altura de linha do título já dá espaço); 40 ou 48 entre o texto e o call to action.

## Como escolher o valor

O valor segue o significado do vão: pequeno entre coisas conectadas, grande entre coisas diferentes. É a [[wiki/concepts/lei-da-proximidade-gestalt]] com números fixos; ver [[wiki/concepts/espaco-em-branco]].

`[skill: ux-ui-mentor]` Escala de referência: 4 (ícone e texto), 8 (inline), 16 (padding de card, entre campos), 24 (entre cards), 32 (entre blocos), 48 (entre seções), 64 (hero). Por que 8: divide por 2 e 4 em inteiros e se alinha com a maioria das densidades de tela. **4 px como sub-grid** para ajustes finos e line-height; isso explica 28 e 36 da lista da aula, mas não 18.

`[skill: ux-ui-mentor]` Na implementação, a escala vira design tokens (`--space-1: 4px`, `--space-2: 8px`...) para que ninguém digite 13 px à mão. Checklist: todo espaçamento é múltiplo de 4 ou 8?

## Relação com outros conceitos

- [[wiki/concepts/consistencia-visual]] — o grid é consistência aplicada a medidas.
- [[wiki/concepts/hierarquia-visual]] — vãos de tamanhos diferentes ordenam a leitura.
- [[wiki/concepts/elementos-da-interface]] — o espaçamento é o primeiro elemento do módulo.

## Linear ou geométrica

O grid de 8 da aula de whitespace é, na prática, uma escala **linear** (passo 8). Na aula de espaçamento e linhas, o autor prefere a **geométrica** (2, 4, 8, 16, 32, 64), em que a diferença entre valores altos se nota mais ([[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]]). A skill usa uma escala híbrida (4, 8, 16, 24, 32, 48, 64). Ver [[wiki/concepts/escala-de-espacamento]].

## Na ferramenta

Em [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]], o grid vira atalho: big nudge de 8 no [[wiki/entities/figma]] faz cada Shift + seta andar 8, e os vãos da aula (16, 32, 128) saem de dois, quatro e dezesseis toques. As colunas de 72 e o gutter de 32 do [[wiki/concepts/grid-de-colunas]] também são múltiplos de 8.

## Key Sources

- [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]]
- [[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]] — escala geométrica preferida à linear de passo 8
- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] — big nudge de 8 no Figma; colunas e gutter múltiplos de 8
