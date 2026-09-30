---
type: concept
title: "CAPTCHA"
aliases: ["captcha", "Completely Automated Public Turing test to tell Computers and Humans Apart"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [seguranca, captcha, bot-detection, teste-de-turing]
skill: tech-mentor-security
status: draft
---

# CAPTCHA

Teste automatizado para distinguir humano de programa. Formalização (2003): um **gerador** cria o desafio e um **testador** confere a resposta sem saber a solução; requisitos: fácil de automatizar, humano passa com alta probabilidade, **nenhum programa conhecido passa, mesmo conhecendo o algoritmo de geração**. Isso exige um **problema de IA em aberto** — logo todo CAPTCHA tem prazo de validade.

## Linha do tempo

1996 proposta de [[wiki/entities/moni-naor]] ([[wiki/concepts/teste-de-turing]] invertido) → 1997–2000 texto distorcido vs. [[wiki/concepts/ocr]] (PayPal, Yahoo) → 2003 paper de formalização → 2007 [[wiki/concepts/recaptcha]] → 2014 CAPTCHA de texto morto por IA do [[wiki/entities/google]] → "Não sou um robô" e reCAPTCHA v3 (score de risco) → 2022 [[wiki/concepts/cloudflare-turnstile]] ([[wiki/concepts/proof-of-work]], [[wiki/concepts/proof-of-space]]) e [[wiki/concepts/funcaptcha]].

## Tese central

Os CAPTCHAs atuais não pedem mais um problema de IA em aberto: viraram **score de risco / prova de ambiente**, apoiados em [[wiki/concepts/seguranca-por-obscuridade]] — fora da definição de 2003. O contorno mais barato não é resolver por IA e sim [[wiki/concepts/servico-de-resolucao-de-captcha]] (humanos por API). Ver [[wiki/concepts/bot-detection]] e [[wiki/concepts/rate-limiting]] como defesas complementares.

## Key sources

- [[wiki/sources/historia-do-captcha-do-teste-de-turing-ao-turnstile]]
