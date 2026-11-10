---
type: concept
title: "Requisição HTTP"
aliases: ["http request", "anatomia da requisição", "http request response"]
date_created: 2026-09-30
date_updated: 2026-11-10
source_count: 4
tags: [http, api, protocolo, cliente-servidor]
skill: tech-mentor-networking
status: stub
---

# Requisição HTTP

Mensagem que o cliente envia ao servidor; o servidor responde com outra mensagem ([[wiki/concepts/http-status-code|status]] + headers + body). É uma **conversa**, e bibliotecas (fetch, Axios) e ferramentas (Postman, navegador) são só interfaces para produzi-la.

## Anatomia

| Parte | Papel |
|---|---|
| [[wiki/concepts/metodos-http\|Método]] | Intenção (GET, POST, PUT, DELETE) |
| URL | Qual [[wiki/concepts/recurso-rest\|recurso]] (ex.: `/usuarios/42`) |
| [[wiki/concepts/http-headers\|Headers]] | Metadados sobre a comunicação |
| Body (opcional) | O conteúdo em si (ex.: nome, e-mail, senha num POST) |

Resposta: status, headers (ex.: `Content-Type`) e body. **HTTP ≠ JSON**: JSON é o formato do conteúdo; HTTP é o protocolo.

## Caminho no servidor

rota → [[wiki/concepts/middleware]] → controller → service → banco → resposta. Normalmente protegida por [[wiki/concepts/http-vs-https|HTTPS]].

## Depuração

[[wiki/concepts/debug-de-requisicao-http]]: a aba Network do DevTools mostra URL, método, headers, payload, status e response.

## Key sources
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — anatomia completa do clique até a resposta

## Key sources (adição 2026-10-06)

- [[wiki/sources/estado-global-stateless-side-effects-reprodutibilidade-galego]] — HTTP stateless: cada requisição carrega a identificação do usuário; ver [[wiki/concepts/request-context]] e [[wiki/concepts/estado-global-em-servidor]].

## Key sources (adição 2026-10-09)
- [[wiki/sources/url-vs-uri-diferenca-urn-identificacao-localizacao]] — a URL da requisição é uma URI que localiza o recurso; query param seleciona o recurso (ver [[wiki/concepts/url]])

## Key sources (adição 2026-11-10)

- [[wiki/sources/polling-sse-websocket-comunicacao-em-tempo-real]] — HTTP como pergunta e resposta: sem gatilho do cliente o servidor não fala, origem do problema de tempo real
