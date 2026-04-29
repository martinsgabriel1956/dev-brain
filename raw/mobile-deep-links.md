---
date: 2026-04-23
tags: [tech-mentor, mobile, deep-links, universal-links, app-links, react-native, flutter]
skill: tech-mentor-mobile/references/deep-links
level: intermediário
---

# Deep Links — Universal Links / App Links

## Contexto
Deep links permitem abrir uma tela específica do app a partir de uma URL — em e-mails, notificações, QR codes, redes sociais. Sem deep links, o máximo que você consegue é abrir o app na tela inicial. Com Universal Links (iOS) e App Links (Android), a URL abre o app se instalado, ou o browser como fallback — sem esquemas proprietários (`myapp://`).

## Como Funciona

### Tipos de deep link

| Tipo | Formato | Fallback | iOS | Android |
|---|---|---|---|---|
| Custom Scheme | `myapp://profile/123` | Erro se não instalado | Sim | Sim |
| Universal Links | `https://app.com/profile/123` | Browser | iOS 9+ | ✗ |
| App Links | `https://app.com/profile/123` | Browser | ✗ | Android 6+ |

### Universal Links — iOS

**Passo 1:** Criar `apple-app-site-association` no servidor (sem extensão, Content-Type: `application/json`):

```json
{
  "applinks": {
    "apps": [],
    "details": [
      {
        "appIDs": ["TEAMID.com.yourcompany.app"],
        "components": [
          { "/": "/profile/*", "comment": "Perfil de usuário" },
          { "/": "/order/*", "comment": "Detalhes de pedido" },
          { "/": "/reset-password", "comment": "Redefinição de senha" }
        ]
      }
    ]
  }
}
```

Hospedar em: `https://yourdomain.com/.well-known/apple-app-site-association`

**Passo 2:** Configurar Associated Domains no Xcode:
```
Capabilities → Associated Domains → applinks:yourdomain.com
```

### App Links — Android

**Passo 1:** Criar `assetlinks.json`:

```json
[{
  "relation": ["delegate_permission/common.handle_all_urls"],
  "target": {
    "namespace": "android_app",
    "package_name": "com.yourcompany.app",
    "sha256_cert_fingerprints": ["SHA256_FINGERPRINT_DO_KEYSTORE"]
  }
}]
```

Hospedar em: `https://yourdomain.com/.well-known/assetlinks.json`

**Passo 2:** Configurar `AndroidManifest.xml`:

```xml
<activity android:name=".MainActivity">
  <intent-filter android:autoVerify="true">
    <action android:name="android.intent.action.VIEW" />
    <category android:name="android.intent.category.DEFAULT" />
    <category android:name="android.intent.category.BROWSABLE" />
    <data
      android:scheme="https"
      android:host="yourdomain.com"
      android:pathPrefix="/profile" />
  </intent-filter>
</activity>
```

### React Native — Expo Router (integração automática)

Expo Router resolve deep links automaticamente pela estrutura de arquivos:

```
app/
├── profile/
│   └── [id].tsx     → /profile/:id
└── order/
    └── [orderId].tsx → /order/:orderId
```

```typescript
// app.json — configurar scheme e domínio
{
  "expo": {
    "scheme": "myapp",
    "intentFilters": [
      {
        "action": "VIEW",
        "autoVerify": true,
        "data": [
          {
            "scheme": "https",
            "host": "yourdomain.com",
            "pathPrefix": "/profile"
          }
        ],
        "category": ["BROWSABLE", "DEFAULT"]
      }
    ]
  }
}
```

```typescript
// Ler params na tela
import { useLocalSearchParams } from "expo-router";

export default function ProfileScreen() {
  const { id } = useLocalSearchParams<{ id: string }>();
  return <UserProfile userId={id} />;
}
```

### React Native — React Navigation (configuração manual)

```typescript
const linking: LinkingOptions<RootStack> = {
  prefixes: ["myapp://", "https://yourdomain.com"],
  config: {
    screens: {
      Home: "",
      Profile: "profile/:userId",
      Order: "order/:orderId",
      ResetPassword: {
        path: "reset-password",
        parse: {
          token: token => decodeURIComponent(token)
        }
      }
    }
  },
  // Handler para quando app está em background/terminated
  async getInitialURL() {
    const url = await Linking.getInitialURL();
    return url;
  },
  subscribe(listener) {
    const sub = Linking.addEventListener("url", ({ url }) => listener(url));
    return () => sub.remove();
  }
};

<NavigationContainer linking={linking}>
  {/* ... */}
</NavigationContainer>
```

### Flutter — GoRouter + uni_links

```dart
// pubspec.yaml: uni_links: ^0.5.1

class DeepLinkService {
  StreamSubscription? _sub;

  void initialize(GoRouter router) {
    // App aberto via link (já estava aberto)
    _sub = uriLinkStream.listen(
      (uri) {
        if (uri != null) router.go(uri.path, extra: uri.queryParameters);
      },
      onError: (err) => console.log({ message: "Deep link error", error: err })
    );
  }

  Future<String?> getInitialLink() async {
    try {
      final uri = await getInitialUri();
      return uri?.toString();
    } catch (_) {
      return null;
    }
  }

  void dispose() => _sub?.cancel();
}

// GoRouter com URL matching
final router = GoRouter(
  initialLocation: "/",
  routes: [
    GoRoute(path: "/profile/:id", builder: (ctx, state) =>
      ProfileScreen(id: state.pathParameters["id"]!)
    ),
  ],
);
```

## Estratégia de Navegação Contextual

O deep link não deve apenas abrir a tela — deve construir o stack de navegação correto:

```typescript
// Ao receber /order/123, o stack deve ser: Home → Orders → OrderDetail
// Não apenas abrir OrderDetail sem contexto de voltar

function handleDeepLink(url: string) {
  const { path, params } = parseLinkingUrl(url);

  if (path === "order/:orderId") {
    navigation.reset({
      index: 2,
      routes: [
        { name: "Home" },
        { name: "Orders" },
        { name: "OrderDetail", params: { orderId: params.orderId } }
      ]
    });
  }
}
```

## Trade-offs

| Aspecto | Custom Scheme | Universal/App Links |
|---|---|---|
| Setup | Simples | Requer hospedagem de arquivo |
| Fallback | Nenhum (erro) | Browser |
| Compartilhamento social | Não funciona | Funciona |
| Segurança | Qualquer app pode interceptar | Verificado por domínio |
| Recomendado para produção | Não | Sim |

## Quando Usar / Quando Evitar

**Use Universal/App Links** sempre em produção — custom schemes podem ser interceptados por apps maliciosos (URL hijacking).

**Implemente sempre fallback web:** a URL deve funcionar no browser para usuários sem o app instalado (landing page de download ou conteúdo real).

**Teste os três estados:** app aberto em foreground, app em background, app não instalado.

**Não esqueça:** deep links em notificações push usam o mesmo mecanismo — unifique o handler.

## Conceitos Relacionados
[[mobile-push-notifications]] · [[mobile-navegacao]] · [[mobile-seguranca]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
