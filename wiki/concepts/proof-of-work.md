---
type: concept
title: "Proof of Work"
aliases: ["prova de trabalho", "PoW"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [seguranca, criptografia, hash, anti-abuso]
skill: tech-mentor-security
status: draft
---

# Proof of Work

O cliente deve achar um **nonce** tal que `hash(desafio + nonce)` comece com muitos zeros. Sem atalho matemático: [[wiki/concepts/hashing]] por força bruta (de ~50 mil a ~2 milhões de tentativas conforme a dificuldade). Mesmo princípio da mineração de Bitcoin em escala minúscula.

Uso anti-bot: custo imperceptível para um usuário, mas proibitivo para um bot que faz 100 mil ações em paralelo. Fraqueza: GPUs paralelizam barato — motivo do [[wiki/concepts/proof-of-space]]. Usado no [[wiki/concepts/cloudflare-turnstile]].

## Key sources

- [[wiki/sources/historia-do-captcha-do-teste-de-turing-ao-turnstile]]
