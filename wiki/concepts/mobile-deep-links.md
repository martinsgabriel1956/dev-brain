---
type: concept
title: "Deep Links Mobile — Universal Links, App Links"
aliases: ["universal links ios", "app links android", "deferred deep links", "mobile url scheme"]
date_created: 2026-04-24
date_updated: 2026-11-16
source_count: 3
tags: [mobile, deep-links, universal-links, app-links, deferred-deep-links]
skill: tech-mentor-mobile
status: stable
---

# Deep Links Mobile

## Tipos

| Tipo | iOS | Android | Segurança | Fallback |
|---|---|---|---|---|
| Custom scheme | `myapp://` | `myapp://` | Baixa | Sem fallback |
| Universal / App Links | `https://app.com/path` | `https://app.com/path` | Alta (HTTPS verificado) | Browser |
| Deferred | Branch.io / FDL | Branch.io / FDL | Alta | Funciona sem app instalado |

## Universal Links (iOS)

1. Hospedar `/.well-known/apple-app-site-association` no domínio
2. `Content-Type: application/json`
3. Associar App ID no arquivo

```json
{
  "applinks": {
    "apps": [],
    "details": [{"appID": "TEAMID.com.example.app", "paths": ["/product/*", "/order/*"]}]
  }
}
```

## App Links (Android)

1. Hospedar `/.well-known/assetlinks.json`
2. Declarar `intent-filter` com `autoVerify="true"` no `AndroidManifest.xml`

## Handling no App

```js
// React Navigation — links enquanto app está aberto
const linking = {
    prefixes: ['https://app.com'],
    config: { screens: { Product: 'product/:id' } }
};

// Cold start — app aberto via link
Linking.getInitialURL().then(url => { /* navegar para tela correta */ });
```

## Ver também

- [[wiki/concepts/mobile-navegacao]] — integrar deep links com stack de navegação
- [[wiki/concepts/mobile-push-notifications]] — notificações com deep link como payload

No app do Ecoleta ([[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]), o botão do WhatsApp usa "um recurso chamado Deep Linking" para abrir o app instalado no celular.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]], `Linking.openURL('whatsapp://send?phone=...&text=...')` abre o WhatsApp pelo esquema do app. O texto vai sem `encodeURIComponent`. O link universal `https://wa.me/` funciona mesmo sem o app.

## Key Sources

- [[wiki/sources/mobile-deep-links]]
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: deep link para o WhatsApp no Ecoleta
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: whatsapp://send no Ecoleta; wa.me como alternativa
