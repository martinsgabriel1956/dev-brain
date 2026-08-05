---
type: concept
title: "useCallback"
aliases: ["use callback", "memoizar função React"]
date_created: 2026-04-22
date_updated: 2026-08-04
source_count: 3
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

## Por que a função "muda" sem useCallback

Uma função declarada no corpo de um componente é **recriada a cada render** — ocupa uma nova posição na memória. Como JavaScript compara funções por [[shallow-compare|referência]] (`===`), um componente filho memoizado com [[react-memo]] que recebe essa função como prop vê "uma função diferente" a cada render do pai, mesmo que o corpo da função seja idêntico — e re-renderiza, quebrando a memoização. `useCallback` resolve isso mantendo a mesma referência entre renders enquanto as dependências não mudarem.

## Dica prática: dependência do próprio estado anterior

Quando a função precisa do valor **anterior** do próprio estado que ela atualiza, prefira a forma funcional do setter em vez de ler a variável de estado diretamente — isso remove a necessidade de incluir aquele estado no array de dependências:

```typescript
// Pior: precisa de `wishlist` nas dependências → useCallback perde a referência
// estável toda vez que wishlist mudar
const addToWishlist = useCallback((item: string) => {
  setWishlist([...wishlist, item]);
}, [wishlist]);

// Melhor: forma funcional do setState, sem dependência de wishlist
const addToWishlist = useCallback((item: string) => {
  setWishlist(prev => [...prev, item]);
}, []);
```

## Relação com React Compiler

O [[react-compiler]] (React 19) pode eliminar `useCallback` manual na maioria dos casos — sobra útil sobretudo quando o filho com `React.memo` depende de igualdade referencial estrita e o compiler não cobre o trecho (ex. código fora das Rules of Hooks).

## Ver também

- [[useMemo]] — mesmo problema de igualdade referencial, mas para valores/objetos em vez de funções
- [[shallow-compare]] — o algoritmo de comparação por trás do problema que `useCallback` resolve
- [[react-memo]] — o componente filho que se beneficia de receber uma função com referência estável

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
- [[wiki/sources/react-19-memoization-sem-usememo-usecallback]]
- [[wiki/sources/react-reconciliacao-memo-usememo-usecallback]]
