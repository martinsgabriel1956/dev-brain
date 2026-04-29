---
type: concept
title: "Back Pressure"
aliases: ["back pressure", "backpressure", "pressão de volta", "producer consumer imbalance"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 1
tags: [back-pressure, streaming, reactive, producer-consumer, flow-control]
skill: tech-mentor-system-design
status: stable
---

## Definição

Back pressure é o mecanismo pelo qual um consumidor sinaliza ao produtor para desacelerar quando não consegue processar dados na velocidade em que são gerados.

Sem back pressure explícito, o sistema o aplica implicitamente — via OOM, crash ou degradação silenciosa.

## Por que importa

O desequilíbrio produtor/consumidor é inevitável em sistemas reais. Back pressure é a única forma de tornar esse desequilíbrio visível e controlável.

Sintomas de back pressure não tratado:
- Fila crescendo sem limite
- Memória subindo continuamente
- Crash por OOM em momentos de pico
- Latência aumentando assintoticamente

## Estratégias de controle

**Desacelerar o produtor** — o consumidor sinaliza capacidade atual, o produtor ajusta a taxa de produção. Mais simples quando ambos estão no mesmo processo.

**Bufferizar com limite** — aceitar até N itens em buffer, rejeitar ou bloquear acima do limite. Torna o back pressure explícito com um bound definido.

**Descartar com política** — quando buffer cheio, descartar os mais antigos (tail drop) ou os de menor prioridade. Útil quando dados têm validade temporal (métricas, logs de debug).

## Implementação

```typescript
// Node.js streams: back pressure nativo via pipe
const readable = fs.createReadStream("big-file.csv");
const writable = fs.createWriteStream("output.csv");

// pipe aplica back pressure automaticamente
// writable emite 'drain' quando pronto para receber mais
readable.pipe(writable);

// Sem pipe — implementação manual
async function processWithBackPressure(readable: Readable) {
  for await (const chunk of readable) {
    const canContinue = writable.write(chunk);
    if (!canContinue) {
      // back pressure: aguarda writable esvaziar o buffer
      await new Promise(resolve => writable.once("drain", resolve));
    }
  }
}
```

```typescript
// RxJS: bufferTime + controle de taxa
import { fromEvent, bufferTime, concatMap } from "rxjs";

fromEvent(eventSource, "data").pipe(
  bufferTime(100),            // agrupa em janelas de 100ms
  concatMap(batch => processBatch(batch)) // processa um batch por vez
).subscribe();
```

## Relação com outros conceitos

- [[concepts/reactive-architecture]] — back pressure é um dos 4 pilares do Reactive Manifesto
- [[concepts/thundering-herd]] — thundering herd é o oposto: consumidores sobrecarregando o produtor/recurso compartilhado
- [[concepts/bulkhead]] — bulkhead limita o impacto; back pressure controla o fluxo

## Key Sources

- [[sources/conceitos-que-ninguem-ensina]]
- [[sources/reactive-architecture]]
