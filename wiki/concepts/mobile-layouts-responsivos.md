---
type: concept
title: "Layouts Responsivos — Mobile"
aliases: ["mobile flexbox", "safe area mobile", "WindowSizeClass android", "responsive layout mobile"]
date_created: 2026-04-24
date_updated: 2026-11-15
source_count: 2
tags: [mobile, layouts, flexbox, safe-area, WindowSizeClass, responsive]
skill: tech-mentor-mobile
status: stable
---

# Layouts Responsivos — Mobile

## SafeArea — Obrigatório em Todas as Plataformas

```js
// React Native
import { SafeAreaView } from 'react-native-safe-area-context';
<SafeAreaView edges={['top', 'bottom']}><Screen /></SafeAreaView>
```

```kotlin
// Compose
WindowCompat.setDecorFitsSystemWindows(window, false)
// usar padding de insets nos composables
```

Sem SafeArea, conteúdo fica atrás do notch, dynamic island e home indicator.

## React Native — Flexbox

```js
// Flexbox RN: flexDirection 'column' por padrão (≠ CSS)
const styles = StyleSheet.create({
    container: { flex: 1, flexDirection: 'row', flexWrap: 'wrap' },
    card: { width: '48%', margin: '1%' },
});

// Responsivo por tela
const { width } = useWindowDimensions();
const columns = width > 600 ? 3 : 2;
```

## Android — WindowSizeClass

```kotlin
val windowSizeClass = calculateWindowSizeClass(this)
when (windowSizeClass.widthSizeClass) {
    WindowWidthSizeClass.Compact -> PhoneLayout()
    WindowWidthSizeClass.Medium -> TabletLayout()
    WindowWidthSizeClass.Expanded -> LargeTabletLayout()
}
```

## Flutter — LayoutBuilder

```dart
LayoutBuilder(
    builder: (context, constraints) {
        if (constraints.maxWidth > 600) return TabletLayout();
        return PhoneLayout();
    }
)
```

`LayoutBuilder` reage às constraints do pai — preferível a `MediaQuery` para componentes reutilizáveis.

## Ver também

- [[wiki/concepts/mobile-design-system]] — tokens de espaçamento como base para layouts
- [[wiki/concepts/mobile-performance-listas]] — listas em grids responsivos

## Suprimir no mobile (visão de design)

Em [[wiki/sources/grids-pratica-2-material-de-apoio-bootstrap-material-design-flexbox-grid]], no mobile "tem alguns elementos que são suprimidos": o formulário da home vira um botão. É a contraparte de design dos layouts nativos acima; ver [[wiki/concepts/design-responsivo]].

## Key Sources

- [[wiki/sources/mobile-layouts-responsivos]]
- [[wiki/sources/grids-pratica-2-material-de-apoio-bootstrap-material-design-flexbox-grid]] — elementos suprimidos no mobile (formulário vira botão)
