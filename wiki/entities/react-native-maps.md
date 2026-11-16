---
type: entity
title: "react-native-maps"
aliases: ["MapView", "react-native-maps Marker"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [react-native, mapas, mobile, biblioteca]
skill: tech-mentor-mobile
status: stub
---

# react-native-maps

Componente de mapa nativo para o [[wiki/entities/react-native]]. Usa o Apple Maps no iOS (ou o Google Maps, se configurado) e o Google Maps no Android, com `MapView`, `Marker`, `Polyline` e outros.

Na NLW #1 com [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]):

- **Montagem:** `expo install react-native-maps`, e o `MapView` vai dentro de uma `View` com `borderRadius`, porque "o borderRadius só funciona nas views".
- **Posição inicial:** `initialRegion={{ latitude, longitude, latitudeDelta: 0.014, longitudeDelta: 0.014 }}`. O mapa só é renderizado quando a posição do `expo-location` chega ([[wiki/concepts/renderizacao-condicional]]); antes disso, abriria no oceano (`[0, 0]`).
- **Marcadores:** `<Marker coordinate onPress>` com filhos próprios (imagem e nome do ponto) no lugar do pino padrão.

**O que é o `latitudeDelta`:** "um cálculo [...] criado na Deep Web", nas palavras de Diego, é só a altura da região visível em graus. 0,014° de latitude ≈ 1,5 km na tela, e quanto maior o delta, menos zoom `[external]` (https://github.com/react-native-maps/react-native-maps/blob/master/docs/mapview.md). O `initialRegion` só vale na montagem; para mover depois, usa-se `region` controlado ou `mapRef.animateToRegion`.

**Produção:** no Android, o Google Maps exige chave de API no build. Com o Expo Go da aula, a chave do próprio Expo cobria isso.

Relacionado: [[wiki/entities/leaflet]] (o mapa da versão web), [[wiki/concepts/geolocation-api]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: mapa dos pontos de coleta
