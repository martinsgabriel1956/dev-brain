---
type: concept
title: "Altura de linha (line-height)"
aliases: ["line-height", "entrelinha", "altura da linha", "leading"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [ui, ui-design, tipografia, line-height, leiturabilidade, css]
skill: ux-ui-mentor
status: stub
---

# Altura de linha (line-height)

Altura da "caixa que circunda o texto" ([[wiki/sources/altura-de-linha-e-largura-do-texto]]). Uma das duas propriedades de [[wiki/concepts/tipografia]] que, junto com a [[wiki/concepts/largura-do-texto]], servem para "deixar mais confortável ao ler".

## Faixas da aula

| Contexto | Aula (slide) | Aula (fala) | `[skill: ux-ui-mentor]` |
|---|---|---|---|
| Corpo de texto | 140% a 160% | "140 a 160", "por volta de 140%" | 1.5–1.6 (artigo longo 1.6–1.8) |
| Títulos | 90% a 120% | "110, 100%" | 1.1–1.2 (subtítulo 1.2–1.3) |

Regra: "quanto menor o texto, maior a altura de linha". Título com 140% fica "estranho". Ver [[wiki/concepts/hierarquia-visual]].

## Ler em px, pensar em razão

O [[wiki/entities/whatfont]] mostra o line-height em px. Para obter a razão, divida pelo tamanho da fonte: 64 / 56 = 1.14 (título), 28 / 20 = 1,4 e 32 / 20 = 1,6 (corpo). `[external]` Em CSS, esse número entra sem unidade (`line-height: 1.4`), o que a MDN recomenda porque herda como fator (https://developer.mozilla.org/en-US/docs/Web/CSS/line-height). `[external]` A WCAG 2.1, critério 1.4.8 (AAA), pede pelo menos 1,5 em blocos de texto (https://www.w3.org/WAI/WCAG21/Understanding/visual-presentation.html).

## A caixa engana a medição

Como a caixa inclui o line-height, medir a distância entre dois textos no [[wiki/entities/figma]] mostra mais do que o vão visível entre as letras (17 em vez de 16 em [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]]). Pelo mesmo motivo, o vão entre título e descrição pode ser só 4 a 8 px: "a altura de linha do título já dá espaço" ([[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]]). Ver [[wiki/concepts/espaco-em-branco]].

## Key Sources

- [[wiki/sources/altura-de-linha-e-largura-do-texto]] — definição, faixas por escala, cálculo da razão com o WhatFont
