---
type: concept
title: "Deploy Strategies"
aliases: ["estratégias de deploy", "deployment strategies"]
date_created: 2026-04-22
date_updated: 2026-07-20
source_count: 3
tags: [devops, deploy, cicd, infra, system-design]
skill: tech-mentor-infra
status: stable
---

# Deploy Strategies

Comparativo das estratégias principais para liberar nova versão em produção.

## Comparativo

| Estratégia | Rollback | Custo | Tráfego misto | Quando usar |
|---|---|---|---|---|
| [[concepts/recreate-deployment]] | Refazer o shutdown/start ao contrário | Sem custo extra | Não (mas com downtime) | Sem SLA de disponibilidade |
| [[concepts/rolling-update]] | Lento (pod a pod) | Sem custo extra | Sim | Deploy rotineiro, mudança backward compatible |
| [[concepts/blue-green-deploy]] | Instantâneo (segundos) | 2x infra | Não | Alto risco, rollback imediato obrigatório |
| [[concepts/canary-release]] | Automático + rápido | +5-20% temp | Sim | Mudança de UX/comportamento, com observabilidade |
| [[concepts/ab-testing-deployment]] | Descarta a variante perdedora | +5-20% temp | Sim | Validar hipótese de negócio, não risco técnico |
| [[concepts/shadow-deployment]] | N/A (v2 nunca serve usuário) | 2x compute | Sim, mas invisível ao usuário | Validar sistema novo com tráfego real, risco zero |

Todas decidem **como** o código chega ao usuário — independente da estratégia, deploy e release continuam sendo eventos separáveis. → [[concepts/deploy-vs-release]]

## Decisão Rápida

```
Sem SLA de disponibilidade?              → Recreate
Deploy rotineiro, baixo risco?            → Rolling
Precisa de rollback em segundos?         → Blue/Green
Precisa de feedback gradual com métricas? → Canary
Quer validar hipótese de negócio?         → A/B
Quer validar sistema novo com zero risco? → Shadow
```

## Pré-requisitos por Estratégia

- **Recreate** — zero pré-requisito, só aceitar a janela de downtime
- **Blue/Green** — dois ambientes provisionados, Service com selector por versão
- **Canary** — Argo Rollouts + Prometheus com error rate configurado
- **Rolling** — zero pré-requisito além do Kubernetes nativo
- **Shadow** — infraestrutura de duplicação/replay de tráfego, isolamento de side effects na v2

## Tráfego Misto → Backward Compatibility

Canary e Rolling têm v1 e v2 simultaneamente. DB schema e API **devem** suportar as duas versões. → [[concepts/expand-contract]]

## Key Sources

- [[sources/blue-green-canary-rolling]]
- [[sources/tipos-de-deploy]]
- [[wiki/sources/deploy-blue-green-na-pratica-vps-nginx]] — implementação prática de [[concepts/blue-green-deploy]] num host único, via [[wiki/concepts/reverse-proxy]] e scripts manuais
