---
date: 2026-04-17
tags: [tech-mentor, sistemas-distribuidos, networking, microsservicos, kubernetes]
skill: tech-mentor-system-design/references/distributed-systems
level: intermediário
---

# Service Discovery

## Contexto
Em ambientes dinâmicos (Kubernetes, ECS, instâncias auto-scaling), os endereços IP dos serviços mudam constantemente. Service Discovery é o mecanismo pelo qual serviços encontram uns aos outros sem hardcode de IPs.

Existem dois modelos fundamentais: **Client-Side** e **Server-Side**.

## Client-Side Discovery

O cliente consulta um **Service Registry** (ex: Eureka, Consul) e decide para qual instância enviar a requisição, aplicando ele mesmo o balanceamento de carga.

```
┌──────────┐   1. "onde está o OrderService?"   ┌─────────────────┐
│ Client   │─────────────────────────────────►  │ Service Registry│
│          │◄──── [10.0.1.5:8080,               │  (Consul/Eureka)│
│          │       10.0.1.6:8080]  ─────────────┘
│          │
│          │   2. escolhe instância (round-robin)
│          │─────────────────────────────────►  OrderService:8080
└──────────┘
```

**Vantagem:** o cliente tem controle total sobre o balanceamento (pode implementar circuit breaker, retry, affinity).
**Desvantagem:** cada cliente precisa de lógica de discovery — aumenta acoplamento e dificulta mudança de estratégia.

## Server-Side Discovery

O cliente envia a requisição para um **Load Balancer ou API Gateway**, que consulta o registry internamente e roteia.

```
┌──────────┐                    ┌───────────────┐    ┌─────────────────┐
│ Client   │──── /orders ──────►│ Load Balancer │───►│ Service Registry│
└──────────┘                    │ (Envoy/Kong)  │    └─────────────────┘
                                │               │
                                └───────────────┘
                                     │
                            ┌────────┴────────┐
                            ▼                 ▼
                     OrderService:1     OrderService:2
```

**Vantagem:** clientes simples, sem lógica de discovery. Mudança de estratégia de LB é transparente.
**Desvantagem:** mais um hop de rede; o load balancer vira ponto crítico.

## DNS-Based Discovery (Kubernetes)

No Kubernetes, o DNS interno é o mecanismo padrão. Cada Service recebe um nome DNS estável.

```yaml
# Service definition
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

```typescript
// O cliente usa o DNS — não precisa de lógica de discovery
const response = await fetch("http://order-service.production.svc.cluster.local/orders");

// Formato: <service-name>.<namespace>.svc.cluster.local
// O kube-dns resolve para o ClusterIP do Service
// O kube-proxy distribui entre os Pods via iptables/IPVS
```

## Consul (Self-hosted, multi-cloud)

Para ambientes fora do Kubernetes ou multi-cloud:

```typescript
// Registrar serviço ao iniciar
await consul.agent.service.register({
  name: "order-service",
  id: `order-service-${process.env.POD_NAME}`,
  address: process.env.POD_IP,
  port: 8080,
  check: {
    http: `http://${process.env.POD_IP}:8080/health`,
    interval: "10s",
    deregisterCriticalServiceAfter: "30s"
  }
});

// Desregistrar ao encerrar
process.on("SIGTERM", async () => {
  await consul.agent.service.deregister(`order-service-${process.env.POD_NAME}`);
});

// Descobrir instâncias saudáveis
const services = await consul.health.service({ service: "order-service", passing: true });
const instances = services[1].map(s => `${s.Service.Address}:${s.Service.Port}`);
```

## Comparativo

| Abordagem | Exemplos | Quando usar |
|---|---|---|
| DNS-based | Kubernetes DNS, Route53 | Padrão no K8s — zero overhead |
| Client-side | Netflix Eureka, Consul + Ribbon | Controle fino de LB no cliente |
| Server-side | Envoy, Kong, AWS ALB | Clientes simples, centralizar LB |
| Service Mesh | Istio, Linkerd | Discovery + mTLS + observabilidade integrados |

## Conceitos Relacionados
[[microsservicos]] · [[kubernetes-core]] · [[service-mesh]] · [[load-balancer]] · [[consistent-hashing]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-17*
