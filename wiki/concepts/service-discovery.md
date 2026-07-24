---
type: concept
title: "Service Discovery"
aliases: ["service discovery", "descoberta de serviços", "service registry"]
date_created: 2026-04-22
date_updated: 2026-07-23
source_count: 2
tags: [sistemas-distribuidos, networking, microsservicos, kubernetes, consul]
skill: tech-mentor-system-design
status: stable
---

# Service Discovery

Mecanismo pelo qual serviços se encontram em ambientes dinâmicos onde IPs mudam constantemente (Kubernetes, ECS, auto-scaling). Dois modelos: client-side e server-side.

## Client-Side Discovery

Cliente consulta um Service Registry e decide para qual instância enviar — aplica ele mesmo o balanceamento.

```
Client → Service Registry: "onde está o OrderService?"
        ← [10.0.1.5:8080, 10.0.1.6:8080]
Client → escolhe instância (round-robin) → OrderService
```

- **Vantagem:** controle total de LB no cliente (circuit breaker, retry, affinity)
- **Desvantagem:** lógica de discovery acoplada em cada cliente em cada linguagem

## Server-Side Discovery

Cliente envia para um Load Balancer/[[wiki/concepts/api-gateway]] que consulta o registry e roteia. Na ausência de qualquer forma de discovery, o problema aparece de forma prática: subir uma nova instância de um serviço não adianta nada se o client não tem como aprender o novo endereço — ele continua batendo na instância antiga, o que motiva introduzir um componente central como o API Gateway (ver [[wiki/sources/api-gateway-padrao-essencial-arquiteturas-distribuidas]]).

```
Client → Load Balancer (Envoy/Kong) → Service Registry → instância
```

- **Vantagem:** clientes simples, estratégia de LB centralizada
- **Desvantagem:** hop extra de rede; LB vira ponto crítico

## DNS-Based (Kubernetes — padrão)

Cada Kubernetes Service recebe nome DNS estável. Zero lógica de discovery na aplicação.

```typescript
// Formato: <service>.<namespace>.svc.cluster.local
const response = await fetch("http://order-service.production.svc.cluster.local/orders");
// kube-dns resolve → ClusterIP
// kube-proxy distribui entre pods via iptables/IPVS
```

```yaml
apiVersion: v1
kind: Service
metadata:
  name: order-service
  namespace: production
spec:
  selector:
    app: order-service
  ports:
    - port: 80
      targetPort: 8080
```

## Consul (Multi-cloud / Fora do K8s)

```typescript
// Registrar com health check
await consul.agent.service.register({
  name: "order-service",
  id: `order-service-${process.env.POD_NAME}`,
  address: process.env.POD_IP,
  port: 8080,
  check: {
    http: `http://${process.env.POD_IP}:8080/health`,
    interval: "10s",
    deregisterCriticalServiceAfter: "30s"  // remove automaticamente instâncias doentes
  }
});

process.on("SIGTERM", async () => {
  await consul.agent.service.deregister(`order-service-${process.env.POD_NAME}`);
});

// Descobrir apenas instâncias saudáveis
const services = await consul.health.service({ service: "order-service", passing: true });
```

## Comparativo

| Abordagem | Exemplos | Quando usar |
|---|---|---|
| DNS-based | Kubernetes DNS | Padrão no K8s — zero overhead |
| Client-side | Eureka, Consul + Ribbon | Controle fino de LB no cliente |
| Server-side | Envoy, Kong, AWS ALB | Clientes simples, LB centralizado |
| Service Mesh | Istio, Linkerd | Discovery + mTLS + observabilidade integrados |

## Key Sources

- [[sources/service-discovery]]
- [[wiki/sources/api-gateway-padrao-essencial-arquiteturas-distribuidas]]
