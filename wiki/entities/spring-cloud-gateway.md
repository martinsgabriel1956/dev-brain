---
type: entity
title: "Spring Cloud Gateway"
aliases: ["SCG"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [api-gateway, spring, rate-limiting, redis]
skill: tech-mentor-backend
status: stub
---

# Spring Cloud Gateway

Gateway do ecossistema Spring ([[wiki/entities/spring-boot]]), evolução do Zuul da Netflix ([[wiki/sources/api-gateway-padrao-essencial-arquiteturas-distribuidas]]). Filtro **RequestRateLimiter**, normalmente com Redis, implementa [[wiki/concepts/token-bucket]] e aceita **chave personalizada** (API key, usuário, e-mail) ([[wiki/sources/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato]]). Ver [[wiki/concepts/api-gateway]].

## Key Sources

- [[wiki/sources/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato]]
