---
type: concept
title: "Espaçamento entre Parágrafos"
aliases: ["paragraph spacing", "espaço entre parágrafos", "quebra de parágrafo", "margin entre parágrafos", "enter clássico"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [ui, ui-design, tipografia, espacamento, espacamento-entre-paragrafos, line-height, legibilidade, consistencia]
skill: ux-ui-mentor
status: stub
---

# Espaçamento entre Parágrafos

Vão vertical entre blocos de texto. Junto com o tamanho do parágrafo, decide se um texto longo parece leve ou "pesado, cansativo" ([[wiki/sources/alinhamento-e-espacamento-de-texto]]).

## Regras da aula

- **Quebre a cada 4 a 8 linhas**, um assunto por parágrafo. Texto corrido "fica muito pesado".
- **Vão do tamanho do line-height**, "o clássico enter". Um pouco maior também serve (caso do G1).
- **Nunca grande a ponto de separar**: vão grande ou linha divisória "separa o conteúdo". É a [[wiki/concepts/lei-da-proximidade-gestalt]]: parágrafos de um mesmo texto têm de parecer um grupo. Ver [[wiki/concepts/espaco-em-branco]].
- **O mesmo vão no site inteiro** ([[wiki/concepts/consistencia-visual]]).
- Imagem ou vídeo no meio do texto pode ter vão maior que o de parágrafo.

## Olhar de dev

`[external]` Em CSS isso é `margin-block-end` (ou `margin-bottom`) no `p`, em `em` ou ligado ao line-height, por exemplo `p + p { margin-block-start: 1lh; }` onde a unidade `lh` tiver suporte. A WCAG 1.4.8 (AAA) pede vão de parágrafo de pelo menos 1,5 vez o espaço entre linhas, mais que a regra da aula: https://www.w3.org/WAI/WCAG21/Understanding/visual-presentation.html. A WCAG 1.4.12 (AA) exige que o layout aguente o usuário aumentar esse vão para 2 vezes o tamanho da fonte sem perder conteúdo: https://www.w3.org/WAI/WCAG21/Understanding/text-spacing.html.

Medir no Figma engana: a caixa de texto já inclui meia entrelinha acima e abaixo ([[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]]).

## Relação com outros conceitos

- [[wiki/concepts/tipografia]]: variável tipográfica, ao lado de line-height, largura e [[wiki/concepts/alinhamento-de-texto|alinhamento]].
- [[wiki/concepts/escala-de-espacamento]]: o vão de parágrafo deriva do line-height, não da escala de 8.
- [[wiki/concepts/densidade-de-informacao]]: parágrafos curtos e vãos regulares aliviam texto denso.

## Key Sources

- [[wiki/sources/alinhamento-e-espacamento-de-texto]] — 4 a 8 linhas por parágrafo; vão = line-height; não separar; consistência
