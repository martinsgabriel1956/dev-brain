---
date: 2026-04-23
tags: [tech-mentor, mobile, monitoramento, sentry, firebase-performance, crashlytics, symbolication, alertas]
skill: tech-mentor-mobile/references/monitoramento
level: avançado
---

# Monitoramento Mobile — Sentry, Firebase Performance, Symbolication, Alertas

## Contexto
Em produção, você não tem DevTools nem console — você descobre problemas quando usuários reclamam ou quando o dashboard mostra aumento de crash rate. Monitoramento mobile exige: crash tracking com stack trace legível (symbolication), performance monitoring com dados reais de usuário (RUM), e alertas que disparam antes de o usuário perceber. A combinação Sentry + Firebase Performance cobre a maior parte dos casos.

## Como Funciona

### 1. Sentry — Crash Tracking + Error Monitoring

```typescript
// React Native — @sentry/react-native
import * as Sentry from "@sentry/react-native";

Sentry.init({
  dsn: process.env.EXPO_PUBLIC_SENTRY_DSN,
  environment: process.env.EXPO_PUBLIC_ENV, // "production" | "staging"
  tracesSampleRate: 0.1, // 10% das sessões têm performance tracking
  profilesSampleRate: 0.1,
  enabled: !__DEV__,

  // Filtrar erros desnecessários
  beforeSend(event) {
    // Não enviar erros de cancelamento de rede
    if (event.exception?.values?.[0]?.type === "AbortError") return null;
    return event;
  },

  integrations: [
    new Sentry.ReactNativeTracing({
      routingInstrumentation: new Sentry.ReactNavigationInstrumentation(),
      tracePropagationTargets: ["api.yourapp.com"]
    })
  ]
});

// Wrapper do app
export default Sentry.wrap(App);
```

```typescript
// Contexto de usuário — para correlacionar erros com usuários
export function identifyUserForSentry(user: User): void {
  Sentry.setUser({
    id: user.id,
    email: user.email,
    username: user.name
  });
}

export function clearSentryUser(): void {
  Sentry.setUser(null);
}

// Tags e context para enriquecer erros
Sentry.setTag("app_version", DeviceInfo.getVersion());
Sentry.setContext("subscription", { plan: user.plan, expiresAt: user.planExpiresAt });

// Capturar erros manuais com contexto
export function captureError(error: Error, context?: Record<string, unknown>): void {
  Sentry.withScope(scope => {
    if (context) scope.setContext("extra", context);
    Sentry.captureException(error);
  });
}

// Breadcrumbs — rastro de ações antes do crash
Sentry.addBreadcrumb({
  category: "user.action",
  message: "User tapped checkout button",
  data: { cartItemCount: cart.items.length, total: cart.total },
  level: "info"
});
```

```kotlin
// Android — Sentry SDK
SentryAndroid.init(context) { options ->
  options.dsn = BuildConfig.SENTRY_DSN
  options.environment = BuildConfig.ENVIRONMENT
  options.tracesSampleRate = 0.1
  options.isEnableUserInteractionTracing = true
  options.isEnableAutoSessionTracking = true
}

// Identificar usuário
Sentry.setUser(User().apply {
  id = user.id
  email = user.email
})
```

### 2. Symbolication — Transformar endereços em stack traces legíveis

Sem symbolication, o crash report mostra: `0x1000a4b20 + 0x34c`. Com symbolication: `ProductRepository.swift:147 - fetchProduct(id:)`.

**iOS — dsym upload:**
```bash
# Fastlane — upload de dSYM após build
lane :upload_symbols do
  download_dsyms(
    app_identifier: "com.yourcompany.app",
    version: "2.1.0",
    build_number: "143"
  )
  upload_symbols_to_sentry(
    api_key: ENV["SENTRY_AUTH_TOKEN"],
    org_slug: "yourorg",
    project_slug: "yourapp"
  )
end
```

**Android — ProGuard mapping:**
```kotlin
// build.gradle.kts — habilitar ProGuard em release
android {
  buildTypes {
    release {
      isMinifyEnabled = true
      isShrinkResources = true
      proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro")
    }
  }
}
```

```yaml
# CI — upload do mapping para Sentry
- name: Upload ProGuard mapping
  run: |
    npx @sentry/cli android upload-proguard \
      --org ${{ secrets.SENTRY_ORG }} \
      --project ${{ secrets.SENTRY_PROJECT }} \
      android/app/build/outputs/mapping/release/mapping.txt
```

**React Native — source maps:**
```bash
# Gerar e fazer upload de source maps
npx react-native bundle \
  --platform android \
  --dev false \
  --entry-file index.js \
  --bundle-output android-release.bundle \
  --sourcemap-output android-release.bundle.map

npx @sentry/cli releases files VERSION upload-sourcemaps \
  android-release.bundle.map \
  --dist BUILD_NUMBER
```

### 3. Firebase Performance — RUM (Real User Monitoring)

```typescript
// React Native — @react-native-firebase/perf
import perf from "@react-native-firebase/perf";

// Trace customizado — medir operações críticas
export async function measureOperation<T>(
  name: string,
  operation: () => Promise<T>,
  attributes?: Record<string, string>
): Promise<T> {
  const trace = await perf().startTrace(name);

  if (attributes) {
    Object.entries(attributes).forEach(([key, value]) => trace.putAttribute(key, value));
  }

  try {
    const result = await operation();
    trace.putMetric("success", 1);
    return result;
  } catch (error) {
    trace.putMetric("error", 1);
    throw error;
  } finally {
    await trace.stop();
  }
}

// Uso
const products = await measureOperation(
  "load_product_list",
  () => productRepository.getProducts({ page: 1 }),
  { source: "api", user_tier: "premium" }
);

// Network monitoring — automático para Axios
// Configurar interceptor para registrar latência
http.interceptors.response.use(
  response => {
    const duration = Date.now() - response.config.metadata.startTime;
    perf().newHttpMetric(response.config.url!, response.config.method!.toUpperCase())
      .then(metric => {
        metric.setResponseCode(response.status);
        metric.setResponseContentType(response.headers["content-type"]);
        metric.stop();
      });
    return response;
  }
);
```

```dart
// Flutter — firebase_performance
final perf = FirebasePerformance.instance;

Future<List<Product>> loadProducts() async {
  final trace = perf.newTrace("load_products");
  await trace.start();

  try {
    final products = await repository.getProducts();
    trace.setMetric("product_count", products.length);
    return products;
  } finally {
    await trace.stop();
  }
}
```

### 4. Firebase Crashlytics — Complementar ao Sentry

```kotlin
// Android — Firebase Crashlytics
FirebaseCrashlytics.getInstance().apply {
  setUserId(user.id)
  setCustomKey("plan", user.plan)
  setCustomKey("app_version", BuildConfig.VERSION_NAME)
}

// Log customizado antes de crash (aparece no relatório)
FirebaseCrashlytics.getInstance().log("User started checkout with ${cart.itemCount} items")

// Erro não-fatal
FirebaseCrashlytics.getInstance().recordException(e)
```

### 5. Alertas de Regressão

```yaml
# Sentry — configurar alertas por projeto
# (via API ou UI do Sentry)

# Alert 1: crash rate
# Condição: crash_free_sessions < 99.5% em 1h
# Ação: notificar Slack #mobile-alerts

# Alert 2: p95 latência de API
# Condição: p95(load_product_list) > 3000ms em 30min
# Ação: notificar PagerDuty

# Alert 3: novo erro com alta frequência
# Condição: novo issue > 50 occurrences em 1h
# Ação: notificar Slack + criar ticket no Linear
```

```typescript
// Health check automático pós-release
// Verificar se crash rate aumentou após deploy

async function checkPostReleaseCrashRate(version: string): Promise<void> {
  const stats = await sentryClient.getProjectStats({
    field: ["sum(session.crashed)"],
    groupBy: ["release"],
    query: `release:${version}`,
    interval: "1h"
  });

  const crashedSessions = stats.data[0]?.[1]?.[0]?.value ?? 0;
  const totalSessions = stats.data[0]?.[1]?.[1]?.value ?? 1;
  const crashRate = crashedSessions / totalSessions;

  if (crashRate > 0.005) { // > 0.5% = alerta
    await notifySlack({
      channel: "#mobile-alerts",
      text: `⚠️ Crash rate ${(crashRate * 100).toFixed(2)}% na versão ${version} — acima do threshold`
    });
  }
}
```

### Dashboard de monitoramento — métricas chave

```
Métricas para monitorar em produção:

Crash & Errors:
□ Crash-free sessions (target: > 99.5%)
□ Error rate por versão (comparar com versão anterior)
□ Top 5 crashes por impacto (usuários afetados × frequência)
□ Regressões: erros novos pós-release

Performance:
□ Cold start p50, p90, p99 por device tier (low/mid/high end)
□ p95 latência dos endpoints críticos (checkout, login, home)
□ Frame rate p50, p95 nas telas principais
□ App size por versão (alertar se cresceu > 5%)

Usuário:
□ Session duration (quedas = algo quebrando)
□ Crash-to-DAU ratio
□ API error rate vista pelo usuário (≠ do servidor)
```

## Trade-offs

| Ferramenta | Crash tracking | Performance | Custo | Ideal para |
|---|---|---|---|---|
| Sentry | Excelente (symbolication, breadcrumbs) | Básico | Grátis até 5k erros/mês | Todos |
| Firebase Crashlytics | Bom | Não tem | Grátis | Alternativa ao Sentry |
| Firebase Performance | Não tem | Excelente (RUM) | Grátis | Complementar ao Sentry |
| Datadog Mobile RUM | Excelente | Excelente | Caro | Enterprise |
| New Relic Mobile | Bom | Bom | Médio | Enterprise |

## Quando Usar / Quando Evitar

**Sentry + Firebase Performance** é a stack padrão para a maioria dos projetos — Sentry para erros, Firebase para performance de usuário real.

**Sempre configure symbolication** antes de ir para produção — crash reports sem symbolication são praticamente inúteis.

**Alertas de crash rate** devem disparar antes de a equipe perceber — configure threshold de 0.5% com janela de 1h pós-deploy.

**Nunca** logar PII (email, CPF, token) no Sentry ou Firebase — configure `beforeSend` para sanitizar.

## Conceitos Relacionados
[[mobile-cicd]] · [[mobile-metricas-criticas]] · [[mobile-baseline-profiles]] · [[mobile-testes]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
