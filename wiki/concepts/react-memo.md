---
type: concept
title: "React.memo"
aliases: ["memo", "React.memo()", "memoização de componente"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 1
tags: [react, hooks, performance, memoização, react-memo, shallow-compare]
skill: tech-mentor-frontend
status: stable
---

# React.memo

Higher-order component que envolve um componente e diz ao React: antes de deixar esse componente entrar no fluxo de renderização (mesmo que o pai tenha renderizado, ou um estado/prop qualquer da árvore tenha mudado), **compare as props e o estado atuais com os da renderização anterior**. Se nada relevante mudou, nem gere uma nova versão do componente na [[wiki/concepts/virtual-dom]] — no React DevTools Profiler isso aparece como `did not render`.

## Uso

```tsx
// Sem memo: re-renderiza sempre que o pai re-renderiza
function Item({ item }: { item: string }) { return <li>{item}</li> }

// Com memo: só re-renderiza se `item` mudar (comparação rasa)
const Item = memo(function Item({ item }: { item: string }) {
  return <li>{item}</li>
})

// Comparação customizada — sobrescreve o shallow compare padrão
const Item = memo(ItemComponent, (prevProps, nextProps) => {
  return prevProps.item.id === nextProps.item.id
})
```

Por padrão, a comparação é uma [[wiki/concepts/shallow-compare]] prop a prop — não uma comparação profunda do conteúdo.

## As quatro situações onde vale a pena usar

1. **Componente puro**: dadas as mesmas props, o retorno é sempre idêntico. Se o componente depende de algo fora das props (data/hora atual, largura da tela, qualquer informação do ambiente), ele não é puro — `memo` não ajuda.
2. **Componente que renderiza com muita frequência** — ex. um item de lista dentro de uma árvore que re-renderiza a cada tecla digitada num input em outro lugar da árvore.
3. **Sempre com as mesmas props entre renders** — se as props mudam a cada render de qualquer forma, `memo` só adiciona uma comparação que sempre conclui "precisa renderizar", piorando a performance.
4. **Componentes médios a grandes** — em componentes muito simples e pequenos, o custo de o React recriar a Virtual DOM e comparar via [[wiki/concepts/reconciliacao]] tende a ser mais rápido que o próprio `memo`.

## Por que `memo` não deve ser usado em tudo

`memo` precisa **percorrer e comparar** props/estado a cada possível renderização para decidir se deixa o componente passar. Esse custo de comparação pode, em componentes triviais ou com props que sempre mudam, ser mais lento do que simplesmente deixar o algoritmo de [[wiki/concepts/reconciliacao]] do React fazer seu trabalho normal. É otimização prematura aplicar `memo` indiscriminadamente "porque é mais fácil".

## Quebra por igualdade referencial

`memo` só funciona se as props recebidas mantiverem a mesma referência entre renders quando o conteúdo não muda. Funções e objetos/arrays criados no corpo do componente pai são recriados a cada render — isso quebra `memo` no filho mesmo sem mudança real de conteúdo. Ver [[wiki/concepts/shallow-compare]], [[wiki/concepts/useCallback]] (funções) e [[wiki/concepts/useMemo]] (objetos/valores calculados).

## Ver também

- [[wiki/concepts/shallow-compare]] — o algoritmo de comparação usado por padrão
- [[wiki/concepts/reconciliacao]] — o que `memo` evita executar quando bloqueia o render
- [[wiki/concepts/useCallback]] — estabiliza funções passadas como prop para componentes `memo`
- [[wiki/concepts/useMemo]] — estabiliza valores/objetos passados como prop para componentes `memo`
- [[wiki/concepts/react-compiler]] — no React 19, memoiza automaticamente na maioria dos casos que hoje exigem `memo` manual

## Key Sources

- [[wiki/sources/react-reconciliacao-memo-usememo-usecallback]]
