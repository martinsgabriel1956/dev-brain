---
type: source
title: "Paginação — Keyset, Cursor e Offset"
aliases: ["paginação", "pagination", "cursor pagination", "keyset pagination", "offset pagination", "seek method"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/pagination.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [pagination, keyset-pagination, cursor-pagination, offset-pagination, seek-method, performance, postgresql]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Offset Pagination (`LIMIT x OFFSET y`) é O(n) — degrada com tabelas grandes e tem phantom records em dados que mudam. Keyset Pagination (Seek Method): filtra pela última row vista (`WHERE (created_at, id) < (last_created_at, last_id)`) — O(log n) com índice composto, estável. Cursor Opaco: encoda o keyset em base64 para o cliente, esconde implementação interna. Bidirecional: `before` e `after` cursors.

## Key Claims

**Claim:** Offset Pagination degrada em tabelas grandes — `OFFSET 10000` faz o banco escanear e descartar 10k rows.
**Evidence:** `SELECT * FROM posts LIMIT 20 OFFSET 10000`: PostgreSQL lê e descarta as primeiras 10.000 rows antes de retornar as 20 desejadas. Performance: O(offset). Com 1M rows e página 50k, cada query escaneia 50k rows. Keyset: `WHERE id > last_id LIMIT 20` usa índice, O(log n) independente da profundidade.
**Confidence:** alta

**Claim:** Keyset Pagination requer índice composto no cursor field + campo de desempate — sem índice, degrada para full scan.
**Evidence:** `WHERE (created_at, id) < (last_created_at, last_id) ORDER BY created_at DESC, id ASC`: índice `(created_at DESC, id ASC)` permite index scan direto ao ponto de partida. Sem índice: full table scan + filter. Para cursor bidirecional: índice na direção oposta também.
**Confidence:** alta

**Claim:** Cursor Opaco em base64 esconde o mecanismo de paginação — cliente não depende do formato interno.
**Evidence:** Expor `?after=2024-01-15T10:30:00Z_uuid` acopla clientes ao formato. Se mudar de keyset para outro mecanismo, todos os clientes quebram. Cursor opaco: `?after=eyJjcmVhdGVkQXQiOiIyMDI0LTAxLTE1In0=` — string base64 que o servidor decodifica. Clientes tratam como token opaco.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/keyset-pagination]]
- [[concepts/cursor-pagination]]
- [[concepts/offset-pagination]]
- [[concepts/seek-method]]
- [[concepts/pagination-performance]]

## Open Questions

- Paginação em dados que precisam de ordenação por relevância (score) — como fazer keyset quando o score muda?
- Paginação bidirecional em APIs públicas — como lidar com clients que armazenam cursors e os usam após semanas?
