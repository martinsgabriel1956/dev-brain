---
type: source
title: "Async I/O e Memory Management"
aliases: ["async io", "event loop", "memory management", "libuv", "io_uring", "node heap", "gc tuning jvm"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/async-io-memory-management.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [async-io, event-loop, memory-management, libuv, io-uring, node-heap, gc-jvm, goroutines, performance]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

Async I/O: Node.js usa single thread + event loop (libuv/epoll) — network I/O usa zero threads extras via epoll, apenas DNS/crypto/fs usam thread pool (4). io_uring (Linux 5.1+, Node 22+, Bun) elimina syscalls via ring buffers compartilhados. Go usa goroutines (M:N scheduling) — não bloqueia threads OS. Memory: Node.js heap monitora com `process.memoryUsage()`, leaks comuns são event listeners não removidos e caches sem limite. JVM: G1GC para equilíbrio, ZGC para pauses sub-milissegundo com heaps > 8GB.

## Key Claims

**Claim:** Bloquear o event loop do Node.js com CPU-bound > 100ms degrada todas as requisições simultâneas — chunk + `setImmediate` é o padrão de mitigação.
**Evidence:** Node.js: JavaScript roda em single thread. CPU puro > 100ms (JSON.parse de payload grande, `crypto.pbkdf2Sync`, loops de processamento) congela o event loop — nenhuma outra requisição é processada durante esse tempo. Mitigação: dividir em chunks de 100 itens com `await new Promise(r => setImmediate(r))` entre chunks, cedendo controle ao event loop para processar outras requisições.
**Confidence:** alta

**Claim:** Memory leaks em Node.js têm 4 causas recorrentes — todas evitáveis com padrões defensivos.
**Evidence:** (1) Event listeners não removidos: `emitter.on` sem `emitter.off` correspondente acumula referências. (2) Closures retendo objetos grandes. (3) Caches sem limite: `Map` que só cresce — solução: `lru-cache` com `max: 500` e TTL. (4) Promises não resolvidas acumuladas. Detecção: `process.memoryUsage()` em loop com alerta se `heapUsed / heapTotal > 0.8`. Clinic.js para profiling de leaks.
**Confidence:** alta

**Claim:** JVM GC choice depende do tamanho do heap — G1GC para heaps < 8GB, ZGC para heaps maiores e latência crítica.
**Evidence:** G1GC (JVM 11+ padrão): `MaxGCPauseMillis=200` como target, bom equilíbrio throughput/latência, heap fixo (`-Xms4g -Xmx4g`) evita resize em produção. ZGC (JVM 21+ stable): pauses sub-milissegundo, escala melhor com heaps grandes. Sinais de problema: GC pause > 100ms frequente, `ps_oldgen` cheio (memory leak), GC thrashing > 10% CPU. Análise com GCViewer/GCEasy a partir de GC logs (`-Xlog:gc*`).
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/event-loop]]
- [[concepts/libuv]]
- [[concepts/io-uring]]
- [[concepts/goroutines]]
- [[concepts/v8-heap]]
- [[concepts/gc-tuning]]
- [[concepts/memory-leak]]
- [[entities/clinic-js]]

## Open Questions

- io_uring em produção com Node.js 22+ — impacto real de performance vs epoll em cargas I/O-bound?
- Goroutines Go vs async/await Node.js para sistemas de alta concorrência — quando Go é claramente superior?
