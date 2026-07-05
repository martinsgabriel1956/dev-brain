---
type: concept
title: "useMemo"
aliases: ["use memo", "memoização React", "memoize"]
date_created: 2026-04-22
date_updated: 2026-07-04
source_count: 2
tags: [react, hooks, performance, memoização, useMemo]
skill: tech-mentor-frontend
status: stable
---

# useMemo

Hook que **memoiza o resultado de um cálculo** — só recalcula quando as dependências mudam.

## Uso

```typescript
const filteredOrders = useMemo(
  () => orders.filter(o => o.status === filter),
  [orders, filter]
);
```

## Quando usar

✅ Cálculos caros: sort/filter de listas grandes, transformações pesadas, criação de objetos complexos passados como prop para componentes memoizados.

❌ Não use para: valores simples, strings, números, cálculos triviais — o overhead de memoização supera o ganho.

## Custo real

`useMemo` tem overhead de:
- Armazenar resultado anterior na memória
- Comparar dependências a cada render

**Meça antes de aplicar.**

## Relação com React Compiler

O [[react-compiler]] (React 19) pode eliminar a necessidade de `useMemo` manual ao inferir memoização automaticamente. Continua útil em casos de borda — ex. integração com libs de terceiros que dependem de referência estável. Não remova `useMemo` existente sem testar/medir.

## Ver também

- [[useCallback]] — memoiza funções em vez de valores
- [[container-presenter]] — separar lógica pesada evita `useMemo` desnecessário
- [[derived-state]] — calcular na renderização sem `useMemo` (para cálculos simples)

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
- [[wiki/sources/react-19-memoization-sem-usememo-usecallback]]
