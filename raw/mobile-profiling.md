---
date: 2026-04-23
tags: [tech-mentor, mobile, profiling, instruments, android-profiler, flutter-devtools, performance]
skill: tech-mentor-mobile/references/performance
level: intermediário
---

# Profiling Mobile — Instruments, Android Studio Profiler, Flutter DevTools

## Contexto
Profiling é o ato de medir antes de otimizar. Sem dados, otimização é palpite. As três ferramentas de profiling mobile cobrem os mesmos problemas — CPU, memória, I/O e rendering — com interfaces diferentes. O fluxo é sempre: medir → identificar gargalo → otimizar → medir de novo.

## Como Funciona

### iOS — Instruments

Instruments é a suíte de profiling da Apple, integrada ao Xcode. Conecte um device físico (simulador não é representativo).

**Time Profiler** — onde o CPU está gastando tempo:
```
Xcode → Product → Profile (⌘I) → Instruments → Time Profiler
```
- Olhe para a Call Tree filtrada por "Self Time" — as funções com maior tempo próprio são os gargalos
- Filtre por "Separate by Thread" para ver qual thread está sobrecarregada
- Main thread bloqueada = jank garantido

**Allocations** — vazamento de memória e alocações excessivas:
```
Instruments → Allocations
- Persistent (vivo): memória que não foi liberada
- Transient (temporário): alocações que já foram liberadas
- Generation: compare antes/depois de uma ação para detectar leaks
```

**Core Animation** — FPS e rendering:
```
Instruments → Core Animation
- FPS abaixo de 60 (ou 120 em ProMotion) indica frames dropped
- Ative "Color Offscreen-Rendered Yellow" para ver layers que renderizam fora da tela
- "Color Blended Layers Red" mostra composição desnecessária
```

**Leaks** — detectar vazamentos:
```
Instruments → Leaks → rode o app por alguns minutos exercitando navegação
- Qualquer barra vermelha = memory leak
- Click na barra → ver stack trace do leak
```

### Android — Android Studio Profiler

```
Android Studio → View → Tool Windows → Profiler → Attach to running process
```

**CPU Profiler:**
- **System Trace:** overhead mínimo, mostra thread activity e frame timing
- **Callstack Sample:** amostragem periódica do stack — bom para encontrar hotspots
- Filtre por "Wall clock time" para ver tempo total, "Thread time" para tempo de CPU puro

```kotlin
// Trace manual no código para marcar seções críticas
import android.os.Trace

Trace.beginSection("ParseProductList")
val products = parseProducts(jsonData)
Trace.endSection()
```

**Memory Profiler:**
- Heap dump: captura estado da memória em um momento
- Allocation tracking: registra cada alocação — caro, use com moderação
- "Retained Size" é o que importa: memória que seria liberada se o objeto fosse coletado

**Network Profiler:**
- Veja payload size, tempo de resposta, requests redundantes
- Conexões simultâneas desnecessárias aparecem aqui

**Janky frames:**
```
Profiler → Display → Frame Rendering
- Verde: ok (< 16ms)
- Amarelo: jank leve (16–32ms)
- Vermelho: jank grave (> 32ms)
```

### Flutter — Flutter DevTools

```bash
# Iniciar com profiling
flutter run --profile

# Abrir DevTools
flutter pub global activate devtools
flutter pub global run devtools
```

**Performance view:**
- UI thread (Dart): lógica, build, layout
- Raster thread (GPU): rendering, shaders
- Qualquer frame > 16ms no UI ou Raster thread = dropped frame

```dart
// Timeline events customizados
import "dart:developer";

Timeline.startSync("ParseProducts");
final products = parseProducts(data);
Timeline.finishSync();
```

**Widget Inspector:**
- Modo "Select Widget Mode" — clique em qualquer widget para ver seus properties e rebuild count
- "Show Performance Overlay" no app: dois gráficos (UI e Raster) — barras acima da linha vermelha = jank

**Memory view:**
- Snapshots para detectar leaks
- "Allocations" mostra rate de alocações por classe
- Crescimento contínuo de memória sem liberação = leak

**CPU Profiler:**
```
DevTools → CPU Profiler → Record → exercite o app → Stop
- Flame chart: eixo X = tempo, eixo Y = call stack
- Barras largas = funções que consomem mais tempo
- Filtre por "User code" para ignorar framework
```

### Métricas a monitorar

| Métrica | Target | Crítico |
|---|---|---|
| Cold start (tempo até first frame) | < 2s | > 3s |
| Frame render time | < 16ms (60fps) | > 32ms |
| ANR (Application Not Responding) | Zero | Qualquer |
| Jank rate | < 0.1% | > 1% |
| Memory (p90 por sessão) | < 150MB | > 300MB |
| Crash-free sessions | > 99.5% | < 99% |

### Profiling no campo — RN

```typescript
// React Native Performance Monitor
import { PerformanceObserver } from "react-native";

// Habilitar no dev: Shake → Perf Monitor
// Mostra: JS FPS, UI FPS, RAM, CPU

// Para profiling de componentes específicos
import { unstable_trace as trace } from "scheduler/tracing";

function handlePress() {
  trace("ButtonPress", performance.now(), () => {
    processExpensiveOperation();
  });
}
```

## Trade-offs

| Ferramenta | Plataforma | Overhead | Uso ideal |
|---|---|---|---|
| Instruments | iOS | Baixo | Profiling completo em device |
| Android Profiler | Android | Médio | Dev iteration rápido |
| Flutter DevTools | Flutter | Baixo | Widget rebuild + frame timing |
| Systrace | Android | Muito baixo | Análise de sistema nível baixo |

## Quando Usar / Quando Evitar

**Profile sempre em device físico** — simuladores/emuladores não refletem memória e CPU real.

**Profile em Release mode** para números representativos — Debug mode tem overhead do DevTools.

**Priorize:** jank e ANR primeiro (usuário percebe imediatamente), depois cold start, depois memória.

**Nunca otimize sem medir primeiro** — o gargalo raramente está onde você acha que está.

## Conceitos Relacionados
[[mobile-metricas-criticas]] · [[mobile-performance-listas]] · [[mobile-animacoes-performaticas]] · [[mobile-baseline-profiles]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
