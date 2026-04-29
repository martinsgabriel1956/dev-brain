---
type: concept
title: "Blue/Green Deploy"
aliases: ["blue green", "blue-green deployment", "swap de ambiente"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [devops, deploy, cicd, kubernetes, rollback, infra]
skill: tech-mentor-infra
status: stable
---

# Blue/Green Deploy

Dois ambientes idênticos: Blue (versão atual) e Green (nova versão). Troca atômica no load balancer — rollback instantâneo.

## Fluxo

```
           Load Balancer
                │
       Blue (v1)   Green (v2)
       [100%]       [0%]    ← antes

                │ swap (muda selector)
                ▼

       Blue (v1)   Green (v2)
         [0%]      [100%]   ← após
         ↑ fica ligado para rollback
```

## Kubernetes

```yaml
apiVersion: v1
kind: Service
metadata:
  name: app-service
spec:
  selector:
    app: myapp
    version: green  # muda de "blue" para "green" para o swap
  ports:
    - port: 80
      targetPort: 3000
```

## Quando Usar

- Releases críticos: checkout, pagamento, auth
- Quando rollback em segundos é mandatório
- Quando você pode pagar 2x de infraestrutura temporariamente

## Quando Evitar

- Budget restrito — custo dobra durante o deploy
- Migrations de DB que não são backward compatible — [[concepts/expand-contract]] é obrigatório

## Comparativo

→ [[concepts/deploy-strategies]]

## Key Sources

- [[sources/blue-green-canary-rolling]]
