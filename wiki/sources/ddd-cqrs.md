---
type: source
title: "DDD com CQRS"
aliases: ["ddd cqrs", "command query separation", "read model", "write model", "projecao"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/ddd-cqrs.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [ddd, cqrs, command-side, query-side, read-model, projection, consistencia-eventual, event-driven]
skill: tech-mentor-backend
status: stable
---

## TL;DR

CQRS separa o modelo de escrita (Command Side — Aggregate normalizado, regras de negócio) do modelo de leitura (Query Side — Read Model desnormalizado, otimizado para queries). Projeções sincronizam Command→Query via Domain Events. O preço: consistência eventual no Read Model. Justifica quando queries complexas conflitam com o modelo de escrita.

## Key Claims

**Claim:** O problema que CQRS resolve: o mesmo modelo não serve bem para escrita e leitura simultaneamente.
**Evidence:** Aggregate normalizado com invariantes é ótimo para escrita (garante consistência). Péssimo para leitura (N JOINs, cálculos em tempo de query). Read Model desnormalizado é ótimo para leitura. Péssimo para escrita (duplicação, inconsistência). CQRS mantém os dois separados.
**Confidence:** alta

**Claim:** Projeções são event handlers que mantêm o Read Model sincronizado com o Command Side.
**Evidence:** OrderPlacedEvent dispara OrderPlacedProjector que atualiza `order_summaries` (tabela desnormalizada). Leitura de orders vai direto para essa tabela — zero JOINs. Atraso entre escrita e leitura = consistência eventual (geralmente < 100ms).
**Confidence:** alta

**Claim:** CQRS é over-engineering sem escala ou complexidade de query que justifique.
**Evidence:** Para apps simples, CQRS adiciona: projeções, event handlers, dois modelos, eventual consistency. O benefício (queries performáticas) só aparece quando as queries são realmente complexas ou o volume justifica read replicas separadas.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/cqrs]]
- [[concepts/ddd-tactical]]
- [[concepts/read-model]]
- [[concepts/projection]]
- [[concepts/consistencia-eventual]]
- [[concepts/event-driven]]

## Open Questions

- Como lidar com queries que precisam de consistência forte (ex: saldo de conta) em arquitetura CQRS com eventual consistency?
- Qual o mecanismo de sincronização entre Command Side e Query Side em caso de falha do event handler?
