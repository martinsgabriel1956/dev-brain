---
type: concept
title: "CSS Grid"
aliases: ["grid", "display: grid", "grid layout", "grid-template-columns"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 3
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

## Key sources

- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: grid de três colunas com `fr` e `gap`; uma coluna no mobile
- [[wiki/sources/frontpush-flex-basis-tamanho-base-flex-itens]]: `[external]` `repeat(auto-fit, minmax(200px, 1fr))` como alternativa aos cards com `flex-basis` + `wrap`, sem a última linha esticada
- [[wiki/sources/frontpush-flexbox-pratica-1-layout-youtube-estrutura-html]]: o esqueleto de duas colunas do layout do YouTube, feito só com flexbox no exercício, também caberia em grid `[external]`
