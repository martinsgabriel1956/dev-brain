---
type: concept
title: "Mass Assignment (BOPLA)"
aliases: ["mass assignment", "bopla", "broken object property level authorization", "atribuicao em massa"]
date_created: 2026-07-04
date_updated: 2026-07-04
source_count: 1
tags: [mass-assignment, bopla, owasp, api-security, appsec]
skill: tech-mentor-security
status: stable
---

# Mass Assignment (BOPLA)

Vulnerabilidade onde um endpoint de escrita (`PATCH`/`PUT`) aceita o corpo da requisição inteiro e o aplica direto no objeto persistido, sem restringir quais campos o cliente pode de fato alterar. O atacante inclui uma propriedade que não deveria poder mudar — como `role` ou `isAdmin` — e ela é aceita junto com os campos legítimos.

## O padrão do bug

```typescript
// VULNERÁVEL
app.patch('/api/users/:id', async (req) => {
  await db.update('users', req.body, { id: req.params.id })
  // req.body pode conter { "username": "novo", "role": "admin" }
})
```

O usuário pretende só mudar o `username`, mas como o servidor não filtra o body, também consegue promover a própria conta a administrador.

## Correção

Whitelist explícita de campos por endpoint — nunca passar `req.body` inteiro para o `update`/`create`, mesmo em ORMs como Prisma ou TypeORM:

```typescript
// CORRETO
app.patch('/api/users/:id', async (req) => {
  const { name, email, bio } = req.body // só esses campos existem daqui pra frente
  await db.update('users', { name, email, bio }, { id: req.params.id })
})
```

## Ver também

- [[wiki/concepts/idor]] — falha irmã: mesmo erro de confiar em input do cliente, mas em leitura (acesso) em vez de escrita (alteração)

## Key Sources

- [[wiki/sources/owasp-top10]]
- [[wiki/sources/vulnerabilidades-comuns-seguranca-apps]]
