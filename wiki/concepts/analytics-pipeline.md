---
type: concept
title: "Analytics Pipeline"
aliases: ["pipeline de analytics", "async analytics", "event analytics"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, analytics, kafka, clickhouse, async, olap]
skill: tech-mentor-system-design
status: stub
---

# Analytics Pipeline

Processamento de eventos analíticos desacoplado do caminho crítico da aplicação.

## Princípio Central

Analytics **nunca** deve estar no caminho crítico de uma operação de negócio. Adiciona latência e cria acoplamento — se o analytics service cair, a operação principal cai junto.

## Arquitetura Típica

```
Operação (redirect, compra, click)
  → publica evento no Kafka: { id, timestamp, metadata }
        ↓
  Analytics Consumer (async)
    → agrega por janela de tempo
    → persiste no ClickHouse (OLAP)
    → serve dashboards via API separada
```

## Contadores em Tempo Real

Para contadores que precisam de resposta rápida (ex: "quantos clicks essa URL teve?"):

```
Redis INCR clicks:{short_code}
  → flush para DB a cada 60s (batch write)
  → evita write amplification no banco principal
```

## ClickHouse vs PostgreSQL para Analytics

PostgreSQL é OLTP — agregações em bilhões de rows são lentas. ClickHouse é colunnar OLAP — projetado para `GROUP BY`, `COUNT`, `SUM` em volumes massivos.

## Mobile — Adapter Pattern

No contexto mobile, o analytics pipeline começa no cliente com o [[concepts/adapter-pattern-analytics]] — um `AnalyticsService` que despacha eventos para múltiplos providers (Mixpanel, Firebase) sem acoplamento direto nos call sites.

## Key Sources

- [[sources/case-url-shortener]]
- [[sources/mobile-platform-engineering]]
