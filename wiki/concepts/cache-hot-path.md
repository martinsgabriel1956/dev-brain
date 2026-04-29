---
type: concept
title: "Cache Hot Path"
aliases: ["hot cache", "cache em camadas", "local cache", "power law cache"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [cache, performance, redis, power-law, system-design]
skill: tech-mentor-system-design
status: stable
---

# Cache Hot Path

Estratégia de cache em camadas que aproveita a distribuição power law do tráfego — a minoria das entradas recebe a maioria dos acessos.

## Power Law no Tráfego

```
Top 1% das URLs  = ~80% dos redirects
Top 20% das URLs = ~95% dos redirects

→ Cache quente de 50GB resolve 91TB de storage
→ A vasta maioria dos dados nunca é acessada
```

## Camadas

```
Request → Hot cache local (in-memory LRU)
              hit (60%) → resposta imediata
              miss ↓
          Redis (distributed cache)
              hit (35%) → resposta + atualiza hot cache
              miss ↓
          PostgreSQL
              → atualiza Redis (TTL 24h) → resposta
```

## Hot Cache Local

Top 1.000 URLs = ~60% do tráfego. LRU in-memory por instância da API.

```
✅ Zero round-trip de rede para URLs virais
✅ Latência sub-milissegundo
❌ Inconsistência temporária entre instâncias (TTL curto mitiga)
❌ Invalidação requer broadcast ou TTL agressivo
```

## TTL Strategy

```
URLs comuns:   Redis TTL 24h
URLs populares: Redis TTL 7 dias
Hot cache local: TTL 5min (consistência eventual aceitável)
```

## Invalidação

- URL deletada → Redis DEL imediato + hot cache expira por TTL
- Destino atualizado → Redis DEL + re-insert

## Relacionado

[[concepts/connection-pooling]] — mesmo princípio de reutilização para economizar overhead por request.

## Key Sources

- [[sources/case-url-shortener]]
