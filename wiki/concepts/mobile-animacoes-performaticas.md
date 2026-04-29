---
type: concept
title: "Animações Performáticas — Mobile"
aliases: ["reanimated 3", "compose animation", "flutter animations", "mobile jank"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [mobile, animacoes, reanimated, compose, flutter, ui-thread, jank]
skill: tech-mentor-mobile
status: stable
---

# Animações Performáticas — Mobile

Animações devem rodar na UI thread — nunca cruzar a bridge JS (RN) ou bloquear a thread principal de lógica.

## React Native — Reanimated 3

```js
const offset = useSharedValue(0);
const animatedStyle = useAnimatedStyle(() => ({
  transform: [{ translateX: offset.value }],
}));
// worklet roda na UI thread — sem bridge
offset.value = withSpring(100);
```

`useSharedValue` e `useAnimatedStyle` executam como **worklets** na UI thread via JSI. Para gestos: `react-native-gesture-handler` + Reanimated 3 integrados.

## Android Compose

```kotlin
val offsetX by animateFloatAsState(
    targetValue = if (moved) 100f else 0f,
    animationSpec = spring()
)
```

`animate*AsState` é declarativo — o framework interpola automaticamente quando o valor muda. `AnimatedVisibility` para entrada/saída de composables.

## Flutter

- `AnimatedContainer`, `AnimatedOpacity` para mudanças simples (implicit animations)
- `AnimationController` + `Tween` para controle fino (explicit animations)
- `Hero` widget para transições entre telas

## Quando Evitar Reanimated

`Animated` API do React Native é suficiente para animações simples sem gesto. Reanimated adiciona complexidade — usar apenas quando a animação é controlada por gesto contínuo ou precisa de interpolações complexas.

## Ver também

- [[mobile-performance-listas]] — virtualização para listas animadas
- [[mobile-profiling]] — medir jank antes de otimizar

## Key Sources

- [[wiki/sources/mobile-animacoes-performaticas]]
