---
type: entity
title: "Knex.js"
aliases: ["Knex", "knex", "knexfile"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [nodejs, sql, query-builder, migrations, biblioteca]
skill: lang-dynamic
status: stub
---

# Knex.js

[[wiki/concepts/query-builder]] SQL para Node.js. Tem um cliente por banco (Postgres, MySQL/MariaDB, SQLite3, MSSQL, Oracle, Redshift), migrations, seeds, transações e pool de conexões. Não é ORM: não mapeia objetos nem relacionamentos ([[wiki/concepts/orm]]).

Na NLW #1 com [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]), é a camada de banco do Ecoleta:

- **Conexão:** `knex({ client: 'sqlite3', connection: { filename }, useNullAsDefault: true })` em `connection.ts`.
- **Consultas:** `knex('items').select('*')`, `where(...).first()`, `join`, `whereIn`, `distinct`.
- **[[wiki/concepts/database-migration|Migrations]]:** `up`/`down` com `schema.createTable` e `dropTable`, `knexfile.ts` com `module.exports`, `knex migrate:latest`. As tabelas `knex_migrations` e `knex_migrations_lock` controlam o que já rodou e impedem duas execuções ao mesmo tempo.
- **[[wiki/concepts/seed-de-banco-de-dados|Seeds]]:** `knex seed:run`.
- **[[wiki/concepts/database-transactions|Transações]]:** `const trx = await knex.transaction()` exige `trx.commit()`/`trx.rollback()` manuais (e o commit foi esquecido na aula). A forma com callback, `knex.transaction(async trx => ...)`, faz isso sozinha `[external]` (https://knexjs.org/guide/transactions.html).

**Diferenças entre bancos que o Knex não esconde:** `insert` só devolve ids no SQLite e no MySQL; no Postgres, só com `.returning('id')`. `decimal()` assume (8, 2). `[external]` (https://knexjs.org/guide/query-builder.html#insert).

`[skill: lang-dynamic]` Hoje, em projeto TypeScript, a skill prefere Kysely (query builder com tipos do schema), Drizzle ([[wiki/concepts/drizzle-orm]]) ou Prisma.

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: conexão, migrations, seeds, transação, join/whereIn
