---
type: source
title: "Altura de linha e largura do texto (módulo de tipografia, edição \"W7\")"
aliases: ["altura de linha e largura do texto", "line-height e largura do texto", "aula 03 tipografia FrontPUSH", "Altura de Linha & Largura de texto"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 0
tags: [ui, ui-design, design, tipografia, line-height, altura-de-linha, largura-do-texto, medida-de-linha, leiturabilidade, whatfont, css, figma]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/altura-de-linha-e-largura-do-texto.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-15
---

# Altura de linha e largura do texto (módulo de tipografia, edição "W7")

## TL;DR

Aula 03 do módulo de [[wiki/concepts/tipografia]] (cerca de 6,5 min), a primeira desse módulo na wiki. As duas propriedades têm o mesmo objetivo: "deixar mais confortável ao ler". **[[wiki/concepts/altura-de-linha|Altura de linha]]** (line-height) é "a caixa que circunda o texto" e depende da escala: **140% a 160% para corpo de texto**, títulos bem mais baixos (o slide diz 90% a 120%; na fala, "110, 100%"); "quanto menor o texto, maior a altura de linha". Para conferir em sites de referência, o [[wiki/entities/whatfont]] mostra o line-height em px, e basta dividir pelo tamanho da fonte (64 / 56 = 1.14 num título; 28 / 20 = 1,4 e 32 / 20 = 1,6 no corpo). **[[wiki/concepts/largura-do-texto|Largura do texto]]**: **60 a 90 caracteres** ou **9 a 15 palavras por linha**, como "coringa". Muito longo cansa ([[wiki/entities/wikipedia]]); curto acelera a leitura de propósito (a coluna estreita da Globo ao lado de uma publicidade); o [[wiki/entities/new-york-times]] limita a coluna com um container e quebra o texto em parágrafos. A próxima etapa leva tudo para o guia de estilos no [[wiki/entities/figma]] e no CSS.

## Key Claims

### Objetivo comum: conforto de leitura

- **Altura de linha e largura servem ao mesmo fim:** "deixar mais confortável ao ler". A escala e o tamanho (aula anterior, não ingerida) "complementam": uma escala "muito grande" numa "tela muito pequena" fica "muito ruim". Ver [[wiki/concepts/design-responsivo]].

### Altura de linha

- **Definição:** "meio que é a caixinha, é a caixa que circunda o texto"; ao aumentar o line-height no Figma, a caixa do texto cresce. Ver [[wiki/concepts/altura-de-linha]].
- **Depende da escala:** "fórmula coringa" de "por volta de 140% do tamanho do texto"; "de 140% a 160% para corpo de texto".
- **Regra inversa:** "quanto menor o texto, maior a altura de linha". Corpo (escala menor) tem line-height maior; títulos (escala maior), menor.
- **Demonstração:** um texto com line-height de 172 fica bom quando baixa para "próximo de 150, 140"; um título fica bom em "110, 100%" e "estranho" com 140. Ver [[wiki/concepts/hierarquia-visual]].
- **Slide:** "140% a 160% para corpo de texto"; "90% a 120% para títulos".
- **Conferir na prática com o WhatFont:** o plugin mostra o line-height em px ("64, não está em porcentagem"); "a gente pode vir aqui e dividir um pelo outro, é a relação entre eles". Título: 64 / 56 = 1.14, "14% a mais"; corpo: 28 / 20 = 1,4; texto menor: 32 / 20 = 1,6. Ver [[wiki/entities/whatfont]].

### Largura do texto

- **Boas práticas:** "de 60 a 90 caracteres por linha" e, em palavras, "de 9 a 15 palavras por linha". "Existem sites que são menores [...] maiores que isso, mas isso aqui é um bom coringa". Ver [[wiki/concepts/largura-do-texto]].
- **Exemplo do slide:** o texto de exemplo tinha 8 palavras por linha ("um pouco abaixo"); alargado para 10, "seria o ideal". Na fala ele diz "10 caracteres por linha", mas contava palavras.
- **Comprimento muda a velocidade:** "quanto mais curto, mais rápida a leitura"; "muito longo dificulta a leitura e muito curto deixa a leitura mais rápida".
- **Globo:** com "uma imagem aqui do lado, uma publicidade", a coluna tem 4 a 6 palavras por linha; "meio que é de propósito, porque você tem um resumão e define se você quer continuar lendo".
- **Wikipedia como contraexemplo:** "não considero um site muito bom para leitura, ele te cansa um pouco rápido", apesar das "muitas referências boas". O problema é "o tamanho da largura de texto". Ver [[wiki/entities/wikipedia]].
- **New York Times:** "sempre faz aqui um container para poder não permitir que fique de ponta a ponta o texto"; e separa em parágrafos, "ele não faz o texto corridão". Ver [[wiki/concepts/espaco-em-branco]].

### Próximo passo

- **Guia de estilos:** os conceitos vão "lá para os guias de estilo" para "criar nossos estilos tanto no Figma como no CSS". Ver [[wiki/entities/frontpush]].

## Entities

- [[wiki/entities/nasser]]: autor (confirmado pelo usuário em 2026-11-15; o nome não é dito na aula). Indícios que já apontavam: o slide anexado tem o logo "W7" das aulas de ícones, botões e formas, confirmadas como dele pelo usuário; o arquivo está na pasta `FrontPush`.
- [[wiki/entities/whatfont]] (novo): plugin de navegador usado para ler o line-height de sites.
- [[wiki/entities/wikipedia]] (novo): contraexemplo de largura de texto.
- [[wiki/entities/new-york-times]]: coluna limitada por container e texto em parágrafos.
- [[wiki/entities/figma]]: onde ele altera o line-height; destino do guia de estilos.
- [[wiki/entities/frontpush]]: curso de onde vem a aula (pasta da transcrição).
- Sem página própria: Globo (site de notícias).

## Concepts

- [[wiki/concepts/altura-de-linha]] (novo)
- [[wiki/concepts/largura-do-texto]] (novo)
- [[wiki/concepts/tipografia]]
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/espaco-em-branco]]
- [[wiki/concepts/design-responsivo]]
- [[wiki/concepts/porque-das-decisoes-de-design]]

## Tensões com a wiki

- **Títulos: 90–120% no slide, 100–110% na fala.** A fala cabe dentro da faixa do slide. `[skill: ux-ui-mentor]` A skill pede 1.1–1.2 para display, 1.2–1.3 para subtítulos, 1.5–1.6 para corpo e 1.6–1.8 para artigo longo. A faixa de corpo da aula (1.4–1.6) começa um pouco abaixo; o 90% do slide fica abaixo do mínimo da skill e pode cortar acentos e descendentes em PT-BR (inferência).
- **60–90 caracteres contra 45–75.** `[skill: ux-ui-mentor]` A skill recomenda 45–75 caracteres no corpo (`max-width: 65ch`). `[external]` A WCAG 2.1, critério 1.4.8 (AAA), pede no máximo 80 caracteres por linha e espaçamento de linha de pelo menos 1,5 em blocos de texto (https://www.w3.org/WAI/WCAG21/Understanding/visual-presentation.html). O teto de 90 da aula passa dos dois.
- **"Muito curto deixa a leitura mais rápida."** A aula trata linha curta como recurso (resumo da Globo). `[skill: ux-ui-mentor]` A skill vê o outro lado: linha muito curta "quebra o ritmo de leitura". As duas cabem: curta serve para escanear, não para texto longo (leitura conciliadora, não dita).
- **"Legibilidade".** O autor diz "melhor legibilidade" para a largura do NYT. `[skill: ux-ui-mentor]` A skill separa legibilidade (reconhecer caracteres, depende da fonte) de leiturabilidade (ler blocos: tamanho, entrelinha, contraste, medida). Altura de linha e largura são leiturabilidade.
- **Fecha uma pendência.** [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] adiou para "a aula de tipografia" o fato de a caixa de texto incluir o line-height. Esta aula define line-height justamente como essa caixa. Ver [[wiki/concepts/altura-de-linha]].
- **Em CSS, sem unidade.** `[external]` A razão que o autor calcula (1.14, 1.4, 1.6) é o valor sem unidade do `line-height`, o recomendado pela MDN por herdar como fator e não como px fixo (https://developer.mozilla.org/en-US/docs/Web/CSS/line-height). O 140% do Figma equivale a `line-height: 1.4`.

## Open Questions

- **Aulas 01 e 02 do módulo** (introdução e escala/tamanho) são citadas e ainda não foram ingeridas.
- **"Line-height de 172"**: 172% ou 172 px? Pelo contexto (comparado com 150 e 140), parece porcentagem.
- **"Deixei de 9 a 15"**: provável "disse"; mantido literal.
- **Qual site da Globo** (G1, ge?) não é dito.
- `date_published` vazio.

## Raw Quotes

> "Quanto menor o texto, maior a altura de linha, mais ou menos é essa regrinha que você tem que ter."

> "A gente pode vir aqui e dividir um pelo outro, é a relação entre eles."

> "Muito longo dificulta a leitura e muito curto deixa a leitura mais rápida."

## Ver também

- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] — caixa de texto inclui o line-height ao medir distâncias
- [[wiki/sources/como-aprender-ui]] — saber justificar escala e line-height
- [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]] — line-height do título já dá espaço até a descrição
