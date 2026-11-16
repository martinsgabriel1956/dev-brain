---
type: concept
title: "Pseudo-elemento CSS"
aliases: ["pseudo-elemento", "pseudo-element", "pseudo-elements", "::before", "::after", "::first-letter", "::first-line", "::placeholder"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [css, frontend, seletores-css, pseudo-elemento]
skill: tech-mentor-frontend
status: stub
---

# Pseudo-elemento CSS

Palavra-chave com **dois dois-pontos** (`::`) que estiliza uma **parte** de um elemento ou cria uma caixa que não existe no HTML: `::first-letter`, `::first-line`, `::before`, `::after`, `::placeholder`, `::selection`. `[external]` https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements

Na aula [[wiki/sources/seletores-e-pseudo-elements-css]], "pseudo-elements" é o nome de toda a lista, explicado como "um falso elemento [...] ou um estado dentro de um outro". Só `first-letter` ("a primeira letra") e `first-line` ("primeira linha") são pseudo-elementos; o resto (`:hover`, `:checked`, `:nth-child`) é [[wiki/concepts/pseudo-classe-css|pseudo-classe]]. A aula de style guide já chamava hover de pseudo-element ([[wiki/concepts/css]]).

`[external]` O placeholder de um input se estiliza com `::placeholder`, não com seletor de atributo (a aula sugere o atributo). A sintaxe antiga de um dois-pontos (`:first-line`) ainda funciona por compatibilidade com CSS2.

## Key sources

- [[wiki/sources/seletores-e-pseudo-elements-css]] — first-letter e first-line; o termo usado para tudo
