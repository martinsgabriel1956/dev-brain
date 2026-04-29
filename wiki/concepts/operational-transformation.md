---
type: concept
title: "Operational Transformation (OT)"
aliases: ["ot", "operational transformation"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 1
tags: [ot, colaboracao-tempo-real, google-docs, servidor-central]
skill: tech-mentor-system-design
status: stub
---

# Operational Transformation

Algoritmo para edição colaborativa que transforma operações em relação ao estado atual antes de aplicá-las. Requer servidor central para sequenciar todas as operações — é o servidor que resolve conflitos.

**Quando usar:** histórico ordenado de operações é requisito, undo/redo colaborativo preciso.

**Usado por:** Google Docs, Etherpad.

**Limitações:** algoritmo de transformação é sutil e difícil de implementar corretamente; latência depende do round-trip ao servidor; offline limitado.

**Alternativa:** [[concepts/crdt]] — sem servidor central, offline-first nativo.

## Key Sources

- [[sources/crdt-colaboracao-tempo-real]]
