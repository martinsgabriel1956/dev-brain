---
type: concept
title: "Redis GEO"
aliases: ["redis geo", "redis geosearch", "redis geoadd"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [redis, geoespacial, localização, system-design, performance]
skill: tech-mentor-system-design
status: stable
---

# Redis GEO

Estrutura nativa do Redis para armazenar coordenadas geográficas e fazer buscas por raio. Internamente usa [[concepts/geohash]] em sorted set.

## Comandos Principais

```python
# Motorista atualiza posição (a cada 4s)
r.geoadd("drivers:active", -46.6558, -23.5617, "driver:42")

# Buscar motoristas em raio de 2km, ordenado por distância
nearby = r.geosearch(
    "drivers:active",
    longitude=-46.6558,
    latitude=-23.5617,
    radius=2,
    unit="km",
    withcoord=True,
    withdist=True,
    sort="ASC",
    count=20
)
# → [("driver:42", 0.3, (-46.6558, -23.5617)), ...]
```

## Por que Redis e Não PostGIS

- PostGIS tem write throughput limitado — não suporta 1.25M writes/s
- Dados de localização são voláteis — não precisam de durabilidade forte
- Redis cluster suporta 1.25M writes/s com 10 shards (~125k writes/s por shard)

## Memória

5M motoristas × ~70 bytes (lat, lng, member) ≈ 350MB — cabe confortavelmente em uma instância Redis.

## Resiliência

Dados efêmeros: se Redis cair, motoristas reenviam posição em 4s. Degradação de UX (mapa pisca), não de correção.

## Key Sources

- [[sources/case-uber]]
