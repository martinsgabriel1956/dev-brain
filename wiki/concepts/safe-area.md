---
type: concept
title: "Safe area"
aliases: ["SafeAreaView", "área segura", "safe-area-context", "insets", "notch"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [mobile, layout, ios, android, react-native]
skill: tech-mentor-mobile
status: stub
---

# Safe area

A parte da tela livre de barra de status, notch (entalhe), Dynamic Island, cantos arredondados e barra de gestos. Conteúdo e toques fora dela ficam escondidos ou disputam gestos com o sistema. O sistema informa os *insets* (top, bottom, left, right) para o layout respeitar.

Na aula de [[wiki/entities/diego-fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]), o `SafeAreaView` do `react-native` substitui o `paddingTop: Constants.statusBarHeight` manual: ele "faz o padding automaticamente [...] do iPhone e também da status bar" e precisa de `flex: 1`. Diego não lembra o nome do "negocinho" do iPhone X: é o notch.

**A ressalva:** o `SafeAreaView` do core só funciona no iOS, e no Android não faz nada. Foi descontinuado no React Native 0.81 em favor do `react-native-safe-area-context` (`SafeAreaProvider`, `SafeAreaView`, `useSafeAreaInsets`) `[external]` (https://reactnative.dev/docs/safeareaview). A aula já o tinha instalado como dependência do [[wiki/entities/react-navigation]]. Com o Android 15 forçando *edge-to-edge*, tratar os insets no Android virou obrigatório `[skill: tech-mentor-mobile]`.

Relacionado: [[wiki/concepts/mobile-layouts-responsivos]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: tela de detalhe do Ecoleta
