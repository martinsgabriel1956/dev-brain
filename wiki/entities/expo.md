---
type: entity
title: "Expo"
aliases: ["Expo Go", "EAS"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 4
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

## Na NLW #2, dia 4 (Diego Fernandes)

`expo init` com blank (TypeScript), Expo Client, Expo Common Issues, `expo install expo-font @expo-google-fonts/...`, `AppLoading` e `@expo/vector-icons` embutido. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]].

## Na NLW #2, dia 5 (Diego Fernandes)

`expo install @react-native-community/async-storage`; o IP do painel do Expo vira o `baseURL`; o Metro mostra o `console.log` do aparelho. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: por que o Expo, SDKs e o app no celular
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: o setup e os módulos usados no app do Ecoleta
- [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy]]: NLW #2, Diego, dia 4: Proffy: init, fontes e vector-icons
- [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]]: NLW #2, Diego, dia 5: AsyncStorage e IP do painel
