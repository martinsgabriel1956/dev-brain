---
type: concept
title: "Cache Layer"
aliases: ["camada de cache", "caching"]
date_created: 2026-05-01
date_updated: 2026-05-01
source_count: 1
tags: [cache, performance, infrastructure, proxy]
skill: tech-mentor-backend
status: stub
---

## Definição

Camada de infraestrutura que armazena resultados de operações custosas em memória (ou storage rápido) para evitar reprocessamento. Pertence à infraestrutura — não é regra de negócio.

## Onde Implementar

O [[proxy-pattern]] é um local idiomático para cache: encapsula a classe real, verifica o cache antes de delegar, e armazena o resultado sem tocar na lógica de negócio.

**Anti-pattern:** colocar lógica de cache no Controller ou na classe de serviço — viola [[single-responsibility-principle]].

## Conceitos Relacionados

- TTL (Time To Live) — tempo de expiração do item em cache
- Cache key — identificador único do item (ex: `report_<id>`)
- Cache miss — item não encontrado, executa operação real
- Cache hit — item encontrado, retorna sem executar operação

## Key Sources

- [[wiki/sources/design-pattern-proxy]]
