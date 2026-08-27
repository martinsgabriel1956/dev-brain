---
type: concept
title: "Read Replicas"
aliases: ["réplica de leitura", "read replica", "replica routing"]
date_created: 2026-04-22
date_updated: 2026-08-27
source_count: 9
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

## Relação com CQRS

Read replicas são o mecanismo concreto por trás do read/write split usado em [[wiki/concepts/cqrs]]: banco de escrita (write) separado do banco de leitura (read/réplicas), escalados independentemente. O mesmo trade-off de replication lag citado acima se aplica — a fonte didática estima 1-3 segundos de delay entre a escrita e a réplica refletir o dado. Ver [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]].

## Read Replica Não É Escalabilidade Horizontal do Banco

[[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]] marca essa distinção explicitamente ao apresentar sharding: read replica escala apenas **leitura/performance** — a escrita continua concentrada no primário. Escalar tanto leitura quanto escrita horizontalmente exige [[wiki/concepts/sharding]], que distribui dados diferentes (não cópias do mesmo dado) entre nós independentes.

## Caso: Réplicas Servindo Rotas de Histórico/Estatística, Não o Placar ao Vivo

[[wiki/sources/world-cup-system-design]] mostra um Web Server que consulta **réplicas de leitura** (`Replica 1`, `Replica 2`) diretamente para as rotas de histórico e estatística (`/matches/{id}/statistic`, `/team/{id}/history`, `/player/{id}/history`) — dados que não mudam a cada segundo e toleram alguma defasagem — enquanto o placar ao vivo (`/matches/{id}/stream`) segue um caminho totalmente separado via [[wiki/concepts/redis]]. É uma divisão de responsabilidade por volatilidade do dado: o que muda a cada evento vai para cache pré-computado; o que muda pouco (histórico consolidado) vai para réplica de banco relacional.

## Réplicas Preservam Schema — Diferença Chave Frente a Eventos

[[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]] marca uma distinção explícita entre as duas formas mais comuns de consistência eventual em CQRS: com read replicas, o read model **preserva exatamente o schema** da base de escrita (mesmas tabelas, colunas, esquema); com sincronização via eventos, o query service pode transformar a informação livremente no formato final que quiser ao consumir (ex.: escrita relacional → leitura em Elasticsearch). Read replicas são, portanto, a opção mais simples quando o objetivo é só volume — não quando o objetivo também inclui divergência de modelo.

## Key Sources

- [[sources/banco-de-dados]]
- [[wiki/sources/cqrs-volume-modelo-consistencia-forte-eventual]] — read replicas como opção de consistência eventual no CQRS que preserva o schema da escrita, em contraste com eventos (que permitem transformação livre do modelo)
- [[wiki/sources/orm-sql-organizacao-regras-negocio-bancos-dados]]
- [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]] — read replicas como base do read/write split em CQRS, com replication lag estimado em 1-3s
- [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]] — distinção explícita entre read replica (escala leitura) e sharding (escala leitura e escrita)
- [[wiki/sources/escalar-leituras-banco-de-dados-entrevista-tier-s]] — read replica como "load balancer de banco de dados" (primário só escreve, réplicas só leem), terceiro degrau da escada de leitura (200-300k+ req/s); tradeoff de replication lag "de até segundos" é o ponto que corta candidatos que não o citam — crítico para fintech, tolerável para feed social
- [[wiki/sources/escalar-para-um-milhao-de-usuarios]] — justificativa didática do read/write split: "a maioria das aplicações lê mais do que escreve", então um banco de escrita alimenta réplicas de leitura
- [[wiki/sources/world-cup-system-design]] — réplicas servindo rotas de histórico/estatística separadas do caminho de placar ao vivo (Redis), divisão por volatilidade do dado
- [[wiki/sources/escalando-aplicacao-zero-a-um-milhao-usuarios-renato-augusto]] — mesma justificativa didática ("a maioria das aplicações lê mais do que escreve"), com exemplo concreto de roteamento no Laravel (chaves `read`/`write`) e cluster Amazon Aurora
