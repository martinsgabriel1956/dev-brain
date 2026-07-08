---
type: source
title: "O Problema de Usar UUID como Primary Key no MySQL"
aliases: ["uuid mysql", "uuidv4 performance", "page splitting uuid"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 0
tags: [uuid, primary-key, mysql, page-splitting, btree, storage, uuidv7, snowflake-id, banco-de-dados]
skill: tech-mentor-data
status: draft
source_file: /home/nemomartins/Documentos/new/dev-study/raw/uuid-primary-key-mysql.md
source_url: https://planetscale.com/blog/the-problem-with-using-a-uuid-primary-key-in-mysql
author: Brian Morrison II (PlanetScale)
date_published: 2024-03-19
date_ingested: 2026-04-23
---

# O Problema de Usar UUID como Primary Key no MySQL

## TL;DR

UUIDv4 (aleatório) como primary key no MySQL causa dois problemas sérios: page splitting no B+ Tree (inserts aleatórios forçam rebalanceamento constante, páginas ficam 50% vazias, performance cai até 10x) e storage excessivo (CHAR(36) = 288 bits vs 32 bits do auto-increment). Solução: usar UUIDv7 em `BINARY(16)` — ordenado por timestamp Unix Epoch, distribuído, sem coordenação central.

## Key Claims

| Claim | Evidência |
|---|---|
| UUIDv4 causa page splitting — páginas ficam com ~50% de utilização | MySQL assume PK sequencial e preenche a 94%; com random, divide as páginas |
| `CHAR(36)` consome 288 bits por UUID vs 32 bits do INT | 9x mais storage; secondary indexes também armazenam o PK |
| UUIDv7 resolve o problema — Unix Epoch timestamp primeiro, resto random | Inserts sequenciais por tempo, sem rastreabilidade de hardware |
| `UUID_TO_BIN(uuid, 1)` com swap flag torna UUIDv1 sequencial no MySQL | Reordena bits do timestamp — solução para quem já usa MySQL built-in |
| Alternativas: Snowflake ID (64 bits, sequencial), ULID, NanoID | PlanetScale usa NanoID internamente |

## Conceitos

- [[wiki/concepts/mysql]] — comportamento de índice/lock do InnoDB, ver também caso de gap locking e reserva de estoque em [[wiki/sources/shopify-redis-para-mysql-skip-locked-black-friday]]
- [[concepts/uuid]] — versões, trade-offs e quando usar cada uma
- [[concepts/page-splitting]] — rebalanceamento do B+ Tree com chaves aleatórias
- [[concepts/database-index]] — B+ Tree, como primary key afeta toda indexação
- [[concepts/snowflake-id]] — alternativa de 64 bits, sequencial e distribuída
- [[concepts/db-sharding]] — UUID é comum em sharding por evitar colisão entre shards

## Open Questions

- UUIDv7 já tem suporte nativo em PostgreSQL 17+ (`gen_random_uuid` ainda gera v4 — precisa de extensão)?
- ULID vs UUIDv7: qual é preferível em novos projetos?

## Key Sources

_Este é o documento primário._
