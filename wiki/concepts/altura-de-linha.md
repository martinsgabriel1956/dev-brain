---
type: concept
title: "Altura de linha"
aliases: ["line-height", "entrelinha", "leading", "espaçamento entre linhas"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 2
tags: [ui, ui-design, tipografia, line-height, legibilidade, acessibilidade, css]
skill: ux-ui-mentor
status: stub
---

# Altura de linha

Variável tipográfica: a altura da caixa de cada linha de texto. Na aula de abertura de [[wiki/concepts/tipografia]], "a altura da caixinha azul de seleção aqui é a altura de linha". Ela é maior que o tamanho da fonte "para poder tornar a leitura mais confortável para o usuário ler" ([[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]).

## Título aperta, corpo abre

Nos títulos "uma caixa sobe na outra": a altura de linha de títulos "é menor do que a altura de linha de corpo de texto". O porquê fica para uma aula posterior.

`[skill: ux-ui-mentor]` Valores de referência: display 1.1–1.2; subtítulos 1.2–1.3; corpo 1.5–1.6; artigo longo 1.6–1.8; tabelas e labels 1.2–1.3. "Quanto maior o texto, menor a entrelinha."

`[external]` A WCAG 1.4.12 (AA) exige que o conteúdo continue funcionando se o usuário aumentar a entrelinha para 1.5 vez o tamanho da fonte (https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html). No CSS, prefira `line-height` sem unidade (`1.5`), que é herdado proporcionalmente.

## Line-height e medição no Figma

A caixa de texto inclui o espaço do line-height, então o Alt do [[wiki/entities/figma]] mede distâncias maiores do que parecem ([[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]]).

## Key Sources

- [[wiki/sources/tipografia-introducao-variaveis-classificacoes-css]]: a caixa azul da seleção; título com entrelinha menor
- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]]: line-height engana a medição de distâncias
