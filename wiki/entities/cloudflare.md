---
type: entity
title: "Cloudflare"
aliases: ["cloudflare"]
date_created: 2026-09-29
date_updated: 2026-10-06
source_count: 2
tags: [organizacao, cdn, seguranca, bot-detection]
skill: tech-mentor-security
status: stub
---

# Cloudflare

Empresa de CDN/segurança que lançou o [[wiki/concepts/cloudflare-turnstile]] em 2022 ([[wiki/concepts/proof-of-work]] + [[wiki/concepts/proof-of-space]]). Ver também [[wiki/concepts/bot-detection]].

## Rate Limit no Cloudflare

Permite regras de rate limit por características da requisição (caminho da URL, país etc.) com bloqueio/mitigação na borda, antes de chegar à aplicação. Ver [[wiki/concepts/rate-limit-camadas-de-posicionamento]].

## Key sources

- [[wiki/sources/historia-do-captcha-do-teste-de-turing-ao-turnstile]]
- [[wiki/sources/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato]] — regras de rate limit na borda
