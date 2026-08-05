---
type: concept
title: "Comparação Rasa (Shallow Compare)"
aliases: ["shallow compare", "igualdade referencial", "referential equality"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 1
tags: [react, javascript, performance, shallow-compare, igualdade-referencial]
skill: tech-mentor-frontend
status: stable
---

# Comparação Rasa (Shallow Compare)

Algoritmo de comparação que [[wiki/concepts/react-memo]], [[wiki/concepts/useMemo]] e [[wiki/concepts/useCallback]] usam por padrão para decidir se um valor "mudou" em relação à renderização anterior. É equivalente a um `===` propriedade por propriedade — **não** entra recursivamente dentro de objetos/arrays para comparar o conteúdo interno (isso seria uma comparação profunda / deep compare).

## Igualdade referencial

Em JavaScript, objetos, arrays e funções são comparados por **referência** (posição na memória), não por valor:

```js
{} === {}              // false — dois objetos distintos, mesmo vazios
[1, 2] === [1, 2]       // false
(() => {}) === (() => {}) // false — funções recriadas nunca são "iguais"

1 === 1                 // true — primitivos comparam por valor
"a" === "a"              // true
```

Isso significa que qualquer objeto, array ou função **recriado no corpo de um componente a cada render** é tratado como "diferente" do anterior pela comparação rasa, mesmo que o conteúdo seja idêntico byte a byte.

## Onde isso quebra otimizações

- Uma função declarada dentro do componente pai, passada como prop para um filho com [[wiki/concepts/react-memo]]: a cada render do pai, a função ocupa uma nova posição de memória → o filho memoizado entende que a prop "mudou" e renderiza de novo, mesmo que o comportamento da função seja idêntico. Resolvido com [[wiki/concepts/useCallback]].
- Um objeto (`{ count, items }`) criado inline no corpo do componente e passado como prop: mesmo problema, resolvido embrulhando a criação do objeto em [[wiki/concepts/useMemo]].
- Valores **primitivos** (number, string, boolean) não sofrem desse problema — `1 === 1` é `true` independente de quantas vezes o componente renderizou, então passar um número como prop para um componente `memo` não precisa de `useMemo` por causa disso (só se o *cálculo* daquele número for caro).

## Customizando a comparação

`React.memo` aceita uma segunda função de comparação customizada, recebendo `prevProps`/`nextProps` e retornando `true`/`false` — permite substituir o shallow compare padrão por uma lógica específica (ex. comparar só um campo `id` em vez do objeto inteiro).

## Ver também

- [[wiki/concepts/react-memo]] — usa shallow compare para decidir se bloqueia a renderização
- [[wiki/concepts/useMemo]] — memoiza valores para evitar recriação de objetos/arrays a cada render
- [[wiki/concepts/useCallback]] — memoiza funções pelo mesmo motivo
- [[wiki/concepts/reconciliacao]] — outro algoritmo de comparação do React, mas sobre a árvore de elementos, não sobre valores de props/estado

## Key Sources

- [[wiki/sources/react-reconciliacao-memo-usememo-usecallback]]
