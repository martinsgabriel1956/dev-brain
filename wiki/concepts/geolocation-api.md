---
type: concept
title: "Geolocation API"
aliases: ["navigator.geolocation", "getCurrentPosition", "geolocalização no navegador"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [browser-api, geolocalizacao, privacidade, frontend]
skill: tech-mentor-frontend
status: stub
---

# Geolocation API

API do navegador para obter a posição do dispositivo: `navigator.geolocation.getCurrentPosition(success, error, options)`, ou `watchPosition` para acompanhar. A posição chega em `position.coords.latitude/longitude/accuracy`.

No Ecoleta ([[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]), centraliza o mapa [[wiki/entities/leaflet]] na posição do usuário quando a tela abre, num [[wiki/concepts/useEffect]] com `[]`. [[wiki/entities/diego-fernandes]] avisa que "as vezes é permissão", e a dica é deixar fixo se falhar.

**O que a aula não trata:**

- **Contexto seguro:** só funciona em HTTPS ou `localhost`. Em HTTP de produção, a API nem existe.
- **Permissão e erro:** o segundo callback recebe `PERMISSION_DENIED`, `POSITION_UNAVAILABLE` ou `TIMEOUT`. Sem ele, o mapa fica em `[0, 0]`. O `{ timeout, maximumAge, enableHighAccuracy }` controla espera e precisão.
- **Pedido no momento certo:** pedir na carga da página, sem contexto, aumenta as recusas. O melhor é pedir após um gesto ("usar minha localização") e ter uma alternativa (escolher no mapa ou pela cidade).
- **Precisão:** no desktop, vem do Wi-Fi ou do IP e pode errar por quilômetros. Vale mostrar o `accuracy`.

`[skill: tech-mentor-frontend]` A skill embrulha a API numa promise ou num hook (`useGeolocation`) com tratamento de erro.

No mobile ([[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]), o equivalente é o `expo-location`: pedido de permissão, `getCurrentPositionAsync`, e os simuladores com localização manual (Custom Location no iOS).

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: posição inicial do mapa do formulário
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: expo-location no app
