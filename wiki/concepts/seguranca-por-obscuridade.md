---
type: concept
title: "Segurança por Obscuridade"
aliases: ["security through obscurity"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [seguranca, principios, criptografia]
skill: tech-mentor-security
status: draft
---

# Segurança por Obscuridade

Depender do **sigilo do algoritmo** para a segurança. Contradiz o princípio de Kerckhoffs [external] (o sistema deve ser seguro mesmo se o adversário conhece tudo exceto a chave) e o terceiro requisito do [[wiki/concepts/captcha]] de 2003 (nenhum programa passa *mesmo conhecendo o algoritmo*).

Na fonte: [[wiki/concepts/recaptcha]] v3 ("ninguém fora do Google sabe o algoritmo") e [[wiki/concepts/funcaptcha]] (script ofuscado + telemetria) dependem disso — e por isso são alvos de [[wiki/concepts/engenharia-reversa]]. Contraste: [[wiki/concepts/proof-of-work]] é público e seguro pelo custo, não pelo segredo.

## Key sources

- [[wiki/sources/historia-do-captcha-do-teste-de-turing-ao-turnstile]]
