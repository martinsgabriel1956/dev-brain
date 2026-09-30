---
type: concept
title: "Serviço de Resolução de CAPTCHA"
aliases: ["captcha farm", "captcha solving service", "2Captcha"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [seguranca, captcha, bot, mercado]
skill: tech-mentor-security
status: draft
---

# Serviço de Resolução de CAPTCHA

Mercado que paga pessoas para resolver [[wiki/concepts/captcha]] em escala (já existia por volta de 2007). Hoje via **API**: o script envia o desafio, uma rede de centenas de humanos resolve e devolve o **token**. Torna irrelevante treinar IA contra a detecção: "compra-se o humano em que ela já confia". Consequência: CAPTCHA vira **custo por ação**, não barreira — reforça a necessidade de [[wiki/concepts/rate-limiting]] e [[wiki/concepts/bot-detection]] em camadas.

## Key sources

- [[wiki/sources/historia-do-captcha-do-teste-de-turing-ao-turnstile]]
