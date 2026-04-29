---
type: concept
title: "HTTP Redirect: 301 vs 302"
aliases: ["301", "302", "permanent redirect", "temporary redirect", "redirect http"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [http, redirect, cache, analytics, system-design]
skill: tech-mentor-system-design
status: stable
---

# HTTP Redirect: 301 vs 302

Trade-off real em URL shorteners: rastreabilidade vs performance.

## 301 — Permanent Redirect

```
Browser cacheia o redirect localmente.
Próximas visitas não chegam ao servidor.

✅ Menos carga no servidor
❌ Analytics impossível — request não chega mais ao backend
❌ Sem rollback — URL de destino não pode ser alterada (browser já cacheou)
```

## 302 — Temporary Redirect

```
Sem cache no browser.
Todo request passa pelo servidor.

✅ Analytics preciso — cada click registrado
✅ URL de destino pode ser alterada a qualquer momento
❌ Mais load no servidor (mitigado com cache no servidor)
```

## Decisão Prática

**302 por padrão** — analytics e flexibilidade. O "mais load no servidor" é mitigado por Redis + CDN cache no lado do servidor.

**301 como opção explícita** — para quem não precisa de tracking: CDNs internos, links de assets estáticos, casos onde a performance do client importa mais que analytics.

## No Contexto de URL Shortener

CDN cacheia os redirects populares para 302 também — diferença de load prático é menor do que parece. O argumento decisivo é a mutabilidade do destino e o analytics.

## Key Sources

- [[sources/case-url-shortener]]
