---
type: entity
title: "React Native"
aliases: ["RN"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [mobile, react-native, react, javascript, ios, android, cross-platform]
skill: tech-mentor-mobile
status: stub
---

# React Native

Framework da Meta para apps iOS e Android com [[wiki/entities/react]] e JavaScript ou TypeScript, desenhando componentes nativos de verdade em vez de uma página web numa WebView (como Ionic e PhoneGap).

Na aula de [[wiki/entities/diego-fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]):

- **Uma base de código** em vez de um app em Objective-C/Swift (IPA) e outro em Java/Kotlin (APK).
- **Nada é convertido para a linguagem nativa:** o aparelho executa o JavaScript num motor embutido ("JavaScript Core", "uma thread de processamento de código JavaScript"), e a interface "é totalmente nativa".
- **Compartilha o pacote `react`** com a web. Muda só o pacote que traduz componentes em interface: HTML no navegador, elementos nativos no celular.
- **Expo** para começar sem Android Studio e Xcode. Ver [[wiki/entities/expo]].

**Hoje:** o motor padrão é o Hermes desde a 0.70, e a Nova Arquitetura (JSI, Fabric, TurboModules, sem a bridge) é padrão desde a 0.76 `[external]` (https://reactnative.dev/docs/hermes). Para módulos próprios, ver [[wiki/concepts/native-module]]; para a escolha entre RN, Flutter, KMP e nativo, [[wiki/concepts/mobile-cross-platform-decision]].

No dia 4 da NLW #1 com [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]), o Ecoleta ganha o app: `View`/`Text` no lugar do HTML, `StyleSheet` com Yoga (tudo flexbox, sem cascata), `RectButton`, React Navigation, react-native-maps, `Linking` e `KeyboardAvoidingView`. "O resto é tudo igual" ao React da web.

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: abordagem tradicional x React Native, JavaScriptCore, interface nativa
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: o app do Ecoleta: diferenças da web, navegação, mapa e deep link
