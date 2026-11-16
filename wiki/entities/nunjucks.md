---
type: entity
title: "Nunjucks"
aliases: ["nunjucks", "njk", "Nunjucks templates"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 5
tags: [nodejs, template-engine, html, mozilla, javascript]
skill: lang-dynamic
status: stub
---

# Nunjucks

[[wiki/concepts/template-engine|Template engine]] para JavaScript, da Mozilla, inspirado no Jinja2. A sintaxe:
- `{{ variável }}` com filtros (`| upper`, `| safe`).
- `{% if %}`, `{% for %}`, `{% set %}`, `{% include %}` e herança com `{% extends %}` e `{% block %}`.
- Comentários em `{# #}`.

`nunjucks.configure(pasta, { express: app })` liga o Nunjucks ao [[wiki/entities/express]] para o `res.render`. O `autoescape` vem ligado por padrão, então `{{ }}` escapa HTML `[external]` (https://mozilla.github.io/nunjucks/api.html#configure).

## Na NLW #1, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] instala o Nunjucks ("vamos fazer o HTML com esteroides") e o configura com `noCache: true` para não servir versões velhas durante o desenvolvimento. Usa quatro recursos:
- **Variáveis:** `{{ title }}`.
- **Partials:** `include` para o cabeçalho e o modal.
- **Layout:** `layout.html` com `extends` e os blocos `styles`, `title`, `content`, `modal` e `scripts`.
- **`set`:** `{% set pageId = "page-home" %}` para o id de cada página.

No VS Code, a extensão Nunjucks Template exige `files.associations` e `emmet.includeLanguages`. A transcrição automática grafou o nome de mais de dez jeitos (Nandux, Nandex, Nunchucks...).

## Na NLW #1, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa `{% for place in places %}` para os cards, `{% if total > 0 %}...{% else %}` para "Nenhum local encontrado" e `{% if saved %}` com `include` do partial `point-created.html`. `[external]` O `for` do Nunjucks aceita `{% else %}` para lista vazia (https://mozilla.github.io/nunjucks/templating.html#for).

Na trilha de [[wiki/entities/diego-fernandes|Diego Fernandes]] da NLW #1 ([[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]), o Nunjucks aparece ao lado de Handlebars e EJS como exemplo do template engine que a API REST deixa de usar.

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], `nunjucks.configure('src/views', { express: server, noCache: true })`, `{{ }}`, `{% for prof in profs %}`, `{% if filters.subject == loop.index %}selected{% endif %}`, com `loop.index` (de 1) e `loop.index0` (de 0). O `==` do Nunjucks é frouxo e compara a string da query com o número do loop; `noCache` ficou sem condição.

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], o estado vazio é `{% if proffys == "" %}<p class="no-results">...{% else %}{% for %}...{% endif %}`. Funciona porque o array vazio vira `""` no `==`; o `{% for %}...{% else %}` do próprio Nunjucks faria isso sem coerção.

## Key sources

- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: configure, render, variáveis, include, extends/block e set no Ecoleta
- [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]]: for, if/else, include condicional
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: citado como template engine do Node, em contraste com a API REST
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: for, if, loop.index; == frouxo
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: NLW #2, dia 5: estado vazio com if/else
