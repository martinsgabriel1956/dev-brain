---
type: concept
title: "Performance de Listas Mobile"
aliases: ["flashlist react native", "lazycol android", "listview builder flutter", "mobile virtualization"]
date_created: 2026-04-24
date_updated: 2026-11-16
source_count: 2
tags: [mobile, listas, flashlist, flatlist, lazycol, virtualizacao, performance]
skill: tech-mentor-mobile
status: stable
---

# Performance de Listas Mobile

Virtualização obrigatória em listas longas — renderizar apenas itens visíveis + buffer.

## React Native — FlashList

```ts
import { FlashList } from '@shopify/flash-list';

<FlashList
    data={products}
    renderItem={({ item }) => <ProductCard product={item} />}
    estimatedItemSize={120}
    keyExtractor={item => item.id}
/>
```

FlashList recicla JSI cell views como RecyclerView nativo. `estimatedItemSize` crítico para performance de scroll.

Anti-pattern: `ScrollView` com `map()` — renderiza todos os itens de uma vez.

## Android — LazyColumn (Compose)

```kotlin
LazyColumn {
    items(products, key = { it.id }) { product ->
        ProductCard(product = product)
    }
}
```

Keys estáveis evitam recomposition desnecessária. `key` por item — nunca por índice.

## Flutter — ListView.builder

```dart
ListView.builder(
    itemCount: products.length,
    itemExtent: 120.0, // altura fixa = scroll position preciso sem medir cada item
    itemBuilder: (context, index) => ProductCard(product: products[index]),
)
```

`itemExtent` elimina cálculo de altura por item — melhora performance de scroll em listas homogêneas.

## Otimizações Comuns

- **Images:** lazy loading com cache (`expo-image`, `Glide`, `Kingfisher`)
- **Separators:** `ItemSeparatorComponent` / `Divider` — não renderizar no item
- **Keys:** ID único estável — nunca índice do array
- **Memoization:** `React.memo` no componente de item se renders são caros

## Ver também

- [[wiki/concepts/mobile-animacoes-performaticas]] — animações em itens de lista
- [[wiki/concepts/mobile-profiling]] — medir jank com Perfetto/Instruments

## Na NLW #2, dia 5 (Diego Fernandes)

Lista de professores em `ScrollView` "da maneira mais fácil possível", com `contentContainerStyle` para o padding; `FlatList`/FlashList virtualizariam, o que a paginação infinita da versão 2.0 vai exigir. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]].

## Key Sources

- [[wiki/sources/mobile-performance-listas]]
- [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]]: NLW #2, Diego, dia 5: ScrollView × FlatList no Proffy
