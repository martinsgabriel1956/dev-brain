---
type: concept
title: "Flexbox (display: flex)"
aliases: ["flexbox", "display flex", "flex", "flex-direction", "justify-content", "align-items", "flex: 1"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 6
tags: [frontend, css, flexbox, layout, display, alinhamento]
skill: tech-mentor-frontend
status: stub
---

# Flexbox (display: flex)

Modelo de layout em uma dimensão: `display: flex` no pai organiza os filhos ao longo de um eixo principal (linha por padrão, coluna com `flex-direction: column`). `justify-content` distribui no eixo principal, `align-items` alinha no eixo cruzado, e `flex` nos filhos diz quanto cada um cresce ou encolhe. Por fora, o elemento flex continua de bloco. Ver [[wiki/concepts/display-css]] e [[wiki/concepts/box-model]].

## Na NLW #1

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa flexbox em quase toda a página do Ecoleta:

- **Header:** `display: flex` põe logo e link lado a lado, `align-items: center` alinha e `justify-content: space-between` separa. "Você não sabe o tanto que a gente sofreu no passado para fazer esse tipo de alinhamento".
- **Coluna que ocupa a sobra:** `.content` em `flex-direction: column`; `main` com `flex: 1` ("preenche automaticamente todo o espaço") e `justify-content: center`. Ao mudar a direção, o mesmo `justify-content` passa a agir na vertical.
- **Botão:** `a` flex com um `span` fixo de 72 px e um `strong` com `flex: 1` + `text-align: center`.
- **Flex por fora é block:** "Quando eu faço [...] display flex, [...] por fora, ela vai ser a propriedade block".

## Precisões

- `flex: 1` é shorthand de `flex-grow: 1; flex-shrink: 1; flex-basis: 0%`, não só flex-grow `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/flex).
- `gap` no contêiner flex substitui margens entre itens; a aula usa `margin-right` no ícone `[external]` (https://developer.mozilla.org/en-US/docs/Web/CSS/gap).
- Para duas dimensões (linhas e colunas ao mesmo tempo), `grid` costuma servir melhor `[skill: tech-mentor-frontend]`.

## Na NLW #1, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa `flex-direction: column` em cada `.field` (label sobre input) e `flex: 1` nos campos de um `.field-group` para que "estique automaticamente preenchendo todo o espaço".

## No módulo de front-end do FrontPUSH (aula 06)

Em [[wiki/sources/frontpush-layout-css-botao-hover-flexbox-media-query]], [[wiki/entities/nasser|Násser]] resume: `display: flex` "pega todos os seus filhos diretos, eles vão virar flex-itens e o container é o flex pai", e "automaticamente um vai ficar do lado do outro", porque o `flex-direction` padrão é `row`. Abaixo de 960 px, uma media query troca para `column`. Cita também Grid Layout e "Grid System com Sass, utilizando float" como alternativas, cada uma com módulo próprio. `[external]` Flexbox é unidimensional, Grid bidimensional; float para colunas é legado.

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] contrasta o flex, "unidimensional", com o [[wiki/concepts/css-grid|grid]], "multidimensional". Dentro de cada item de coleta, `flex-direction: column` com `justify-content: space-between` separa imagem e texto na vertical, porque "eu inverti o fluxo". O `span` usa `flex: 1` para ocupar a sobra. No modal, o input com `flex: 1` empurra o botão de 72 px para o canto.

## Key sources

- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: header, coluna com `flex: 1`, botão com span + strong
- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: campos do formulário em coluna e flex: 1
- [[wiki/sources/frontpush-layout-css-botao-hover-flexbox-media-query]]: filhos diretos viram itens; `row` padrão; `column` na media query
- [[wiki/sources/frontpush-position-css-relative-absolute-coordenadas]]: position "não é feito para fazer layout em si"; no FrontPUSH, "o resto todo, eu utilizo o flexbox"
- [[wiki/sources/frontpush-conclusao-modulo-css-estilo-layout-animacao-documentacao]]: "centralizar uma div" com flexbox ou grid como exemplo de dúvida para o Google
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: flex x grid; space-between em coluna; flex: 1 no input
