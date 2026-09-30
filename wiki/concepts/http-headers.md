---
type: concept
title: "Headers HTTP"
aliases: ["http headers", "cabeçalhos http", "authorization header", "content-type"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
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

## Key sources
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — headers como frases da conversa
