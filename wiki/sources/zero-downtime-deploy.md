---
type: source
title: "Zero-Downtime Deploy"
aliases: ["zero-downtime", "deploy sem downtime"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 0
tags: [deploy, zero-downtime, blue-green, canary, rolling-update, expand-contract, graceful-shutdown, migrations]
skill: tech-mentor-system-design
status: stable
source_file: /home/gabriel-martins/Documentos/dev-study/raw/zero-downtime-deploy.md
source_url: ""
author: ""
date_published: 2026-03-27
date_ingested: 2026-04-22
---

# Zero-Downtime Deploy

## TL;DR

Deploy sem downtime exige duas coisas: estratégia de tráfego (Rolling/Blue-Green/Canary) + migrations backward compatible via Expand-Contract. Regra fundamental: nunca migre schema e código no mesmo deploy.

## Key Claims

**Claim:** Rolling Update é o padrão nativo do Kubernetes — substitui pods um a um, aguardando readiness.
**Evidence:** `maxUnavailable: 0` garante que capacidade nunca diminui durante o rollout. `minReadySeconds: 30` absorve instabilidade pós-start. v1 e v2 convivem → API obrigatoriamente backward compatible.
**Confidence:** alta

**Claim:** Blue/Green oferece rollback instantâneo ao custo de 2× infra durante o switch.
**Evidence:** Switch = `kubectl patch service` trocando seletor. Rollback = mesmo comando revertendo. Todo tráfego muda atomicamente — sem período de convivência de versões.
**Confidence:** alta

**Claim:** Canary é a estratégia mais segura para mudanças de risco, mas requer infraestrutura de roteamento e observabilidade.
**Evidence:** Exposição gradual (5% → 20% → 100%) com rollback automático se error rate > threshold. Requer Prometheus ou equivalente para análise automática de métricas.
**Confidence:** alta

**Claim:** Expand-Contract é o único padrão safe para migrations sem downtime.
**Evidence:** 3 deploys separados: (1) ADD COLUMN nova + dual-write, (2) backfill em lotes, (3) DROP COLUMN antiga. `ALTER TABLE ADD COLUMN NULL` é safe. `DROP COLUMN` imediato é destrutivo.
**Confidence:** alta

**Claim:** Graceful shutdown requer: SIGTERM handler, `/health/ready` que retorna 503 durante shutdown, e preStop sleep para absorver lag do LB.
**Evidence:** `terminationGracePeriodSeconds: 60` + `preStop sleep 5` garante que o LB para de rotear antes de o pod fechar conexões ativas.
**Confidence:** alta

## Operações DB — Segurança

| Operação | Segura? | Como fazer |
|---|---|---|
| `ADD COLUMN NULL` | ✅ | Direto |
| `DROP COLUMN` | ❌ imediato | Código para de usar → deploy → drop |
| `RENAME COLUMN` | ❌ imediato | Add nova + dual-write → migrate → drop |
| `CREATE INDEX` | ⚠️ | `CREATE INDEX CONCURRENTLY` |
| `ADD FOREIGN KEY` | ⚠️ | `NOT VALID` → `VALIDATE CONSTRAINT` separado |

## Concepts & Entities Touched

[[concepts/zero-downtime-deploy]] · [[concepts/rolling-update]] · [[concepts/blue-green-deploy]] · [[concepts/canary-release]] · [[concepts/expand-contract]] · [[concepts/feature-flags]] · [[concepts/circuit-breaker]]

## Open Questions

- Canary com múltiplos serviços dependentes — como coordenar percentual entre eles sem drift?
- Expand-Contract em tabelas com bilhões de rows — backfill em lotes sem impacto de I/O?
- Quando usar Blue/Green vs Canary em mudanças de schema críticas?
