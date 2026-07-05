---
type: concept
title: "Concurrent Mode"
aliases: ["React Concurrent", "concorrência React", "useTransition", "useDeferredValue"]
date_created: 2026-04-22
date_updated: 2026-07-04
source_count: 1
tags: [react, performance, concurrent-mode, react-18, react-19]
skill: tech-mentor-frontend
status: stable
---

# Concurrent Mode

Modelo de renderização do **React 18+** que permite ao React **pausar, retomar e priorizar renders** sem bloquear a UI. Resolve o problema de inputs lentos durante processamentos pesados.

## Hooks principais

### useTransition
Marca um update de estado como **não urgente** — o input responde imediatamente enquanto o resultado pesado é calculado em background.

```typescript
const [isPending, startTransition] = useTransition();

function handleSearch(value: string) {
  setQuery(value); // urgente: input atualiza imediatamente
  startTransition(() => {
    setResults(filterOrders(value)); // não urgente: pode esperar
  });
}
```

### useDeferredValue
Adia o uso de um valor em um **componente filho específico**:

```typescript
function SearchResults({ query }: { query: string }) {
  const deferredQuery = useDeferredValue(query);
  const results = useMemo(() => filterOrders(deferredQuery), [deferredQuery]);
  return <OrderList orders={results} />;
}
```

## useTransition vs useDeferredValue

| | useTransition | useDeferredValue |
|---|---|---|
| Controle | Você controla qual setState é não urgente | Você adia o valor num filho |
| Uso | Quando você controla o setState | Quando recebe o valor via prop |

## Relação com o React Compiler

O [[react-compiler]] é um recurso distinto — atua em build time memoizando valores/funções automaticamente, enquanto Concurrent Mode atua em runtime priorizando renders. Ambos chegaram junto com React 18/19 e são frequentemente confundidos por serem apresentados juntos como "novidades de performance".

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
