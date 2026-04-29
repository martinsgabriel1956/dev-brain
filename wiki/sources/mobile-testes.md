---
type: source
title: "Testes Mobile — Detox, Maestro, XCUITest, Espresso, integration_test"
aliases: ["mobile testes", "detox react native", "maestro mobile", "xcuitest ios", "espresso android"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-testes.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, testes, detox, maestro, xcuitest, espresso, integration-test, unit-test]
skill: tech-mentor-mobile
status: stable
---

# Testes Mobile

## TL;DR

Pirâmide mobile: unit tests (lógica de negócio/ViewModel) na base, testes de integração (composables/widgets) no meio, E2E (Detox/Maestro) no topo. Maestro substitui Detox para RN pela legibilidade do YAML e estabilidade. XCUITest para iOS nativo; Espresso para Android nativo. Testar fluxo de negócio principal em E2E — não cada tela isoladamente.

## Claims Principais

| Claim | Confiança |
|---|---|
| Maestro YAML é mais legível e estável que Detox para E2E em React Native | Alta |
| ViewModel deve ser testável sem Android framework — usar Fake em vez de Mock | Alta |
| Flutter `integration_test` roda no dispositivo real — acesso ao engine Flutter | Alta |
| E2E apenas para happy path dos fluxos críticos — custo de manutenção alto | Alta |
| Snapshot tests para componentes visuais — detectam regressões de UI não intencionais | Média |

## Conceitos Abordados

- [[mobile-testes]] · [[mobile-cicd]] · [[mobile-metricas-criticas]] · [[mobile-profiling]] · [[piramide-de-testes]]
