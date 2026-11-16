---
type: concept
title: "Status Code HTTP"
aliases: ["status code", "códigos de status http", "401 vs 403", "200 404 500"]
date_created: 2026-09-30
date_updated: 2026-11-16
source_count: 8
tags: [http, api, status-code, erros]
skill: tech-mentor-networking
status: stub
---

# Status Code HTTP

Número na resposta que **comunica o resultado da intenção** do cliente. Pergunta certa: "o que o servidor está me dizendo?", e não "deu 200?".

| Código | Significado | Observação |
|---|---|---|
| 200 OK | processada com sucesso | |
| 201 Created | recurso criado | típico de POST |
| 301 Moved Permanently | mudou de endereço definitivamente | [[wiki/concepts/http-redirect-301-302]] |
| 400 Bad Request | requisição inadequada | |
| 401 Unauthorized | autenticação ausente/inválida | na prática, "não autenticado" — [[wiki/concepts/autenticacao-e-autorizacao]] |
| 403 Forbidden | sei quem você é, mas não tem permissão | autorização |
| 404 Not Found | recurso não existe | |
| 429 Too Many Requests | estourou o [[wiki/concepts/rate-limiting]] | |
| 500 Internal Server Error | algo quebrou no servidor | |

[[wiki/concepts/middleware]] costuma responder 401/403 antes de a requisição chegar ao controller — por isso o código do negócio "nunca é executado".

[external] Famílias: 1xx informativo, 2xx sucesso, 3xx redirecionamento, 4xx erro do cliente, 5xx erro do servidor (RFC 9110 §15, https://www.rfc-editor.org/rfc/rfc9110#name-status-codes).

## 429 Too Many Requests

Definido pela RFC 6585 (2012), com `Retry-After` opcional. Ver [[wiki/concepts/http-429-too-many-requests]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]], "ponto não encontrado" responde 400, mas o código certo é 404. 400 é requisição malformada, como um `id` que não é número.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]], o `errors()` do celebrate responde 400 com `message` e as chaves inválidas. Sem imagem, o controller quebra com 500.

## No JStack, aula 02

Em [[wiki/sources/jstack-http-e-apis-rest]], as famílias pelo primeiro dígito e os principais: 200, 201, 204, 400, "401/403: Unauthorized", 404, 405, 409, 500. Duas imprecisões: 401 (não autenticado) e 403 (sem permissão) não são a mesma coisa, e o status não é um header; no HTTP/2 ele aparece como o pseudo-header `:status` ([[wiki/concepts/http2]]).

## Na NLW #2, dia 2 (Diego Fernandes)

201 no `POST /classes` e no `POST /connections`; 400 para filtros ausentes (certo) e para "erro inesperado" ao gravar, que seria 500. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]].
## No JStack, aula 04

Em [[wiki/sources/jstack-criando-o-servidor-http]], `response.writeHead(200, {...})`: o status é o primeiro argumento, e 200 "porque a gente não tem regra de negócio nenhuma". No Node também dá para usar `response.statusCode = 201`.

## No JStack, aula 05

Em [[wiki/sources/jstack-criando-a-primeira-rota-da-api]]: 200 na listagem e 404 para "Cannot GET /asd". 405 Method Not Allowed é citado para "a rota users existe, mas [...] um post" e descartado; o 405 deve vir com o header `Allow`.

## Key sources
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — lista comentada de status e mudança de pergunta
- [[wiki/sources/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato]] — 429 e RFC 6585
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: 400 usado para not found (deveria ser 404)
- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: 400 do celebrate; 500 por req.file ausente
- [[wiki/sources/jstack-http-e-apis-rest]]: famílias e principais códigos; 401/403 juntos e status como "header" (corrigidos)
- [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]]: NLW #2, Diego, dia 2: 201 e 400; 400 no lugar de 500
- [[wiki/sources/jstack-criando-o-servidor-http]]: 200 no writeHead do Node
- [[wiki/sources/jstack-criando-a-primeira-rota-da-api]]: 404 de fallback; 405 citado e descartado
