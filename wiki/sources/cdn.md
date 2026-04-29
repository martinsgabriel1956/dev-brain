---
type: source
title: "CDN — Content Delivery Network"
aliases: []
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/cdn.md
source_url: ""
author: ""
date_published: "2026-03-27"
date_ingested: 2026-04-22
source_count: 0
tags: [cdn, cache, edge, performance, system-design]
skill: tech-mentor-backend
status: stable
---

## TL;DR

CDN é uma rede de servidores distribuídos (PoPs) que cacheia conteúdo próximo ao usuário. Para assets estáticos transforma 120ms em 5ms. Assets com hash no nome recebem TTL máximo (`immutable`). HTML não deve ser cacheado (referencia assets por hash). APIs públicas usam `s-maxage`. Edge computing (Cloudflare Workers, Lambda@Edge) permite executar lógica no edge com CPU limitada (~50ms) e cold start ~0ms.

## Claims Principais

| Claim | Confiança |
|---|---|
| CDN reduz latência de São Paulo → us-east-1 de ~120ms para ~5-10ms | Alta |
| Assets com hash no nome devem usar `Cache-Control: immutable` com max-age máximo | Alta |
| HTML não deve ser cacheado — referencia assets por hash que mudam a cada deploy | Alta |
| `s-maxage` controla cache do CDN especificamente, sobrescrevendo `max-age` para proxies | Alta |
| ETag permite revalidação sem transferir body — resposta 304 economiza bandwidth | Alta |
| Surrogate Keys (Cloudflare/Fastly) permitem invalidação de grupos de URLs por tag | Alta |
| Edge functions têm CPU ~50ms, sem filesystem, cold start ~0ms (V8 isolates) | Alta |
| CDN não ajuda com dados personalizados por usuário, mutações, WebSocket ou consistência forte | Alta |
| CDN também atua como proteção: WAF, rate limiting, DDoS absorption, origin shielding | Alta |

## Conceitos Abordados

- [[cdn]]
- [[edge-computing]]
- [[cache-control]]
- [[etag]]
- [[surrogate-keys]]
- [[cache-invalidation]]
- [[pop-point-of-presence]]
- [[waf]]
- [[ddos-protection]]
