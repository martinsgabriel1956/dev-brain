---
type: entity
title: "Leaflet"
aliases: ["react-leaflet", "Leaflet.js", "OpenStreetMap tiles"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [mapas, javascript, open-source, react]
skill: tech-mentor-frontend
status: stub
---

# Leaflet

Biblioteca JavaScript de mapas interativos, de código aberto. É usada com tiles do OpenStreetMap (ou de outros provedores) e, no React, por meio do react-leaflet.

Na NLW #1 com [[wiki/entities/diego-fernandes|Diego Fernandes]] ([[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]), substitui o Google Maps, que exige conta e cartão de crédito ("seria um rolo"):

- **Montagem:** CSS do Leaflet no `index.html`, `<Map center zoom>`, `<TileLayer>` do OpenStreetMap e `<Marker position>`.
- **Interação:** `onClick` com `LeafletMouseEvent` dá `event.latlng`, que vira estado e move o marcador. O `center` inicial vem da [[wiki/concepts/geolocation-api]].

**react-leaflet hoje:**

- `<Map>` virou `<MapContainer>` no v3. Eventos vão por `useMapEvents` num componente filho, e props como `center` e `zoom` só valem na montagem; para mover depois, usa-se `map.setView` `[external]` (https://react-leaflet.js.org/docs/api-map/).
- Os tiles públicos do OpenStreetMap têm política de uso e não servem para tráfego alto. Em produção, usa-se um provedor de tiles ou servidor próprio `[external]` (https://operations.osmfoundation.org/policies/tiles/).

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]], o app mobile troca o Leaflet pelo react-native-maps, e o `zoom` vira `latitudeDelta`.

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: mapa do formulário, clique e marcador
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: contraponto: react-native-maps no mobile
