---
type: concept
title: "Indicador de foco (outline, :focus-visible, :focus-within)"
aliases: ["indicador de foco", "focus indicator", "outline", "outline: none", "focus visible", ":focus-visible", ":focus-within"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [css, acessibilidade, foco, teclado, wcag, formulario, frontend]
skill: tech-mentor-frontend
status: stub
---

# Indicador de foco

A marca visual que mostra qual elemento recebe o teclado. O navegador desenha um `outline` em links, botões e campos focados. Quem navega com Tab depende dela para saber onde está, e a WCAG exige que ela exista no critério 2.4.7 (Focus Visible) e, na versão 2.2, que não fique escondida (2.4.11) `[external]` (https://www.w3.org/WAI/WCAG22/Understanding/focus-visible).

- **`outline: 0` / `outline: none`** tira a marca. Só é aceitável com um substituto visível no lugar.
- **`:focus`** casa sempre que o elemento está em foco, inclusive por clique.
- **`:focus-visible`** casa quando o navegador acha que a marca é útil, em geral ao navegar pelo teclado. É o jeito usual de ter estilo próprio sem incomodar quem usa mouse.
- **`:focus-within`** casa no pai quando algum descendente está em foco. Serve para destacar o bloco inteiro de um campo.

`[skill: tech-mentor-frontend]` Padrão recomendado: manter o outline do navegador ou trocá-lo por `:focus-visible { outline: 2px solid <cor>; outline-offset: 2px }` com contraste de pelo menos 3:1 contra o fundo. Testar com Tab, sem mouse. Ver [[wiki/concepts/acessibilidade]].

## Na NLW #2, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]], [[wiki/entities/mayk-brito|Mayk]] põe `outline: 0` nos campos do formulário de busca e reconhece o custo: "isso não é uma prática muito, muito adequada, porque a gente precisa desse outline de uma maneira visual pra ajudar quem precisa de acessibilidade". O substituto é uma linha de 2 px sob o campo, feita com `.input-block:focus-within::after` e `position: absolute`, como no layout do Proffy. Ver [[wiki/concepts/pseudo-elemento-css]].

O substituto cobre só o `input`. Nos `select`, que também perderam o outline, ele dispensa a linha porque "quando a gente clica nele automaticamente ele abre". Isso vale para o mouse; quem chega pelo Tab não vê onde está. Inferência do agente com base no critério 2.4.7.

## Na NLW #2, dia 1 (Diego Fernandes)

Mesma linha de foco do Mayk, agora em React: `outline: 0` no input e `.input-block:focus-within::after` como substituto. O indicador existe; falta só conferir o contraste. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]].

## Key sources

- [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]: `outline: 0` nos campos, linha com `:focus-within::after` só no input, select sem substituto
- [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]: NLW #2, Diego, dia 1: :focus-within::after em React
