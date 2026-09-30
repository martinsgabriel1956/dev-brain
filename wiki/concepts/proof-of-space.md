---
type: concept
title: "Proof of Space"
aliases: ["prova de espaço", "PoSpace"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [seguranca, memoria, anti-abuso]
skill: tech-mentor-security
status: draft
---

# Proof of Space

O servidor pede que o cliente construa e **guarde em memória** uma tabela grande calculada em sequência específica; depois consulta uma **posição aleatória**. Quem guardou responde na hora; quem recalcula demora e é detectado.

Complementa o [[wiki/concepts/proof-of-work]]: cálculo em paralelo é barato (GPU), **RAM não escala barato** ([[wiki/concepts/memoria-ram]]). Usado no [[wiki/concepts/cloudflare-turnstile]].

## Key sources

- [[wiki/sources/historia-do-captcha-do-teste-de-turing-ao-turnstile]]
