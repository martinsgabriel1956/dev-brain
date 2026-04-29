---
date: 2026-04-17
tags: [tech-mentor, performance, async, io, memoria, node, go, jvm]
skill: tech-mentor-system-design/references/performance
level: avançado
---

# Async I/O e Memory Management

## Async I/O — Fundamentos

### Event Loop (Node.js / libuv)

O Node.js usa um único thread com event loop. I/O é delegado ao libuv (C), que usa epoll (Linux) / kqueue (macOS) para I/O assíncrono real.

```
┌──────────────────────┐
│   JavaScript Thread  │  ← seu código roda aqui (single thread)
│   (V8 engine)        │
└──────────┬───────────┘
           │ callbacks
┌──────────▼───────────┐
│   Event Loop         │  ← fila de eventos e timers
│   (libuv)            │
└──────────┬───────────┘
           │ I/O async
┌──────────▼───────────┐
│   Thread Pool (4)    │  ← DNS lookup, crypto, fs (não suporta epoll)
│   + epoll (kernel)   │  ← network I/O via epoll — zero threads!
└──────────────────────┘
```

**O que bloqueia o event loop (deve evitar):**
- Loops síncronos longos (> 100ms de CPU puro)
- `JSON.parse` em payloads muito grandes
- `crypto.pbkdf2Sync`, `fs.readFileSync`
- `require()` de módulos grandes em runtime

```typescript
// Ruim — bloqueia o event loop por N * operação_tempo
function processItems(items: unknown[]) {
  return items.map(item => heavySync(item)); // bloqueia thread
}

// Bom — divide em chunks e cede controle ao event loop
async function processItemsAsync(items: unknown[]) {
  const CHUNK_SIZE = 100;
  const results = [];

  for (let i = 0; i < items.length; i += CHUNK_SIZE) {
    const chunk = items.slice(i, i + CHUNK_SIZE);
    results.push(...chunk.map(item => heavySync(item)));
    await new Promise(r => setImmediate(r)); // cede ao event loop entre chunks
  }

  return results;
}
```

### io_uring (Linux 5.1+)

Interface kernel mais moderna que epoll. Usa ring buffers compartilhados entre user space e kernel — zero syscalls para submeter/completar I/O. Node.js 22+ e Bun usam io_uring.

### Goroutines (Go)

Go usa M:N threading — N goroutines mapeadas para M OS threads via GOMAXPROCS.

```go
// Goroutines são baratas — cada uma começa com ~2KB de stack
// (cresce dinamicamente até o limite)
func processRequests(requests []Request) []Result {
  results := make(chan Result, len(requests))

  for _, req := range requests {
    go func(r Request) {
      results <- process(r)
    }(req)
  }

  output := make([]Result, 0, len(requests))
  for range requests {
    output = append(output, <-results)
  }
  return output
}
```

---

## Memory Management

### GC Tuning — JVM (G1GC e ZGC)

```bash
# G1GC — padrão JVM 11+, bom equilíbrio
-XX:+UseG1GC
-XX:MaxGCPauseMillis=200       # target de pausa máxima
-XX:G1HeapRegionSize=16m       # tamanho das regiões
-Xms4g -Xmx4g                  # heap fixo (evita resize em produção)

# ZGC — sub-milissegundo, JVM 21+ (stable)
-XX:+UseZGC
-Xmx8g
# ZGC escala melhor com heaps grandes (> 8GB)
```

**Sinais de problema de GC:**
- GC pause > 100ms frequente → escalar heap ou mudar GC
- `ps_oldgen` cheio frequentemente → memory leak
- GC thrashing: > 10% de CPU em GC → objetos de longa vida excessivos

```bash
# Habilitar GC logging para análise
-Xlog:gc*:file=gc.log:time,uptime:filecount=5,filesize=50m

# GCViewer ou GCEasy para análise visual dos logs
```

### Node.js Heap

```typescript
// Monitorar heap em produção
setInterval(() => {
  const { heapUsed, heapTotal, external } = process.memoryUsage();
  console.log({
    message: "Memory usage",
    heapUsedMB: Math.round(heapUsed / 1024 / 1024),
    heapTotalMB: Math.round(heapTotal / 1024 / 1024),
    externalMB: Math.round(external / 1024 / 1024)
  });

  // Alerta se heap > 80% do total
  if (heapUsed / heapTotal > 0.8) {
    console.log({ message: "High heap usage — possible memory leak" });
  }
}, 60_000);
```

**Causas comuns de memory leak em Node:**
- Event listeners não removidos (`emitter.on` sem `emitter.off`)
- Closures que retêm referência a objetos grandes
- Caches em memória sem limite de tamanho (`Map` que só cresce)
- Promises não resolvidas acumuladas

```typescript
// Prevenção: cache com limite de tamanho
import LRU from "lru-cache";

const cache = new LRU<string, unknown>({
  max: 500,           // máximo de 500 entradas
  ttl: 1000 * 60 * 5 // TTL de 5 minutos
});
```

### Detectar Leak com Clinic.js

```bash
# Heapprofile — identifica onde memória está sendo alocada
clinic heapprofile -- node server.js

# Depois de gerar tráfego:
# Procura objetos que crescem indefinidamente no flame graph de memória
```

## Conceitos Relacionados
[[flame-graph-profiling]] · [[performance-methods]] · [[kubernetes-core]] · [[observabilidade]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-17*
