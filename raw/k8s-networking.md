---
date: 2026-04-17
tags: [tech-mentor, kubernetes, networking, cni, cilium, networkpolicy, infra]
skill: tech-mentor-infra/references/kubernetes
level: avançado
---

# K8s Networking — CNI, Cilium, NetworkPolicy, Gateway API

## Modelo de Rede do Kubernetes

Três regras fundamentais do modelo flat de rede do K8s:
1. Todo pod pode se comunicar com todo pod sem NAT
2. Todo node pode se comunicar com todo pod sem NAT
3. O IP que um pod vê como seu próprio é o mesmo que outros pods usam para alcançá-lo

Isso é implementado pelo **CNI (Container Network Interface)** — plugin que configura interfaces de rede nos pods.

```
Node A                          Node B
┌─────────────────────┐        ┌─────────────────────┐
│ Pod A1 (10.0.1.2)  │        │ Pod B1 (10.0.2.3)  │
│ Pod A2 (10.0.1.3)  │        │ Pod B2 (10.0.2.4)  │
│                     │        │                     │
│ veth pairs → bridge │◄──────►│ veth pairs → bridge │
│ (cni0/eth0)         │ overlay│ (cni0/eth0)         │
└─────────────────────┘  (VXLAN│ Geneve)└─────────────────────┘
```

---

## CNI — Principais Implementações

| CNI | Mecanismo | Destaque |
|---|---|---|
| **Flannel** | VXLAN overlay | Simples, sem NetworkPolicy nativo |
| **Calico** | BGP ou VXLAN | NetworkPolicy + performance |
| **Cilium** | eBPF | L7 policy, mTLS, observabilidade nativa |
| **Weave** | Mesh overlay | Multi-cloud simples |

---

## Cilium — eBPF Native Networking

Cilium substitui iptables por programas eBPF no kernel — mais rápido, menos overhead, visibilidade L7.

```yaml
# Instalar Cilium via Helm
helm install cilium cilium/cilium --version 1.15.0 \
  --set kubeProxyReplacement=true \     # substitui kube-proxy completamente
  --set hubble.enabled=true \           # observabilidade de rede
  --set hubble.relay.enabled=true \
  --set hubble.ui.enabled=true
```

```bash
# Hubble — inspecionar tráfego de rede em tempo real
hubble observe --namespace production --protocol http
# → order-api → payment-service (200 OK, 45ms)
# → order-api → inventory-service (503 Service Unavailable, 2ms)
```

---

## NetworkPolicy — Firewall de Pods

Por padrão, todos os pods se comunicam livremente. NetworkPolicy implementa micro-segmentação.

```yaml
# Política: order-api só pode receber tráfego do ingress e enviar para payment-service e DB
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: order-api-policy
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: order-api
  policyTypes:
    - Ingress
    - Egress

  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: ingress-nginx
      ports:
        - protocol: TCP
          port: 8080

  egress:
    - to:
        - podSelector:
            matchLabels:
              app: payment-service
      ports:
        - protocol: TCP
          port: 3000
    - to:
        - podSelector:
            matchLabels:
              app: postgres
      ports:
        - protocol: TCP
          port: 5432
    # DNS sempre liberado
    - ports:
        - protocol: UDP
          port: 53
```

**Regra de ouro:** deny-all por default, allow-list explícito. Sem NetworkPolicy, o cluster é completamente flat — qualquer pod comprometido alcança qualquer outro.

```yaml
# Default deny-all no namespace
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: production
spec:
  podSelector: {}          # aplica a todos os pods
  policyTypes: [Ingress, Egress]
  # sem regras = nada permitido
```

---

## Gateway API — Sucessor do Ingress

O `Ingress` resource tem limitações sérias para roteamento avançado. A **Gateway API** (GA no K8s 1.31) resolve isso com objetos mais expressivos.

```yaml
# GatewayClass + Gateway (gerenciado pelo time de infra)
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: production-gateway
  namespace: infra
spec:
  gatewayClassName: cilium
  listeners:
    - name: https
      protocol: HTTPS
      port: 443
      tls:
        mode: Terminate
        certificateRefs:
          - name: wildcard-cert

---
# HTTPRoute (gerenciado pelo time de produto)
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: orders-route
  namespace: production
spec:
  parentRefs:
    - name: production-gateway
      namespace: infra
  hostnames: ["api.example.com"]
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /orders
      backendRefs:
        - name: order-api
          port: 8080
          weight: 90
        - name: order-api-canary
          port: 8080
          weight: 10    # canary release: 10% do tráfego
```

**Por que Gateway API > Ingress:**
- Separação de responsabilidades: infra gerencia Gateway, produto gerencia HTTPRoute
- Suporte nativo a canary, header-based routing, traffic splitting
- Extensível via annotations tipadas (não strings genéricas)

## Conceitos Relacionados
[[kubernetes-core]] · [[service-mesh]] · [[zero-trust]] · [[service-discovery]] · [[blue-green-canary-rolling]]

---
*Fonte: tech-mentor skill · tech-mentor-infra · 2026-04-17*
