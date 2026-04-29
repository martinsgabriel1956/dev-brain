---
date: 2026-04-23
tags: [tech-mentor, mobile, performance, listas, flashlist, lazy-column, listview, react-native, flutter, compose]
skill: tech-mentor-mobile/references/performance
level: intermediário
---

# Otimização de Listas Mobile — FlashList, LazyColumn, ListView.builder

## Contexto
Listas são o padrão mais comum em apps mobile e o maior causador de jank quando mal implementadas. O problema central é renderizar centenas/milhares de itens sem alocar memória para todos ao mesmo tempo — a solução é virtualização: renderizar apenas o que está visível + um buffer. Cada plataforma tem sua solução otimizada.

## Como Funciona

### React Native — FlashList (Shopify)

FlatList é o padrão do RN, mas sofre com jank em listas com muitos itens heterogêneos. FlashList é 10x mais performática por reutilizar componentes nativamente.

```typescript
import { FlashList } from "@shopify/flash-list";

type Product = {
  id: string;
  name: string;
  price: number;
  imageUrl: string;
};

// CORRETO — FlashList com todas as otimizações
export function ProductList({ products }: { products: Product[] }) {
  const renderItem = useCallback(
    ({ item }: { item: Product }) => <ProductCard product={item} />,
    []
  );

  const keyExtractor = useCallback((item: Product) => item.id, []);

  return (
    <FlashList
      data={products}
      renderItem={renderItem}
      keyExtractor={keyExtractor}
      estimatedItemSize={120} // altura estimada do item — crítico para performance
      getItemType={item => (item.featured ? "featured" : "regular")} // múltiplos tipos
      onEndReached={handleLoadMore}
      onEndReachedThreshold={0.5}
      ListHeaderComponent={<ListHeader />}
      ListEmptyComponent={<EmptyState />}
      ItemSeparatorComponent={() => <View style={styles.separator} />}
      removeClippedSubviews // remove do render tree quando fora da tela
      maxToRenderPerBatch={10}
      windowSize={10} // número de telas a manter em memória
    />
  );
}

// ProductCard deve ser memoizado se tiver props estáveis
const ProductCard = React.memo(function ProductCard({ product }: { product: Product }) {
  return (
    <View style={styles.card}>
      <Image source={{ uri: product.imageUrl }} style={styles.image} resizeMode="cover" />
      <Text numberOfLines={2}>{product.name}</Text>
      <Text>{formatCurrency(product.price)}</Text>
    </View>
  );
});
```

```typescript
// Pagination com FlashList
export function PaginatedProductList() {
  const [page, setPage] = useState(1);
  const [products, setProducts] = useState<Product[]>([]);
  const [isLoadingMore, setIsLoadingMore] = useState(false);
  const [hasMore, setHasMore] = useState(true);

  async function handleLoadMore() {
    if (isLoadingMore || !hasMore) return;
    setIsLoadingMore(true);

    try {
      const newProducts = await fetchProducts({ page: page + 1, limit: 20 });
      if (newProducts.length < 20) setHasMore(false);
      setProducts(prev => [...prev, ...newProducts]);
      setPage(prev => prev + 1);
    } finally {
      setIsLoadingMore(false);
    }
  }

  return (
    <FlashList
      data={products}
      renderItem={({ item }) => <ProductCard product={item} />}
      estimatedItemSize={120}
      onEndReached={handleLoadMore}
      onEndReachedThreshold={0.3}
      ListFooterComponent={isLoadingMore ? <ActivityIndicator /> : null}
    />
  );
}
```

### Android Compose — LazyColumn / LazyRow

```kotlin
@Composable
fun ProductList(
  products: List<Product>,
  onLoadMore: () -> Unit,
  isLoading: Boolean
) {
  val listState = rememberLazyListState()

  // Detectar quando o usuário chegou perto do fim
  val shouldLoadMore = remember {
    derivedStateOf {
      val lastVisible = listState.layoutInfo.visibleItemsInfo.lastOrNull()?.index ?: 0
      val totalItems = listState.layoutInfo.totalItemsCount
      lastVisible >= totalItems - 5 // carregar mais quando restam 5 itens
    }
  }

  LaunchedEffect(shouldLoadMore.value) {
    if (shouldLoadMore.value) onLoadMore()
  }

  LazyColumn(
    state = listState,
    contentPadding = PaddingValues(horizontal = 16.dp, vertical = 8.dp),
    verticalArrangement = Arrangement.spacedBy(12.dp)
  ) {
    items(
      items = products,
      key = { it.id } // essencial para animações e performance
    ) { product ->
      ProductCard(
        product = product,
        modifier = Modifier.animateItem() // anima inserção/remoção
      )
    }

    if (isLoading) {
      item { CircularProgressIndicator(modifier = Modifier.fillMaxWidth().padding(16.dp)) }
    }
  }
}

@Composable
fun ProductCard(product: Product, modifier: Modifier = Modifier) {
  // Compose reutiliza composables automaticamente — sem equivalente ao React.memo necessário
  // Mas use remember para computações caras
  val formattedPrice = remember(product.price) { formatCurrency(product.price) }

  Card(modifier = modifier.fillMaxWidth()) {
    Row(modifier = Modifier.padding(12.dp)) {
      AsyncImage(
        model = product.imageUrl,
        contentDescription = product.name,
        modifier = Modifier.size(80.dp).clip(RoundedCornerShape(8.dp)),
        contentScale = ContentScale.Crop
      )
      Column(modifier = Modifier.padding(start = 12.dp)) {
        Text(product.name, maxLines = 2, overflow = TextOverflow.Ellipsis)
        Text(formattedPrice, style = MaterialTheme.typography.titleMedium)
      }
    }
  }
}
```

### Flutter — ListView.builder / SliverList

```dart
// ListView.builder — virtualização automática
class ProductListScreen extends StatelessWidget {
  final List<Product> products;
  const ProductListScreen({required this.products, super.key});

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: products.length,
      itemExtent: 120, // altura fixa = máxima performance (evita layout pass)
      itemBuilder: (context, index) {
        final product = products[index];
        return ProductCard(product: product);
      },
    );
  }
}

// Para alturas variáveis — sem itemExtent
ListView.builder(
  itemCount: products.length,
  itemBuilder: (context, index) => ProductCard(product: products[index]),
)

// CustomScrollView + SliverList para layouts complexos (parallax, header sticky)
CustomScrollView(
  slivers: [
    SliverAppBar(pinned: true, title: const Text("Produtos")),
    SliverList.builder(
      itemCount: products.length,
      itemBuilder: (ctx, i) => ProductCard(product: products[i]),
    ),
    if (isLoading)
      const SliverToBoxAdapter(
        child: Center(child: CircularProgressIndicator()),
      ),
  ],
)

// Grid — SliverGrid
SliverGrid.builder(
  gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
    crossAxisCount: 2,
    crossAxisSpacing: 12,
    mainAxisSpacing: 12,
    childAspectRatio: 0.75,
  ),
  itemCount: products.length,
  itemBuilder: (ctx, i) => ProductCard(product: products[i]),
)
```

### Otimização de imagens em listas

```typescript
// React Native — FastImage para cache e loading otimizado
import FastImage from "react-native-fast-image";

// Pré-carregar imagens da próxima página
function prefetchNextPage(products: Product[]) {
  FastImage.preload(
    products.map(p => ({ uri: p.imageUrl, priority: FastImage.priority.low }))
  );
}

function ProductCard({ product }: { product: Product }) {
  return (
    <FastImage
      source={{
        uri: product.imageUrl,
        priority: FastImage.priority.normal,
        cache: FastImage.cacheControl.immutable // para URLs com hash
      }}
      style={styles.image}
      resizeMode={FastImage.resizeMode.cover}
    />
  );
}
```

## Anti-patterns de lista — NUNCA fazer

```typescript
// 1. Inline arrow function em renderItem — recria a função em cada render
<FlatList renderItem={({ item }) => <ProductCard product={item} />} /> // ERRADO

// 2. Index como key
<FlatList keyExtractor={(_, index) => index.toString()} /> // ERRADO

// 3. Scroll view com mapa (sem virtualização)
<ScrollView>
  {products.map(p => <ProductCard key={p.id} product={p} />)} // ERRADO — 1000 itens = 1000 componentes na memória
</ScrollView>

// 4. Computação pesada no render do item sem memoização
function ProductCard({ product }: { product: Product }) {
  const analysis = expensiveAnalysis(product); // roda em todo render ERRADO
}
```

## Trade-offs

| Solução | Plataforma | Virtualização | Performance | Tipos mistos |
|---|---|---|---|---|
| FlatList | RN | Sim | Média | Sim (mas lento) |
| FlashList | RN | Sim (nativo) | Alta | Sim (getItemType) |
| LazyColumn | Android | Sim | Alta | Sim (items com key) |
| ListView.builder | Flutter | Sim | Alta | Sim |
| SliverList | Flutter | Sim | Alta | Sim (com Sliver) |
| ScrollView + map | Todas | Não | Péssima | Sim |

## Conceitos Relacionados
[[mobile-metricas-criticas]] · [[mobile-animacoes-performaticas]] · [[mobile-profiling]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
