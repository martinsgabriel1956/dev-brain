---
type: concept
title: "Profiling Mobile"
aliases: ["android studio profiler", "xcode instruments", "perfetto android", "hermes profiler rn"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [mobile, profiling, perfetto, instruments, android-profiler, cpu, memory]
skill: tech-mentor-mobile
status: stable
---

# Profiling Mobile

Medir antes de otimizar — nunca otimizar por intuição.

## Android — Perfetto

```bash
# Capturar trace via adb
adb shell perfetto -o /data/misc/perfetto-traces/trace.pftrace \
    -c - --txt <<EOF
buffers: { size_kb: 63488 }
data_sources: { config { name: "track_event" } }
data_sources: { config { name: "android.gpu.memory" } }
EOF

adb pull /data/misc/perfetto-traces/trace.pftrace
# Abrir em https://ui.perfetto.dev
```

Mais preciso que Android Studio Profiler para system-level tracing. Identifica: frames lentos, thread blocking, GC pauses.

## Android Studio Profiler

CPU Profiler: `Sample Java/Kotlin Methods` para overhead mínimo. Memory Profiler: heap dump para detectar leaks. Network Profiler: waterfall de requests.

## iOS — Xcode Instruments

- **Time Profiler:** CPU por frame — identificar métodos lentos na main thread
- **Allocations:** crescimento de memória — detectar retenção de objetos
- **Leaks:** referências cíclicas não resolvidas pelo ARC
- **App Launch:** breakdown do cold start por fase

```
xctrace record --template "Time Profiler" --launch -- /path/to/app.app
```

## React Native — Hermes Profiler

```bash
# Conectar com Flipper → Hermes Debugger → Start Sampling
# Ou via React Native Debugger
```

Sampling profile — overhead mínimo em produção. Exportar como `.cpuprofile` para Chrome DevTools.

## Memory Leaks em Listas

Causa comum: listener/observer adicionado no `onAttach` e não removido no `onDetach`:

```kotlin
// ❌ Leak
override fun onBindViewHolder(holder: ViewHolder, position: Int) {
    viewModel.liveData.observe(owner) { /* ... */ } // observer nunca removido
}

// ✅ Correto
override fun onBindViewHolder(holder: ViewHolder, position: Int) {
    holder.bind(items[position]) // sem observação no adapter
}
```

## Ver também

- [[mobile-metricas-criticas]] — thresholds para identificar problemas
- [[mobile-animacoes-performaticas]] — medir jank de animações
- [[mobile-baseline-profiles]] — usar Macrobenchmark para baseline

## Key Sources

- [[wiki/sources/mobile-profiling]]
