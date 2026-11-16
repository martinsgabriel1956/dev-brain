---
type: concept
title: "Recurso (REST)"
aliases: ["resource", "pensar em recursos", "rest resource"]
date_created: 2026-09-30
date_updated: 2026-11-16
source_count: 7
tags: [rest, api, recurso, design-de-api]
skill: tech-mentor-networking
status: stub
---

# Recurso (REST)

Ideia central de uma API REST: a URL identifica um **recurso** (`/usuarios/42`) e o [[wiki/concepts/metodos-http|método]] expressa o que fazer com ele. Mentalidade: "qual recurso estou acessando?" em vez de "qual função chamo?" — isso torna REST intuitivo.

Relacionado: [[wiki/concepts/requisicao-http]], [[wiki/concepts/contrato-de-api]], [[wiki/concepts/api-versioning]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]], o primeiro argumento de `app.get('/users', ...)` é "qual que é o recurso que eu tô querendo acessar". Ver [[wiki/concepts/api-rest]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]], a rota é "o endereço completo da nossa requisição" e o recurso é "qual entidade estamos acessando do sistema".

## No JStack, aula 02

Em [[wiki/sources/jstack-http-e-apis-rest]], o endpoint ("tudo que vem depois do nosso domínio") identifica o recurso: `/products` para a coleção e `/products/10` para um item, sempre no plural. O `/10` é chamado de "parâmetros" (route params, diferentes dos query params).

## No JStack, aula 05

Em [[wiki/sources/jstack-criando-a-primeira-rota-da-api]]: `/users` sem ID é a coleção, e o cliente "está esperando uma listagem"; o item (`/users/:id`) fica para depois.

## Key sources
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — mudança de mentalidade função → recurso
- [[wiki/sources/jstack-http-e-apis-rest]]: endpoint identifica o recurso; coleção × item
- [[wiki/sources/jstack-criando-a-primeira-rota-da-api]]: coleção /users

## Na NLW #2, dia 2 (Diego Fernandes)

Rota é "o endereço da nossa aplicação" e recurso é "o que vem [...] depois [...] dessa URL base" (`users`, `contacts`), sempre no plural. `POST /classes` cria usuário, aula e horários, mas o recurso é a aula: "é o que eu vou criar como entidade". Ver [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]].

## Key sources (adição 2026-10-09)
- [[wiki/sources/url-vs-uri-diferenca-urn-identificacao-localizacao]] — a URI identifica o recurso; num endpoint HTTP ela é também URL ([[wiki/concepts/uri]], [[wiki/concepts/url]])
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: /users como recurso no Express
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: rota x recurso
- [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]]: NLW #2, Diego, dia 2: rota × recurso; POST /classes como entidade
