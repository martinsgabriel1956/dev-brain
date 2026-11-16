---
type: entity
title: "JStack"
aliases: ["JStack", "JSTack", "Jstack"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 6
tags: [curso, javascript, nodejs, react, educacao]
skill: lang-dynamic
status: stub
---

# JStack

Curso brasileiro de JavaScript full stack (Node.js, React, React Native) de [[wiki/entities/mateus-silva]], vendido pela Hotmart. Relatos de alunos destacam conceitos de base, como pooling no Node, pouco vistos em tutoriais `[external]` https://www.tabnews.com.br/dareDevil/jstack-vale-a-pena (relato de comunidade, confiança média). Não confundir com o utilitário `jstack` do JDK.

Na aula 01 ([[wiki/sources/jstack-como-funciona-o-nodejs]]), o [[wiki/entities/nodejs|Node.js]] é "a tecnologia de back-end que a gente vai usar para desenvolver todos os projetos ao decorrer do curso".

## Aula 02

Em [[wiki/sources/jstack-http-e-apis-rest]]: API, anatomia de request e response HTTP, status codes, DevTools e REST como "representação do estado". O título do módulo no player é "Primeiros passos no Node.js".

## Aula 03

Em [[wiki/sources/jstack-o-que-sao-modulos]]: primeira aula com código; os três tipos de módulo do Node, `require`, `module.exports` e `exports`, e `require('os')`. O curso chama as seções de "capítulos" para não confundir com módulos do Node; o npm entra no capítulo seguinte.

## Aula 04

Em [[wiki/sources/jstack-criando-o-servidor-http]]: começa a primeira API, em Node puro com `http`, antes do Express; `src/index.js`, `createServer`, `writeHead`, `end`, `listen` e reinício manual (sem nodemon).

## Aula 05

Em [[wiki/sources/jstack-criando-a-primeira-rota-da-api]]: `GET /users` com `if` por método e URL, mocks em `src/mocks/users.js`, `JSON.stringify` e 404 "Cannot GET". Anuncia o arquivo de rotas para a aula seguinte.

## Aula 06

Em [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]]: `UserController` (objeto; classes no próximo módulo), CRUD, `routes.js` com `{ endpoint, method, handler }` e despacho com `find`.

## Key sources

- [[wiki/sources/jstack-como-funciona-o-nodejs]]: aula 01, como funciona o Node.js
- [[wiki/sources/jstack-http-e-apis-rest]]: aula 02, HTTP e APIs REST
- [[wiki/sources/jstack-o-que-sao-modulos]]: aula 03, módulos e require
- [[wiki/sources/jstack-criando-o-servidor-http]]: aula 04, servidor HTTP
- [[wiki/sources/jstack-criando-a-primeira-rota-da-api]]: aula 05, primeira rota
- [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]]: aula 06, controller e rotas
