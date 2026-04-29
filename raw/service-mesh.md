---
date: 2026-03-29
tags: [tech-mentor, system-design, arquitetura, service-mesh, istio, linkerd, mtls]
skill: tech-mentor-system-design/references/service-mesh
level: arquiteto
---

# Service Mesh (Istio, Linkerd, mTLS)

## Contexto

Em microsserviços, todo serviço precisa de: retry logic, timeout, circuit breaker, mTLS, distributed tracing, métricas de rede. Sem service mesh, cada equipe implementa isso no código da aplicação — duplicado em cada serviço, em cada linguagem.

Service mesh move essas responsabilidades para a infraestrutura de rede. A aplicação não sabe que existe — ela só escreve e lê da rede normalmente.

---

## Como Funciona — Sidecar Pattern

Um proxy container é injetado em cada pod, interceptando todo tráfego de rede. Os proxies são coordenados por um control plane centralizado.

```
Sem service mesh:
  Serviço A (código + retry + mTLS + tracing)  →  Serviço B (código + retry + mTLS + tracing)

Com service mesh:
  Serviço A (só código)  →  [Proxy A]  ↔  [Proxy B]  →  Serviço B (só código)
                                ↕                ↕
                           Control Plane (Istiod)
```

O proxy intercepta tanto tráfego de saída (outbound) quanto de entrada (inbound). Do ponto de vista da aplicação, ela fala com localhost — o proxy faz todo o trabalho.

```bash
# Com Istio, habilitar injeção automática na namespace
kubectl label namespace checkout istio-injection=enabled

# Pod com sidecar injetado aparece como 2/2
kubectl get pods -n checkout
# NAME                    READY   STATUS
# checkout-api-xxx        2/2     Running   ← app + istio-proxy
```

---

## mTLS Automático

Sem service mesh: comunicação interna em plaintext ou TLS configurado manualmente por serviço.

Com Istio: mTLS automático entre todos os serviços — sem alterar uma linha de código da aplicação. Cada serviço recebe um certificado SPIFFE (identidade criptográfica baseada em Service Account do Kubernetes).

```yaml
# PeerAuthentication — modo mTLS por namespace
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: checkout
spec:
  mtls:
    mode: STRICT      # rejeita plaintext — apenas mTLS permitido
    # PERMISSIVE: aceita ambos (útil durante migração)
    # DISABLE: sem mTLS
```

```yaml
# AuthorizationPolicy — controle de quem pode chamar quem
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: checkout-policy
  namespace: checkout
spec:
  selector:
    matchLabels:
      app: checkout-api
  action: ALLOW
  rules:
    - from:
        - source:
            principals:
              # apenas frontend e order-service podem chamar checkout-api
              - "cluster.local/ns/frontend/sa/frontend-service"
              - "cluster.local/ns/orders/sa/order-service"
      to:
        - operation:
            methods: ["GET", "POST"]
            paths: ["/api/*"]
```

**O que isso garante**: mesmo que um pod seja comprometido, ele não consegue chamar serviços para os quais não tem permissão — mesmo dentro do cluster.

---

## Controle de Tráfego — Istio

### Canary Deploy sem alterar código

```yaml
# VirtualService — split de tráfego
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: checkout-api
spec:
  hosts:
    - checkout-api
  http:
    - match:
        - headers:
            x-canary:
              exact: "true"    # header explícito sempre vai para canary
      route:
        - destination:
            host: checkout-api
            subset: canary
    - route:
        - destination:
            host: checkout-api
            subset: stable
          weight: 90
        - destination:
            host: checkout-api
            subset: canary
          weight: 10           # 10% do tráfego geral para canary

---
# DestinationRule — define os subsets e circuit breaker
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: checkout-api
spec:
  host: checkout-api
  subsets:
    - name: stable
      labels:
        version: v1
    - name: canary
      labels:
        version: v2
  trafficPolicy:
    outlierDetection:
      consecutiveGatewayErrors: 5
      interval: 10s
      baseEjectionTime: 30s   # circuit breaker: ejeta instância com erros por 30s
```

### Retry e Timeout declarativo

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: payment-service
spec:
  hosts:
    - payment-service
  http:
    - timeout: 5s
      retries:
        attempts: 3
        perTryTimeout: 2s
        retryOn: "5xx,reset,connect-failure,retriable-4xx"
      route:
        - destination:
            host: payment-service
```

### Fault Injection — Chaos Engineering no nível de rede

```yaml
# Injetar falha para testar resiliência sem alterar código
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
            value: 10.0      # 10% dos requests com atraso artificial
          fixedDelay: 5s
        abort:
          percentage:
            value: 5.0       # 5% dos requests retornam 503
          httpStatus: 503
      route:
        - destination:
            host: payment-service
```

---

## Observabilidade Automática

O service mesh coleta golden signals de rede sem instrumentação na aplicação:

```promql
-- Taxa de erro por serviço (PromQL — Prometheus)
sum(rate(istio_requests_total{
  destination_service_name="order-service",
  response_code=~"5.."
}[5m])) /
sum(rate(istio_requests_total{
  destination_service_name="order-service"
}[5m]))

-- Latência P99
histogram_quantile(0.99,
  sum(rate(istio_request_duration_milliseconds_bucket{
    destination_service_name="order-service"
  }[5m])) by (le)
)
```

**Kiali** visualiza o service graph com taxas de erro por link, latências e status mTLS em tempo real — sem configurar nada na aplicação.

---

## Istio vs Linkerd

| | Istio | Linkerd |
|---|---|---|
| **Sidecar** | Envoy (poderoso, pesado) | linkerd-proxy (leve, escrito em Rust) |
| **mTLS** | ✅ | ✅ |
| **Traffic management** | Muito rico (canary, fault injection, mirror) | Básico (split de tráfego) |
| **Observabilidade** | Kiali, Grafana, Jaeger | Dashboard built-in |
| **Complexidade operacional** | Alta | Baixa |
| **Memory overhead por pod** | ~200MB | ~30MB |
| **Quando usar** | Precisa de traffic shaping avançado | Quer mTLS + observabilidade sem overhead |

---

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| **Cross-cutting concerns** | Retry, mTLS, tracing sem alterar código | Adiciona latência (microsegundos por hop) |
| **Segurança** | mTLS automático, AuthorizationPolicy por serviço | Complexidade de gerenciamento de certificados |
| **Observabilidade** | Golden signals automáticos de rede | Não substitui instrumentação de negócio |
| **Traffic shaping** | Canary, A/B, fault injection declarativo | Curva de aprendizado alta (muitos CRDs) |
| **Operação** | Time de plataforma gerencia, times de produto não tocam | Overhead operacional real: atualizações, debugging de proxy |

---

## Quando Usar / Quando Evitar

```
Precisa de mTLS entre todos os serviços?
└── Sim → Service mesh (vs gerenciar certificados manualmente por serviço)

Precisa de canary/traffic splitting sem alterar código?
└── Sim → Istio VirtualService

Precisa de observabilidade automática de rede entre serviços?
└── Sim → qualquer service mesh entrega isso

Time pequeno, pouca expertise em Kubernetes?
└── Evite mesh — overhead operacional é alto
    Use bibliotecas de resiliência na aplicação (opossum, resilience4j)

Menos de 10 serviços em produção?
└── Provavelmente não justifica — API Gateway + libs resolvem 80% dos casos

Mais de 10 serviços, SREs dedicados?
└── Avalie Linkerd (simples) → Istio (quando precisar de traffic shaping avançado)
```

---

## Ambient Mesh — Istio sem Sidecar (Istio 1.22+)

O modelo sidecar tem um custo: cada pod ganha um container Envoy (~50-200MB). Em clusters grandes, o overhead é significativo.

**Ambient mesh** move o proxy para o nível do nó (ztunnel), eliminando o sidecar por pod:

```
Modelo sidecar:  Pod [app + envoy] → Pod [app + envoy]
Modelo ambient:  Pod [app] → ztunnel (nó) → waypoint (namespace) → Pod [app]
```

```bash
istioctl install --set profile=ambient
kubectl label namespace production istio.io/dataplane-mode=ambient

# Waypoint proxy (L7) apenas para namespaces que precisam de políticas avançadas
istioctl waypoint apply --namespace payments
```

**Quando preferir ambient**: clusters grandes, overhead de memória crítico, operação mais simples. Sidecar ainda é mais estável e oferece controle granular por pod.

---

## Conceitos Relacionados

[[api-gateway-bff]] · [[microservicos-vs-monolito-modular]] · [[circuit-breaker]] · [[distributed-tracing]] · [[zero-downtime-deploy]] · [[observabilidade]]

---

*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-29*
