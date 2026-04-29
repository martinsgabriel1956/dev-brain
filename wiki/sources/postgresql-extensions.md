---
type: source
title: "PostgreSQL Avançado — pg_partman, pglogical, pg_repack, Savepoints"
aliases: ["postgresql extensions", "pg_partman", "pglogical", "pg_repack", "savepoints", "particionamento postgresql"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/postgresql-extensions.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [postgresql, pg-partman, pglogical, pg-repack, savepoints, particionamento, replicacao-logica, desfragmentacao, nested-transactions]
skill: tech-mentor-data
status: stable
---

## TL;DR

4 extensões avançadas do PostgreSQL: pg_partman (particionamento automático com retenção), pglogical (replicação lógica entre versões diferentes), pg_repack (desfragmentação sem lock exclusivo — alternativa ao VACUUM FULL), Savepoints (nested transactions com rollback parcial).

## Key Claims

**Claim:** pg_partman automatiza particionamento e retenção — DROP de partição antiga é O(1) vs DELETE O(n).
**Evidence:** `DROP TABLE events_2024_01` é instantâneo. `DELETE FROM events WHERE created_at < '2024-02-01'` requer vacuum, gera dead tuples, pode durar horas em tabelas grandes. Particionamento por mês + retenção de 12 meses via pg_partman = operação automática e barata.
**Confidence:** alta

**Claim:** pg_repack desfragmenta tabelas sem lock exclusivo — VACUUM FULL pode ser substituído.
**Evidence:** VACUUM FULL requer lock exclusivo — tabela inacessível durante operação que pode durar horas. pg_repack cria tabela temporária, replica mudanças via trigger, faz swap atômico. A aplicação continua operando durante a operação.
**Confidence:** alta

**Claim:** pglogical permite replicação lógica entre versões diferentes do PostgreSQL — essencial para upgrades zero-downtime.
**Evidence:** Replicação física: mesma versão obrigatória. pglogical replicação lógica: PostgreSQL 12 → PostgreSQL 16 em paralelo. Estratégia de upgrade: replica para nova versão, valida, faz failover, sem downtime.
**Confidence:** alta

**Claim:** Savepoints permitem rollback parcial de transação — sem abortar a transação inteira.
**Evidence:** `SAVEPOINT sp1` + operação que falha + `ROLLBACK TO SAVEPOINT sp1` = volta para o ponto, transação continua. Útil para: batch insert com falhas parciais toleráveis, lógica de retry dentro de uma transação.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/particionamento-postgresql]]
- [[concepts/pg-partman]]
- [[concepts/pg-repack]]
- [[concepts/pglogical]]
- [[concepts/savepoints]]
- [[concepts/vacuum-postgresql]]

## Open Questions

- pg_partman com particionamento HASH para distribuição uniforme — como redistribuir partições se o N mudar?
- pglogical em upgrade de major version: como lidar com extensões que têm mudanças no schema do sistema?
