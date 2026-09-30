---
type: concept
title: "FunCaptcha (Arkose Labs)"
aliases: ["fun captcha", "Arkose Labs", "captcha 3D do Roblox"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [seguranca, captcha, arkose, roblox]
skill: tech-mentor-security
status: draft
---

# FunCaptcha (Arkose Labs)

CAPTCHA gamificado usado pelo [[wiki/entities/roblox]]: rotacionar modelo 3D de cabeça para baixo com setas, ou escolher em grade de dados. Mais de **1.200 variações** (modelo, fundo, regra) dificultam treinar classificador genérico. Verificação: resposta do puzzle + **script ofuscado** + telemetria cruzados no servidor para checar se o ambiente é um navegador real — de novo [[wiki/concepts/seguranca-por-obscuridade]]. Mais fricção que [[wiki/concepts/cloudflare-turnstile]] (ver `fraud-abuse.md` [skill: tech-mentor-security]).

## Key sources

- [[wiki/sources/historia-do-captcha-do-teste-de-turing-ao-turnstile]]
