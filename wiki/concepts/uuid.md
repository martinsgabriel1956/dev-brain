---
type: concept
title: "UUID — Universally Unique Identifier"
aliases: ["uuid", "uuidv4", "uuidv7", "ulid", "nanoid"]
date_created: 2026-04-23
date_updated: 2026-08-06
source_count: 2
tags: [uuid, primary-key, distribuido, uuidv7, ulid, snowflake-id, banco-de-dados, idor, sharding]
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

## Quando vale a pena usar (além de performance)

[[wiki/sources/uuid-quando-usar-pergunta-diogo]] discute UUID sob a ótica de decisão de arquitetura, não apenas de índice, com dois argumentos de negócio:

1. **Merge de bases separadas por shard/cliente/região.** Chaves sequenciais colidem ao consolidar bases distintas em um único banco — cenário comum em [[wiki/concepts/db-sharding]]. UUID, por ter colisão praticamente impossível (128 bits randômicos), evita a reescrita manual de chaves que esse merge normalmente exige.
2. **Dificultar enumeração de recursos (mitigação parcial de [[wiki/concepts/idor]]).** IDs sequenciais expostos em URL de API REST (`/organizacoes/1/usuarios/2`) permitem que um atacante varie o número e acesse dados de outro usuário/cliente, especialmente em sistemas multi-tenant com tabelas compartilhadas. UUID como identificador público dificulta esse ataque — mas não substitui checagem de autorização real (`WHERE id = $1 AND user_id = $2`), é defesa complementar.

**Estratégia híbrida** (evita as desvantagens de espaço/performance nas queries internas, mantendo a proteção onde importa): sequência inteira (int) usada internamente em joins e queries; UUID/hash gerado só nas tabelas expostas por rota pública. Ganha agilidade de índice/comparação internamente e ainda dificulta enumeração externamente.

## Key Sources

- [[sources/uuid-primary-key-mysql]]
- [[sources/case-url-shortener]] (Snowflake ID como alternativa)
- [[wiki/sources/uuid-quando-usar-pergunta-diogo]] — argumentos de negócio para UUID (merge de shards, anti-enumeração) e estratégia híbrida sequência-interna + UUID-público
