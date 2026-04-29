---
type: concept
title: "Three-Phase Commit (3PC)"
aliases: ["3pc", "three phase commit", "protocolo de três fases"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [sistemas-distribuidos, consistencia, transacoes, 3pc, academico]
skill: tech-mentor-system-design
status: stable
---

# Three-Phase Commit (3PC)

Extensão do [[concepts/two-phase-commit]] que adiciona fase PreCommit para eliminar blocking quando coordinator falha. **Uso real: acadêmico.**

## As Três Fases

```
Coordinator                  Participants
    │──── CanCommit? ────────────►│  Fase 1: PREPARE
    │◄─── Yes/No ─────────────────│
    │                             │
    │──── PreCommit ─────────────►│  Fase 2: PRE-COMMIT  ← nova fase
    │◄─── ACK ────────────────────│
    │                             │
    │──── DoCommit ──────────────►│  Fase 3: COMMIT
    │◄─── ACK ────────────────────│
```

## O que Resolve vs 2PC

Se coordinator cai **após PreCommit**: participants consultam uns aos outros, todos receberam PreCommit → assumem commit → COMMIT sem blocking.

Se coordinator cai **antes do PreCommit**: participants não confirmaram → ABORT.

## Por que Não é Usado em Produção

Assume que partições de rede não ocorrem. Em redes reais, partição após PreCommit causa [[concepts/split-brain]]:

```
Coordinator + A  ←──✗──→  B

A: viu todos os ACKs → COMMIT
B: isolado, timeout → ABORT
→ inconsistência
```

## Comparativo

| Aspecto | 2PC | 3PC | Raft/Paxos |
|---|---|---|---|
| Blocking na falha | Sim | Não* | Não |
| Tolerância a partição | Não | Não | Sim |
| Uso real | Raramente | Acadêmico | etcd, CockroachDB |

*apenas se não houver partição

## Alternativas para Produção

→ [[concepts/saga-pattern]], [[concepts/outbox-pattern]], [[concepts/raft-paxos]], [[concepts/distributed-transactions]]

## Key Sources

- [[sources/3pc]]
