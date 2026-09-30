---
type: concept
title: "Subdomínio (DDD)"
aliases: ["subdomínio", "subdomain", "subdomínios"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [ddd, subdominio, dominio, strategic-design]
skill: tech-mentor-backend
status: stub
---

# Subdomínio (DDD)

## TL;DR

Divisão natural do domínio do **problema** (negócio) em partes com regras, responsabilidades e complexidades próprias. Distinto de [[wiki/concepts/bounded-context]], que é limite técnico/linguístico do domínio da **solução**: um subdomínio pode ter **um ou mais** bounded contexts, dependendo da complexidade ([[wiki/sources/bounded-context-contextos-delimitados-bernardo-lobato]]).

## Observação

Não confundir com [[wiki/concepts/dominio]] (nome + TLD de DNS), página homônima de outra área. Ver [[wiki/concepts/ddd]] para o conceito de domínio no DDD.

> Página stub: o vídeo #2 da série (domínio/subdomínio) não está na wiki; não há tipologia (core/supporting/generic) na fonte atual.

## Key Sources

- [[wiki/sources/bounded-context-contextos-delimitados-bernardo-lobato]] — subdomínio = divisão do negócio; relação 1:N com bounded contexts
