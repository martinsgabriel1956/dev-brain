---
type: concept
title: "Read Replicas"
aliases: ["réplica de leitura", "read replica", "replica routing"]
date_created: 2026-04-22
date_updated: 2026-07-03
source_count: 2
tags: [banco-de-dados, escalabilidade, read-replicas, postgresql, system-design]
skill: tech-mentor-system-design
status: stable
---

# Read Replicas

Cópias do banco primário que recebem apenas leituras. Escala reads horizontalmente sem tocar no primário.

## Roteamento explícito

```typescript
const primary = new PrismaClient({ datasourceUrl: PRIMARY_URL });
const replica = new PrismaClient({ datasourceUrl: REPLICA_URL });

const orders = await replica.order.findMany({ where: { userId } }); // leitura → réplica
const order = await primary.order.create({ data: orderData });      // escrita → primário
```

## Quando Usar

- ✅ Workload read-heavy (>80% reads)
- ✅ Queries analíticas pesadas que não podem afetar o primário
- ❌ Quando consistência imediata é obrigatória (saldos, inventário crítico)
- ❌ Como substituto para queries lentas — otimize [[concepts/database-index]] primeiro

## Read-Your-Writes

Problema: após escrever no primário, leitura na réplica pode não ver o dado ainda (replication lag). → [[concepts/read-your-writes]]

## Regra Prática: Relatório Nunca Bate em Produção

Relatório deve sempre consultar uma réplica, nunca o banco primário — no primário, o relatório concorre por recursos com processos mais críticos do sistema. Essa regra se sustenta porque a maioria dos sistemas lê muito mais do que escreve (escrita costuma ser ~10% do tempo), o que torna réplicas uma forma eficiente de ganhar escala sem sobrecarregar o primário. Ver [[wiki/sources/orm-sql-organizacao-regras-negocio-bancos-dados]].

## Key Sources

- [[sources/banco-de-dados]]
- [[wiki/sources/orm-sql-organizacao-regras-negocio-bancos-dados]]
