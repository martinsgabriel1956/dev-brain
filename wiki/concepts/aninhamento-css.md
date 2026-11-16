---
type: concept
title: "Aninhamento no CSS (nesting)"
aliases: ["nesting", "CSS nesting", "aninhamento SCSS", "regras aninhadas"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 4
tags: [css, scss, sass, nesting, seletores]
skill: tech-mentor-frontend
status: stub
---

# Aninhamento no CSS (nesting)

Escrever uma regra dentro de outra para que o seletor de dentro valha só no contexto do de fora. `h1 { color: white; span { color: blue; } }` equivale ao seletor descendente `h1 span` ([[wiki/concepts/seletores-css]]).

## Na introdução ao Sass do FrontPUSH

Em [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]], [[wiki/entities/nasser|Násser]] mostra no [[wiki/entities/codepen]] o `h1 span` do CSS padrão e depois a mesma coisa em SCSS: "eu posso colocar as tags uma dentro da outra [...] melhora o meu entendimento do que está dentro de determinada tag ou não". Na época, um recurso do [[wiki/concepts/pre-processador-css|pré-processador]] "que não é permitido no CSS puro".

## Hoje

- `[skill: tech-mentor-frontend]` Aninhamento nativo no Chrome 112+, Firefox 117+ e Safari 16.5+ (2023); para navegadores velhos, `postcss-nesting` ou Lightning CSS.
- `[external]` Diferenças para o Sass: o nativo não concatena sufixos (`&__elemento` do BEM só funciona no Sass) e trata `&` como `:is()`, o que pode mudar a especificidade (https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_nesting).
- Aninhar fundo demais cria seletores longos e específicos; a regra comum é não passar de três níveis ([[wiki/concepts/especificidade-css]]).

## Hierarquia na aula de @import (FrontPUSH)

Em [[wiki/sources/frontpush-import-e-partials-sass]], o `span` aninhado no `h1` sai no CSS como `h1 span`: "no Sass ele fica mais organizado, porque tem essa seção de hierarquia [...] você entende que esse está dentro dessa tag".

## A aula de nesting (FrontPUSH, aula 05)

Em [[wiki/sources/frontpush-nesting-aninhamento-sass]], a aula dedicada:
- **Tags:** `.list` > `li` > `a`, o desenho de menu → itens → links; o CSS gerado é idêntico ao escrito à mão.
- **`&` (seletor pai):** "coloque colado dessa tag". `&:hover`, `&.active` (× `& .active`, com espaço) e `&::before`. `[external]` Também `&__item` (sufixo BEM, só no Sass) e `.dark &` (contexto).
- **Propriedades:** `border: { style: solid; color: purple; }` → `border-style`, `border-color`. Só no Sass, pouco usado ("eu faço mesmo o de tags").
- "Pode emendar n cascatas" (slide): cada nível soma especificidade; ver Hoje.

## @media aninhada via mixin (FrontPUSH, Sass aula 06)

Em [[wiki/sources/frontpush-mixin-e-content-sass]], o `@include responsive { ... }` dentro do `h1` produz uma media query "aninhada" na regra. `[skill: tech-mentor-frontend]` O aninhamento nativo já permite `@media` dentro do seletor, sem mixin.

## Key sources

- [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss]]: `h1` com `span` dentro, em SCSS
- [[wiki/sources/frontpush-import-e-partials-sass]]: `h1` com `span` aninhado; CSS gerado
- [[wiki/sources/frontpush-nesting-aninhamento-sass]]: aula dedicada: tags, `&`, propriedades
- [[wiki/sources/frontpush-mixin-e-content-sass]]: media query dentro do seletor via mixin
