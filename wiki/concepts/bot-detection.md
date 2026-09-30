---
type: concept
title: "Detecção de Bots"
aliases: ["bot detection", "anti-bot", "detecção de automação"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [seguranca, bot-detection, fraude, anti-abuso]
skill: tech-mentor-security
status: draft
---

# Detecção de Bots

Conjunto de técnicas para separar tráfego humano de automatizado. Camadas vistas na fonte: desafios ativos ([[wiki/concepts/captcha]]), score passivo ([[wiki/concepts/recaptcha]] v3), provas de custo ([[wiki/concepts/proof-of-work]], [[wiki/concepts/proof-of-space]]), prova de navegador real ([[wiki/concepts/cloudflare-turnstile]]), telemetria + script ofuscado ([[wiki/concepts/funcaptcha]]).

Sinais citados: idade do cookie, fingerprint do navegador, ambiente. Limite estrutural: quem controla um humano real (ver [[wiki/concepts/servico-de-resolucao-de-captcha]]) ou muitos cookies "maduros" passa. Complementos de aplicação: [[wiki/concepts/rate-limiting]], velocity checks [skill: tech-mentor-security, `fraud-abuse.md`].

**Divergência a registrar:** a fonte diz que o movimento do mouse não afetou o reCAPTCHA em testes; a skill lista dinâmica de mouse como sinal comum de bot detection [skill: tech-mentor-security]. Ver Open Questions na fonte.

## Key sources

- [[wiki/sources/historia-do-captcha-do-teste-de-turing-ao-turnstile]]
