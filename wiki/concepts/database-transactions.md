---
type: concept
title: "Database Transactions"
aliases: ["transações", "prisma transaction", "$transaction"]
date_created: 2026-04-22
date_updated: 2026-07-03
source_count: 2
tags: [banco-de-dados, acid, transactions, prisma, postgresql]
skill: tech-mentor-system-design
status: stable
---

# Database Transactions

Mecanismo que garante que operações dependentes ocorram como uma unidade atômica. → [[concepts/acid]]

## Problema sem transação

```typescript
// ❌ Se a segunda falhar, a primeira já foi executada
await db.account.update({ where: { id: fromId }, data: { balance: { decrement: 100 } } });
await db.account.update({ where: { id: toId }, data: { balance: { increment: 100 } } });
```

## Solução

```typescript
// ✅ Ou as duas ocorrem, ou nenhuma
await db.$transaction(async tx => {
  await tx.account.update({ where: { id: fromId }, data: { balance: { decrement: 100 } } });
  await tx.account.update({ where: { id: toId }, data: { balance: { increment: 100 } } });
});
```

## Regra

Toda operação Prisma com dependência entre queries **deve** usar `$transaction`. Sem isso, qualquer falha parcial deixa o banco em estado inválido — viola Atomicity do [[concepts/acid]].

## Por Que É Difícil de Reimplementar

Se você tentasse fazer um fork de um banco relacional sem SQL (ex: trocar o parser/VM do SQLite por uma DSL própria), transactions são citadas como a parte genuinamente difícil de recriar — junto com indexação e otimização de queries. Acessar os dados brutos é trivial; garantir atomicidade sob concorrência não é. Ver [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]].

## Key Sources

- [[sources/banco-de-dados]]
- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]]
