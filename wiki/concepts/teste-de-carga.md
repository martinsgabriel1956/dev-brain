---
type: concept
title: "Teste de Carga"
aliases: ["load testing", "load test", "teste de stress", "benchmark http", "autocannon"]
date_created: 2026-11-11
date_updated: 2026-11-11
source_count: 3
tags: [performance, teste-de-carga, autocannon, k6, artillery, testes]
skill: lang-dynamic
status: stub
---

# Teste de Carga

Teste de carga simula muitos clientes simultâneos contra a aplicação para ver como ela responde sob volume: quantas requisições aguenta, quanto a latência sobe e quando começa a falhar. Duas rotas que parecem igualmente rápidas num `curl` podem ter capacidades muito diferentes.

## Ferramentas citadas na wiki

- **autocannon:** benchmark HTTP em Node.js. Por padrão, 10 conexões por 10 segundos; aceita número de conexões, duração, headers e corpo ([external](https://github.com/mcollina/autocannon)). Mostra latência (p50/p90/p99) e requisições por segundo `[skill: lang-dynamic]`.
- **k6:** thresholds como SLO e uso em CI. Ver [[wiki/sources/performance-methods]].
- **Artillery** com Playwright, para simular uma Black Friday. Ver [[wiki/sources/5-dicas-performance-javascript]].

## Teste de carga junto com profiling

O teste de carga mostra que a rota está lenta; o [[wiki/concepts/cpu-profiling]] mostra por quê. Em [[wiki/sources/cpu-profiling-nodejs-inspector-autocannon-erick-wendel]], o autocannon rodou com o profiler gravando, e cada mudança no código foi medida no mesmo teste: 2000, 11.000 e 13.000 requisições.

## Cuidados

- **Uma rodada não basta.** No mesmo vídeo, duas execuções iguais deram 10.000 e 11.000. Rode várias vezes e compare médias.
- **Olhe percentis, não só o total.** p95 e p99 mostram a cauda que afeta usuários reais. Ver [[wiki/sources/performance-methods]].
- **Profiler ligado custa.** Os números servem para comparar rodadas entre si, não como capacidade de produção.

## Key sources

- [[wiki/sources/cpu-profiling-nodejs-inspector-autocannon-erick-wendel]]: autocannon com CPU profiling.
- [[wiki/sources/5-dicas-performance-javascript]]: Playwright, Artillery e OpenTelemetry.
- [[wiki/sources/performance-methods]]: k6 e thresholds como SLO.
