---
type: concept
title: "ORM (Object-Relational Mapping)"
aliases: ["orm", "object relational mapping", "mapeamento objeto-relacional"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 1
tags: [orm, sql, banco-de-dados, prisma, hibernate, doctrine, abstracao]
skill: tech-mentor-backend
status: stub
---

# ORM (Object-Relational Mapping)

Camada que mapeia objetos/entidades do código para linhas de tabelas relacionais, permitindo escrever código declarativo em vez de SQL cru. Exemplos: Prisma e TypeORM (Node/TypeScript), Hibernate (Java), Doctrine (PHP), Sequelize.

## O Que um ORM Realmente É

Um ORM **não elimina SQL** — ele gera SQL por baixo dos panos a partir do código declarativo que você escreve. É uma abstração, não uma substituição do banco. Ver discussão em [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]].

```typescript
// Código declarativo (Prisma)
await db.user.findMany({ where: { active: true } })

// SQL gerado por baixo
SELECT * FROM users WHERE active = true;
```

## Por Que Usar

- Abstrai o banco da camada de domínio ([[wiki/concepts/postgresql]] pode ser trocado sem reescrever regra de negócio)
- Parametrização automática — mitiga [[wiki/concepts/sql-injection]] por padrão, desde que não se use raw query com interpolação
- Produtividade em CRUD — menos boilerplate que SQL manual

## Limitações (Leaky Abstraction)

Um ORM esconde SQL até você bater num caso de borda — query complexa, agregação pesada, ou performance ruim por N+1 queries. Nesses casos, entender o SQL gerado (ou escrever raw SQL) continua sendo necessário. Ver [[wiki/concepts/sql-alem-do-basico]] — dominar SQL além do ORM é um diferencial de portfólio.

## Alternativas

- **DSL customizada** — ver [[wiki/concepts/domain-specific-language]]
- **Raw SQL parametrizado** — mais controle, mais responsabilidade
- **Backend as a Service** (Supabase, Firebase) — abstrai a API, mas por baixo continua havendo um banco (Postgres, no caso do Supabase) executando SQL

## Key Sources

- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]]
