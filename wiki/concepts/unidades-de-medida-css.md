---
type: concept
title: "Unidades de medida no CSS (px, pt, em, rem, cm, %)"
aliases: ["unidades CSS", "medidas relativas", "medidas absolutas", "px rem em", "CSS units"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 3
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

## Key Sources

- [[wiki/sources/box-model-tudo-e-caixa-tags-semanticas-padding-margin-border]] — lista do slide; fixas x relativas; % e rem para responsividade
- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: % x px, vh e vw
- [[wiki/sources/frontpush-box-model-margin-padding-display-unidades]]: px preferido; pt e polegadas; `%` do pai; `vw`/`vh`
