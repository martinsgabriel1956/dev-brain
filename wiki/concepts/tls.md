---
type: concept
title: "Tls"
aliases: []
date_created: 2026-09-22
date_updated: 2026-11-16
source_count: 4
tags: [tls]
skill: tech-mentor-backend
status: stub
---

# Tls

Stub criado durante sweep de lint (links quebrados) a partir de referências em 2 página(s) da wiki — conteúdo completo pendente de ingest dedicado.

## Contexto das citações

- Em [[wiki/sources/http-tcp-quic]]: [[wiki/concepts/tls]]
- Em [[wiki/sources/tls-mtls-vpn]]: [[wiki/concepts/tls]]

## Pendências

Página não nasceu de um ingest próprio; TL;DR acima é reconstruído apenas a partir do texto das páginas que a citam. Precisa de fonte dedicada para virar `draft`/`stable`.

Em [[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete]], o S do HTTPS é "simplesmente porque tem uma criptografia em questão de segurança"; sem ele, o navegador avisa que "a conexão não é segura". A criptografia é o TLS, que também autentica o servidor por certificado.

## Key sources

- [[wiki/sources/http-tcp-quic]]
- [[wiki/sources/tls-mtls-vpn]]
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — HTTPS: navegador e servidor negociam criptografia antes da requisição sair
- [[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete]]: FrontPUSH, JavaScript aula 13: HTTPS como criptografia
