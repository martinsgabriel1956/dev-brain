---
type: source
title: "Pirâmide de Testes"
aliases: ["test pyramid", "ice cream cone", "testing trophy"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/piramide-de-testes.md
source_url: ""
author: "tech-mentor-testing skill"
date_published: 2026-03-27
date_ingested: 2026-04-22
source_count: 0
tags: [testes, pirâmide, estratégia, unitário, integração, e2e, ci, testcontainers, playwright]
skill: tech-mentor-testing
status: stable
---

# Pirâmide de Testes

## TL;DR

Modelo de distribuição de testes: muitos unitários na base, moderados de integração no meio, poucos E2E no topo. Inverter é o anti-pattern "ice cream cone" — suite lenta, frágil, sem confiança. Variante Testing Trophy (Kent C. Dodds) eleva o centro de gravidade para integração em sistemas com muito I/O e pouca lógica de domínio.

## Key Claims

**Claim:** Quanto mais alto na pirâmide, mais lento, caro e frágil — distribuição correta é muitos unitários, moderados integração, poucos E2E.
**Evidence:** Unitários: ~ms, flakiness quase zero. Integração: ~segundos, flakiness baixo. E2E: ~10-30s, flakiness alto. Inverter = ice cream cone = suite com feedback loop de horas.
**Confidence:** alta

**Claim:** E2E não bloqueia PR — bloqueia deploy para produção.
**Evidence:** CI em 3 stages: unit (bloqueia PR) → integration (<2min, bloqueia PR) → e2e (staging, bloqueia release). E2E em PR torna o loop de feedback insuportável para o time.
**Confidence:** alta

**Claim:** Mocks de banco são frágeis e enganosos — usar banco real via Testcontainers nos testes de integração.
**Evidence:** Mock de banco valida que o código chama o mock corretamente, não que a query SQL funciona. Testcontainers sobe container real do PostgreSQL para cada test run.
**Confidence:** alta

**Claim:** Testing Trophy (Kent C. Dodds) é válido para sistemas com muito I/O e lógica de domínio rasa — centro de gravidade sobe para integração.
**Evidence:** Next.js/CRUD APIs têm pouca lógica de negócio pura para testar com unitários. TypeScript + ESLint + Zod funcionam como testes "gratuitos" (static layer).
**Confidence:** alta

## Conceitos & Entities Tocados

[[concepts/piramide-de-testes]] · [[concepts/tdd]] · [[concepts/contract-testing]] · [[concepts/test-doubles]]

## Open Questions

- Testcontainers em CI com muitos workers paralelos — overhead de startup aceitável?
- Flaky E2E em Playwright — estratégia de quarantine vs fix imediato?
- Testing Trophy em sistemas financeiros com lógica de pricing complexa — ainda faz sentido?
