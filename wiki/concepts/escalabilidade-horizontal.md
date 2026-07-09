---
type: concept
title: "Escalabilidade Horizontal"
aliases: ["horizontal scaling", "scale out", "escalar horizontalmente"]
date_created: 2026-06-26
date_updated: 2026-07-09
source_count: 5
tags: [escalabilidade, arquitetura, sistemas-distribuidos, nosql, redis, backend]
skill: tech-mentor-backend
status: stable
---

# Escalabilidade Horizontal

## TL;DR

Aumentar capacidade adicionando mais máquinas ao sistema (scale out), ao invés de aumentar recursos na mesma máquina (scale up / escalabilidade vertical).

## Horizontal vs Vertical

| | Vertical (Scale Up) | Horizontal (Scale Out) |
|---|---|---|
| Estratégia | Mais CPU/RAM/banda na mesma máquina | Mais máquinas no cluster |
| Custo | Caro; hardware tem teto físico | Linear com o número de nós |
| Disponibilidade | Ponto único de falha | Redundância por design |
| Complexidade | Simples | Requer coordenação distribuída |
| Melhor para | Bancos relacionais, sessão com estado | [[nosql]], stateless services |

## NoSQL e Escalabilidade Horizontal

Bancos [[nosql]] foram projetados para escalar horizontalmente. Exemplos:

- **[[redis]] Cluster** — 16.384 hash slots distribuídos entre N masters; adicionar nós redistribui slots
- **Cassandra** — partição por consistent hashing; adicionar nó redistribui automaticamente
- **MongoDB** — sharding nativo por shard key

## Por Que Bancos Relacionais Escalam Menos Horizontalmente

Normalização e transações ACID entre tabelas exigem coordenação entre nós (2PC, distributed locks) — o que é caro e complexo. Por isso PostgreSQL e Oracle escalam melhor verticalmente.

## Redis e Single CPU

[[redis]] roda em **um único CPU por instância**. Escalar verticalmente (mais núcleos) não ajuda. A solução correta é clusterizar: múltiplas instâncias redis em diferentes nós, cada uma usando 1 CPU.

## Pré-requisitos para funcionar

1. **Servidores [[stateless]]** — sessão em Redis, arquivos em S3, dados no banco; nada em memória local
2. **[[load-balancer]]** — distribui requisições entre as instâncias
3. **[[auto-scaling]]** — sobe e derruba instâncias automaticamente por regras (CPU, fila, memória)

Quando distribuir dados entre máquinas, entra o [[cap-theorem]] — consistência vs disponibilidade vs tolerância a partições.

## Caso especial: serviços de conexão persistente (WebSocket)

Escalar horizontalmente um serviço de conexões longas (WebSocket) tem uma restrição que serviços HTTP request-response não têm: exige [[wiki/concepts/load-balancer|load balancer de camada 4]] em vez de camada 7, porque o LB não pode reabrir a conexão para rotear (quebraria o tunelamento TCP). Além disso, servidores replicados não se comunicam entre si automaticamente — precisam de um broker externo (ex: [[wiki/concepts/redis]] Pub/Sub) para que uma mensagem publicada num servidor alcance um usuário conectado em outro. Ver [[wiki/concepts/chat-distribuido]].

## Key Sources

- [[wiki/sources/como-arquitetar-com-cache-e-redis]]
- [[wiki/sources/escalabilidade-vertical-horizontal-system-design]]
- [[wiki/sources/updates-tempo-real-polling-sse-websocket]] — escalabilidade horizontal de servidores WebSocket, LB L4 obrigatório, comunicação entre servidores via Redis Pub/Sub
- [[wiki/sources/escalabilidade-horizontal-load-balancer-algoritmos]] — tipos de load balancer e algoritmos de balanceamento (Weighted RR, Least Connections, Least Time, Sticky RR) usados para distribuir carga entre as réplicas
- [[wiki/sources/10-conceitos-fundamentais-backend]] — framing de entrada nível-10-conceitos: começar com um servidor só, crescer para "mais usuários, mais chamadas de API, mais consultas ao banco, mais jobs assíncronos, mais picos inesperados"
