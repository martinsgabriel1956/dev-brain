---
type: entity
title: "Expo"
aliases: ["Expo Go", "EAS"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [mobile, react-native, expo, ferramenta]
skill: tech-mentor-mobile
status: stub
---

# Expo

Framework e conjunto de ferramentas em torno do [[wiki/entities/react-native]]. Na aula de [[wiki/entities/diego-fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]), o motivo é o começo sem atrito:

- **Sem Expo:** é preciso instalar a SDK do Android (pelo Android Studio) e o Xcode, ambos "extremamente pesados", e procurar uma biblioteca de terceiros para cada recurso nativo.
- **Com Expo:** o app Expo, instalado da loja no celular, "já tem a parte do Android e a parte do iOS" e as APIs de mapa, geolocalização, câmera, sensores e calendário. Quem desenvolve escreve só JavaScript, e dá para testar no iPhone sem Mac.
- Diego deixa as limitações para depois.

**Hoje:** a documentação do React Native recomenda começar por um framework e indica o Expo `[external]` (https://reactnative.dev/docs/environment-setup). O app Expo Go serve para experimentar; projetos reais usam *development builds*, com módulos nativos próprios. Gerar e publicar o app de iOS continua exigindo macOS ou o build na nuvem (EAS Build).

No Ecoleta, o Expo cobre o mapa, a geolocalização, o deep link para o WhatsApp ([[wiki/concepts/mobile-deep-links]]) e o Mail Compose.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: `expo-cli` global com `expo init` (template blank TypeScript), QR code em modo LAN, emulador ou Snack, Expo Google Fonts com `AppLoading`, `@expo/vector-icons`, `expo-location`, `expo-mail-composer` e `expo-constants`. Desde então, a CLI virou local (`npx create-expo-app`, `npx expo start`) e o `AppLoading` deu lugar ao `expo-splash-screen`.

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: por que o Expo, SDKs e o app no celular
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: o setup e os módulos usados no app do Ecoleta
