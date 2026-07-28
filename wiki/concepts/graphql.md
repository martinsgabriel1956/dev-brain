---
type: concept
title: "GraphQL"
aliases: ["graphql", "graph query language"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [graphql, api-design, n-plus-one, dataloader, meta, frontend-backend, over-fetching, under-fetching]
skill: tech-mentor-backend
status: draft
---

# GraphQL

Linguagem de query para APIs, criada pela [[wiki/entities/meta]] (então Facebook), que fica na camada **entre frontend e backend**. Em vez de o servidor definir endpoints fixos com um formato de resposta rígido, o cliente descreve exatamente a estrutura de dados que quer — incluindo relações aninhadas — e o servidor monta a resposta correspondente.

```graphql
query {
  post(id: "123") {
    title
    comments {
      body
      author { name }
    }
  }
}
```

## Problema que Resolve

REST tradicional, com endpoints fixos, força uma escolha ruim quando múltiplos clientes (mobile, web, admin) têm necessidades diferentes de dados: **over-fetching** (retornar campos que o cliente não usa) ou **under-fetching** (cliente precisa de várias chamadas sequenciais para montar uma tela). GraphQL resolve os dois deixando o cliente pedir exatamente o shape que precisa numa única query — mesmo racional que motiva um [[wiki/concepts/bff-pattern]], mas de forma genérica em vez de um endpoint por tela.

## Origem Histórica — Ligada ao N+1 entre Frontend e Backend

O [[wiki/concepts/n-plus-one]] é tradicionalmente descrito como um problema entre backend e banco de dados. Ele passou a existir **também** entre frontend e backend quando o modelo de renderização mudou: antes, o frontend pedia uma página inteira pronta ao backend (server-side rendering / "HTML over the wire" — ainda o modelo de Rails, Django templates, Laravel), e não havia N+1 porque não existiam endpoints adicionais para buscar mais dados. Quando UIs mais interativas (React e afins) passaram a buscar dados via chamadas a endpoints, o mesmo problema estrutural do banco foi replicado nessa camada: 1 request para uma lista + N requests para os relacionados de cada item.

A Meta/Facebook, com múltiplos frontends evoluindo rápido (mobile, web, iPad) e dados profundamente aninhados (usuário → post → comentário), criou o GraphQL para deixar o frontend "dizer o que quer" numa única query, em vez de multiplicar endpoints especializados a cada nova tela. Ver [[wiki/sources/problema-n-mais-1-graphql-orm-solucoes]].

## N+1 dentro do Próprio GraphQL — DataLoader

Resolver N+1 na camada front↔back não elimina o N+1 na camada back↔banco: um resolver ingênuo por campo aninhado ainda dispara uma query por item (ex.: uma query de categoria por produto, N vezes). A solução padrão é o **DataLoader** — agrupa (`batch`) todos os `.load(id)` disparados no mesmo tick em uma única query `WHERE id IN (...)`, com cache por request. Ver detalhe técnico em `tech-mentor-backend/references/graphql.md`.

## Por que Sempre POST

GraphQL nunca usa GET — sempre POST, mesmo em queries que não alteram nada. Motivo técnico, não semântico: uma URL de GET tem limite prático de tamanho (~2000–2048 caracteres); passar uma lista de IDs como query param estouraria esse limite rapidamente. POST manda os parâmetros no body, sem esse teto.

## GraphQL vs REST

| Critério | GraphQL | REST |
|---|---|---|
| Shape da resposta | Cliente define | Servidor define |
| Over/under-fetching | Eliminado | Comum |
| Cache HTTP | Difícil (tudo POST) | Nativo por URL |
| Paginação | Cursor-based (`Connection`/`PageInfo`) | Depende da implementação |

## Quando Faz Sentido

- Múltiplos clientes com necessidades de dados divergentes.
- Dados com relações profundamente aninhadas.
- Time de frontend com autonomia para evoluir queries sem depender de novos endpoints no backend.

Não compensa para APIs públicas simples ou quando cache HTTP agressivo por CDN é prioridade — nesse caso, REST com [[wiki/concepts/bff-pattern]] costuma ser mais simples de operar.

## Syntax Sugar Inspirado em GraphQL, fora do GraphQL

Algumas ORMs replicam a ergonomia de "pedir uma estrutura aninhada numa chamada só" na camada backend↔banco, mesmo sem usar GraphQL. Ver [[wiki/concepts/drizzle-orm]] — `db.query.users.findMany({ with: { posts: true } })` não é GraphQL, mas foi visivelmente inspirado na mesma ideia de deixar o chamador declarar o shape que quer.

## Key Sources

- [[wiki/sources/problema-n-mais-1-graphql-orm-solucoes]]
