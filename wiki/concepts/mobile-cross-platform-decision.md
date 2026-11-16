---
type: concept
title: "Decisão Cross-Platform Mobile"
aliases: ["flutter vs react native", "cross platform decision", "mobile platform choice"]
date_created: 2026-04-24
date_updated: 2026-11-16
source_count: 3
tags: [mobile, cross-platform, flutter, react-native, kmp, nativo, decisao]
skill: tech-mentor-mobile
status: stable
---

# Decisão Cross-Platform Mobile

## Framework de Decisão

| Critério | Flutter | React Native | KMP | Nativo |
|---|---|---|---|---|
| UI pixel-perfect cross-platform | ✅ | ⚠️ | ❌ (UI nativa) | ✅ por plataforma |
| Reutilização de código web | ❌ | ✅ (JS) | ⚠️ (lógica) | ❌ |
| Performance de listas/animações | ✅ | ✅ (Nova Arq.) | N/A | ✅ |
| Hardware intensivo (BT, AR, saúde) | ⚠️ | ⚠️ | ⚠️ | ✅ |
| Team com Kotlin/Swift expertise | ❌ | ❌ | ✅ | ✅ |
| Time to market (MVP) | ✅ | ✅ | ❌ | ❌ |

## Flutter

Renderiza com Impeller/Skia próprio — UI **idêntica** em iOS e Android. Dart como linguagem. Ideal quando UI cross-platform consistente é prioridade e o time aceita aprender Dart.

## React Native (Nova Arquitetura)

JSI elimina bridge — chamadas síncronas para módulos nativos. Ideal quando o time já tem expertise em React/TypeScript.

## KMP

Compartilha domain + data layer; UI permanece nativa (Compose + SwiftUI). Sem comprometer fidelidade nativa. Ideal para times com Kotlin expertise.

## Nativo Puro

Obrigatório para: ARKit/ARCore intensivo, Bluetooth BLE avançado, HealthKit/Health Connect, jogos com Metal/Vulkan.

**Regra geral:** team expertise > performance teórica. Um time JS que força Swift vai entregar pior que um time JS com RN.

## Ver também

- [[wiki/concepts/mobile-kmp]] — KMP em profundidade
- [[wiki/concepts/mobile-design-system]] — como manter consistência entre plataformas

Em [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]], a defesa de iniciante do [[wiki/entities/react-native]]: uma base em vez de um app em Objective-C/Swift e outro em Java/Kotlin, e interface nativa ao contrário de Ionic/PhoneGap.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]], a defesa prática: o mesmo React da web, com estilos em CSS-em-JS via Yoga, roda em Android e iOS.

## Key Sources

- [[wiki/sources/mobile-cross-platform-decision]]
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: React Native x dois apps nativos
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: prática do RN + Expo no Ecoleta
