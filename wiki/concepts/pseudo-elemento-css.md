---
type: concept
title: "Pseudo-elemento CSS"
aliases: ["pseudo-elemento", "pseudo-element", "pseudo-elements", "::before", "::after", "::first-letter", "::first-line", "::placeholder"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 4
tags: [css, frontend, seletores-css, pseudo-elemento]
skill: tech-mentor-frontend
status: stub
---

# Pseudo-elemento CSS

Palavra-chave com **dois dois-pontos** (`::`) que estiliza uma **parte** de um elemento ou cria uma caixa que não existe no HTML: `::first-letter`, `::first-line`, `::before`, `::after`, `::placeholder`, `::selection`. `[external]` https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements

Na aula [[wiki/sources/seletores-e-pseudo-elements-css]], "pseudo-elements" é o nome de toda a lista, explicado como "um falso elemento [...] ou um estado dentro de um outro". Só `first-letter` ("a primeira letra") e `first-line` ("primeira linha") são pseudo-elementos; o resto (`:hover`, `:checked`, `:nth-child`) é [[wiki/concepts/pseudo-classe-css|pseudo-classe]]. A aula de style guide já chamava hover de pseudo-element ([[wiki/concepts/css]]).

`[external]` O placeholder de um input se estiliza com `::placeholder`, não com seletor de atributo (a aula sugere o atributo). A sintaxe antiga de um dois-pontos (`:first-line`) ainda funciona por compatibilidade com CSS2.

## Na NLW #1 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]]: "são elementos que não tem aqui no HTML, mas a gente vai criar ele através do CSS". `span::after` com `content: ""` vira um filho no DevTools; com `content: "blá blá"`, o texto aparece. Na página, o `::after` recebe o ícone de busca como `background-image` com 20x20.

## before e after "como se fosse duas divs" (FrontPUSH, aula 04)

Em [[wiki/sources/frontpush-seletores-css-filho-irmao-atributo-nth-child-pseudo-elements]], [[wiki/entities/nasser|Násser]] diz que usa `::after` e `::before` "demais": "como se fosse duas divs" que não precisam existir no HTML, e por isso o código fica "mais clean". A setinha do botão "entrar para a turma" do [[wiki/entities/frontpush]] é um deles. Na demo, `article { position: relative }` e `::after { content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 50% }` ([[wiki/concepts/css-position]]). `[external]` Ficam dentro do elemento (primeiro e último filho), não antes e depois dele; exigem `content`, não estão no DOM e não existem em `<img>`/`<input>`: https://developer.mozilla.org/en-US/docs/Web/CSS/::after. Também `p::first-letter`, com "text transform capitalized" (o valor é `capitalize`, e para a primeira letra basta `uppercase`).

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa `body::after` com `content: ""` e `position: fixed` para desenhar a faixa cinza de fundo da página de resultados: "o elemento que o CSS está criando não existe na página". Como vem por último, fica por cima de tudo, e `z-index: -1` o manda para trás. Ver [[wiki/concepts/css-position]].

## Key sources

- [[wiki/sources/seletores-e-pseudo-elements-css]] — first-letter e first-line; o termo usado para tudo
- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: `::after` com content e ícone de busca
- [[wiki/sources/frontpush-seletores-css-filho-irmao-atributo-nth-child-pseudo-elements]]: `::before`/`::after` como "duas divs"; setinha do FrontPUSH; `::first-letter`
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: `body::after` como faixa de fundo
