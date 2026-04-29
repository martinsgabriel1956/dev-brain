---
type: concept
title: "Raft / Paxos"
aliases: ["raft", "paxos", "consenso distribuído", "quorum consensus"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [sistemas-distribuidos, consenso, raft, paxos, quorum, etcd]
skill: tech-mentor-system-design
status: stub
---

# Raft / Paxos

Algoritmos de consenso distribuído que toleram partições de rede via quorum — diferente de [[concepts/two-phase-commit]] e [[concepts/three-phase-commit]].

## Mecanismo Central: Quorum

Uma decisão só avança se a maioria dos nós (quorum) concordar. Partição que isola minoria não consegue avançar — evita [[concepts/split-brain]].

## Raft vs Paxos

- **Paxos** — original (Lamport, 1989). Correto mas difícil de implementar e entender.
- **Raft** — projetado para ser compreensível. Mais usado em sistemas modernos.

## Uso Real

| Sistema | Algoritmo |
|---|---|
| etcd | Raft |
| CockroachDB | Raft |
| Kafka KRaft | Raft |
| Zookeeper | Zab (variante de Paxos) |
| Google Spanner | Paxos |

## Quando Usar

Para **consenso de liderança** e **replicação de log** com tolerância a partição. Não é um substituto direto para transações de aplicação — para isso, veja [[concepts/saga-pattern]] e [[concepts/distributed-transactions]].

## Key Sources

- [[sources/3pc]]
