---
type: concept
title: "Derived State"
aliases: ["estado derivado", "valores derivados React", "computed values"]
date_created: 2026-04-22
date_updated: 2026-08-03
source_count: 2
tags: [react, estado, derived-state, performance, renderização, frontend-frameworks]
skill: tech-mentor-frontend
status: stable
---

# Derived State

**Valores que podem ser calculados a partir de estado ou props existentes.** Não devem ser armazenados em `useState` — devem ser calculados durante a renderização.

## O problema de guardar estado derivado em useState + useEffect

```typescript
// ❌ Anti-padrão — 3 renderizações, estado inconsistente entre elas
const [items, setItems] = useState<Item[]>([]);
const [filtered, setFiltered] = useState<Item[]>([]);
const [total, setTotal] = useState(0);

useEffect(() => {
  setFiltered(items.filter(i => i.active));
}, [items]); // render 2

useEffect(() => {
  setTotal(filtered.length);
}, [filtered]); // render 3
// Entre render 1 e render 3: items já mudou, total ainda é o valor antigo
```

**Problema:** entre a primeira e a terceira renderização o componente está em estado inconsistente — `items` já mudou mas `total` ainda reflete o valor anterior.

## A solução — calcular na renderização

```typescript
// ✅ 1 renderização, impossível ficar inconsistente
const [items, setItems] = useState<Item[]>([]);

const filtered = items.filter(i => i.active); // derivado
const total = filtered.length;                 // derivado de derivado
```

Tudo é calculado na mesma renderização — nunca existe momento em que os valores estão dessincronizados.

## E a performance?

Filtrar 1000 itens na renderização leva **< 1ms**. O overhead de duas renderizações extras com effects é maior na maioria dos casos.

Se o cálculo for genuinamente pesado (medido com Profiler), use [[useMemo]] — não `useEffect` + `useState`:

```typescript
// ✅ Para cálculos pesados — memoiza mas ainda é síncrono na renderização
const filtered = useMemo(
  () => heavyFilter(items),
  [items]
);
```

## Regra

> Se dá para calcular a partir de estado ou props existentes → não coloca em `useState`.

## Ver também

- [[useEffect]] — anti-padrão de sincronizar estado derivado
- [[useMemo]] — memoizar cálculos pesados na renderização
- [[useState]] — quando estado real é necessário

## O mesmo princípio, fora do React

O problema é framework-agnostic: qualquer estado que possa ser calculado a partir de outro estado existente (ex. `filtrados` calculado a partir de `itens` + `filtro`) não deveria virar estado próprio, porque cria dois valores que precisam ser mantidos manualmente em sincronia — se o dev esquecer de atualizar um lado após o outro mudar, eles dessincronizam. Um valor derivado, calculado na hora, não tem como ficar fora de sincronia porque não existe estado duplicado.

## Key Sources

- [[wiki/sources/useeffect-problemas-e-solucoes]]
- [[wiki/sources/10-conceitos-internos-frameworks-frontend]]
