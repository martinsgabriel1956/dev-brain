---
type: concept
title: "Altura de linha (line-height)"
aliases: ["line-height", "entrelinha", "leading", "altura da linha", "espaçamento entre linhas"]
date_created: 2026-11-15
date_updated: 2026-11-16
source_count: 5
tags: [ui, ui-design, tipografia, line-height, legibilidade, leiturabilidade, acessibilidade, css]
skill: ux-ui-mentor
status: stub
---

# Altura de linha (line-height)

Variável tipográfica: a altura da caixa de cada linha de texto, a "caixa que circunda o texto" ([[wiki/sources/altura-de-linha-e-largura-do-texto]]). Na aula de abertura de [[wiki/concepts/tipografia]], "a altura da caixinha azul de seleção aqui é a altura de linha"; ela é maior que o tamanho da fonte "para poder tornar a leitura mais confortável para o usuário ler" ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]).

É uma das duas propriedades que, junto com a [[wiki/concepts/largura-do-texto]], servem para "deixar mais confortável ao ler" ([[wiki/sources/altura-de-linha-e-largura-do-texto]]).

## Título aperta, corpo abre

Na aula de abertura, nos títulos "uma caixa sobe na outra": a altura de linha de títulos "é menor do que a altura de linha de corpo de texto". O porquê fica para uma aula posterior ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]).

Essa aula posterior dá a regra: "quanto menor o texto, maior a altura de linha". Título com 140% fica "estranho" ([[wiki/sources/altura-de-linha-e-largura-do-texto]]). Ver [[wiki/concepts/hierarquia-visual]].

## Faixas: aula x skill

A aula e a skill dão faixas diferentes, e dentro da aula o slide e a fala também não coincidem:

| Contexto | Aula (slide) | Aula (fala) | `[skill: ux-ui-mentor]` |
|---|---|---|---|
| Corpo de texto | 140% a 160% | "140 a 160", "por volta de 140%" | 1.5–1.6 (artigo longo 1.6–1.8) |
| Títulos | 90% a 120% | "110, 100%" | display 1.1–1.2 (subtítulo 1.2–1.3) |
| Tabelas e labels | — | — | 1.2–1.3 |

Colunas da aula: [[wiki/sources/altura-de-linha-e-largura-do-texto]]. O piso de corpo da aula (140%) fica abaixo do da skill (1.5). A skill resume: "quanto maior o texto, menor a entrelinha", a mesma regra dita ao contrário.

## Ler em px, pensar em razão

O [[wiki/entities/whatfont]] mostra o line-height em px. Para obter a razão, divida pelo tamanho da fonte: 64 / 56 = 1.14 (título), 28 / 20 = 1,4 e 32 / 20 = 1,6 (corpo) ([[wiki/sources/altura-de-linha-e-largura-do-texto]]).

`[external]` Em CSS, prefira `line-height` sem unidade (`line-height: 1.4`, `1.5`), que a MDN recomenda porque é herdado como fator, proporcionalmente (https://developer.mozilla.org/en-US/docs/Web/CSS/line-height).

## Acessibilidade

Dois critérios WCAG diferentes tocam no valor 1,5:

- `[external]` **1.4.12 Text Spacing (AA):** o conteúdo precisa continuar funcionando se o usuário aumentar a entrelinha para 1.5 vez o tamanho da fonte (https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html).
- `[external]` **1.4.8 Visual Presentation (AAA):** pede pelo menos 1,5 em blocos de texto (https://www.w3.org/WAI/WCAG21/Understanding/visual-presentation.html).

## A caixa engana a medição

A caixa de texto inclui o espaço do line-height, então o Alt do [[wiki/entities/figma]] mede distâncias maiores do que o vão visível entre as letras (17 em vez de 16 em [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]]). Pelo mesmo motivo, o vão entre título e descrição pode ser só 4 a 8 px: "a altura de linha do título já dá espaço" ([[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]]). Ver [[wiki/concepts/espaco-em-branco]].

## Na aula de CSS

Em [[wiki/sources/principais-propriedades-css-color-background-font]], `line-height` é "aquela propriedade que a gente vê em UI" para melhorar "a leitura, a legibilidade". A aula a descreve como "espaçamento de uma letra da outra, que é a altura da linha": a primeira metade descreve `letter-spacing` ([[wiki/concepts/tracking]]); a segunda é a correta.

## Key Sources

- [[wiki/sources/altura-de-linha-e-largura-do-texto]]: definição, faixas por escala, cálculo da razão com o WhatFont
- [[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]: a caixa azul da seleção; título com entrelinha menor
- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]]: line-height engana a medição de distâncias
- [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]]: vão de 4 a 8 px entre título e descrição
- [[wiki/sources/principais-propriedades-css-color-background-font]]: line-height descrito como espaço entre letras (confusão com letter-spacing)
