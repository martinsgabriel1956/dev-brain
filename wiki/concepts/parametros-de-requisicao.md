---
type: concept
title: "Parâmetros de requisição (route, query e body)"
aliases: ["route params", "request params", "query params", "request body", "tipos de parâmetros"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [http, api, rest, express, backend]
skill: lang-dynamic
status: stub
---

# Parâmetros de requisição (route, query e body)

Os três lugares onde um cliente manda dados para uma rota HTTP, como [[wiki/entities/diego-fernandes]] os apresenta no dia 2 da NLW #1 ([[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]):

| Tipo | Onde | No Express | Para quê |
|---|---|---|---|
| **Route params** | no caminho, `/users/:id` | `request.params.id` | identificar um recurso; "99% das vezes [...] obrigatório" |
| **Query params** | depois do `?`, `?search=on&page=2` | `request.query.search` | filtro, paginação, ordenação; opcionais |
| **Request body** | no corpo (JSON) | `request.body`, com `app.use(express.json())` | dados para criar ou editar |

**O que a tabela não diz:**

- **Tudo chega como texto.** `:id` é string e query pode ser string, array ou ausente, então "o query pode vir qualquer coisa". `Number()` e `String()` só calam o TypeScript; o certo é validar com schema e responder 400 ([[wiki/concepts/validacao-de-entrada]]).
- **Query string fica gravada** em logs, histórico e cabeçalhos `Referer`. Dado sensível vai no body ou em header, sempre com HTTPS. Ver [[wiki/concepts/query-string]].
- **Headers são a quarta via,** para autenticação (`Authorization`), formato (`Content-Type`) e idioma.

Relacionado: [[wiki/concepts/recurso-rest]], [[wiki/concepts/metodos-http]], [[wiki/concepts/requisicao-http]], [[wiki/concepts/middleware]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: route params, query params e body no Insomnia e no Express
