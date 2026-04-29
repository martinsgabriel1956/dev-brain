---
type: concept
title: "Canary Release"
aliases: ["canary deploy", "canary release", "lançamento canário"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [devops, deploy, cicd, canary, observabilidade, argo-rollouts, infra]
skill: tech-mentor-infra
status: stable
---

# Canary Release

Porcentagem pequena do tráfego vai para nova versão. Percentual aumenta conforme métricas são validadas. Rollback automático se métricas degradam.

## Fluxo

```
v1: ████████████████████ 95%
v2: █                    5%   ← Canary inicial

→ sem alertas após 30min → aumenta para 20%
→ sem alertas após 1h   → 100%
```

## Argo Rollouts

```yaml
spec:
  strategy:
    canary:
      steps:
        - setWeight: 5
        - pause: { duration: 30m }
        - setWeight: 20
        - pause: { duration: 1h }
        - analysis:
            templates:
              - templateName: error-rate-check
        - setWeight: 100
```

## Análise Automática

```yaml
spec:
  metrics:
    - name: error-rate
      successCondition: result[0] < 0.01  # < 1% erros
      provider:
        prometheus:
          query: |
            sum(rate(http_requests_total{status=~"5.."}[5m])) /
            sum(rate(http_requests_total[5m]))
```

## Quando Usar

- Features que podem ter impacto imprevisto no comportamento do usuário
- Quando você tem Prometheus + análise automática configurados
- Mudanças de UX ou fluxos críticos com incerteza

## Pré-requisito

Observabilidade madura. Sem métricas confiáveis, análise automática não funciona — rollback vira manual.

## Tráfego Misto

v1 e v2 servem ao mesmo tempo. API e DB schema **devem** ser backward compatible. → [[concepts/expand-contract]]

## Comparativo

→ [[concepts/deploy-strategies]]

## Key Sources

- [[sources/blue-green-canary-rolling]]
