---
type: source
title: "React — Tudo que você precisa saber"
aliases: ["react overview", "react fundamentos"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/nemomartins/Documentos/new/dev-study/raw/react-tudo-que-voce-precisa-saber.md
source_url: ""
author: "Claude (tech-mentor-frontend)"
date_published: 2026-04-22
date_ingested: 2026-04-22
source_count: 0
tags: [react, frontend, hooks, componentes, estado, performance, arquitetura]
skill: tech-mentor-frontend
status: stable
---

# React — Tudo que você precisa saber

## TL;DR

Visão geral completa do React: modelo mental, hooks fundamentais, padrões de componentes, gerenciamento de estado, performance e arquitetura de projetos. Cobre React 18 e 19.

---

## Claims Principais

| Claim | Evidência | Confiança |
|---|---|---|
| React é biblioteca, não framework | Não inclui roteamento, estado global, fetch por padrão | Alta |
| UI = f(state) — renderização determinística | Dado o mesmo estado, o output JSX é sempre o mesmo | Alta |
| `setCount(prev => prev + 1)` é obrigatório quando o novo estado depende do anterior | Stale closure em Concurrent Mode pode capturar valor desatualizado | Alta |
| Context API causa re-render em todos os consumidores | Qualquer mudança no value propaga para baixo | Alta |
| `useMemo`/`useCallback` têm custo — não use em tudo | Overhead de memoização pode superar o ganho em casos simples | Alta |
| React Compiler (React 19 beta) elimina necessidade de memoização manual | Analisa código e adiciona memoization automaticamente | Média |

---

## Conceitos Abordados

- [[jsx]]
- [[useState]]
- [[useEffect]]
- [[useRef]]
- [[useReducer]]
- [[useMemo]]
- [[useCallback]]
- [[context-api]]
- [[custom-hooks]]
- [[error-boundary]]
- [[compound-components]]
- [[container-presenter]]
- [[concurrent-mode]]
- [[feature-sliced-architecture]]

## Entidades Abordadas

- [[react]]

---

## Quotes Relevantes

> "UI = f(state) — dado um estado, a UI é uma função determinística dele."

> "Nunca ignore warnings de dependências. O linter está certo."

> "Estado colocado onde é usado: menos re-renders, código mais fácil de deletar, sem estado 'órfão' no global store."

---

## Questões Abertas

- Quando o React Compiler sair de beta, `useMemo`/`useCallback` tornam-se anti-padrão?
- Como integrar Error Boundaries com frameworks de logging (Sentry, Datadog)?
