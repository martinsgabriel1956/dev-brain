---
date: 2026-04-23
tags: [tech-mentor, mobile, layout, flexbox, responsivo, react-native, flutter, compose]
skill: tech-mentor-mobile/references/layouts
level: fundamento
---

# Layouts Responsivos — Mobile

## Contexto
Mobile tem dezenas de tamanhos de tela, densidades de pixel e orientações. Layout responsivo não é só "funcionar em iPhone e Android" — é adaptar a experiência a telas de 4" a tablets de 13", modos portrait/landscape, e densidade de pixels de 1x a 3x. A base é sempre o sistema de layout da plataforma.

## Como Funciona

### React Native — Flexbox

RN usa Flexbox com `flexDirection: "column"` como default (diferente da web que é `row`).

```typescript
import { Dimensions, useWindowDimensions } from "react-native";

// Hook recomendado — reativo a mudanças de orientação
export function useBreakpoints() {
  const { width } = useWindowDimensions();
  return {
    isSmall: width < 360,
    isMedium: width >= 360 && width < 768,
    isTablet: width >= 768
  };
}

// Layout adaptativo
export function ProductGrid() {
  const { isTablet } = useBreakpoints();

  return (
    <View style={styles.container}>
      <FlatList
        data={products}
        numColumns={isTablet ? 3 : 2}
        key={isTablet ? "tablet" : "phone"} // força recriação ao mudar colunas
        renderItem={({ item }) => <ProductCard product={item} />}
        columnWrapperStyle={styles.row}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16
  },
  row: {
    gap: 12
  }
});
```

```typescript
// SafeArea — essencial para notch e home indicator
import { SafeAreaView } from "react-native-safe-area-context";

export function Screen({ children }: { children: React.ReactNode }) {
  return (
    <SafeAreaView style={{ flex: 1 }} edges={["top", "bottom"]}>
      {children}
    </SafeAreaView>
  );
}
```

```typescript
// Unidades — sempre com PixelRatio para assets, nunca px fixo para layout
import { PixelRatio } from "react-native";

const FONT_SCALE = PixelRatio.getFontScale();
const fontSize = 16 * Math.min(FONT_SCALE, 1.3); // cap para acessibilidade
```

### Flutter — Column/Row + LayoutBuilder

```dart
// LayoutBuilder — análogo ao CSS container queries
class AdaptiveGrid extends StatelessWidget {
  final List<Product> products;
  const AdaptiveGrid({required this.products, super.key});

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        final crossAxisCount = constraints.maxWidth > 600 ? 3 : 2;
        return GridView.builder(
          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: crossAxisCount,
            crossAxisSpacing: 12,
            mainAxisSpacing: 12,
            childAspectRatio: 0.75,
          ),
          itemCount: products.length,
          itemBuilder: (ctx, i) => ProductCard(product: products[i]),
        );
      },
    );
  }
}
```

```dart
// MediaQuery para breakpoints globais
class ResponsiveLayout extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.sizeOf(context); // .sizeOf é mais eficiente que .of
    final isTablet = size.width >= 768;

    return isTablet
      ? Row(children: [Sidebar(), Expanded(child: Content())])
      : Content();
  }
}
```

```dart
// SafeArea — evitar sobreposição com notch/home indicator
Scaffold(
  body: SafeArea(
    child: Column(/* ... */),
  ),
)
```

### Android Compose — Adaptive Layouts

```kotlin
// WindowSizeClass — biblioteca oficial do Jetpack
@Composable
fun AdaptiveHomeScreen() {
  val windowSizeClass = calculateWindowSizeClass()
  
  when (windowSizeClass.widthSizeClass) {
    WindowWidthSizeClass.Compact -> SinglePaneLayout()
    WindowWidthSizeClass.Medium -> TwoPaneLayout(fraction = 0.4f)
    WindowWidthSizeClass.Expanded -> TwoPaneLayout(fraction = 0.3f)
  }
}

// Padding consistente com WindowInsets
Scaffold(
  contentWindowInsets = WindowInsets.safeDrawing
) { paddingValues ->
  Column(modifier = Modifier.padding(paddingValues)) {
    /* content */
  }
}
```

### iOS SwiftUI — GeometryReader + ViewThatFits

```swift
// GeometryReader — ler dimensões do container
struct AdaptiveCard: View {
  var body: some View {
    GeometryReader { geo in
      let isWide = geo.size.width > 600
      Group {
        if isWide {
          HStack { thumbnail; details }
        } else {
          VStack { thumbnail; details }
        }
      }
    }
  }
}

// ViewThatFits — SwiftUI 16+ adapta ao espaço disponível
ViewThatFits(in: .horizontal) {
  HStack { label; description } // tenta primeiro
  VStack { label; description } // fallback
}
```

## Trade-offs

| Técnica | Plataforma | Reativo | Complexidade | Uso ideal |
|---|---|---|---|---|
| Flexbox + useWindowDimensions | RN | Sim | Baixa | Layout geral |
| LayoutBuilder | Flutter | Sim | Baixa | Grid/cards adaptáveis |
| WindowSizeClass | Android | Sim | Baixa | Breakpoints oficiais |
| GeometryReader | iOS | Sim | Média | Layouts complexos |
| SafeArea | Todas | Sim | Nenhuma | Sempre usar |

## Quando Usar / Quando Evitar

**Sempre use SafeArea** — apps sem SafeArea ficam atrás do notch/home indicator em qualquer device moderno.

**Use LayoutBuilder/useWindowDimensions** em vez de `Dimensions.get("window")` — este não é reativo a mudanças de orientação.

**Evite tamanhos fixos (px/pt) para containers** — use porcentagens, flex, ou valores relativos à tela.

**Tablet support:** defina breakpoints claros (≥768px = tablet) e teste em emulador iPad/Android tablet antes de marcar como completo.

**Font scaling:** respeite as configurações de acessibilidade do usuário — não bloqueie o font scale do sistema abaixo de 1.0.

## Conceitos Relacionados
[[mobile-navegacao]] · [[mobile-state-management-local]] · [[mobile-performance-listas]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
