---
type: concept
title: "Pseudo-elemento CSS"
aliases: ["pseudo-elemento", "pseudo-element", "pseudo-elements", "::before", "::after", "::first-letter", "::first-line", "::placeholder"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [css, frontend, seletores-css, pseudo-elemento]
skill: tech-mentor-frontend
status: stub
---

# Pseudo-elemento CSS

Palavra-chave com **dois dois-pontos** (`::`) que estiliza uma **parte** de um elemento ou cria uma caixa que não existe no HTML: `::first-letter`, `::first-line`, `::before`, `::after`, `::placeholder`, `::selection`. `[external]` https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements

Na aula [[wiki/sources/seletores-e-pseudo-elements-css]], "pseudo-elements" é o nome de toda a lista, explicado como "um falso elemento [...] ou um estado dentro de um outro". Só `first-letter` ("a primeira letra") e `first-line` ("primeira linha") são pseudo-elementos; o resto (`:hover`, `:checked`, `:nth-child`) é [[wiki/concepts/pseudo-classe-css|pseudo-classe]]. A aula de style guide já chamava hover de pseudo-element ([[wiki/concepts/css]]).

`[external]` O placeholder de um input se estiliza com `::placeholder`, não com seletor de atributo (a aula sugere o atributo). A sintaxe antiga de um dois-pontos (`:first-line`) ainda funciona por compatibilidade com CSS2.

## before e after "como se fosse duas divs" (FrontPUSH, aula 04)

Em [[wiki/sources/frontpush-seletores-css-filho-irmao-atributo-nth-child-pseudo-elements]], [[wiki/entities/nasser|Násser]] diz que usa `::after` e `::before` "demais": "como se fosse duas divs" que não precisam existir no HTML, e por isso o código fica "mais clean". A setinha do botão "entrar para a turma" do [[wiki/entities/frontpush]] é um deles. Na demo, `article { position: relative }` e `::after { content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 50% }` ([[wiki/concepts/css-position]]). `[external]` Ficam dentro do elemento (primeiro e último filho), não antes e depois dele; exigem `content`, não estão no DOM e não existem em `<img>`/`<input>`: https://developer.mozilla.org/en-US/docs/Web/CSS/::after. Também `p::first-letter`, com "text transform capitalized" (o valor é `capitalize`, e para a primeira letra basta `uppercase`).

## Key sources

- [[wiki/sources/seletores-e-pseudo-elements-css]] — first-letter e first-line; o termo usado para tudo
- [[wiki/sources/frontpush-seletores-css-filho-irmao-atributo-nth-child-pseudo-elements]]: `::before`/`::after` como "duas divs"; setinha do FrontPUSH; `::first-letter`
