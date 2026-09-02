---
type: concept
title: "Back Pressure"
aliases: ["back pressure", "backpressure", "pressão de volta", "producer consumer imbalance"]
date_created: 2026-04-23
date_updated: 2026-09-02
source_count: 4
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

## Antes de escalar: identificar o gargalo real

[[wiki/sources/back-pressure-producer-consumer-filas-bounded-admission-control]] enfatiza que o primeiro passo diante de back pressure não é escalar hardware — é identificar onde está o [[wiki/concepts/gargalo]]. Se o consumidor só processa 10 itens/min porque o banco de dados tem essa limitação própria de velocidade, aumentar a capacidade do consumidor não resolve nada.

Técnicas mais baratas que jogar mais hardware no problema:

- **Podar stale jobs** — remover da fila itens antigos, com erro, ou que não fazem mais sentido.
- **Priorizar** os itens mais importantes dentro da fila.
- **Processar em batches** — ex.: batch insert em vez de inserts individuais, aumentando vazão sem aumentar capacidade de hardware.

## Admission control e low/high watermark

Além de bufferizar com limite, é possível controlar ativamente a admissão de novos itens antes que entrem na fila — ver [[wiki/concepts/admission-control]]. Uma técnica concreta demonstrada em [[wiki/sources/back-pressure-producer-consumer-filas-bounded-admission-control]]: o produtor pausa quando a fila ultrapassa um *high watermark* e só retoma quando ela cai abaixo de um *low watermark*, evitando tanto o crescimento sem limite quanto a oscilação rápida entre pausar e retomar.

Outras estratégias complementares: **rate limit no produtor** (trava a taxa de produção na capacidade do consumidor — ver [[wiki/concepts/rate-limiting]]), **mais consumidores em paralelo** via [[wiki/concepts/escalabilidade-horizontal]], e **auto scaling baseado no tamanho da fila** (ver [[wiki/concepts/auto-scaling]]) — mais difícil de configurar, mas viável. Cuidado com [[wiki/concepts/retry-backoff|retry]] agressivo entre produtor e fila: pode adicionar ainda mais pressão a um sistema já sobrecarregado.

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

## Starvation por Competição de Fluxos (não é a mesma causa)

[[wiki/concepts/ambulance-pattern]] descreve um efeito colateral irmão, mas com causa diferente: não é o consumidor mais lento que o produtor, é um fluxo de alta prioridade que sempre fura a fila e trava o fluxo normal — starvation por competição de prioridade, não por descompasso de velocidade. A correção também é diferente: em vez de bufferizar/descartar/desacelerar, separa-se fisicamente os fluxos em filas distintas.

## Relação com outros conceitos

- [[concepts/reactive-architecture]] — back pressure é um dos 4 pilares do Reactive Manifesto
- [[concepts/thundering-herd]] — thundering herd é o oposto: consumidores sobrecarregando o produtor/recurso compartilhado
- [[concepts/bulkhead]] — bulkhead limita o impacto; back pressure controla o fluxo
- [[wiki/concepts/ambulance-pattern]] — starvation por competição entre fluxos de prioridades diferentes, não por velocidade de consumo

## Key Sources

- [[sources/conceitos-que-ninguem-ensina]]
- [[sources/reactive-architecture]]
- [[wiki/sources/operador-de-crud-vs-engenheiro-repertorio]] — back pressure citado como exemplo do "mundo debaixo do CRUD": produtor mais rápido que consumidor exige decidir entre descartar, segurar ou derrubar
- [[wiki/sources/back-pressure-producer-consumer-filas-bounded-admission-control]] — identificar o gargalo antes de escalar, técnicas baratas (poda de stale jobs, priorização, batching), e demonstração prática de admission control com low/high watermark via BullMQ + Redis
- [[wiki/sources/ambulance-pattern-priorizacao-mensagens-mark-richards]] — starvation por competição de prioridade dentro da mesma fila, resolvida com separação física de filas em vez de controle de fluxo
