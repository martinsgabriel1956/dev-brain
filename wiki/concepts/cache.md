---
type: concept
title: "Cache"
aliases: ["caching", "cache de aplicação"]
date_created: 2026-06-26
date_updated: 2026-07-24
source_count: 5
tags: [cache, performance, redis, arquitetura, backend, grande-rollback]
skill: tech-mentor-backend
status: stable
---

# Cache

## TL;DR

Estratégia de guardar dados já processados em memória de acesso rápido para evitar recomputação ou viagem ao banco. O objetivo é encurtar o caminho entre a aplicação e os dados.

## Quando Usar

Cache resolve bem **dados com baixa volatilidade e alta frequência de leitura**:

- Feature flags / toggles
- Menus e permissões de usuário
- Saldo e extrato (atualiza só em transações)
- Tokens de sessão
- Catálogos de produto, configurações

## Quando NÃO Usar

- Dados financeiros críticos (consistência > performance)
- Dados que mudam a cada request (overhead > ganho)
- Datasets pequenos (L1 in-process resolve sem Redis)
- Endpoints write-heavy (cache ajuda read-heavy)

## Padrões de Cache

| Padrão | Leitura | Escrita | Consistência |
|---|---|---|---|
| [[cache-aside]] (Lazy) | Cache + DB on miss | Só DB (invalida cache) | Eventual |
| Write-Through | Cache hit | Cache + DB simultâneo | Forte |
| Write-Behind | Cache hit | Só cache (sync assíncrono) | Eventual |

## Hierarquia de Velocidade

```
L1 — In-process (Map/LRU)   ns   — por processo, sem I/O
L2 — Redis / Memcached       μs  — compartilhado entre instâncias
L3 — CDN Edge               ms   — economiza RTT de rede
L4 — Database               ms   — fonte de verdade
```

## Tradeoffs

Adicionar cache aumenta a complexidade: [[tradeoff-de-cache]]. É necessário pensar em:

- Estratégia de invalidação (TTL fixo, evento, tag)
- Sincronismo entre cache e banco de dados
- Manutenção de mais uma tecnologia no stack

## Principais Implementações

- **[[redis]]** — banco in-memory chave-valor; caso de uso principal
- Memcached — alternativa mais simples ao Redis (sem persistência, sem tipos ricos)
- In-process LRU — L1 local ao processo (node-lru-cache, Guava Cache)

## Key Sources

- [[wiki/sources/como-arquitetar-com-cache-e-redis]]
- [[wiki/sources/escalabilidade-vertical-horizontal-system-design]] — cache como "melhor amigo antes de escalar"; banco é o gargalo mais comum
- [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]] — contraponto: cache como camada de reserva foi removido em favor do banco relacional puro, ver [[wiki/concepts/grande-rollback]]
- [[wiki/sources/10-conceitos-fundamentais-backend]] — framing didático de cache hit/miss; a pergunta central não é "usar cache ou não" mas "quando essa resposta deixa de ser verdade"
- [[wiki/sources/system-design-simulador-hotel-booking-replit]] — demonstração num simulador interativo: mesmo tráfego, banco de dados saturado a 115% cai drasticamente ao conectar cache, porque a maioria das leituras de um sistema de reserva de hotel repete os mesmos quartos populares (read-heavy); IA avaliadora do exercício aponta cache invalidation como lacuna não tratada
