---
type: concept
title: "Unidades de medida no CSS (px, pt, em, rem, cm, %)"
aliases: ["unidades CSS", "medidas relativas", "medidas absolutas", "px rem em", "CSS units"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 10
tags: [css, unidades, responsividade, rem, em, porcentagem]
skill: tech-mentor-frontend
status: stub
---

# Unidades de medida no CSS (px, pt, em, rem, cm, %)

O slide de box model do [[wiki/entities/frontpush|FrontPUSH]] lista px, pt, em, rem, cm e %. [[wiki/entities/nasser|Násser]] separa as **fixas** (pixel) das **relativas** (em, rem e porcentagem) e liga as relativas à [[wiki/concepts/design-responsivo|responsividade]]: "não necessariamente você vai só aplicar em uma interface medidas fixas, como em pixels" ([[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]]).

## Relativas a quê

`[skill: tech-mentor-frontend]` / `[external]` (https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Values_and_units):

- `em`: font-size do próprio elemento (no `font-size`, do pai); compõe em cascata quando aninhado.
- `rem`: font-size do elemento raiz (`html`); respeita o tamanho de fonte que o usuário configurou no navegador, por isso é a escolha usual para tipografia e espaçamentos.
- `%`: o bloco que contém (largura) ou, no [[wiki/concepts/border-radius]], as dimensões da própria caixa — 50% faz elipse, ou círculo se width = height.
- `px`, `pt`, `cm`: absolutas; pt e cm fazem sentido em impressão.
- Não citadas na aula: `vw`/`vh`, `ch` (largura de linha em caracteres) e `clamp()` para tamanhos fluidos.

## Na NLW #1 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] contrasta `%` ("faz um cálculo de 90% do tamanho da página") com `px` ("900 sempre será 900", "pixel nunca é flexível") e usa `vh` ("a altura está dividida em 100 bloquinhos") e `vw` na posição do fundo.

## px, pt, polegadas e % do pai (módulo de front-end do FrontPUSH)

Em [[wiki/sources/frontpush-box-model-margin-padding-display-unidades]], [[wiki/entities/nasser|Násser]] prefere `px` entre as fixas ("a gente está em uma tela bem mais próxima"), mostra `pt` e polegadas (`in`) e explica `%` como "do pai". `[external]` `1in` = 96 px CSS, valor fixo, não polegada física; `height` em `%` só funciona com pai de altura definida, e `padding`/`margin` em `%` usam a largura do bloco que contém: https://developer.mozilla.org/en-US/docs/Web/CSS/percentage.

## Na NLW #2, dia 1 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: 100% = 16 px = 1 rem por padrão. `%` é relativo ao pai, `rem` ao `:root` e `em` ao pai ("0.2 de 3 de 100 de 50"); `px` é fixo. O Proffy parte de `:root { font-size: 60% }` e texto em `1.6rem` (15,36 px; o truque de 10 px é 62,5%). Tensões: `rem` não acompanha a tela, e sim a fonte do root e a preferência do usuário; e o px do CSS não é o pixel físico, então 16 px num 4K não é "um pontinho".

## Na NLW #2, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]], a landing começa com `:root { font-size: 40% }` (6,4 px de base, pequeno demais) e, acima de 700 px, passa a `62.5%`, "1rem equivale a 10 pixels", o que só vale com o padrão de 16 px do navegador. `fr` é "uma unidade de medida [...] chamada de frações". No desktop, px para gaps e paddings, "uma coisa mais fixa mesmo".

## px na tipografia responsiva (FrontPUSH, Sass)

Em [[wiki/sources/frontpush-mixin-e-content-sass]], os tamanhos responsivos estão todos em `px` (72, 48, 36). `[skill: tech-mentor-frontend]` Em `rem`, o texto acompanha o tamanho de fonte que o usuário escolheu no navegador, coisa que `px` ignora.

## % calculada pelo Sass (FrontPUSH)

Em [[wiki/sources/frontpush-funcoes-sass]], `($col / $total) * 100%` devolve `%` porque o Sass carrega unidades nas contas: `0.25 * 100%` = `25%`. `[skill: tech-mentor-frontend]` No CSS puro, `calc(3 / 12 * 100%)` faz o mesmo.

## Key Sources

- [[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]] — lista do slide; fixas x relativas; % e rem para responsividade
- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: % x px, vh e vw
- [[wiki/sources/frontpush-box-model-margin-padding-display-unidades]]: px preferido; pt e polegadas; `%` do pai; `vw`/`vh`
- [[wiki/sources/frontpush-display-flex-flex-container-filhos-diretos]]: item em block ocupa "100% do elemento do pai" por padrão
- [[wiki/sources/frontpush-flex-direction-flex-wrap-flex-flow]]: `max-width`, `min-width`, `max-height` e `min-height` como "boa prática"
- [[wiki/sources/frontpush-flex-basis-tamanho-base-flex-itens]]: `flex-basis` aceita %, em, px (slide)
- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: NLW #2, dia 1: %, rem, em, px; root 60%
- [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]: NLW #2, dia 2: root 40% e 62,5%; fr; px no desktop
- [[wiki/sources/frontpush-mixin-e-content-sass]]: tipografia em px; rem respeita a preferência do usuário
- [[wiki/sources/frontpush-funcoes-sass]]: % calculada com unidade no Sass
