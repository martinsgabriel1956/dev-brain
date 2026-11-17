---
type: concept
title: "CSS Grid"
aliases: ["grid", "display: grid", "grid layout", "grid-template-columns", "grid-template-areas", "grid-area"]
date_created: 2026-11-16
date_updated: 2026-11-17
source_count: 11
tags: [css, layout, grid, frontend]
skill: tech-mentor-frontend
status: stub
---

# CSS Grid

`display: grid` organiza os filhos em linhas **e** colunas ao mesmo tempo. O [[wiki/concepts/flexbox]] trabalha num eixo por vez. As peças básicas:
- `grid-template-columns` define as colunas, em px, % ou `fr` (fração do espaço livre). `repeat(3, 1fr)` equivale a `1fr 1fr 1fr`.
- Os itens que não cabem nas colunas vão para linhas novas, criadas automaticamente.
- `gap` separa linhas e colunas sem criar margem nas bordas.

`[skill: tech-mentor-frontend]` `repeat(auto-fill, minmax(260px, 1fr))` cria colunas responsivas sem media query. `subgrid` alinha o conteúdo de cards vizinhos. Não confundir com o [[wiki/concepts/grid-de-colunas]] do design, que é a malha de layout no Figma.

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] apresenta o grid como "multidimensional" e o flex como "unidimensional":
- **Colunas:** testa `200px 200px 200px`, depois `200px 800px 200px`, que estoura a tela, e fica com `1fr 1fr 1fr`.
- **`gap`:** troca a margem pelo `gap: 16px`; com margin "seria um trabalho um pouco complexo".
- **Onde aparece:** nos itens de coleta e nos cards da página de resultados (com `gap: 24px`). Abaixo de 900 px, os cards passam a `1fr`.

## Na NLW #2, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]], a landing do Proffy no desktop usa `grid-template-columns: 2fr 1fr 2fr`, `grid-template-rows: 350px 1fr` e `grid-template-areas: "proffy image image" "button button texting"`, com `grid-area` em cada bloco e `gap: 60px`. Sem áreas, "o grid vai tentando se ajustar". Alinha com `align-self` e `justify-self` ("o justify do grid"). Na página study, os filtros usam `repeat(4, 1fr)`. O DevTools desenha as linhas do grid ao passar o mouse no container.

## Na mentoria do FrontPUSH (Násser, inferido)

Em [[wiki/sources/frontpush-mentoria-pratica-com-css-grid]], o layout é tratado como planilha: "uma tabela cheia de células pequenas", em que cada card é um "mesclar e centralizar" do Excel. A altura da linha sai do **menor elemento**. O resultado é uma matriz 5 × 5 escrita em `grid-template-areas` "em forma de matriz", com `grid-area` em cada item e `grid-gap` no lugar de margin. Para outra tela, a media query redefine só o template. A regra de bolso: duas dimensões, grid; uma dimensão, [[wiki/concepts/flexbox]].

`[external]` Os nomes da matriz vão separados por espaço (`"A A A B B"`); colados (`"AAABB"`), viram uma célula só. Cada área precisa ser um retângulo, e `.` marca uma célula vazia: https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-areas. `grid-gap` é o nome antigo de `gap`.

## Na NLW #2, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]], no desktop o `.schedule-item` (dia da semana, das, até) vira grid `2fr 1fr 1fr` com `column-gap: 1.6rem`.

## Grid system por classes × CSS Grid (FrontPUSH, Sass)

Em [[wiki/sources/frontpush-for-while-each-sass]], o "sistema de grids" do curso é feito de classes `.grid-N` com largura em px geradas por `@for`. `[skill: tech-mentor-frontend]` O equivalente nativo é `repeat(12, 1fr)` com `gap` e `grid-column: span N`, sem conta de gutter e fluido.

## Na NLW #2, dia 1 (Diego Fernandes)

Landing no desktop com `grid-template-rows: 350px 1fr`, `grid-template-columns: 2fr 1fr 1fr` e áreas `"logo hero hero" "buttons buttons total"`; `1fr` é "ocupe o espaço que sobrar". Para o mesmo layout, Mayk usou `2fr 1fr 2fr`. O form de busca usa `repeat(3, 1fr)` com `column-gap`. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]].

## Grid system sem Grid Layout (FrontPUSH, Sass aula 10)

Em [[wiki/sources/frontpush-grid-system-sass-parte-1]], o grid system é feito "nem flexbox, nem grid layout", com largura em %. `[skill: tech-mentor-frontend]` É o modelo pré-Grid (floats do Bootstrap 3); `repeat(12, 1fr)` + `gap` + `grid-column: span N` faz o mesmo com gutter exato.

## Na NLW #2, dia 3 (Diego Fernandes)

`.schedule-item` com `grid-template-columns: 2fr 1fr 1fr` (dia ocupa metade) e `column-gap`; filtros passam a quatro colunas com o botão Buscar. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]].

## Key sources

- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: grid de três colunas com `fr` e `gap`; uma coluna no mobile
- [[wiki/sources/frontpush-flex-basis-tamanho-base-flex-itens]]: `[external]` `repeat(auto-fit, minmax(200px, 1fr))` como alternativa aos cards com `flex-basis` + `wrap`, sem a última linha esticada
- [[wiki/sources/frontpush-flexbox-pratica-1-layout-youtube-estrutura-html]]: o esqueleto de duas colunas do layout do YouTube, feito só com flexbox no exercício, também caberia em grid `[external]`
- [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]: NLW #2, dia 2: template-areas, grid-area, fr, self-alignment
- [[wiki/sources/frontpush-mentoria-pratica-com-css-grid]]: mentoria: `grid-template-areas` desenhado como "mesclar e centralizar" no Excel, `grid-area` por item, `grid-gap`; nova matriz numa media query
- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: NLW #2, dia 3: schedule-item em 2fr 1fr 1fr
- [[wiki/sources/frontpush-for-while-each-sass]]: sistema de classes × `grid-column: span`
- [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]: NLW #2, Diego, dia 1: 2fr 1fr 1fr com template-areas; repeat(3, 1fr)
- [[wiki/sources/frontpush-grid-system-sass-parte-1]]: grid system de % sem Grid Layout
- [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy]]: NLW #2, Diego, dia 3: schedule-item 2fr 1fr 1fr
- [[wiki/sources/frontpush-jsx-webpack-babel-react-createelement-create-react-app]]: FrontPUSH, React aula 06: CSS Grid como exemplo de recurso novo sem suporte; Babel não ajuda em CSS (Autoprefixer)
