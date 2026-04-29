---
type: source
title: "Offline-First Avançado — Sync, Conflict Resolution, CRDT"
aliases: ["mobile offline avancado", "sync conflict resolution mobile", "crdt mobile"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-offline-first-avancado.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, offline-first, sync, conflict-resolution, crdt, delta-sync, watermark]
skill: tech-mentor-mobile
status: stable
---

# Offline-First Avançado

## TL;DR

Sincronização avançada: delta sync com `updated_at` watermark (buscar apenas o que mudou), conflict resolution com Last-Write-Wins (timestamp) ou CRDT para colaboração simultânea. Fila de operações com idempotency key garante exatamente uma vez no servidor. PowerSync/WatermelonDB para sync automático. Conflitos devem ser detectados no servidor — cliente não tem autoridade.

## Claims Principais

| Claim | Confiança |
|---|---|
| Delta sync com watermark `updated_at` — buscar apenas registros novos desde o último sync | Alta |
| Last-Write-Wins com timestamp de servidor — não de cliente (clock skew) | Alta |
| CRDT para edição colaborativa simultânea sem conflito — Y.js, Automerge | Alta |
| Idempotency key em operações de escrita — retry seguro sem duplicação | Alta |
| Servidor tem autoridade em conflitos — cliente apresenta opções, server decide | Alta |

## Conceitos Abordados

- [[mobile-offline-first-avancado]] · [[mobile-offline-first-basico]] · [[mobile-armazenamento-local]] · [[crdt-colaboracao-tempo-real]]
