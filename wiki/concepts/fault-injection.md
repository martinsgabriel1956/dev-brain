---
type: concept
title: "Fault Injection"
aliases: ["fault injection", "injeção de falha", "chaos istio"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [resiliencia, service-mesh, chaos-engineering, istio, testes]
skill: tech-mentor-system-design
status: stable
---

# Fault Injection

Injeção deliberada de falhas de rede (delay, abort) para testar resiliência de serviços sem alterar código da aplicação. No Istio, configurável via VirtualService.

## Tipos

**Delay** — introduz latência artificial em % dos requests.
**Abort** — retorna erro HTTP em % dos requests.

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: payment-service
spec:
  hosts:
    - payment-service
  http:
    - fault:
        delay:
          percentage:
            value: 10.0      # 10% dos requests com atraso de 5s
          fixedDelay: 5s
        abort:
          percentage:
            value: 5.0       # 5% dos requests retornam 503
          httpStatus: 503
      route:
        - destination:
            host: payment-service
```

## Quando Usar

- Validar que circuit breakers disparam corretamente
- Testar comportamento de timeout no serviço chamador
- Confirmar que retry logic não causa cascata em caso de falha total
- Parte de [[concepts/game-day]] — fault injection sem precisar matar pods

## Diferença de Chaos Engineering

Fault injection no mesh opera na camada de rede, é declarativo e reversível (basta remover o VirtualService). Chaos engineering pode operar em infra (kill de pods, falha de nó) — escopo e reversibilidade diferentes.

## Key Sources

- [[sources/service-mesh]]
