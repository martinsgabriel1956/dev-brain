---
type: concept
title: "Argo Rollouts"
aliases: ["Argo Rollouts", "progressive delivery", "analysis template", "rollback automático por métricas"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [devops, kubernetes, deploy, progressive-delivery, canary]
skill: tech-mentor-infra
status: stable
---

# Argo Rollouts

Controller Kubernetes para progressive delivery — estende o `Deployment` padrão com suporte a canary, blue/green e **rollback automático baseado em métricas**.

## O que resolve

`kubectl rollout` padrão não sabe se o deploy causou degradação. Argo Rollouts consulta métricas (Prometheus, Datadog, etc.) durante o rollout e reverte automaticamente se os critérios falharem.

## AnalysisTemplate — rollback por métricas

```yaml
apiVersion: argoproj.io/v1alpha1
kind: AnalysisTemplate
metadata:
  name: error-rate-check
spec:
  metrics:
    - name: error-rate
      interval: 1m                       # consulta a cada 1 minuto
      successCondition: result[0] < 0.01 # passa se error rate < 1%
      failureLimit: 3                    # 3 falhas consecutivas → rollback
      provider:
        prometheus:
          address: http://prometheus:9090
          query: |
            sum(rate(http_requests_total{status=~"5.."}[5m]))
            /
            sum(rate(http_requests_total[5m]))
```

## Fluxo de deploy com Argo Rollouts

```
1. Nova imagem → Argo atualiza X% dos pods (canary)
2. AnalysisRun consulta Prometheus a cada 1min
3a. Métricas OK → Argo avança para 100% dos pods
3b. 3 falhas consecutivas → Argo reverte para versão anterior automaticamente
```

## Rollback manual

```bash
# Reverter para versão anterior
kubectl rollout undo deployment/api

# Reverter para revisão específica
kubectl rollout undo deployment/api --to-revision=3
```

## Argo Rollouts vs Flagger

| | Argo Rollouts | Flagger |
|---|---|---|
| Integração | Kubernetes nativo | Service mesh (Istio, Linkerd) |
| Análise | AnalysisTemplate declarativo | Canary CRD com webhooks |
| Foco | Progressive delivery geral | Tráfego granular via mesh |

## Ver também

- [[concepts/ci-cd]] — Argo Rollouts implementa o CD do pipeline
- [[concepts/canary-release]] — estratégia de rollout progressivo
- [[concepts/blue-green-deploy]] — estratégia alternativa suportada
- [[concepts/observabilidade]] — métricas Prometheus que alimentam o AnalysisTemplate

## Key Sources

- [[sources/cicd-pipeline]]
