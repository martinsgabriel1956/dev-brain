---
type: concept
title: "Surge Pricing"
aliases: ["preço dinâmico", "dynamic pricing", "surge multiplier"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, uber, pricing, kafka, redis, stream-processing]
skill: tech-mentor-system-design
status: stable
---

# Surge Pricing

Preço dinâmico baseado em ratio demand/supply por região geográfica. Desacoplado do caminho crítico do matching.

## Arquitetura

```
Demand signal:
  Kafka stream de pedidos → agrega por geohash (5 chars = ~5km)
  Janela de 5 minutos → requests/min por célula

Supply signal:
  Redis GEO → contar motoristas disponíveis por célula

Surge multiplier:
  ratio = demand / supply
  ratio > 2.0 → 1.5×
  ratio > 3.0 → 2.0×
  ratio > 5.0 → 3.0× (cap máximo)

Atualização: a cada 30s por célula
Cache: Redis com TTL 30s → Pricing Service serve sem query ao stream
```

## Por que Desacoplado

Calcular surge no caminho crítico do match adicionaria latência. Kafka + Redis cache permite servir o multiplier atual em <1ms sem bloquear o matching.

## Geohash de 5 chars

Granularidade de ~5km por célula — suficiente para capturar variação de demanda por bairro sem granularidade excessiva.

## Key Sources

- [[sources/case-uber]]
