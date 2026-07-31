---
type: concept
title: "Canary Release"
aliases: ["canary deploy", "canary release", "lançamento canário"]
date_created: 2026-04-22
date_updated: 2026-07-31
source_count: 4
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

## Canary Deployment vs. Canary Release (feature flag)

Existe uma segunda forma de "Canary" que não é essa estratégia de infraestrutura: em vez de duas instâncias, você segrega usuários em grupos e mostra uma feature escondida atrás de uma [[concepts/feature-flags|feature flag]] para uma fração deles. Tecnicamente isso é um **release** gradual, não um **deploy** gradual — ver [[concepts/deploy-vs-release]]. O termo "Canary deployment" tradicionalmente se refere à versão com instâncias/tráfego separado descrita acima.

A Meta aplica exatamente essa mesma lógica de rollout escalonado (funcionários → fração pequena de tráfego → 100%) tanto no nível de deploy de código quanto no de feature flag (via seu sistema interno Gatekeeper) — ver caso real em [[wiki/sources/rapid-release-at-massive-scale-facebook]].

## Canary vs. A/B Testing

Mecanicamente parecido (split de tráfego por percentual), mas o objetivo é diferente: Canary reduz **risco técnico** (a v2 quebra alguma coisa?); [[concepts/ab-testing-deployment]] valida **hipótese de negócio** (a v2 vende/converte mais?). Ver essa página para o comparativo completo.

## Comparativo

→ [[concepts/deploy-strategies]]

## Key Sources

- [[sources/blue-green-canary-rolling]]
- [[sources/tipos-de-deploy]]
- [[wiki/sources/rapid-release-at-massive-scale-facebook]] — caso real (Meta/Facebook) de rollout escalonado em escala massiva
- [[wiki/sources/continuous-integration-delivery-deploy-vs-release]] — cita o caso da Meta de segunda mão, como ilustração didática da distinção deploy/release
