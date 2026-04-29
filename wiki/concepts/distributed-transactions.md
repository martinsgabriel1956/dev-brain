---
type: concept
title: "Distributed Transactions"
aliases: ["transações distribuídas", "transações em microsserviços"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [sistemas-distribuidos, consistencia, transacoes, microsservicos]
skill: tech-mentor-system-design
status: stub
---

# Distributed Transactions

Garantia de atomicidade entre múltiplos serviços ou bancos de dados independentes.

## O Problema

Em microsserviços, cada serviço tem seu próprio banco. Não existe transação ACID nativa entre eles. Coordenar commits requer protocolo explícito.

## Abordagens

| Abordagem | Consistência | Locks | Uso |
|---|---|---|---|
| [[concepts/two-phase-commit]] | Forte | Sim (blocking) | Raramente em prod |
| [[concepts/three-phase-commit]] | Forte* | Não* | Acadêmico |
| [[concepts/saga-pattern]] | Eventual | Não | Microsserviços |
| [[concepts/outbox-pattern]] | Eventual (at-least-once) | Não | Eventos/mensageria |
| CockroachDB/Spanner | Forte | Via [[concepts/raft-paxos]] | Banco distribuído |

*apenas sem partições de rede

## Regra Prática

Para a maioria dos casos em microsserviços: **Saga + Outbox**. Para consenso de infraestrutura: **Raft (etcd)**. 2PC e 3PC como protocolo de aplicação: evite.

## Key Sources

- [[sources/3pc]]
