---
type: entity
title: "React"
aliases: ["ReactJS", "React.js"]
date_created: 2026-04-22
date_updated: 2026-07-19
source_count: 3
tags: [react, frontend, biblioteca, facebook, meta]
skill: tech-mentor-frontend
status: stable
---

# React

Biblioteca JavaScript para construção de interfaces de usuário. Criada pelo Facebook (Meta) em 2013. Não é um framework — não inclui roteamento, estado global ou fetch por padrão.

## Modelo Mental

**UI = f(state)** — dado o mesmo estado, o output é sempre o mesmo JSX. Isso torna a UI previsível e testável.

## Versões Relevantes

- **React 16.8** — introduziu Hooks (`useState`, `useEffect`, etc.)
- **React 18** — Concurrent Mode, `useTransition`, `useDeferredValue`, `useSyncExternalStore`
- **React 19** — `use()` hook, `useActionState`, React Compiler (beta), Server Actions aprimorados

## Ecossistema Principal

| Necessidade | Solução |
|---|---|
| Roteamento web | React Router / Next.js App Router |
| Estado global | Zustand, Jotai, Redux Toolkit |
| Server state | [[tanstack-query]], SWR |
| Formulários | React Hook Form + Zod |
| Metaframeworks | Next.js, Remix, Astro |
| Testes | React Testing Library + Vitest |

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
- [[wiki/sources/react-19-memoization-sem-usememo-usecallback]]
- [[wiki/sources/underengineering-overengineering-mario-souto]] — React Hook Form citado como exemplo de lib madura a preferir em vez de construir gerenciamento de formulário do zero, evitando [[wiki/concepts/under-engineering]]
