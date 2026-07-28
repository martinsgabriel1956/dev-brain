---
type: concept
title: "Drizzle ORM"
aliases: ["drizzle", "drizzle-orm", "drizzle-kit"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [orm, typescript, drizzle, migrations, postgresql, sql]
skill: tech-mentor-backend
status: stub
---

# Drizzle ORM

[[wiki/concepts/orm]] mínima para TypeScript/JavaScript, citada como alternativa mais enxuta a Prisma/TypeORM — fica próxima de SQL puro, mas garante schema explícito, geração automática de arquivos de [[wiki/concepts/database-migration|migration]] e type safety.

## Fluxo Básico

1. Declarar o schema em TypeScript (`pgTable`, colunas com tipo, constraints como `.notNull()`, `.unique()`).
2. `drizzle-kit generate` — compara o schema declarado com o histórico interno (journal + snapshots) e gera os arquivos de migration necessários para o diff.
3. `drizzle-kit migrate` (ou script próprio) — aplica as migrations pendentes no banco.
4. Queries feitas via API do Drizzle no código da aplicação.

Alterar o schema (adicionar/remover campo) e rodar `generate` novamente cria uma nova migration derivada do diff — sem precisar escrever SQL manualmente na maioria dos casos.

## Pacotes

`drizzle-orm` (runtime/query API) + `drizzle-kit` (CLI para generate/migrate, dependência de desenvolvimento).

## Key Sources

- [[wiki/sources/database-migrations-sql-cru-vs-orm-drizzle]]
