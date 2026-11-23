---
type: concept
title: "CRUD"
aliases: ["Create, Read, Update, Delete", "crud", "operações CRUD"]
date_created: 2026-11-16
date_updated: 2026-11-23
source_count: 3
tags: [crud, api, rest, banco-de-dados, backend, metodos-http]
skill: tech-mentor-backend
status: stub
---

# CRUD

As quatro operações básicas sobre dados persistidos: **C**reate, **R**ead, **U**pdate, **D**elete. É o vocabulário comum entre banco, API e tela.

| Operação | SQL | HTTP (REST) | Rota típica |
|---|---|---|---|
| Create | `INSERT` | `POST` | `POST /users` |
| Read (lista) | `SELECT` | `GET` | `GET /users` |
| Read (um) | `SELECT ... WHERE id` | `GET` | `GET /users/:id` |
| Update | `UPDATE` | `PUT` (inteiro) / `PATCH` (parcial) | `PUT /users/:id` |
| Delete | `DELETE` | `DELETE` | `DELETE /users/:id` |

Ver [[wiki/concepts/metodos-http]] e [[wiki/concepts/api-rest]]. O mapeamento é convenção: há ações que não cabem em CRUD (aprovar, cancelar, enviar), modeladas como sub-recurso (`POST /orders/:id/cancel`) ou como mudança de estado.

Não confundir com [[wiki/concepts/crud-resolvido]], a tese de que construir CRUD virou commodity.

## No JStack (aula 06)

Em [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]]: "crud são as operações de create, read, update e delete": criar usuário, pegar todos ou um "a partir do ID", atualizar e remover, todas como funções do [[wiki/concepts/controller]] de usuários. A aula implementa só a listagem.

Em [[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete]], o POST é "de criar, de create, que sempre remete ao CRUD"; PUT atualiza e DELETE apaga. O Read é o GET.

## Key sources

- [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]]: CRUD de usuários como as funções do controller
- [[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete]]: FrontPUSH, JavaScript aula 13: POST como o C do CRUD
- [[wiki/sources/frontpush-monetizacao-freelancer-como-construir-um-portfolio]]: o blog com CRUD como peça de portfólio
