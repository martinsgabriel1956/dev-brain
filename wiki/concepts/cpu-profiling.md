---
type: concept
title: "CPU Profiling"
aliases: ["cpu profile", "perfil de cpu", ".cpuprofile", "profiler de cpu", "node inspector profiler"]
date_created: 2026-11-11
date_updated: 2026-11-11
source_count: 1
tags: [performance, cpu-profiling, nodejs, v8, diagnostico, observabilidade]
skill: lang-dynamic
status: draft
---

# CPU Profiling

CPU profiling é gravar, durante uma janela de tempo, em quais funções o processo gastou CPU. O profiler amostra a pilha de chamadas em intervalos curtos, e o resultado mostra quem custa mais, de quem foi chamado e quanto tempo levou. Serve para achar o gargalo quando ninguém sabe onde ele está.

## Em Node.js, sem instalar nada

Node.js roda sobre V8 e expõe o protocolo do Chrome DevTools pelo módulo `node:inspector`. A versão com promises dá um fluxo curto ([external](https://nodejs.org/api/inspector.html)):

```js
import { Session } from 'node:inspector/promises'
import { writeFile } from 'node:fs/promises'

const session = new Session()
session.connect()
await session.post('Profiler.enable')
await session.post('Profiler.start')
// ... carga real ou teste de carga ...
const { profile } = await session.post('Profiler.stop')
await writeFile(`cpu-profile-${Date.now()}.cpuprofile`, JSON.stringify(profile))
session.disconnect()
```

O `.cpuprofile` abre no VS Code, na aba Performance do Chrome DevTools e em visualizadores web. Outras opções de linha de comando são `node --cpu-prof`, o `clinic flame` e o `0x`, que geram flame graphs `[skill: lang-dynamic]`.

## Como ler

1. **Grave com carga.** Sem tráfego, o profile mostra só o processo ocioso. Um [[wiki/concepts/teste-de-carga]] dá o volume que expõe o gargalo.
2. **Recorte a janela do teste** e ignore o tempo ocioso (idle).
3. **Comece pelo topo** da lista por tempo e desça pela árvore até a rota ou o endpoint. Ver [[wiki/concepts/flame-graph]].
4. **Olhe o garbage collector.** Muito tempo de GC sugere alocação demais, como cópias profundas por requisição. Ver [[wiki/concepts/gerenciamento-de-memoria]].
5. **Mude uma coisa por vez e meça de novo.** Rode mais de uma vez, porque o aquecimento do JIT varia o resultado.

## Exemplo

Em [[wiki/sources/cpu-profiling-nodejs-inspector-autocannon-erick-wendel]], o profile pôs o `cloneDeep` do [[wiki/entities/lodash]] com pouco mais de 10% do tempo gravado. Tirá-lo levou a rota de 2000 para 11.000 requisições no mesmo teste. Num servidor Node.js, CPU gasto no caminho da requisição segura a fila inteira: ver [[wiki/concepts/event-loop-performance-js]].

## Limites

- O profile diz onde a CPU foi gasta, não onde a requisição esperou. Espera de I/O e de banco pede tracing: ver [[wiki/concepts/opentelemetry]] e [[wiki/concepts/observabilidade]].
- Gravar tem custo, então números absolutos medidos com o profiler ligado não valem para produção.

## Key sources

- [[wiki/sources/cpu-profiling-nodejs-inspector-autocannon-erick-wendel]]: `node:inspector/promises`, teste com autocannon e a remoção do `cloneDeep`.
- [[wiki/sources/performance-methods]]: flame graph como ferramenta de CPU profiling.
