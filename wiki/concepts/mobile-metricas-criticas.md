---
type: concept
title: "Métricas Críticas de Performance Mobile"
aliases: ["cold start mobile", "mobile KPIs", "crash-free rate", "ANR mobile", "mobile TTI"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [mobile, metricas, performance, cold-start, FPS, ANR, crash-rate, TTI]
skill: tech-mentor-mobile
status: stable
---

# Métricas Críticas de Performance Mobile

## Thresholds de Referência

| Métrica | Threshold | Consequência se falhar |
|---|---|---|
| Cold Start | < 2s | Abandono do usuário |
| Warm Start | < 1s | UX degradada |
| FPS | ≥ 60fps (90/120 em premium) | Jank perceptível |
| ANR Rate | < 0.1% | Google Play badge negativo |
| Crash-free rate | > 99.5% | Bloqueio de rollout |
| Time to Interactive | < 3s | UX ruim mesmo com startup rápido |

## Tipos de Start

- **Cold Start:** app não estava na memória — processo criado, Application criada, primeira Activity
- **Warm Start:** processo existe, Activity recriada — mais rápido, mas ainda carrega dados
- **Hot Start:** app em background voltando ao foreground — mais rápido possível

## Ferramentas de Medição

- **Android:** `adb shell am start-activity -W` para timing; Perfetto para breakdown por fase
- **iOS:** Instruments `App Launch` template
- **Firebase Performance:** automaticamente registra cold/warm start sem instrumentação

## TTI vs Startup

Startup = primeira frame visível. TTI = usuário pode interagir de verdade. Spinner visível durante TTI = UX ruim apesar de startup rápido.

## Dispositivo de Teste

Sempre medir em dispositivo médio-baixo (Motorola G series, Samsung A03). Flagship esconde problemas que a maioria dos usuários enfrenta.

## Ver também

- [[mobile-baseline-profiles]] — reduzir cold start no Android
- [[mobile-profiling]] — identificar o que está lento
- [[mobile-monitoramento]] — monitorar em produção

## Key Sources

- [[wiki/sources/mobile-metricas-criticas]]
