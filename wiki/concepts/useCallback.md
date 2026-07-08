---
type: concept
title: "useCallback"
aliases: ["use callback", "memoizar função React"]
date_created: 2026-04-22
date_updated: 2026-07-04
source_count: 2
tags: [react, hooks, performance, memoização, useCallback]
skill: tech-mentor-frontend
status: stable
---

# useCallback

Hook que **memoiza a referência de uma função** — retorna a mesma instância entre renders enquanto as dependências não mudarem.

## Uso

```typescript
const handleDelete = useCallback((id: string) => {
  deleteOrder(id);
}, []); // sem deps — não depende de estado
```

## Quando usar

✅ Funções passadas como prop para componentes com `React.memo` — sem `useCallback`, o componente filho re-renderiza mesmo que a lógica não mude (referência nova a cada render).

✅ Funções usadas como dependência de `useEffect` ou `useMemo`.

❌ Não use globalmente em todas as funções de um componente — overhead sem ganho.

## Diferença de useMemo

```typescript
// useMemo — memoiza o VALOR retornado
const value = useMemo(() => compute(a, b), [a, b]);

// useCallback — memoiza a FUNÇÃO em si
const fn = useCallback(() => compute(a, b), [a, b]);
// equivalente a:
const fn = useMemo(() => () => compute(a, b), [a, b]);
```

## Relação com React Compiler

O [[react-compiler]] (React 19) pode eliminar `useCallback` manual na maioria dos casos — sobra útil sobretudo quando o filho com `React.memo` depende de igualdade referencial estrita e o compiler não cobre o trecho (ex. código fora das Rules of Hooks).

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
- [[wiki/sources/react-19-memoization-sem-usememo-usecallback]]
