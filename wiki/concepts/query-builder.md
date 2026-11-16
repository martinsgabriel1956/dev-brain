---
type: concept
title: "Query builder"
aliases: ["construtor de queries", "query-builder SQL"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [sql, banco-de-dados, nodejs, abstracao]
skill: lang-dynamic
status: stub
---

# Query builder

Biblioteca que monta SQL com chamadas encadeadas na linguagem da aplicação, como `knex('users').where('name', 'Diego').select('*')` no lugar de `SELECT * FROM users WHERE name = 'Diego'`. Fica entre o SQL cru e o [[wiki/concepts/orm]]: não há entidades nem mapeamento de objetos, só a consulta.

Na aula de [[wiki/entities/diego-fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]), as vantagens do [[wiki/entities/knex]] são três: escrever "apenas JavaScript", ganhar o IntelliSense e trocar "do SQLite para o Postgres" sem mudar as queries.

**O que um query builder de fato dá:**

- **Valores parametrizados por padrão,** o que protege contra [[wiki/concepts/sql-injection]] desde que não se use `raw` com interpolação.
- **Composição:** filtros opcionais acrescentados com `if`, em vez de concatenar strings.
- **Sintaxe portável,** mas não comportamento portável: retorno de ids, tipos decimais, `ILIKE` e chaves estrangeiras variam por banco.

`[skill: lang-dynamic]` Em TypeScript, o Kysely tipa o resultado a partir do schema, coisa que o Knex não faz.

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: Knex x SQL; "um formato unificado para todos os bancos"
