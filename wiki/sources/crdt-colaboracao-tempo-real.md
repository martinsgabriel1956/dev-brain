---
type: source
title: "CRDT e Colaboração em Tempo Real"
aliases: ["crdt", "operational transformation", "yjs", "colaboração tempo real"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 0
tags: [crdt, ot, yjs, colaboracao-tempo-real, offline-first, websocket, system-design]
skill: tech-mentor-system-design
status: draft
source_file: /home/nemomartins/Documentos/new/dev-study/raw/crdt-colaboracao-tempo-real.md
source_url:
author:
date_published:
date_ingested: 2026-04-23
---

# CRDT e Colaboração em Tempo Real

## TL;DR

Sistemas colaborativos (Google Docs, Figma, Notion) precisam resolver conflitos de edição simultânea sem coordenação centralizada bloqueante. OT (Operational Transformation) usa servidor central para sequenciar operações; CRDT é uma estrutura de dados que sempre converge deterministicamente, permite offline-first e P2P. Y.js é o padrão da indústria para CRDT de sequência.

## Key Claims

| Claim | Evidência |
|---|---|
| OT requer servidor central obrigatório | Precisa sequenciar todas as ops — Google Docs, Etherpad |
| CRDT não precisa de servidor central | P2P possível; Figma, Linear, Y.js, Liveblocks o usam |
| Y.js é o padrão da indústria | Biblioteca mais madura para texto colaborativo com CRDT |
| CRDT tem 3 propriedades formais | Comutatividade, associatividade, idempotência das ops de merge |
| Escala: sharding por documento (room) | Cada documento em um nó de relay; conexões do mesmo doc no mesmo nó |

## Conceitos

- [[concepts/crdt]] — Conflict-free Replicated Data Type
- [[concepts/operational-transformation]] — OT, alternativa com servidor central
- [[concepts/offline-first]] — design que aplica mudanças localmente e sincroniza depois
- [[concepts/presenca-online]] — cursores e presença em sistemas colaborativos
- [[concepts/websocket-vs-polling]] — transporte usado pelo relay server

## Entidades

- [[entities/yjs]] — biblioteca CRDT de sequência, padrão da indústria
- [[entities/figma]] — usa CRDT para colaboração em design
- [[entities/linear-app]] — usa Y.js para edição colaborativa

## Open Questions

- Quando OT é preferível a CRDT mesmo com a complexidade do servidor central (undo/redo colaborativo preciso)?
- Y.js vs Automerge: qual é a diferença prática de performance?

## Key Sources

_Este é o documento primário._
