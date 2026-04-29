---
type: source
title: "Blue/Green, Canary e Rolling Deploy"
aliases: ["deploy strategies", "estratégias de deploy"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [devops, deploy, cicd, resiliencia, kubernetes, infra]
skill: tech-mentor-infra
source_file: /home/gabriel-martins/Documentos/dev-study/raw/blue-green-canary-rolling.md
source_url: ""
author: "tech-mentor skill"
date_published: 2026-04-14
date_ingested: 2026-04-22
status: stable
---

# Blue/Green, Canary e Rolling Deploy

## TL;DR

Três estratégias para liberar nova versão em produção com risco controlado. Blue/Green: troca atômica com rollback instantâneo (custo 2x). Canary: exposição gradual com análise de métricas (requer observabilidade). Rolling: substituição pod a pod, nativo no Kubernetes, rollback lento. DB migrations requerem Expand-Contract para ser compatíveis com ambas as versões.

## Key Claims

- **Blue/Green** — swap atômico no load balancer, rollback em segundos, custo 2x de infra durante deploy. → [[concepts/blue-green-deploy]]
- **Canary** — tráfego vai gradualmente para v2 (5% → 20% → 100%), rollback automático se métricas degradam. Requer Prometheus + Argo Rollouts. → [[concepts/canary-release]]
- **Rolling Update** — nativo no Kubernetes, sem custo extra, mas tráfego misto inevitável e rollback lento. → [[concepts/rolling-update]]
- **DB migrations com Expand-Contract** — renomear coluna em 3 fases para compatibilidade com v1 e v2 simultâneas. → [[concepts/expand-contract]]
- **Observabilidade é pré-requisito do Canary** — análise automática de error rate via Prometheus é o que torna o rollback automático possível. → [[concepts/deploy-strategies]]
- **Tráfego misto exige backward compatibility** — Canary e Rolling têm v1 e v2 servindo ao mesmo tempo: API e DB schema devem suportar as duas versões.

## Entities

- [[entities/kubernetes]]
- [[entities/argo-rollouts]]
- [[entities/prometheus]]

## Concepts

[[concepts/blue-green-deploy]] · [[concepts/canary-release]] · [[concepts/rolling-update]] · [[concepts/expand-contract]] · [[concepts/deploy-strategies]] · [[concepts/feature-flags]] · [[concepts/zero-downtime-deploy]]

## Open Questions

- Canary com múltiplos serviços dependentes — como coordenar percentual entre eles?
- Expand-Contract em bancos com bilhões de rows — backfill sem lock longo?

## Raw Quotes

> "A troca é atômica no load balancer — sem downtime e com rollback instantâneo."

> "Duas versões simultâneas requerem backward compatibility (API, DB schema)."

> "A migration de banco deve ser compatível com ambas as versões do código durante a janela de deploy."
