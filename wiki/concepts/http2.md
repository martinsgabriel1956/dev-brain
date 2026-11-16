---
type: concept
title: "Http2"
aliases: []
date_created: 2026-09-22
date_updated: 2026-11-16
source_count: 5
tags: [http2]
skill: tech-mentor-backend
status: stub
---

# Http2

Stub criado durante sweep de lint (links quebrados) a partir de referências em 2 página(s) da wiki — conteúdo completo pendente de ingest dedicado.

## Contexto das citações

- Em [[wiki/sources/grpc]]: [[wiki/concepts/http2]]
- Em [[wiki/sources/http-tcp-quic]]: [[wiki/concepts/http2]]

## Pendências

Página não nasceu de um ingest próprio; TL;DR acima é reconstruído apenas a partir do texto das páginas que a citam. Precisa de fonte dedicada para virar `draft`/`stable`.

## "Menos arquivos" no Sass (FrontPUSH)

Em [[wiki/sources/frontpush-import-e-partials-sass]], o argumento para compilar tudo num CSS é ter menos requisições, a lógica do HTTP/1.1. Com a multiplexação do HTTP/2, vários arquivos pequenos custam pouco; o motivo que continua valendo é o CSS bloquear a renderização ([[wiki/concepts/critical-rendering-path]]).

## Pseudo-headers (JStack, aula 02)

Em [[wiki/sources/jstack-http-e-apis-rest]], o exemplo lista `path`, método e `scheme` "dentro dos headers" e chama o status code de "outro header". É o que o DevTools mostra numa conexão HTTP/2: os pseudo-headers `:method`, `:scheme`, `:authority`, `:path` e `:status`, que no HTTP/1.1 ficam na linha de requisição e na linha de status `[external]` https://www.rfc-editor.org/rfc/rfc9113#name-request-pseudo-header-field.

## Key sources

- [[wiki/sources/grpc]]
- [[wiki/sources/http-tcp-quic]]
- [[wiki/sources/jstack-http-e-apis-rest]]: pseudo-headers :path/:method/:scheme/:status vistos como "headers"

## Key sources (adição 2026-10-14)
- [[wiki/sources/historia-do-front-end-akita-ep4]] — reduz a necessidade de concatenar assets ([[wiki/concepts/pipeline-de-assets]])
- [[wiki/sources/frontpush-import-e-partials-sass]]: argumento de "menos requests" do Sass, datado pelo HTTP/2
