---
type: concept
title: "CRDT — Conflict-free Replicated Data Type"
aliases: ["crdt", "conflict free replicated data type"]
date_created: 2026-04-23
date_updated: 2026-09-04
source_count: 2
tags: [crdt, colaboracao-tempo-real, offline-first, local-first, convergencia, distribuido]
skill: tech-mentor-system-design
status: stub
---

# CRDT

Estrutura de dados projetada para ser replicada em múltiplos nós e sempre convergir para o mesmo estado, independente da ordem de recebimento das operações. Não precisa de servidor central de coordenação.

**Propriedades formais:** comutatividade, associatividade e idempotência das operações de merge.

**Tipos básicos:** G-Counter (incremento apenas), PN-Counter (inc/dec), LWW-Register (last-write-wins), OR-Set (add/remove).

**Para texto colaborativo:** CRDT de sequência — Logoot/LSEQ ou Y.js (padrão da indústria).

**Trade-off vs OT:** OT preserva histórico e permite undo/redo colaborativo preciso; CRDT é mais simples de implementar, suporta offline-first e P2P.

## Relação com Local-First

Em arquiteturas [[wiki/concepts/local-first]], CRDT é a alternativa a [[wiki/concepts/last-write-wins]] para resolver conflitos entre réplicas que editaram offline: em vez de a escrita mais recente sobrescrever silenciosamente as demais, o merge converge deterministicamente sem descartar dados — ao custo de maior complexidade de implementação.

## Key Sources

- [[sources/crdt-colaboracao-tempo-real]]
- [[wiki/sources/local-first-vs-offline-first]]
