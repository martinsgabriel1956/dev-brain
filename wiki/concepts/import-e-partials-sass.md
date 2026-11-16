---
type: concept
title: "@import, @use e partials no Sass"
aliases: ["@import Sass", "@use", "@forward", "partials", "partial Sass", "_arquivo.scss", "módulos do Sass"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [css, sass, scss, import, partials, modulos, organizacao]
skill: tech-mentor-frontend
status: stub
---

# @import, @use e partials no Sass

Como o [[wiki/concepts/pre-processador-css|Sass]] junta vários arquivos num CSS só. Um **partial** é um arquivo cujo nome começa com `_` (`_colors.scss`): o compilador não gera CSS para ele, e ele só existe para ser carregado por outro. A importação omite o `_` e a extensão: `@import "colors"` ou `@use "colors"`.

## No FrontPUSH (aula 03 do módulo de Sass)

Em [[wiki/sources/frontpush-import-e-partials-sass]], [[wiki/entities/nasser|Násser]] separa as cores num `colors.scss` com variáveis, importa no topo do `style.scss` e mostra o problema: o compilador também gerou `colors.css` e `colors.css.map`. Com `_colors.scss`, sai só o `style.css`. Regras dele: organizar por categoria (cores, tipografia, layout, botões), importar primeiro o que define (variáveis, mixins) e só depois o que usa, e gerar um arquivo só, para ter menos requisições.

## @import → @use

- `[external]` `@import` está deprecado desde o Dart Sass 1.80 (2024) e sai no 3.0 (https://sass-lang.com/documentation/breaking-changes/import/). Problemas: tudo vira global, o mesmo arquivo importado duas vezes duplica CSS, e não dá para saber de onde veio uma variável.
- `@use "colors";` carrega o módulo uma vez e expõe `colors.$branco`; `@use "colors" as *;` dispensa o prefixo; `@use "config" with ($cor: red);` configura variáveis `!default`. `@forward` reexporta, para montar um `_index.scss` por pasta (https://sass-lang.com/documentation/at-rules/use/).
- Migração automática: `sass-migrator module --migrate-deps style.scss`.
- A ordem continua importando: `@use` tem de vir antes das outras regras do arquivo.

## @import do CSS puro é outra coisa

`[external]` `@import url(x.css)` nativo faz o navegador baixar o segundo arquivo só depois de ler o primeiro, em série, o que atrasa a renderização ([[wiki/concepts/critical-rendering-path]]). O Sass só gera isso se o caminho terminar em `.css`, usar `url()` ou tiver media query. Ver [[wiki/concepts/pipeline-de-assets]].

## Organização típica

`[skill: tech-mentor-frontend]` Pastas por camada (settings/variáveis, tools/mixins, base, components, utilities), como no ITCSS, cada uma com partials e um `_index.scss` que faz `@forward`; o `main.scss` só faz `@use` delas. Ver [[wiki/concepts/componentizacao]].

## _shadows.scss (FrontPUSH, aula 04)

Em [[wiki/sources/frontpush-variaveis-sass]], um segundo partial, `_shadows.scss`, guarda a variável de sombra. Ele atribui um erro de compilação à falta do underline; o underline só evita o CSS extra, então a causa provável era outra.

## Key sources

- [[wiki/sources/frontpush-import-e-partials-sass]]: `colors.scss` importado, depois `_colors.scss` como partial; "a ordem importa"
- [[wiki/sources/frontpush-variaveis-sass]]: `_shadows.scss`; erro atribuído ao underline
