---
type: concept
title: "Rolling Update"
aliases: ["rolling deploy", "rolling update", "atualização gradual"]
date_created: 2026-04-22
date_updated: 2026-07-09
source_count: 2
tags: [devops, deploy, cicd, kubernetes, rolling, infra]
skill: tech-mentor-infra
status: stable
---

# Rolling Update

Pods/instâncias substituídas gradualmente, um lote por vez. Sempre há mistura de versões durante o deploy. Nativo no Kubernetes.

## Fluxo

```
4 réplicas, maxUnavailable=1, maxSurge=1:

[v1, v1, v1, v1]
[v2, v1, v1, v1]
[v2, v2, v1, v1]
[v2, v2, v2, v1]
[v2, v2, v2, v2]  ← completo
```

## Kubernetes

```yaml
spec:
  replicas: 4
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 1
```

## Quando Usar

- Deploys rotineiros de microsserviços
- Mudanças backward compatible
- Quando aceita rollback mais lento (processo inverso pod a pod)

## Quando Evitar

- Quando rollback rápido é crítico → use [[concepts/blue-green-deploy]]
- Quando precisa validar métricas antes de escalar → use [[concepts/canary-release]]
- Quando mudança não é backward compatible com tráfego misto

## Comparativo

→ [[concepts/deploy-strategies]]

## Alternativa mais simples (e mais arriscada)

Se você não substituir gradualmente e simplesmente desligar tudo e subir a nova versão de uma vez, isso é [[concepts/recreate-deployment]] — mais simples, mas com downtime na janela entre shutdown e start.

## Key Sources

- [[sources/blue-green-canary-rolling]]
- [[sources/tipos-de-deploy]]
