---
type: concept
title: "Snowflake ID"
aliases: ["snowflake", "distributed id generation", "geração de id distribuído"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [system-design, id-generation, distributed-systems, snowflake, base62]
skill: tech-mentor-system-design
status: stable
---

# Snowflake ID

ID único distribuído gerado sem coordenação central. Criado pelo Twitter.

## Estrutura (64 bits)

```
timestamp (41 bits) | worker_id (10 bits) | sequence (12 bits)

timestamp  → milissegundos desde epoch customizado (~69 anos de vida útil)
worker_id  → identifica a máquina/processo (até 1.024 workers)
sequence   → contador por milissegundo por worker (até 4.096 IDs/ms/worker)
```

## Propriedades

- **Sem colisão garantida** — unicidade por worker_id + timestamp + sequence
- **Sem coordenação central** — cada worker gera independentemente
- **Ordenado por tempo** — IDs crescentes facilitam debugging e range queries
- **Escala horizontal trivial** — adicionar worker = aumentar throughput linearmente

## Base62 para URL Shortener

```
Snowflake ID (int64) → base62 → 7-8 chars
Base62 = [a-z, A-Z, 0-9] = 62 símbolos
7 chars = 62^7 = 3,5 trilhões de combinações
→ 100M URLs/dia por ~95 anos
```

## Comparativo com Alternativas

| Abordagem | Colisão | Previsível | Coordenação |
|---|---|---|---|
| MD5 truncado | Sim | Não | Não |
| ID sequencial | Não | Sim (enumerável) | Necessária |
| Snowflake + Base62 | Não | Não | Apenas worker_id |

## Único Ponto de Coordenação

Atribuição de `worker_id` — feita uma vez no startup via ZooKeeper, etcd, ou registro em banco. Depois disso, zero coordenação.

## Key Sources

- [[sources/case-url-shortener]]
