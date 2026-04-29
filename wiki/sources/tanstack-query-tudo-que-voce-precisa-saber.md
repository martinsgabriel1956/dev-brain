---
type: source
title: "TanStack Query — Tudo que você precisa saber"
aliases: ["react query", "tanstack query overview", "server state react"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/nemomartins/Documentos/new/dev-study/raw/tanstack-query-tudo-que-voce-precisa-saber.md
source_url: ""
author: "Claude (tech-mentor-frontend)"
date_published: 2026-04-22
date_ingested: 2026-04-22
source_count: 0
tags: [tanstack-query, react-query, server-state, cache, mutations, frontend, react]
skill: tech-mentor-frontend
status: stable
---

# TanStack Query — Tudo que você precisa saber

## TL;DR

Visão geral completa do TanStack Query: modelo mental de server state, setup, `useQuery`, `useMutation`, optimistic updates, infinite scroll, polling, WebSocket, prefetch, integração com Next.js Server Actions e comparativo com SWR.

---

## Claims Principais

| Claim | Evidência | Confiança |
|---|---|---|
| `useState` + `useEffect` para fetch é anti-padrão | Sem cache, retry, deduplicação, devtools — boilerplate enorme | Alta |
| `queryKey` é o endereço do cache — estruture hierarquicamente | Permite invalidação granular por nível da hierarquia | Alta |
| `staleTime: 0` (padrão) refetch toda vez que componente monta ou janela foca | Comportamento padrão do TanStack Query v5 | Alta |
| `gcTime` substituiu `cacheTime` a partir da v5 | Breaking change na v5 | Alta |
| `useSuspenseQuery` elimina `isLoading`/`isError` — delega para boundaries | `data` é sempre definido após o boundary | Alta |
| TanStack Query (~13KB) vs SWR (~4KB) — TQ tem mais features, SWR menor bundle | Comparativo de bundle size oficial | Alta |

---

## Conceitos Abordados

- [[tanstack-query]]
- [[useQuery]]
- [[useMutation]]
- [[query-key]]
- [[optimistic-updates]]
- [[infinite-query]]
- [[server-state]]
- [[swr]]

## Conceitos Relacionados (wiki existente)

- [[error-boundary]] — integração com `QueryErrorResetBoundary`
- [[useEffect]] — substituído pelo TanStack Query para fetch
- [[context-api]] — anti-padrão para server state
- [[react]] — ecossistema

## Entidades Abordadas

- [[tanstack]] (entidade)

---

## Quotes Relevantes

> "Dados do servidor não são seu estado — são um snapshot remoto que precisa de cache, revalidação e sincronização."

> "O que você ganha de graça: cache automático, deduplicação de requests, retry em falha, refetch em foco de janela, loading/error states, devtools visuais."

---

## Questões Abertas

- Com Server Components (RSC) no Next.js, qual o papel do TanStack Query no cliente? Ainda faz sentido em apps 100% RSC?
- `useSuspenseQuery` + Streaming SSR — como funciona o handoff servidor→cliente?
