---
date: 2026-04-17
tags: [tech-mentor, infra, kubernetes, k8s, pod, deployment, statefulset, rbac, probes, hpa]
skill: tech-mentor-infra/references/kubernetes
level: intermediário
---

# Kubernetes Core — Pod, Deployment, StatefulSet, RBAC, Probes e Autoscaling

## Contexto

Kubernetes é o sistema operacional dos microsserviços — orquestra containers abstraindo infraestrutura de rede, storage e scheduling. Entender os recursos core (Pod, Deployment, Service, ConfigMap, Secret) é pré-requisito para qualquer trabalho de plataforma. O diferencial do K8s é o reconciliation loop: você declara o estado desejado, o control plane trabalha continuamente para alcançá-lo.

---

## Conceitos Fundamentais

```
Control Plane:
  API Server    → ponto de entrada de todas as operações (kubectl, operators)
  etcd          → state store distribuído (toda configuração do cluster)
  Scheduler     → decide em qual Node cada Pod roda
  Controller Manager → reconciliation loops para cada resource type

Data Plane:
  Node          → máquina (VM ou bare metal) que roda os Pods
  kubelet       → agente em cada Node, executa as instruções do control plane
  kube-proxy    → gerencia regras de rede (iptables/IPVS) para Services
  Container Runtime → CRI (containerd, CRI-O) — executa os containers

Hierarquia:
  Cluster → Node → Pod → Container
  Namespace → agrupa resources logicamente (não é isolamento de segurança por padrão)
```

---

## Pod — A Unidade Atômica

```yaml
# Pod raramente criado diretamente — use Deployment/StatefulSet
# Este exemplo mostra as configurações mais importantes
apiVersion: v1
kind: Pod
metadata:
  name: order-service
  namespace: production
  labels:
    app: order-service
    version: "1.2.0"
spec:
  containers:
    - name: order-service
      image: myregistry.io/order-service:1.2.0
      
      # Portas expostas (informativo — não afeta rede)
      ports:
        - containerPort: 3000
          protocol: TCP

      # Recursos — SEMPRE definir em produção
      resources:
        requests:           # mínimo garantido pelo scheduler
          cpu: "100m"       # 100 millicores = 0.1 CPU
          memory: "128Mi"
        limits:             # máximo permitido
          cpu: "500m"
          memory: "512Mi"
          # Sem CPU limit → melhor performance (throttling afeta latência)
          # Sem memory limit → OOMKilled se vazar memória

      # Variáveis de ambiente
      env:
        - name: NODE_ENV
          value: "production"
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: order-service-secrets
              key: DATABASE_URL
        - name: POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name  # metadata do próprio Pod

      # ConfigMap como variáveis
      envFrom:
        - configMapRef:
            name: order-service-config

      # Probes — fundamentais para zero-downtime
      livenessProbe:         # Pod está vivo? Falha → restart
        httpGet:
          path: /health
          port: 3000
        initialDelaySeconds: 15    # aguardar antes da primeira check
        periodSeconds: 10          # frequência das checks
        failureThreshold: 3        # falhas consecutivas antes de restart

      readinessProbe:        # Pod está pronto para receber tráfego? Falha → remove do Service
        httpGet:
          path: /ready
          port: 3000
        initialDelaySeconds: 5
        periodSeconds: 5
        failureThreshold: 2

      startupProbe:          # Substituição do liveness durante startup lento (ex: JVM)
        httpGet:
          path: /health
          port: 3000
        failureThreshold: 30       # 30 * 10s = 5 minutos de tolerância
        periodSeconds: 10

      # Volume mounts
      volumeMounts:
        - name: tmp-dir
          mountPath: /tmp
        - name: config-volume
          mountPath: /app/config
          readOnly: true

  # Graceful shutdown — tempo para o Pod processar conexões pendentes
  terminationGracePeriodSeconds: 30

  volumes:
    - name: tmp-dir
      emptyDir: {}           # ephemeral, deletado com o Pod
    - name: config-volume
      configMap:
        name: order-service-config

  # Tolerância a falhas de Node
  topologySpreadConstraints:
    - maxSkew: 1
      topologyKey: kubernetes.io/hostname
      whenUnsatisfiable: DoNotSchedule
      labelSelector:
        matchLabels:
          app: order-service
```

---

## Deployment — Stateless Workloads

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-service
  namespace: production
spec:
  replicas: 3
  
  selector:
    matchLabels:
      app: order-service     # deve combinar com template.metadata.labels

  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1            # pods extras durante update
      maxUnavailable: 0      # zero downtime: nenhum Pod fica indisponível

  template:
    metadata:
      labels:
        app: order-service
        version: "1.2.0"
    spec:
      # serviceAccountName: order-service-sa  # para RBAC + IRSA/Workload Identity
      
      containers:
        - name: order-service
          image: myregistry.io/order-service:1.2.0
          # ... (mesmas configs do Pod acima)

---
# Service — exposição e load balancing interno
apiVersion: v1
kind: Service
metadata:
  name: order-service
  namespace: production
spec:
  selector:
    app: order-service        # seleciona Pods com este label
  ports:
    - protocol: TCP
      port: 80                # porta do Service
      targetPort: 3000        # porta do container
  type: ClusterIP             # interno ao cluster (default)
  # type: LoadBalancer        # cria LoadBalancer externo no cloud provider
  # type: NodePort            # expõe em porta alta em cada Node (desenvolvimento)
```

---

## StatefulSet — Workloads com Estado

```yaml
# StatefulSet para banco de dados ou qualquer workload que precisa:
# - Identidade de Pod estável (pod-0, pod-1, pod-2)
# - Storage persistente por Pod (cada Pod tem seu PVC)
# - Ordem de deploy/scale definida (pod-0 antes de pod-1)

apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres
  namespace: production
spec:
  serviceName: postgres-headless  # Service headless para DNS estável
  replicas: 3
  selector:
    matchLabels:
      app: postgres

  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
        - name: postgres
          image: postgres:16
          env:
            - name: PGDATA
              value: /var/lib/postgresql/data/pgdata
          volumeMounts:
            - name: postgres-data
              mountPath: /var/lib/postgresql/data
          resources:
            requests:
              cpu: "500m"
              memory: "1Gi"
            limits:
              memory: "2Gi"

  # PVC criado automaticamente para cada Pod (postgres-data-postgres-0, etc.)
  volumeClaimTemplates:
    - metadata:
        name: postgres-data
      spec:
        accessModes: ["ReadWriteOnce"]
        storageClassName: "gp3"
        resources:
          requests:
            storage: 50Gi

---
# Service Headless — cada Pod tem DNS próprio
# DNS: postgres-0.postgres-headless.production.svc.cluster.local
apiVersion: v1
kind: Service
metadata:
  name: postgres-headless
  namespace: production
spec:
  clusterIP: None              # headless: sem VIP, DNS retorna IPs dos Pods diretamente
  selector:
    app: postgres
  ports:
    - port: 5432
      targetPort: 5432
```

---

## RBAC — Role-Based Access Control

```yaml
# ServiceAccount — identidade do Pod dentro do cluster
apiVersion: v1
kind: ServiceAccount
metadata:
  name: order-service-sa
  namespace: production

---
# Role — permissões dentro de um namespace
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: order-service-role
  namespace: production
rules:
  - apiGroups: [""]
    resources: ["configmaps", "secrets"]
    verbs: ["get", "list", "watch"]
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "list"]

---
# RoleBinding — vincular Role ao ServiceAccount
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: order-service-rolebinding
  namespace: production
subjects:
  - kind: ServiceAccount
    name: order-service-sa
    namespace: production
roleRef:
  kind: Role
  apiGroup: rbac.authorization.k8s.io
  name: order-service-role

---
# ClusterRole — permissões em todo o cluster (use com moderação)
# ClusterRoleBinding — vincular ClusterRole a qualquer subject
```

---

## Autoscaling — HPA e KEDA

```yaml
# HPA — Horizontal Pod Autoscaler (CPU/Memory)
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: order-service-hpa
  namespace: production
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: order-service
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
          type: AverageValue
          averageValue: 400Mi

---
# KEDA ScaledObject — scale por métricas externas (Kafka lag, SQS depth, etc.)
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: order-processor-scaledobject
  namespace: production
spec:
  scaleTargetRef:
    name: order-processor
  minReplicaCount: 1
  maxReplicaCount: 50
  pollingInterval: 15       # verificar a cada 15s
  cooldownPeriod: 300       # aguardar 5min antes de scale-down
  triggers:
    - type: kafka
      metadata:
        bootstrapServers: kafka.production.svc.cluster.local:9092
        consumerGroup: order-processor
        topic: orders.created
        lagThreshold: "100"   # 1 replica por 100 mensagens de lag
```

---

## ConfigMap e Secret

```yaml
# ConfigMap — configurações não-sensíveis
apiVersion: v1
kind: ConfigMap
metadata:
  name: order-service-config
  namespace: production
data:
  LOG_LEVEL: "info"
  MAX_RETRY_ATTEMPTS: "3"
  FEATURE_NEW_CHECKOUT: "true"

---
# Secret — dados sensíveis (base64 encoded, não criptografado por padrão)
# Para criptografia real: External Secrets Operator + AWS Secrets Manager/Vault
apiVersion: v1
kind: Secret
metadata:
  name: order-service-secrets
  namespace: production
type: Opaque
stringData:                  # stringData aceita valores não-encoded (converte automaticamente)
  DATABASE_URL: "postgresql://user:pass@postgres:5432/orders"
  REDIS_URL: "redis://redis:6379"
  JWT_SECRET: "super-secret-key"
```

---

## Trade-offs

| Resource | Uso Correto | Anti-pattern |
|---|---|---|
| **Deployment** | APIs, workers stateless | Bancos de dados, qualquer storage |
| **StatefulSet** | PostgreSQL, Kafka, Redis com persistência | APIs — não precisam de identity estável |
| **DaemonSet** | Monitoring agents, log shippers | Workloads de aplicação |
| **Job/CronJob** | Migrations, batch processing | Serviços de longa duração |
| **Liveness probe** | Detectar deadlocks, processo travado | Health checks lentos → restart loops |
| **Readiness probe** | Controlar quando receber tráfego | Omitir → requests antes do app estar pronto |

## Quando Usar / Quando Evitar

**Requests sem limits:** CPU sem limit = melhor latência (sem throttling), memória sem limit = OOMKilled sem controle. Recomendação: sem CPU limit, com memory limit.

**Namespace como isolamento:** namespaces organizam, não isolam. Para isolamento real: Network Policies, Pod Security Standards, RBAC granular.

**StatefulSet para banco:** na maioria dos casos, use RDS/Cloud DB em vez de rodar banco no K8s. StatefulSet para banco faz sentido apenas quando latência sub-ms ou custo são críticos.

**KEDA sobre HPA custom metrics:** KEDA tem suporte nativo a dezenas de triggers (Kafka, SQS, RabbitMQ, Prometheus, cron) — preferir ao invés de HPA com external metrics adapter manual.

## Conceitos Relacionados

[[kubernetes-autoscaling]] · [[kubernetes-networking]] · [[kubernetes-security]] · [[service-mesh]] · [[argocd]]

---
*Fonte: tech-mentor skill · tech-mentor-infra · 2026-04-17*
