---
date: 2026-04-01
tags: [tech-mentor, security, kubernetes, rbac, network-policy, pod-security, falco, audit, cis-benchmark]
skill: tech-mentor-security/references/kubernetes-security
level: intermediário
---

# Kubernetes Security

## Contexto

Kubernetes tem uma superfície de ataque ampla: API server exposto, RBAC mal configurado dá acesso irrestrito, Network Policies ausentes permitem lateral movement livre entre pods. A postura de segurança padrão de um cluster novo não é segura — precisa ser endurecida explicitamente.

## Como Funciona

Cinco camadas de defesa no K8s:

```
1. CIS Benchmark      → baseline de configuração do cluster
2. Pod Security Standards → restrições por namespace
3. RBAC mínimo        → least privilege para pods e operadores
4. Network Policies   → zero trust dentro do cluster
5. Audit Logging      → rastreabilidade de todas as operações
```

## Código de Referência

### CIS Benchmark com kube-bench

```bash
kubectl apply -f https://raw.githubusercontent.com/aquasecurity/kube-bench/main/job.yaml
kubectl logs -f job/kube-bench

# Checks críticos que frequentemente falham:
# 1.2.7  API Server: --authorization-mode deve incluir RBAC
# 1.2.13 API Server: --anonymous-auth deve ser false
# 1.2.24 Admission plugins deve incluir NodeRestriction
# 4.2.1  kubelet: --anonymous-auth deve ser false
# 5.1.1  RBAC: service accounts sem cluster-admin
```

### Pod Security Standards (PSS)

Substitui PodSecurityPolicy (removida no K8s 1.25). Aplicado por namespace via labels.

| Perfil | O que permite | Quando usar |
|---|---|---|
| `privileged` | Sem restrições | Infra crítica (CNI, CSI) |
| `baseline` | Bloqueia escalações óbvias | Workloads gerais |
| `restricted` | Hardening máximo | Workloads sensíveis, compliance |

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: payments
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/audit: restricted
    pod-security.kubernetes.io/warn: restricted

---
# Pod conforme com restricted
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: app
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop: ["ALL"]
```

### RBAC Mínimo

```yaml
# ServiceAccount com permissões mínimas
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: payments-role
  namespace: payments
rules:
  - apiGroups: [""]
    resources: ["configmaps", "secrets"]
    verbs: ["get", "list", "watch"]
    resourceNames: ["payments-config", "payments-secrets"]  # recursos específicos!
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: payments-rolebinding
  namespace: payments
subjects:
  - kind: ServiceAccount
    name: payments-sa
roleRef:
  kind: Role
  name: payments-role
  apiGroup: rbac.authorization.k8s.io
```

```bash
# Auditoria de RBAC
kubectl auth can-i --list --as=system:serviceaccount:payments:payments-sa
kubectl who-can get secrets -n payments  # plugin kubectl-who-can

# Service accounts com cluster-admin — deve ser vazio em prod
kubectl get clusterrolebindings -o json | jq '
  .items[] |
  select(.roleRef.name == "cluster-admin") |
  {binding: .metadata.name, subjects: .subjects}'

# Pods com automount de service account token desnecessário
kubectl get pods -A -o json | \
  jq '.items[] | select(.spec.automountServiceAccountToken != false) | {pod: .metadata.name, ns: .metadata.namespace}'
```

**Anti-patterns de RBAC:**
- `verbs: ["*"]` — wildcard em verbos
- `resources: ["*"]` — wildcard em recursos
- `automountServiceAccountToken: true` (default) quando não precisar do token

### Network Policies — Zero Trust no Cluster

```yaml
# Default deny — tudo bloqueado no namespace
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: payments
spec:
  podSelector: {}
  policyTypes: [Ingress, Egress]

---
# Liberar apenas o necessário
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: payments-api-policy
  namespace: payments
spec:
  podSelector:
    matchLabels:
      app: payments-api
  policyTypes: [Ingress, Egress]
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: ingress
          podSelector:
            matchLabels:
              app: nginx-ingress
      ports:
        - port: 8443
  egress:
    - to:
        - podSelector:
            matchLabels:
              app: postgres
      ports:
        - port: 5432
    - to:
        - podSelector:
            matchLabels:
              app: redis
      ports:
        - port: 6379
    - to: []  # DNS — obrigatório
      ports:
        - port: 53
          protocol: UDP
```

### Audit Logging

```yaml
# audit-policy.yaml
rules:
  - level: None
    nonResourceURLs: ["/healthz", "/readyz"]

  - level: Metadata  # metadados apenas — não o conteúdo do secret
    resources:
      - group: ""
        resources: ["secrets", "configmaps"]

  - level: RequestResponse  # log completo de deletes em produção
    verbs: ["delete"]
    namespaces: ["payments", "orders"]

  - level: RequestResponse  # qualquer mudança em RBAC
    resources:
      - group: "rbac.authorization.k8s.io"
        resources: ["rolebindings", "clusterrolebindings"]

  - level: Metadata  # padrão para o restante
```

```yaml
# Flags do kube-apiserver
--audit-policy-file=/etc/kubernetes/audit-policy.yaml
--audit-log-path=/var/log/kubernetes/audit.log
--audit-log-maxage=30
--audit-log-maxbackup=10
--audit-log-maxsize=100
```

### OPA Gatekeeper — Políticas além do PSS

```yaml
# Bloquear imagens sem digest (tag mutável = supply chain risk)
apiVersion: templates.gatekeeper.sh/v1
kind: ConstraintTemplate
metadata:
  name: k8srequireddigest
spec:
  targets:
    - target: admission.k8s.gatekeeper.sh
      rego: |
        package k8srequireddigest
        violation[{"msg": msg}] {
          container := input.review.object.spec.containers[_]
          not contains(container.image, "@sha256:")
          msg := sprintf("Container %v deve usar digest, não tag", [container.name])
        }
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| PSS restricted | Segurança por padrão no namespace | Quebra workloads que assumem root |
| Network Policy default-deny | Lateral movement impossível | Cada serviço novo exige policy explícita |
| RBAC mínimo | Blast radius reduzido | Mais YAML para gerenciar |
| Audit logging | Rastreabilidade completa | Volume de logs alto, precisa de retenção |

## Quando Usar / Quando Evitar

**Sempre aplique** em produção: PSS `restricted` nos namespaces de negócio, Network Policy default-deny, RBAC sem wildcards, audit logging habilitado.

**kube-bench** deve ser parte do processo de criação de novos clusters — não uma auditoria trimestral.

## Conceitos Relacionados

[[container-hardening]] · [[runtime-security]] · [[zero-trust]] · [[cloud-security]] · [[devsecops-pipeline]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-01*
