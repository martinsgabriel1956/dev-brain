---
type: concept
title: "Animações Performáticas — Mobile"
aliases: ["reanimated 3", "compose animation", "flutter animations", "mobile jank"]
date_created: 2026-04-24
date_updated: 2026-11-19
source_count: 6
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

- [[wiki/concepts/mobile-performance-listas]] — virtualização para listas animadas
- [[wiki/concepts/mobile-profiling]] — medir jank antes de otimizar

## Na NLW #2, dia 4 (Diego Fernandes)

"Não tem a parte de animações" refere-se ao CSS; o RN tem `Animated`/Reanimated, e o ripple do `RectButton` vem do Gesture Handler. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]].

## Na web: testar no celular e cortar (FrontPUSH, otimização aula 07)

Em [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]]: "teste, teste, teste" no aparelho real via Live Server na mesma rede; se continuar travando, "capa no celular" (estático ou `display: none`). Complementos: throttling de CPU no DevTools, `chrome://inspect` por USB, telas de 120 Hz (8,3 ms por quadro) e `prefers-reduced-motion`.

## Key Sources

- [[wiki/sources/mobile-animacoes-performaticas]]
- [[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]] — filtros SVG exportados do Figma (sombra) têm custo de renderização ao animar (nota do agente)
- [[wiki/sources/imagens-e-ilustracoes-vetorizar-icones-figma-pen-tool-bend-tool]] — ícones animados com sombra interna e externa no SVG (filtros com custo de renderização; nota do agente)
- [[wiki/sources/frontpush-layout-css-botao-hover-flexbox-media-query]]: hover com `transform: scale` (compositor) no CSS da web; ver [[wiki/concepts/transition-e-transform-css]]
- [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]]: NLW #2, Diego, dia 4: animações × CSS no RN
- [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]]: FrontPUSH, otimização aula 07: teste em aparelho e corte no mobile
