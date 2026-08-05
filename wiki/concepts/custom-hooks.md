---
type: concept
title: "Custom Hooks"
aliases: ["hooks customizados", "hooks reutilizáveis React"]
date_created: 2026-04-22
date_updated: 2026-08-03
source_count: 2
tags: [react, hooks, reuso, composição]
skill: tech-mentor-frontend
status: stable
---

# Custom Hooks

Funções que **extraem lógica stateful reutilizável** para fora de componentes. Toda função que começa com `use` e chama outros hooks é um custom hook.

## Por que usar

- Reutilizar lógica entre componentes sem duplicação
- Testar lógica isolada do JSX
- Componente fica responsável só pela UI

## Exemplos canônicos

### useDebounce
```typescript
function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => setDebouncedValue(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);

  return debouncedValue;
}
```

### usePrevious
```typescript
function usePrevious<T>(value: T): T | undefined {
  const ref = useRef<T>();
  useEffect(() => { ref.current = value; });
  return ref.current;
}
```

### useEventListener
```typescript
function useEventListener<K extends keyof WindowEventMap>(
  eventName: K,
  handler: (event: WindowEventMap[K]) => void,
  element: EventTarget = window
) {
  const handlerRef = useRef(handler);
  useEffect(() => { handlerRef.current = handler; });

  useEffect(() => {
    const listener = (event: Event) => handlerRef.current(event as WindowEventMap[K]);
    element.addEventListener(eventName, listener);
    return () => element.removeEventListener(eventName, listener);
  }, [eventName, element]);
}
```

### useDataSet — sincronizar um estado externo à árvore

Um custom hook pode conectar o React a um estado que vive **fora** de qualquer componente — a base de bibliotecas como [[wiki/concepts/zustand]]:

```typescript
function useDataSet(dataSet) {
  const { map, subscriber } = dataSet;
  const [state, setState] = useState(map.get("value"));

  useEffect(() => {
    return subscriber.subscribe((event) => {
      const currentValue = map.get("value");
      const nextValue = typeof event === "function" ? event(currentValue) : event;
      map.set("value", nextValue);
      setState(nextValue);
    });
  }, [map, subscriber]);

  function setValue(value) {
    subscriber.emit(value);
  }

  return [state, setValue];
}
```

`useEffect` faz o `subscribe` no [[wiki/concepts/observer-pattern|observer]] externo e retorna o `unsubscribe` como cleanup; `useState` guarda a cópia local que dispara o re-render. Ver [[wiki/sources/recriando-zustand-javascript-puro-sem-provider]] para a implementação completa, incluindo a store (`createDataSet`) que esse hook consome.

## Custom Hooks vs Render Props vs HOC

- **Custom Hook**: compartilhar lógica/estado — preferível na maioria dos casos
- **Render Props**: injetar lógica em componentes de terceiros
- **HOC**: controlar renderização ou adicionar JSX em volta

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
- [[wiki/sources/recriando-zustand-javascript-puro-sem-provider]] — `useDataSet`, hook que sincroniza estado externo com `useState`/`useEffect`
