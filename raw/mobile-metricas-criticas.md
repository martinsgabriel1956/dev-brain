---
date: 2026-04-23
tags: [tech-mentor, mobile, performance, cold-start, jank, anr, métricas]
skill: tech-mentor-mobile/references/performance
level: intermediário
---

# Métricas Críticas de Performance Mobile

## Contexto
Performance mobile não é abstrata — tem números concretos que a Play Store e App Store usam para ranking, e que usuários sentem diretamente. Cold start > 3s perde 50% dos usuários antes do app abrir. Jank (frames perdidos) é a segunda causa de desinstalação. ANR no Android pode resultar em remoção da Play Store. Essas três métricas são o piso mínimo de qualidade.

## Como Funciona

### 1. Cold Start < 2s

**Cold start:** app não está em memória, processo é criado do zero.
**Warm start:** processo existe, Activity/ViewController é recriada.
**Hot start:** app volta do background, tudo em memória.

```
Cold start timeline Android:
zygote fork → Application.onCreate() → MainActivity.onCreate() → first frame

Cold start timeline iOS:
dyld load → main() → UIApplicationMain() → viewDidLoad() → first frame
```

**Android — medir:**
```bash
adb shell am start-activity -W -n com.yourapp/.MainActivity
# ThisTime: tempo desta atividade
# TotalTime: tempo total desde o launch
# WaitTime: tempo até resposta do sistema
```

**iOS — medir via Instruments:**
```
Instruments → App Launch → gravar cold start
Medir: "Time to first frame" na timeline
```

**Otimizações de cold start:**

```kotlin
// Android — NÃO fazer no Application.onCreate()
class App : Application() {
  override fun onCreate() {
    super.onCreate()
    // ERRADO: inicializar tudo aqui bloqueia o start
    // heavySDK.initialize(this)
    // databaseMigration.run()

    // CORRETO: apenas o essencial
    FirebaseApp.initializeApp(this) // rápido
    
    // Inicializações pesadas em background
    lifecycleScope.launch(Dispatchers.IO) {
      heavySDK.initialize(this@App)
    }
  }
}
```

```swift
// iOS — Lazy initialization
class AppDelegate: UIResponder, UIApplicationDelegate {
  func application(_ application: UIApplication, didFinishLaunchingWithOptions ...) -> Bool {
    // Apenas essencial
    configureAppearance()
    
    // Analytics e SDKs pesados: defer
    DispatchQueue.global(qos: .background).async {
      AnalyticsSDK.configure()
    }
    
    return true
  }
}
```

```typescript
// React Native — lazy imports e defer de setup
// ERRADO: importar tudo no topo
import HeavyLibrary from "heavy-library"; // 2MB de JS

// CORRETO: lazy import
const HeavyLibrary = React.lazy(() => import("heavy-library"));

// Expo: usar expo-font com Promise.all para carregar fontes em paralelo
export default function App() {
  const [loaded] = useFonts({ Inter_400Regular, Inter_700Bold });
  
  if (!loaded) return <SplashScreen />;
  return <RootNavigator />;
}
```

**Baseline Profiles Android** (reduz cold start em até 40%):
→ Ver [[mobile-baseline-profiles]]

### 2. Jank < 16ms/frame (60fps)

Jank = frame que leva mais de 16ms para renderizar (para 60fps) ou 8ms (para 120fps).

```
Frame budget:
60fps → 16.67ms por frame
90fps → 11.11ms por frame
120fps → 8.33ms por frame
```

**Causas comuns de jank:**

```typescript
// JANK: processamento pesado na thread de UI
export function ProductList({ products }: { products: Product[] }) {
  // Este sort roda em toda re-renderização — bloqueia a UI thread
  const sorted = products.sort((a, b) => b.price - a.price);
  return <FlatList data={sorted} />;
}

// SEM JANK: memoizar operações pesadas
export function ProductList({ products }: { products: Product[] }) {
  const sorted = useMemo(
    () => [...products].sort((a, b) => b.price - a.price),
    [products]
  );
  return <FlashList data={sorted} estimatedItemSize={80} />;
}
```

```kotlin
// Android — NUNCA fazer I/O na main thread
// ERRADO
val user = database.userDao().getUser(id) // bloqueia UI!

// CORRETO
viewModelScope.launch(Dispatchers.IO) {
  val user = database.userDao().getUser(id)
  withContext(Dispatchers.Main) { updateUi(user) }
}
```

**Detectar jank:**
```bash
# Android
adb shell dumpsys gfxinfo com.yourapp framestats

# Saída relevante:
# Janky frames: X (Y.Z%)
# 50th percentile: Xms
# 90th percentile: Xms
# 95th percentile: Xms
# 99th percentile: Xms
```

```dart
// Flutter — SchedulerBinding para monitorar frames
SchedulerBinding.instance.addTimingsCallback((timings) {
  for (final timing in timings) {
    if (timing.totalSpan.inMilliseconds > 16) {
      console.log({
        "message": "Jank detected",
        "duration": timing.totalSpan.inMilliseconds,
        "buildDuration": timing.buildDuration.inMilliseconds,
        "rasterDuration": timing.rasterDuration.inMilliseconds,
      });
    }
  }
});
```

### 3. ANR Zero (Android Not Responding)

ANR ocorre quando a main thread fica bloqueada por > 5s (input) ou > 10s (broadcast/service).

```kotlin
// Causas comuns de ANR:

// 1. I/O na main thread
val file = File(path).readText() // ANR se arquivo grande

// 2. Lock contention
synchronized(heavyObject) { /* operação longa */ }

// 3. Binder transaction pesada
val result = remoteService.heavyOperation() // bloqueia até retornar

// Solução: StrictMode para detectar em dev
if (BuildConfig.DEBUG) {
  StrictMode.setThreadPolicy(
    StrictMode.ThreadPolicy.Builder()
      .detectDiskReads()
      .detectDiskWrites()
      .detectNetwork()
      .penaltyLog()
      .build()
  )
}
```

**iOS equivalente — Main Thread Checker:**
```
Xcode → Product → Scheme → Run → Diagnostics → Main Thread Checker ✓
Detecta operações de UI fora da main thread
```

### Monitoramento em produção

```typescript
// Firebase Performance — custom traces
import perf from "@react-native-firebase/perf";

async function loadUserProfile(userId: string) {
  const trace = await perf().startTrace("load_user_profile");
  trace.putAttribute("user_type", "premium");

  try {
    const user = await fetchUser(userId);
    trace.putMetric("profile_fields_count", Object.keys(user).length);
    return user;
  } finally {
    await trace.stop();
  }
}
```

## Checklist de Performance

```
Cold Start:
□ Application.onCreate() / AppDelegate não tem I/O síncrono
□ Fontes/assets carregados em paralelo
□ SDKs pesados inicializados em background thread
□ Splash screen esconde o loading inicial

Jank:
□ Listas usam FlatList/FlashList (RN) ou LazyColumn (Android) ou ListView.builder (Flutter)
□ Imagens têm dimensões corretas (não escalar no runtime)
□ Sem sort/filter caros em render sem memoização
□ Animações usam a thread nativa (Reanimated 3 / Compose Animated)

ANR / freeze:
□ StrictMode ativado em debug (Android)
□ Main Thread Checker ativado (iOS)
□ Sem SharedPreferences.edit().commit() na main thread
□ Sem operações de rede síncronas na UI thread
```

## Conceitos Relacionados
[[mobile-profiling]] · [[mobile-performance-listas]] · [[mobile-animacoes-performaticas]] · [[mobile-baseline-profiles]] · [[mobile-monitoramento]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
