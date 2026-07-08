---
type: concept
title: "Database Transactions"
aliases: ["transações", "prisma transaction", "$transaction"]
date_created: 2026-04-22
date_updated: 2026-07-03
source_count: 3
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

## Isolamento: Nuance Sobre Transações Concorrentes

Duas transações concorrentes sobre o mesmo dado não deixam de rodar — Isolation não significa que uma "espera educadamente" a outra sem competir. Se duas transações tentam escrever valores diferentes no mesmo saldo (ex.: uma seta `0`, outra seta `15`) ao mesmo tempo, ambas efetivamente executam; o valor final é um dos dois, nunca uma mistura — consistente com alguma ordem serial válida, não necessariamente com "nenhuma interferência". Ver [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]].

## Key Sources

- [[sources/banco-de-dados]]
- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]]
- [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]] — mesmo exemplo de transferência bancária para atomicidade; nuance sobre isolamento em escritas concorrentes
