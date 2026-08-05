---
type: concept
title: "useMemo"
aliases: ["use memo", "memoização React", "memoize"]
date_created: 2026-04-22
date_updated: 2026-08-04
source_count: 3
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

## `useMemo` para Igualdade Referencial (não só para cálculo caro)

Além de evitar recálculo, `useMemo` resolve o mesmo problema de [[shallow-compare|igualdade referencial]] que [[useCallback]] resolve para funções — mas para **valores não primitivos**. Um objeto ou array criado inline no corpo do componente (`{ count, items }`) é recriado a cada render, ocupando nova posição de memória; se esse valor for passado como prop para um componente [[react-memo|memoizado]], a comparação rasa vai considerá-lo "diferente" mesmo com conteúdo idêntico, quebrando a memoização do filho.

```typescript
// Sem useMemo: novo objeto a cada render, quebra memo do filho
const summary = { count: items.length, total };

// Com useMemo: mesma referência entre renders enquanto items/total não mudam
const summary = useMemo(() => ({ count: items.length, total }), [items, total]);
```

Para valores **primitivos** (number, string, boolean) esse problema não existe — `1 === 1` é sempre `true` independente de quantas vezes o componente renderizou. Nesse caso `useMemo` só vale a pena se o *cálculo* do valor for caro, não pela referência.

## Ver também

- [[useCallback]] — memoiza funções em vez de valores
- [[shallow-compare]] — o algoritmo de comparação por trás do problema de igualdade referencial que `useMemo` resolve para objetos/arrays
- [[react-memo]] — o componente que se beneficia de receber props com referência estável
- [[container-presenter]] — separar lógica pesada evita `useMemo` desnecessário
- [[derived-state]] — calcular na renderização sem `useMemo` (para cálculos simples)

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
- [[wiki/sources/useeffect-problemas-e-solucoes]]
- [[wiki/sources/react-19-memoization-sem-usememo-usecallback]]
- [[wiki/sources/react-reconciliacao-memo-usememo-usecallback]]
