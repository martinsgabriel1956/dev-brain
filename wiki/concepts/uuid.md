---
type: concept
title: "UUID — Universally Unique Identifier"
aliases: ["uuid", "uuidv4", "uuidv7", "ulid", "nanoid"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 1
tags: [uuid, primary-key, distribuido, uuidv7, ulid, snowflake-id, banco-de-dados]
skill: tech-mentor-data
status: stub
---

# UUID

Identificador único de 128 bits projetado para ser gerado sem coordenação entre sistemas.

**Versões relevantes:**

| Versão | Base | Ordenável | Rastreável | Uso |
|---|---|---|---|---|
| v1 | Timestamp gregoriano + MAC | ❌ (LSB primeiro) | ✅ hardware | Legado |
| v4 | Totalmente aleatório | ❌ | ❌ | Mais comum, mas problemático como PK |
| v6 | Timestamp gregoriano (MSB primeiro) | ✅ | ✅ | Transição v1 → v7 |
| v7 | Unix Epoch + random | ✅ | ❌ | **Recomendado para PKs** |

**Problema como primary key no MySQL:** UUIDv4 causa page splitting no B+ Tree — inserts aleatórios forçam rebalanceamento constante; páginas ficam com ~50% de utilização ao invés de 94%.

**Solução:** UUIDv7 em `BINARY(16)` — ordenado temporalmente, distribuído, 128 bits compactos.

**Alternativas:**
- **Snowflake ID**: 64 bits, sequencial, requer worker_id de infra
- **ULID**: 128 bits, Base32, ordenável, compatível com UUID
- **NanoID**: URL-safe, compacto (~12 chars), não-ordenável

## Key Sources

- [[sources/uuid-primary-key-mysql]]
- [[sources/case-url-shortener]] (Snowflake ID como alternativa)
