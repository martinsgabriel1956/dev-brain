---
type: concept
title: "React Compiler"
aliases: ["React Forget", "compilador React", "memoização automática React"]
date_created: 2026-07-04
date_updated: 2026-07-04
source_count: 2
tags: [react, hooks, performance, memoização, react-compiler, react-19]
skill: tech-mentor-frontend
status: stable
---

# React Compiler

Compilador (antes conhecido como "React Forget") introduzido no **React 19** que analisa o código dos componentes em build time e adiciona memoização automaticamente — eliminando, na maioria dos casos, a necessidade de escrever [[useMemo]], [[useCallback]] e `React.memo` manualmente.

## Como funciona

O compiler analisa o grafo de dependências do componente e:

- Detecta re-renders desnecessários e os pula.
- Memoiza cálculos custosos por baixo dos panos (equivalente a `useMemo` automático).
- Garante referências de função estáveis entre renders (equivalente a `useCallback` automático).

```tsx
// Antes — memoização manual e frágil
const ExpensiveList = React.memo(({ items, onSelect }: Props) => {
  const sortedItems = useMemo(
    () => [...items].sort((a, b) => a.name.localeCompare(b.name)),
    [items]
  );
  const handleSelect = useCallback((id: string) => onSelect(id), [onSelect]);
  return <List items={sortedItems} onSelect={handleSelect} />;
});

// Depois — com o compiler, mesmo resultado sem boilerplate
function ExpensiveList({ items, onSelect }: Props) {
  const sortedItems = [...items].sort((a, b) => a.name.localeCompare(b.name));
  return <List items={sortedItems} onSelect={(id) => onSelect(id)} />;
}
```

## Como habilitar

```bash
npm install babel-plugin-react-compiler
```

```js
// babel.config.js
module.exports = {
  plugins: [["babel-plugin-react-compiler", {}]],
};
```

## Quando `useMemo`/`useCallback` manuais ainda fazem sentido

- Integração com **bibliotecas de terceiros** que dependem explicitamente de um valor memoizado estável (a lib espera a referência, não o compiler).
- Cálculos genuinamente extremos que fogem da análise estática do compiler (caso raro, sem exemplo consolidado na literatura ainda).
- Código que **viola as Rules of Hooks** — o compiler simplesmente não otimiza esses trechos; usar o React DevTools para identificar onde ele não conseguiu atuar.

Na prática, a recomendação é: escrever o componente simples primeiro, medir performance, e só then decidir se ainda vale a pena memoizar manualmente algo pontual.

## Relação com outros conceitos

- [[useMemo]] e [[useCallback]] — o compiler substitui o uso manual desses hooks na maioria dos casos, mas não os torna obsoletos como API (edge cases continuam existindo).
- [[concurrent-mode]] — recurso distinto (concorrência de renderização via `useTransition`/`useDeferredValue`) frequentemente confundido/agrupado com o compiler por ambos serem novidades de React 18/19 relacionadas a performance.

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
- [[wiki/sources/react-19-memoization-sem-usememo-usecallback]]
