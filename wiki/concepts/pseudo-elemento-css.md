---
type: concept
title: "Pseudo-elemento CSS"
aliases: ["pseudo-elemento", "pseudo-element", "pseudo-elements", "::before", "::after", "::first-letter", "::first-line", "::placeholder"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 9
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

## Na NLW #2, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]], `.input-block:focus-within::after` cria a linha de foco do campo: `content: ''` obrigatório, `width: calc(100% - 3.2rem)`, `height: 2px`, `position: absolute; bottom: 0; left: 1.6rem`. Mayk diz que "o CSS vai criar um elemento HTML"; é um pseudo-elemento, fora do DOM. No DevTools, ele aparece e some conforme o foco.

## Na NLW #2, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]], a linha de foco com `:focus-within::after` passa a valer também para a `.textarea-block`, que recebe `position: relative`.

## Facilidades no Sass (FrontPUSH)

Em [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]], "facilidades com pseudo-elemento e estados" é uma das vantagens do Sass listadas por [[wiki/entities/nasser|Násser]], sem demonstração nesta aula. `[external]` No SCSS, `&::before` dentro do bloco do elemento gera `elemento::before` (https://sass-lang.com/documentation/style-rules/parent-selector/).

## &::before nos links (FrontPUSH, Sass aula 05)

Em [[wiki/sources/frontpush-nesting-aninhamento-sass]], [[wiki/entities/nasser|Násser]] diz usar `::before`/`::after` "demais" em links para criar efeitos, aninhados com `&` (como no projeto Nubank). O `content: ""` é o que faz o pseudo-elemento existir.

## Na NLW #2, dia 1 (Diego Fernandes)

`::after` gera a linha de foco (`content: ''`, 2 px, `position: absolute`, `calc(100% - 3.2rem)`); o `content` é "obrigatório sempre que a gente coloca o after e o before". Ver [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]].

## Key sources

- [[wiki/sources/seletores-e-pseudo-elements-css]] — first-letter e first-line; o termo usado para tudo
- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: `::after` com content e ícone de busca
- [[wiki/sources/frontpush-seletores-css-filho-irmao-atributo-nth-child-pseudo-elements]]: `::before`/`::after` como "duas divs"; setinha do FrontPUSH; `::first-letter`
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: `body::after` como faixa de fundo
- [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]: NLW #2, dia 2: linha de foco com ::after e calc()
- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: NLW #2, dia 3: linha de foco estendida ao textarea
- [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]]: introdução ao Sass: pseudo-elementos como vantagem
- [[wiki/sources/frontpush-nesting-aninhamento-sass]]: Sass aula 05: `&::before` com `content` vazio
- [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]: NLW #2, Diego, dia 1: ::after como linha de foco
