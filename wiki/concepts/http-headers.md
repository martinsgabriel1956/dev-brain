---
type: concept
title: "Headers HTTP"
aliases: ["http headers", "cabeçalhos http", "authorization header", "content-type"]
date_created: 2026-09-30
date_updated: 2026-11-16
source_count: 2
tags: [http, headers, api, metadados]
skill: tech-mentor-networking
status: stub
---

# Headers HTTP

**Metadados da comunicação** numa [[wiki/concepts/requisicao-http]] ou resposta — informação *sobre* a mensagem, não o conteúdo (que vai no body). Analogia: etiqueta da encomenda vs. conteúdo da caixa.

| Header | Diz |
|---|---|
| `Content-Type` | formato do conteúdo enviado (ex.: `application/json`) |
| `Accept` | formatos de resposta aceitos pelo cliente |
| `Authorization` | credenciais (ex.: `Bearer <token>`, ver [[wiki/concepts/jwt]]) |
| `Cookie` | dados de sessão ([[wiki/concepts/sessoes-http-cookies]]) |
| `User-Agent` | origem: navegador, app ou bot |
| `Cache-Control` | se a resposta pode ser guardada/reaproveitada ([[wiki/concepts/http-caching]]) |

## Armadilhas de depuração

Um 401 pode vir de erro trivial: header com nome errado, esquecer `Bearer` ou o espaço depois dele, token expirado ([[wiki/concepts/debug-de-requisicao-http]]). Headers também participam de [[wiki/concepts/cors]] (`Access-Control-Allow-Origin` etc.).

**Correção:** a RFC 6648 (2012) desaconselha o prefixo `X-` em headers novos `[external]` https://www.rfc-editor.org/rfc/rfc6648. E um header de organização vindo do cliente precisa ser validado no servidor ([[wiki/concepts/multi-tenancy]]).

## Na NLW #2, dia 2 (Diego Fernandes)

Descritos como o que define se a mensagem quer "criar [...] uma lista [...] editar, deletar": quem faz isso é o método. Os cabeçalhos levam `Content-Type`, `Authorization`, `Accept`. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]].

## Key sources
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — headers como frases da conversa
- [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]]: NLW #2, Diego, dia 2: headers × método
