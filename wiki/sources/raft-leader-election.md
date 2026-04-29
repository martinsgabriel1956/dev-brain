---
type: source
title: "Raft e Leader Election"
aliases: ["raft consensus", "leader election", "etcd raft", "log replication"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 0
tags: [raft, leader-election, consenso, etcd, log-replication, quorum, split-brain, system-design]
skill: tech-mentor-system-design
status: draft
source_file: /home/nemomartins/Documentos/new/dev-study/raw/raft-leader-election.md
source_url:
author:
date_published:
date_ingested: 2026-04-23
---

# Raft e Leader Election

## TL;DR

Raft é o algoritmo de consenso mais legível e amplamente usado (etcd, CockroachDB, Consul, TiKV). Três papéis: Leader (único, escreve), Follower (replica), Candidate (em eleição). Eleição: timeout aleatório (150–300ms) evita split vote; precisa de quorum (N/2+1) para ganhar. Replicação de log: leader envia AppendEntries; só committa quando maioria confirma. Safety: nenhum nó com log incompleto pode se tornar líder.

## Key Claims

| Claim | Evidência |
|---|---|
| Timeout aleatório (150–300ms) evita empate em eleição | Design paper do Raft — Ongaro & Ousterhout |
| Quorum = N/2 + 1 — cluster de 3 tolera 1 falha; de 5 tolera 2 | Matemática de quorum |
| Log entry só é committada quando maioria confirma | Safety: dado committado nunca é perdido |
| Candidato com log atrasado não pode ganhar eleição | Votante compara term e índice do log |
| Log compaction via snapshot evita crescimento ilimitado do log | etcd usa snapshots periódicos |
| etcd é o uso canônico do Raft — Kubernetes o usa para estado do cluster | Kubernetes API server → etcd |

## Conceitos

- [[concepts/raft-paxos]] — já existe no index
- [[concepts/split-brain]] — o que Raft previne com quorum
- [[concepts/quorum]] — fundação matemática da eleição
- [[concepts/distributed-lock]] — leader election como forma de lock distribuído
- [[concepts/consistency-models]] — Raft garante linearizabilidade

## Key Sources

_Este é o documento primário._
