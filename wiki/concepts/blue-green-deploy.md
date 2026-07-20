---
type: concept
title: "Blue/Green Deploy"
aliases: ["blue green", "blue-green deployment", "swap de ambiente"]
date_created: 2026-04-22
date_updated: 2026-07-20
source_count: 3
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

## Por que o rollback é tão rápido

A versão antiga (Blue) continua de pé, rodando em paralelo, mesmo depois do swap — rollback é literalmente redirecionar o tráfego de volta, sem precisar reverter código nem refazer deploy. Essa é a vantagem central que o distingue do [[concepts/rolling-update]] (rollback lento, pod a pod) e justifica pagar o custo de 2x infraestrutura durante a janela de transição.

## Blue/Green num Host Único (sem Kubernetes)

O mesmo conceito — duas versões vivas em paralelo, troca atômica de roteamento, rollback instantâneo — funciona sem cluster nenhum: um [[wiki/concepts/reverse-proxy|reverse proxy]] (Nginx) na frente de duas instâncias da aplicação, cada uma numa porta diferente, na mesma VPS. Em vez de trocar `Service.selector` no Kubernetes, um script edita a diretiva `proxy_pass` do Nginx e recarrega a config — a operação é a mesma "seta de roteamento", só que implementada manualmente com scripts bash em vez de um controller.

## Key Sources

- [[sources/blue-green-canary-rolling]]
- [[sources/tipos-de-deploy]]
- [[wiki/sources/deploy-blue-green-na-pratica-vps-nginx]] — demo prática em VPS única, sem Kubernetes: Nginx como reverse proxy trocando entre duas portas via script
