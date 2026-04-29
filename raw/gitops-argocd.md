---
date: 2026-04-17
tags: [tech-mentor, platform, gitops, argocd, flux, kubernetes, cicd]
skill: tech-mentor-platform/references/gitops
level: avançado
---

# GitOps — ArgoCD e Flux

## GitOps — O Modelo

GitOps define que o **estado desejado da infraestrutura é declarado em Git** e um agente reconcilia continuamente o estado real com o declarado. O operador de CD roda dentro do cluster, não fora — pull-based, não push-based.

```
Push-based (CI/CD tradicional):
  GitHub Actions → kubectl apply → K8s
  (pipeline tem credenciais de acesso ao cluster — risco de segurança)

Pull-based (GitOps):
  GitHub ← ArgoCD poll ← K8s cluster
  (cluster não expõe nada externamente — menor surface de ataque)

Reconciliation Loop:
  Git state ──► ArgoCD compara ──► K8s atual
                       │
                  diferente? → aplica mudança
                  igual?     → nada a fazer
```

## ArgoCD — Configuração Básica

```yaml
# Application — declara que o cluster deve refletir o que está no repo
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: order-api
  namespace: argocd
spec:
  project: production
  source:
    repoURL: https://github.com/myorg/order-api-deploy
    targetRevision: main
    path: k8s/production
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true        # remove recursos deletados do Git
      selfHeal: true     # reverte mudanças manuais no cluster
    syncOptions:
      - CreateNamespace=true
      - ServerSideApply=true
```

## ApplicationSet — Multi-cluster e Multi-env

```yaml
# Cria uma Application por ambiente automaticamente
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: order-api-envs
spec:
  generators:
    - list:
        elements:
          - env: staging
            cluster: https://staging-k8s.internal
            revision: main
          - env: production
            cluster: https://prod-k8s.internal
            revision: v1.5.2   # produção usa tag fixa, não main
  template:
    metadata:
      name: "order-api-{{env}}"
    spec:
      source:
        repoURL: https://github.com/myorg/order-api-deploy
        targetRevision: "{{revision}}"
        path: "k8s/{{env}}"
      destination:
        server: "{{cluster}}"
        namespace: production
```

## Sync Waves — Ordenação de Recursos

```yaml
# Garante que o banco de dados sobe antes da aplicação
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-api
  annotations:
    argocd.argoproj.io/sync-wave: "2"  # wave 2 — sobe depois do DB
---
apiVersion: batch/v1
kind: Job
metadata:
  name: run-migrations
  annotations:
    argocd.argoproj.io/sync-wave: "1"  # wave 1 — primeiro
    argocd.argoproj.io/hook: PreSync   # roda antes do sync principal
    argocd.argoproj.io/hook-delete-policy: HookSucceeded
```

## Flux — Alternativa GitOps

Flux usa o mesmo modelo pull-based mas com controllers compostos (source, kustomize, helm) — mais modular que ArgoCD.

```yaml
# GitRepository — fonte dos manifests
apiVersion: source.toolkit.fluxcd.io/v1
kind: GitRepository
metadata:
  name: order-api-deploy
spec:
  interval: 1m
  url: https://github.com/myorg/order-api-deploy
  ref:
    branch: main
  secretRef:
    name: github-token

---
# Kustomization — o que reconciliar
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: order-api
spec:
  interval: 5m
  sourceRef:
    kind: GitRepository
    name: order-api-deploy
  path: "./k8s/production"
  prune: true
  healthChecks:
    - apiVersion: apps/v1
      kind: Deployment
      name: order-api
      namespace: production
```

## ArgoCD vs. Flux

| Aspecto | ArgoCD | Flux |
|---|---|---|
| UI | Dashboard rico | Mínimo (uso via CLI/API) |
| Multi-cluster | ApplicationSet nativo | Fleet e multi-tenant |
| Extensibilidade | Plugins e hooks | Controllers compostos |
| RBAC | Granular por projeto | Via K8s RBAC |
| Curva de aprendizado | Menor (UI intuitiva) | Maior (mais componentes) |
| Notificações | Notification Controller | Notification Controller |

## CI/CD com GitOps

```
CI Pipeline (GitHub Actions):
  build → test → push image (com tag SHA) → update deploy repo

CD (ArgoCD/Flux):
  detect change in deploy repo → apply to cluster
```

```yaml
# GitHub Actions — atualiza a tag da imagem no repositório de deploy
- name: Update image tag in deploy repo
  run: |
    git clone https://github.com/myorg/order-api-deploy.git
    cd order-api-deploy
    # Atualiza a tag no kustomization.yaml
    kustomize edit set image order-api=ghcr.io/myorg/order-api:${{ github.sha }}
    git commit -am "chore: update order-api to ${{ github.sha }}"
    git push
```

## Conceitos Relacionados
[[terraform]] · [[kubernetes-core]] · [[k8s-autoscaling]] · [[cicd-pipeline]] · [[platform-engineering-devex]]

---
*Fonte: tech-mentor skill · tech-mentor-platform · 2026-04-17*
