---
type: concept
title: "Redis"
aliases: ["redis cache", "redis db"]
date_created: 2026-06-26
date_updated: 2026-06-26
source_count: 1
tags: [redis, cache, nosql, banco-in-memory, chave-valor, backend]
skill: tech-mentor-backend
status: stable
---

# Redis

## TL;DR

Banco [[nosql]] [[banco-in-memory]] do tipo chave-valor. Projetado para latência mínima — armazena tudo na RAM e acessa por chave, sem esquema, sem SQL. Caso de uso principal: [[cache]].

## Modelo de Dados

```
chave                  →  valor
"saldo-cliente-123"    →  "1500.00"
"sessao-abc"           →  { userId: 42, role: "admin" }  (hash)
"fila-emails"          →  ["msg1", "msg2"]               (list)
```

**Tipos de valor suportados:** `string`, `hash`, `list`, `set`, `sorted set`, `stream`, `HyperLogLog`, `bitmap`

A chave pode ser longa e semântica. Busca por prefixo (`GET cod_cliente:*`) permite recuperar ou limpar grupos de registros.

## Pontos Fortes

| Aspecto | Detalhe |
|---|---|
| Performance | Latência sub-milissegundo; o mais rápido para leitura/escrita |
| Difusão | Amplamente conhecido; suporte em todas as linguagens |
| Cloud | Serviço gerenciado nativo em AWS (ElastiCache), GCP, Azure |
| Deploy | Container, local, cloud managed, servidor físico |
| Cluster | [[escalabilidade-horizontal]] simples — bem documentada |

## Pontos Fracos

| Aspecto | Detalhe |
|---|---|
| Memória limitada | Limitado pela RAM disponível na máquina/cluster |
| Single CPU | Uma instância usa apenas 1 núcleo — clusterize para escalar CPU |
| Sem SQL | Sem suporte a queries relacionais |
| Segurança | Permissões estáticas por DB (Redis < 6); Redis 6+ introduziu ACLs granulares |
| Persistência | In-memory por padrão; RDB/AOF são opcionais e adicionam overhead |

## Padrões de Uso

- **[[cache-aside]]** — busca no Redis; em miss vai ao banco e popula com TTL
- **[[cqrs]] read layer** — Redis como projeção otimizada de leitura; SQL como fonte de verdade
- **[[feature-flag]]** — interruptores de código com latência mínima
- **Session store** — tokens de sessão, permissões de menu, extrato do cliente
- **Pub/Sub** — broadcast efêmero em tempo real (sem persistência)
- **Streams** — fila robusta com consumer groups e ACK

## Quando NÃO Usar Redis

- Dados financeiros críticos onde consistência > performance
- Dados com alta volatilidade (mudam a cada request)
- Datasets que cabem em memória de processo (L1 cache resolve sem Redis)

## Escalabilidade

- **Sentinel** — HA sem sharding; failover automático; dataset cabe em um nó
- **Cluster** — sharding horizontal com 16.384 hash slots; dataset maior que memória de um nó

## Key Sources

- [[wiki/sources/como-arquitetar-com-cache-e-redis]]
