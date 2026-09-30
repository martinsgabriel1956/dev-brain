---
type: concept
title: "Cloudflare Turnstile"
aliases: ["turnstile"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [seguranca, captcha, cloudflare, bot-detection]
skill: tech-mentor-security
status: draft
---

# Cloudflare Turnstile

Alternativa a CAPTCHA da [[wiki/entities/cloudflare]] (2022): roda pequenos **desafios JS não interativos** ([[wiki/concepts/proof-of-work]] e [[wiki/concepts/proof-of-space]]). Não prova humanidade; prova que há **navegador real executando JS**, e não script HTTP puro. Integração e privacidade: [skill: tech-mentor-security] `fraud-abuse.md` (widget + validação server-side em `siteverify`). Ver [[wiki/concepts/bot-detection]].

## Key sources

- [[wiki/sources/historia-do-captcha-do-teste-de-turing-ao-turnstile]]
