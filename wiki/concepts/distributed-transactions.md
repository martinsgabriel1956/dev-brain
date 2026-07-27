---
type: concept
title: "Distributed Transactions"
aliases: ["transações distribuídas", "transações em microsserviços"]
date_created: 2026-04-22
date_updated: 2026-07-27
source_count: 2
tags: [sistemas-distribuidos, consistencia, transacoes, microsservicos, idempotencia]
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

## Transação Não É Idempotência

Transação e [[wiki/concepts/idempotencia]] resolvem problemas diferentes e complementares, não intercambiáveis: a transação impede que uma operação fique **pela metade** (débito sem crédito correspondente); a idempotência impede que a operação **inteira** aconteça duas vezes por retry. Um pagamento pode estar perfeitamente atômico (ou aconteceu por completo, ou não aconteceu) e ainda assim ser cobrado duas vezes se nenhuma chave idempotente identificar que duas tentativas representam a mesma intenção. Produtos financeiros geralmente precisam das duas proteções no mesmo fluxo.

## Key Sources

- [[sources/3pc]]
- [[wiki/sources/idempotencia-pagamentos-retry-sistemas-distribuidos]] — distinção explícita entre o que a transação resolve e o que a idempotência resolve
