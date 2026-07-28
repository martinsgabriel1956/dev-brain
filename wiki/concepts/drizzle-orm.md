---
type: concept
title: "Drizzle ORM"
aliases: ["drizzle", "drizzle-orm", "drizzle-kit"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 2
tags: [orm, typescript, drizzle, migrations, postgresql, sql, graphql, n-plus-one, left-join]
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

## Ergonomia Próxima de SQL — e de GraphQL

O Drizzle expõe uma API de query com sintaxe quase idêntica a SQL puro:

```typescript
db.select().from(users).leftJoin(posts, eq(users.id, posts.userId))
```

O ganho de usar essa camada em vez de escrever SQL puro é o **type safety**: o Drizzle sabe o que a query retorna e devolve um objeto tipado.

Além disso, o Drizzle tem **relational queries**, com sintaxe deliberadamente parecida com [[wiki/concepts/graphql]] — pedir uma estrutura aninhada numa chamada só, em vez de compor JOINs manualmente:

```typescript
db.query.users.findMany({
  with: { posts: true },
})
```

Isso **não é GraphQL** — é syntax sugar para trazer, na camada backend↔banco, uma ergonomia parecida com a que o GraphQL oferece na camada frontend↔backend, resolvendo o mesmo tipo de [[wiki/concepts/n-plus-one|N+1]] sem precisar compor um LEFT JOIN manual. Ver [[wiki/sources/problema-n-mais-1-graphql-orm-solucoes]].

## Key Sources

- [[wiki/sources/database-migrations-sql-cru-vs-orm-drizzle]]
- [[wiki/sources/problema-n-mais-1-graphql-orm-solucoes]] — relational queries inspiradas em GraphQL, LEFT JOIN equivalente
