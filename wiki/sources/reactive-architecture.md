---
type: source
title: "Reactive Architecture"
aliases: ["reactive architecture", "reactive manifesto", "backpressure", "message-driven", "elasticidade", "resilience reactive"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/reactive-architecture.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [reactive-architecture, reactive-manifesto, backpressure, message-driven, elasticity, resilience, rxjs, node-streams]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Reactive Architecture (Reactive Manifesto): 4 pilares — Responsive (responde em tempo), Resilient (falha localizada), Elastic (escala sob carga), Message-Driven (comunicação assíncrona via mensagens). Backpressure é o conceito central: consumidor sinaliza ao produtor para reduzir taxa quando não consegue acompanhar — em vez de cair ou descartar silenciosamente. Node.js Streams e RxJS implementam backpressure.

## Key Claims

**Claim:** Backpressure previne cascata de falhas — consumidor lento sinaliza de volta ao produtor em vez de cair.
**Evidence:** Sem backpressure: produtor emite a 100k msg/s, consumidor processa 10k msg/s → buffer explode → OOM. Com backpressure: `writeStream.write()` retorna `false` quando buffer cheio → `readStream.pause()` → consumer processa → `drain` event → `readStream.resume()`. Node.js `pipe()` implementa automaticamente.
**Confidence:** alta

**Claim:** Message-Driven é o fundamento dos outros 3 pilares do Reactive Manifesto — sem ele, os outros são difíceis de implementar.
**Evidence:** Responsiveness: mensagem assíncrona não bloqueia o emissor. Resilience: falha em um componente não se propaga via call stack — apenas a fila para. Elasticity: adicionar consumers horizontalmente sem modificar produtores. Comunicação síncrona (HTTP request/response) torna difícil isolar falhas e escalar independentemente.
**Confidence:** alta

**Claim:** RxJS `bufferTime` + `concatMap` implementa backpressure para consumidores lentos — coleta e processa em batches.
**Evidence:** Produtor rápido (10ms) + consumidor lento (100ms): sem buffer → consumidor sobrecarregado. `bufferTime(100)` coleta 10 eventos em 100ms. `concatMap` processa um batch de cada vez, em sequência. Buffer limitado previne acúmulo infinito. Alternativa: `throttleTime` (descarta) vs `bufferTime` (acumula).
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/reactive-architecture]]
- [[concepts/backpressure]]
- [[concepts/message-driven]]
- [[concepts/reactive-manifesto]]
- [[concepts/rxjs]]
- [[concepts/node-streams]]

## Open Questions

- Backpressure em sistemas distribuídos com múltiplos consumers — como propagar sinal de "lento" de volta ao produtor em Kafka?
- Reactive Manifesto em microserviços modernos — continua relevante ou foi absorvido por práticas de resilience padrão?
