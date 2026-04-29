---
date: 2026-04-23
tags: [tech-mentor, mobile, platform-engineering, sdk, módulos-nativos, devex, arquitetura]
skill: tech-mentor-mobile/references/platform-engineering
level: arquiteto
---

# Platform Engineering Mobile — Shared SDK, Módulos Nativos, DX da Equipe

## Contexto
Platform Engineering mobile é a camada de infraestrutura que a equipe de produto consome sem precisar entender os detalhes. É o que permite múltiplos times mobile entregarem features rapidamente sem reinventar autenticação, logging, analytics ou storage em cada feature. O output não é um app — é a plataforma que suporta múltiplos apps.

## Como Funciona

### O que vai em um Shared SDK mobile

```
SDK compartilhado:
├── Auth          → tokens, refresh, biometria, login social
├── Networking    → base HTTP client, retry, timeout, interceptors
├── Storage       → MMKV/Keychain/Keystore abstraídos
├── Analytics     → adapter pattern (troca provider sem mudar chamadas)
├── Logging       → estruturado, com contexto, sanitizado
├── FeatureFlags  → abstração sobre Remote Config / LaunchDarkly
├── Crash         → Sentry configurado e wrappers
├── Push          → FCM/APNs token management
└── Utils         → date formatting, currency, validators
```

### Módulo de Analytics — Adapter Pattern

O erro mais comum: chamar Firebase Analytics ou Amplitude diretamente em 200 lugares. Quando você troca de provider, é um PR de 500 linhas.

```typescript
// packages/analytics/src/index.ts
type EventProperties = Record<string, string | number | boolean>;

type AnalyticsProvider = {
  initialize(): Promise<void>;
  identify(userId: string, traits?: EventProperties): void;
  track(event: string, properties?: EventProperties): void;
  screen(name: string, properties?: EventProperties): void;
  reset(): void;
};

class AnalyticsService {
  private providers: AnalyticsProvider[] = [];

  register(provider: AnalyticsProvider) {
    this.providers.push(provider);
  }

  async initialize() {
    await Promise.all(this.providers.map(p => p.initialize()));
  }

  identify(userId: string, traits?: EventProperties) {
    this.providers.forEach(p => p.identify(userId, traits));
  }

  track(event: string, properties?: EventProperties) {
    this.providers.forEach(p => p.track(event, properties));
  }

  screen(name: string, properties?: EventProperties) {
    this.providers.forEach(p => p.screen(name, properties));
  }

  reset() {
    this.providers.forEach(p => p.reset());
  }
}

export const analytics = new AnalyticsService();

// Providers
class MixpanelProvider implements AnalyticsProvider {
  async initialize() { await Mixpanel.init(MIXPANEL_TOKEN); }
  identify(userId: string, traits?: EventProperties) { Mixpanel.identify(userId); }
  track(event: string, properties?: EventProperties) { Mixpanel.track(event, properties); }
  screen(name: string) { Mixpanel.track(`Screen: ${name}`); }
  reset() { Mixpanel.reset(); }
}

class FirebaseProvider implements AnalyticsProvider {
  async initialize() { /* Firebase init */ }
  identify(userId: string) { analytics().setUserId(userId); }
  track(event: string, properties?: EventProperties) {
    analytics().logEvent(event.replace(/\s/g, "_").toLowerCase(), properties);
  }
  screen(name: string) { analytics().logScreenView({ screen_name: name }); }
  reset() { analytics().resetAnalyticsData(); }
}

// Configuração no app
analytics.register(new MixpanelProvider());
analytics.register(new FirebaseProvider());
await analytics.initialize();
```

### Módulo de Networking — Base Client

```typescript
// packages/networking/src/client.ts
type RequestConfig = {
  method: "GET" | "POST" | "PUT" | "PATCH" | "DELETE";
  path: string;
  body?: unknown;
  params?: Record<string, string | number>;
  headers?: Record<string, string>;
  signal?: AbortSignal;
};

type ApiError = {
  status: number;
  message: string;
  code?: string;
};

class ApiClient {
  private baseUrl: string;
  private getToken: () => string | null;
  private onUnauthorized: () => void;

  constructor(config: {
    baseUrl: string;
    getToken: () => string | null;
    onUnauthorized: () => void;
  }) {
    this.baseUrl = config.baseUrl;
    this.getToken = config.getToken;
    this.onUnauthorized = config.onUnauthorized;
  }

  async request<T>(config: RequestConfig): Promise<T> {
    const url = new URL(this.baseUrl + config.path);

    if (config.params) {
      Object.entries(config.params).forEach(([k, v]) => url.searchParams.set(k, String(v)));
    }

    const token = this.getToken();
    const headers: Record<string, string> = {
      "Content-Type": "application/json",
      ...config.headers
    };

    if (token) headers.Authorization = `Bearer ${token}`;

    const response = await fetch(url.toString(), {
      method: config.method,
      headers,
      body: config.body ? JSON.stringify(config.body) : undefined,
      signal: config.signal
    });

    if (response.status === 401) {
      this.onUnauthorized();
      throw new ApiError(401, "Unauthorized", "UNAUTHORIZED");
    }

    if (!response.ok) {
      const errorBody = await response.json().catch(() => ({}));
      throw new ApiError(response.status, errorBody.error ?? "Request failed", errorBody.code);
    }

    if (response.status === 204) return undefined as T;
    return response.json() as Promise<T>;
  }

  get<T>(path: string, params?: Record<string, string | number>, signal?: AbortSignal) {
    return this.request<T>({ method: "GET", path, params, signal });
  }

  post<T>(path: string, body?: unknown) {
    return this.request<T>({ method: "POST", path, body });
  }

  patch<T>(path: string, body?: unknown) {
    return this.request<T>({ method: "PATCH", path, body });
  }

  delete(path: string) {
    return this.request<void>({ method: "DELETE", path });
  }
}

// Singleton compartilhado
export const apiClient = new ApiClient({
  baseUrl: process.env.EXPO_PUBLIC_API_URL!,
  getToken: () => useAuthStore.getState().token,
  onUnauthorized: () => useAuthStore.getState().logout()
});
```

### Módulo Nativo — Criando um Native Module (RN)

Quando não existe uma lib npm para funcionalidade nativa específica:

```kotlin
// Android — NativeModule
@ReactModule(name = SecureStorageModule.NAME)
class SecureStorageModule(reactContext: ReactApplicationContext) :
  ReactContextBaseJavaModule(reactContext) {

  companion object { const val NAME = "SecureStorage" }

  override fun getName() = NAME

  @ReactMethod
  fun setItem(key: String, value: String, promise: Promise) {
    try {
      val keyAlias = "$NAME.$key"
      val keyGenSpec = KeyGenParameterSpec.Builder(keyAlias, KeyProperties.PURPOSE_ENCRYPT or KeyProperties.PURPOSE_DECRYPT)
        .setBlockModes(KeyProperties.BLOCK_MODE_GCM)
        .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
        .build()

      // ... implementação com Android Keystore
      promise.resolve(null)
    } catch (e: Exception) {
      promise.reject("STORAGE_ERROR", e.message, e)
    }
  }

  @ReactMethod
  fun getItem(key: String, promise: Promise) {
    // ... leitura do Keystore
    promise.resolve(decryptedValue)
  }
}
```

```swift
// iOS — NativeModule
@objc(SecureStorageModule)
class SecureStorageModule: NSObject {

  @objc
  func setItem(_ key: String, value: String, resolve: @escaping RCTPromiseResolveBlock, reject: @escaping RCTPromiseRejectBlock) {
    let query: [String: Any] = [
      kSecClass as String: kSecClassGenericPassword,
      kSecAttrAccount as String: key,
      kSecValueData as String: value.data(using: .utf8)!,
      kSecAttrAccessible as String: kSecAttrAccessibleWhenUnlockedThisDeviceOnly
    ]
    SecItemDelete(query as CFDictionary)
    let status = SecItemAdd(query as CFDictionary, nil)
    if status == errSecSuccess { resolve(nil) }
    else { reject("STORAGE_ERROR", "Failed to store item", nil) }
  }

  @objc
  static func requiresMainQueueSetup() -> Bool { false }
}
```

```typescript
// TypeScript — interface tipada sobre o módulo nativo
import { NativeModules } from "react-native";

type SecureStorageNative = {
  setItem(key: string, value: string): Promise<void>;
  getItem(key: string): Promise<string | null>;
  deleteItem(key: string): Promise<void>;
};

const { SecureStorage } = NativeModules as { SecureStorage: SecureStorageNative };

export const secureStorage = {
  set: (key: string, value: string) => SecureStorage.setItem(key, value),
  get: (key: string) => SecureStorage.getItem(key),
  delete: (key: string) => SecureStorage.deleteItem(key)
};
```

### DX da equipe mobile — Toolchain

```typescript
// Ferramentas para melhorar DX

// 1. CLI interno para scaffolding de features
// packages/cli/create-feature.ts
// $ yarn create-feature --name UserProfile --type screen

// 2. Generators — criar boilerplate consistente
// plop.js ou hygen
module.exports = plop => {
  plop.setGenerator("feature", {
    description: "Cria estrutura de feature",
    prompts: [
      { type: "input", name: "name", message: "Nome da feature:" }
    ],
    actions: [
      { type: "add", path: "src/features/{{camelCase name}}/index.ts", templateFile: "templates/feature-index.hbs" },
      { type: "add", path: "src/features/{{camelCase name}}/hooks/use{{pascalCase name}}.ts", templateFile: "templates/hook.hbs" },
      { type: "add", path: "src/features/{{camelCase name}}/{{pascalCase name}}Screen.tsx", templateFile: "templates/screen.hbs" },
      { type: "add", path: "src/features/{{camelCase name}}/__tests__/{{pascalCase name}}.spec.ts", templateFile: "templates/spec.hbs" }
    ]
  });
};

// 3. Shared ESLint + TypeScript config como pacote
// packages/eslint-config-mobile/index.js
// packages/tsconfig-mobile/tsconfig.json
// Consumido por: "@yourorg/eslint-config-mobile"
```

### Monorepo — estrutura para múltiplos apps

```
apps/
├── consumer/          → app de consumidor (B2C)
├── driver/            → app de entregador
└── merchant/          → app de lojista
packages/
├── ui/                → design system compartilhado
├── networking/        → cliente HTTP
├── analytics/         → adapter de analytics
├── auth/              → autenticação
├── storage/           → MMKV, Keychain/Keystore
├── feature-flags/     → abstração de feature flags
└── eslint-config/     → regras de lint compartilhadas

# Turborepo para builds incrementais
# pnpm workspaces para gerenciamento de dependências
```

## Trade-offs

| Aspecto | Monorepo + SDK | Repos separados |
|---|---|---|
| Consistência | Alta (uma versão do SDK) | Baixa (cada app diverge) |
| Setup inicial | Alto | Baixo |
| CI | Complexo (build por app) | Simples |
| Compartilhamento de código | Trivial | Difícil |
| Onboarding | Mais fácil (um repositório) | Mais difícil |
| Blast radius de mudança no SDK | Alto (afeta todos os apps) | Zero |

## Quando Usar / Quando Evitar

**SDK compartilhado** quando 2+ apps mobile da mesma empresa precisam de autenticação, analytics e networking idênticos.

**Monorepo** quando os apps são mantidos pela mesma equipe e compartilham componentes de UI.

**Módulos nativos custom** apenas quando não existe lib matura para a funcionalidade — o custo de manutenção de código nativo iOS + Android é alto.

## Conceitos Relacionados
[[mobile-design-system]] · [[mobile-cicd]] · [[mobile-monitoramento]] · [[mobile-kmp]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
