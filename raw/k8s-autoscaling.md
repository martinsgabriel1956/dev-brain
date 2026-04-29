---
date: 2026-04-17
tags: [tech-mentor, kubernetes, autoscaling, hpa, keda, karpenter, infra]
skill: tech-mentor-infra/references/kubernetes
level: avançado
---

# K8s Autoscaling — HPA, VPA, KEDA, Karpenter

## Visão Geral

```
Tipo       → O que escala     → Baseado em
HPA        → Pods (réplicas)  → CPU, memória, métricas customizadas
VPA        → Requests/limits  → Uso histórico de resources
KEDA       → Pods (réplicas)  → Eventos externos (filas, Kafka, cron)
Karpenter  → Nodes            → Pods pendentes por falta de capacidade
```

---

## HPA — Horizontal Pod Autoscaler

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: order-api
  minReplicas: 2
  maxReplicas: 20
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70   # escala quando CPU média > 70%
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: 80
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 60   # aguarda 60s antes de escalar para cima
      policies:
        - type: Pods
          value: 4
          periodSeconds: 60  # máximo 4 pods por minuto
    scaleDown:
      stabilizationWindowSeconds: 300  # aguarda 5min antes de escalar para baixo
```

**Fórmula do HPA:** `réplicas_desejadas = ceil(réplicas_atuais × (métrica_atual / target))`

---

## VPA — Vertical Pod Autoscaler

VPA ajusta `requests` e `limits` dos containers com base no uso histórico. **Não escala réplicas** — aumenta recursos por pod.

```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: order-api-vpa
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: order-api
  updatePolicy:
    updateMode: "Off"  # Off = apenas recomenda, não aplica automaticamente
    # Auto = aplica (requer restart do pod)
    # Initial = aplica apenas em pods novos
  resourcePolicy:
    containerPolicies:
      - containerName: api
        minAllowed: { cpu: "100m", memory: "128Mi" }
        maxAllowed: { cpu: "2", memory: "2Gi" }
```

**Cuidado:** VPA em `Auto` mode faz restart dos pods para aplicar novos resources — incompatível com HPA para CPU/memória. Use VPA para right-sizing inicial, depois configure HPA.

---

## KEDA — Kubernetes Event-Driven Autoscaler

KEDA escala Deployments baseado em eventos externos: tamanho de fila SQS, lag de consumer Kafka, jobs no banco, etc.

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: order-processor-scaler
spec:
  scaleTargetRef:
    name: order-processor
  minReplicaCount: 0        # pode escalar para zero (zero-cost quando idle)
  maxReplicaCount: 50
  cooldownPeriod: 60
  triggers:
    - type: kafka
      metadata:
        bootstrapServers: kafka:9092
        consumerGroup: order-processor
        topic: orders
        lagThreshold: "100"   # 1 réplica por 100 mensagens no lag
    - type: aws-sqs-queue
      metadata:
        queueURL: https://sqs.us-east-1.amazonaws.com/123/orders
        queueLength: "10"
        awsRegion: us-east-1
    - type: cron
      metadata:
        timezone: America/Sao_Paulo
        start: "0 8 * * 1-5"   # escala em dias úteis às 8h
        end: "0 20 * * 1-5"    # reduz às 20h
        desiredReplicas: "5"
```

---

## Karpenter — Node Autoscaler

Enquanto o Cluster Autoscaler escala node groups inteiros, o **Karpenter** provisiona nodes individuais do tipo exato necessário para os pods pendentes — muito mais rápido e econômico.

```yaml
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: general
spec:
  template:
    metadata:
      labels: { billing: production }
    spec:
      requirements:
        - key: kubernetes.io/arch
          operator: In
          values: ["arm64", "amd64"]
        - key: karpenter.sh/capacity-type
          operator: In
          values: ["spot", "on-demand"]   # prefere spot, fallback on-demand
        - key: node.kubernetes.io/instance-type
          operator: In
          values: ["m6g.large", "m6g.xlarge", "m7g.large"]
      nodeClassRef:
        group: karpenter.k8s.aws
        kind: EC2NodeClass
        name: default
  limits:
    cpu: 1000      # teto de CPU no cluster
  disruption:
    consolidationPolicy: WhenUnderutilized   # consolida nodes ociosos
    consolidateAfter: 30s
```

## Trade-offs

| Solução | Velocidade | Custo | Complexidade |
|---|---|---|---|
| HPA | ~30s (nova réplica) | Pré-provisionado | Baixa |
| KEDA | ~30s | Pode usar zero | Média |
| Karpenter | ~45s (novo node) | Spot + consolidação | Alta (setup) |
| VPA | Restart do pod | Right-sizing | Média |

## Conceitos Relacionados
[[kubernetes-core]] · [[kafka]] · [[sqs-sns]] · [[finops-cost-aware-architecture]] · [[graceful-degradation]]

---
*Fonte: tech-mentor skill · tech-mentor-infra · 2026-04-17*
