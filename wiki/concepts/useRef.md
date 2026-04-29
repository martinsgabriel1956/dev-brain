---
type: concept
title: "useRef"
aliases: ["use ref", "ref React", "referência DOM"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [react, hooks, ref, dom, useRef]
skill: tech-mentor-frontend
status: stable
---

# useRef

Hook com dois usos principais:
1. **Acessar o DOM diretamente** (foco, scroll, medição)
2. **Guardar valores mutáveis sem causar re-render**

## Acesso ao DOM

```typescript
function AutoFocusInput() {
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  return <input ref={inputRef} />;
}
```

## Valor sem re-render

Ideal para guardar IDs de timers, instâncias externas, valor anterior:

```typescript
function Timer() {
  const intervalRef = useRef<NodeJS.Timeout | null>(null);

  function start() {
    intervalRef.current = setInterval(() => tick(), 1000);
  }

  function stop() {
    if (intervalRef.current) clearInterval(intervalRef.current);
  }
}
```

## Diferença de useState

| `useRef` | `useState` |
|---|---|
| Mutação direta (`ref.current = x`) | Imutável — precisa de setter |
| Não causa re-render | Causa re-render |
| Para valores que o componente não exibe | Para valores que afetam a UI |

## useImperativeHandle

Quando o pai precisa chamar métodos imperativos num filho, use `useImperativeHandle` + `forwardRef` para expor uma API controlada — ver [[compound-components]].

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
