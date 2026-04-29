---
date: 2026-04-17
tags: [tech-mentor, sistemas-distribuidos, consistencia, transacoes]
skill: tech-mentor-system-design/references/distributed-systems
level: avançado
---

# 3PC — Three-Phase Commit

## Contexto
O **2PC (Two-Phase Commit)** tem um problema crítico: se o coordinator cair durante a fase de commit, os participants ficam **bloqueados indefinidamente** — não sabem se devem commitar ou abortar, e ficam com o lock ativo até o coordinator recuperar.

O **3PC** foi proposto para resolver esse problema adicionando uma fase intermediária que permite aos participants se recuperar sem o coordinator.

## As Três Fases

```
Coordinator                  Participants
    │                             │
    │──── CanCommit? ────────────►│  Fase 1: PREPARE
    │◄─── Yes/No ─────────────────│
    │                             │
    │──── PreCommit ─────────────►│  Fase 2: PRE-COMMIT
    │◄─── ACK ────────────────────│  (participantes prontos, aguardando confirmação)
    │                             │
    │──── DoCommit ──────────────►│  Fase 3: COMMIT
    │◄─── ACK ────────────────────│
```

**Fase 1 (CanCommit?):** igual ao 2PC — "você consegue commitar?"

**Fase 2 (PreCommit):** coordinator confirma que todos estão prontos e envia PreCommit. **Esta fase não existe no 2PC.** Participants respondem ACK e entram no estado "prepared to commit".

**Fase 3 (DoCommit):** coordinator envia o commit final.

## O Que 3PC Resolve

Se o coordinator cair **após o PreCommit** mas **antes do DoCommit**, os participants podem se recuperar consultando uns aos outros:

```
Coordinator caiu após PreCommit

Participant A pergunta para B e C:
  "Vocês receberam PreCommit?"
  B: "Sim"
  C: "Sim"

Todos receberam PreCommit → assumem que o coordinator ia commitar → COMMIT
```

Se o coordinator cair **antes do PreCommit**, os participants ainda não confirmaram → ABORT.

## Por Que 3PC Não É Usado em Produção

O 3PC assume que **partições de rede não ocorrem** — só lida com falhas de crash. Em redes reais, partições são comuns e o 3PC fica vulnerável ao **"split-brain"**:

```
Coordinator + Participant A  ←──✗──→  Participant B

A e B ficam particionados após PreCommit.
A decide commitar (viu todos os ACKs antes da partição)
B, isolado, decide abortar por timeout
→ inconsistência: A commitou, B abortou
```

Este cenário é exatamente o que o **Raft** e o **Paxos** resolvem com quorum — eles toleram partições de rede, algo que o 3PC não consegue.

## Comparativo

| Aspecto | 2PC | 3PC | Raft/Paxos |
|---|---|---|---|
| Fases | 2 | 3 | Contínuo (log replication) |
| Blocking na falha do coordinator | Sim | Não (mas assume sem partição) | Não |
| Tolerância a partição de rede | Não | Não | Sim |
| Complexidade | Média | Alta | Muito alta |
| Uso real | Bancos relacionados (raramente) | Acadêmico | etcd, CockroachDB, Kafka KRaft |

## O Que Usar no Lugar

Para transações distribuídas em produção:

1. **Saga Pattern** — consistência eventual com compensação (sem locks distribuídos)
2. **Outbox + CDC** — garantia de entrega sem 2PC
3. **Raft/etcd** — para consenso real com tolerância a partição
4. **CockroachDB/Spanner** — implementam distributed transactions com consenso correto

## Conceitos Relacionados
[[two-phase-commit]] · [[saga-pattern]] · [[raft-leader-election]] · [[outbox-pattern]] · [[distributed-locks]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-17*
