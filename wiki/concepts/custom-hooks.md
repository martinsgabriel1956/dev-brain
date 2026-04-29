---
type: concept
title: "Custom Hooks"
aliases: ["hooks customizados", "hooks reutilizáveis React"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
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

## Custom Hooks vs Render Props vs HOC

- **Custom Hook**: compartilhar lógica/estado — preferível na maioria dos casos
- **Render Props**: injetar lógica em componentes de terceiros
- **HOC**: controlar renderização ou adicionar JSX em volta

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
