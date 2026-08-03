---
type: concept
title: "Distributed Tracing"
aliases: ["tracing distribuído", "opentelemetry", "spans", "trace context"]
date_created: 2026-04-23
date_updated: 2026-08-03
source_count: 3
tags: [distributed-tracing, observabilidade, opentelemetry, jaeger, spans, w3c-trace-context]
skill: tech-mentor-infra
status: draft
---

# Distributed Tracing

Técnica de observabilidade que registra o caminho completo de um request por múltiplos serviços, mostrando latência por etapa.

**Conceitos:** Trace (fluxo completo end-to-end) → Spans (unidade de trabalho com duração) → traceparent (W3C padrão de propagação entre serviços).

**Padrão de instrumentação:** OpenTelemetry SDK → OTel Collector → Jaeger ou Grafana Tempo.

**HttpInstrumentation** propaga `traceparent` automaticamente em todo axios/fetch — sem mudar código de negócio.

**Sampling obrigatório:** não rastreie 100% das requests. Overhead ~5%; usar tail-based sampling.

**Quando usar:** > 2–3 serviços em cadeia. Abaixo disso, APM + logs estruturados são suficientes.

## OpenTelemetry é padrão, não ferramenta de um vendor

O SDK do OpenTelemetry é a mesma peça usada por baixo de quase todo o mercado de observabilidade — New Relic, Splunk, Google, Amazon, Grafana e Datadog contribuem para o mesmo projeto, mesmo mantendo cada um sua própria ferramenta de coleta/visualização por trás. Isso é o que permite trocar de backend (ex. Datadog → Grafana Tempo) sem reinstrumentar a aplicação.

## Instrumentação de bibliotecas, não só de rotas

Instrumentação não se limita a endpoints HTTP: pacotes de instrumentação existem para bibliotecas de baixo nível (ex. `fs`, query builders como Knex, clientes de cache como Redis). Cada operação dessas vira automaticamente um span no trace — o que já revelou, em um caso relatado, um pacote compartilhado entre microsserviços travando o event loop do Node.js, corrigido com ganho de ~50% de velocidade após a atualização do pacote.

## Uso por IA para correlação automática

Traces (junto com métricas e logs) alimentam agentes de IA conectados via MCP a backends de observabilidade (ex. Grafana MCP), que correlacionam os três sinais automaticamente para achar causa raiz — inclusive apontando a linha de código exata — sem que um humano precise cruzar `traceId` manualmente entre bases. Ver [[wiki/concepts/investigacao-de-incidentes-com-ia-e-mcp]].

## Key Sources

- [[sources/distributed-tracing]]
- [[wiki/sources/observabilidade-ponta-a-ponta-opentelemetry-ia-amsterdam]] — arquitetura do Collector, instrumentação de libs de baixo nível, e correlação automática via IA/MCP
- [[wiki/sources/sre-capacidade-observabilidade-confiabilidade-custo]] — framing didático de tracing como a resposta natural a "tá muito lento" (fluxo/jornada/trace da chamada)
