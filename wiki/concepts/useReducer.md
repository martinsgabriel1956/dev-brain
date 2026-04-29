---
type: concept
title: "useReducer"
aliases: ["use reducer", "reducer React", "Redux-like React"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [react, hooks, estado, useReducer, reducer]
skill: tech-mentor-frontend
status: stable
---

# useReducer

Alternativa ao [[useState]] para **estado complexo com múltiplas ações relacionadas**. Segue o padrão Redux: `(state, action) => newState`.

## Quando usar

- Mais de 2-3 estados que mudam juntos
- Lógica de transição de estado complexa
- Próximo estado depende de múltiplos valores do estado atual

## Estrutura

```typescript
type State = { items: Item[]; total: number };
type Action =
  | { type: "ADD"; payload: Item }
  | { type: "REMOVE"; payload: string }
  | { type: "CLEAR" };

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case "ADD":
      return { items: [...state.items, action.payload], total: state.total + action.payload.price };
    case "REMOVE":
      const item = state.items.find(i => i.id === action.payload)!;
      return { items: state.items.filter(i => i.id !== action.payload), total: state.total - item.price };
    case "CLEAR":
      return { items: [], total: 0 };
  }
}

function Cart() {
  const [state, dispatch] = useReducer(reducer, { items: [], total: 0 });
  // ...
}
```

## Vantagens sobre useState para estado complexo

- Reducer é uma função pura — fácil de testar isoladamente
- Todas as transições de estado ficam num lugar só
- `dispatch` tem referência estável — não precisa de `useCallback`

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
