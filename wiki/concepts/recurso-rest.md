---
type: concept
title: "Recurso (REST)"
aliases: ["resource", "pensar em recursos", "rest resource"]
date_created: 2026-09-30
date_updated: 2026-11-16
source_count: 4
tags: [rest, api, recurso, design-de-api]
skill: tech-mentor-networking
status: stub
---

# Recurso (REST)

Ideia central de uma API REST: a URL identifica um **recurso** (`/usuarios/42`) e o [[wiki/concepts/metodos-http|método]] expressa o que fazer com ele. Mentalidade: "qual recurso estou acessando?" em vez de "qual função chamo?" — isso torna REST intuitivo.

Relacionado: [[wiki/concepts/requisicao-http]], [[wiki/concepts/contrato-de-api]], [[wiki/concepts/api-versioning]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]], o primeiro argumento de `app.get('/users', ...)` é "qual que é o recurso que eu tô querendo acessar". Ver [[wiki/concepts/api-rest]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]], a rota é "o endereço completo da nossa requisição" e o recurso é "qual entidade estamos acessando do sistema".

## Key sources
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — mudança de mentalidade função → recurso

## Key sources (adição 2026-10-09)
- [[wiki/sources/url-vs-uri-diferenca-urn-identificacao-localizacao]] — a URI identifica o recurso; num endpoint HTTP ela é também URL ([[wiki/concepts/uri]], [[wiki/concepts/url]])
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: /users como recurso no Express
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: rota x recurso
