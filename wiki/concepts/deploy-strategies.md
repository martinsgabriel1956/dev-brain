---
type: concept
title: "Deploy Strategies"
aliases: ["estratégias de deploy", "deployment strategies"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [devops, deploy, cicd, infra, system-design]
skill: tech-mentor-infra
status: stable
---

# Deploy Strategies

Comparativo das três estratégias principais para liberar nova versão em produção.

## Comparativo

| Estratégia | Rollback | Custo | Tráfego misto | Quando usar |
|---|---|---|---|---|
| [[concepts/blue-green-deploy]] | Instantâneo (segundos) | 2x infra | Não | Alto risco, rollback imediato obrigatório |
| [[concepts/canary-release]] | Automático + rápido | +5-20% temp | Sim | Mudança de UX/comportamento, com observabilidade |
| [[concepts/rolling-update]] | Lento (pod a pod) | Sem custo extra | Sim | Deploy rotineiro, mudança backward compatible |

## Decisão Rápida

```
Precisa de rollback em segundos?         → Blue/Green
Precisa de feedback gradual com métricas? → Canary
Deploy rotineiro, baixo risco?            → Rolling
```

## Pré-requisitos por Estratégia

- **Blue/Green** — dois ambientes provisionados, Service com selector por versão
- **Canary** — Argo Rollouts + Prometheus com error rate configurado
- **Rolling** — zero pré-requisito além do Kubernetes nativo

## Tráfego Misto → Backward Compatibility

Canary e Rolling têm v1 e v2 simultaneamente. DB schema e API **devem** suportar as duas versões. → [[concepts/expand-contract]]

## Key Sources

- [[sources/blue-green-canary-rolling]]
