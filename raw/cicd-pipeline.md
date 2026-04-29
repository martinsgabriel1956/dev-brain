---
date: 2026-03-27
tags: [tech-mentor, system-design, deploy, cicd, github-actions, pipeline, automacao]
skill: tech-mentor-system-design/references/zero-downtime-deployments.md
level: intermediário
---

# CI/CD Pipeline

## Contexto

CI/CD não é uma ferramenta — é uma disciplina. Continuous Integration: todo código mergeado é testado automaticamente. Continuous Delivery: todo commit que passa está pronto para produção. Continuous Deployment: vai automaticamente. Princípio central: **fail fast** — os testes mais rápidos ficam primeiro.

## Como Funciona

### A Estrutura de um Pipeline

```
Push → CI Pipeline                    CD Pipeline
│                                     │
├── 1. Fast Feedback (< 5 min)        ├── 5. Deploy Staging
│    ├── Lint + type check            │    └── Smoke tests
│    ├── Unit tests                   │
│    └── Security scan (secrets)      ├── 6. Deploy Produção
│                                     │    ├── Canary / Rolling / Blue-Green
├── 2. Build                          │    └── Health check pós-deploy
│    ├── Docker image                 │
│    └── Push para registry           └── 7. Rollback automático
│                                          se error rate > threshold
├── 3. Integration tests
└── 4. Security gates
```

## Código de Referência

### CI Pipeline — GitHub Actions

```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint-and-typecheck:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: "20", cache: "npm" }
      - run: npm ci
      - run: npm run lint
      - run: npm run typecheck

  unit-tests:
    runs-on: ubuntu-latest
    needs: lint-and-typecheck
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: "20", cache: "npm" }
      - run: npm ci
      - run: npm run test:unit -- --coverage --coverageThreshold='{"global":{"lines":70}}'

  build:
    runs-on: ubuntu-latest
    needs: unit-tests
    steps:
      - uses: actions/checkout@v4
      - uses: docker/build-push-action@v5
        with:
          push: true
          tags: ghcr.io/${{ github.repository }}:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

  integration-tests:
    runs-on: ubuntu-latest
    needs: unit-tests
    services:
      postgres:
        image: postgres:16
        env: { POSTGRES_DB: testdb, POSTGRES_PASSWORD: test }
        options: --health-cmd pg_isready --health-retries 5
      redis:
        image: redis:7
        options: --health-cmd "redis-cli ping" --health-retries 5
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: "20", cache: "npm" }
      - run: npm ci
      - run: npm run db:migrate
        env: { DATABASE_URL: "postgresql://postgres:test@localhost/testdb" }
      - run: npm run test:integration
        env:
          DATABASE_URL: "postgresql://postgres:test@localhost/testdb"
          REDIS_URL: "redis://localhost:6379"

  security-scan:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - uses: aquasecurity/trivy-action@master
        with:
          image-ref: ghcr.io/${{ github.repository }}:${{ github.sha }}
          severity: "HIGH,CRITICAL"
          exit-code: "1"
```

### CD Pipeline — Deploy Automatizado

```yaml
name: CD
on:
  push:
    branches: [main]

jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - run: |
          kubectl set image deployment/api \
            api=ghcr.io/${{ github.repository }}:${{ github.sha }} \
            --namespace=staging
          kubectl rollout status deployment/api --namespace=staging --timeout=5m
      - run: npm run test:smoke -- --env=staging

  deploy-production:
    runs-on: ubuntu-latest
    needs: deploy-staging
    environment: production  # requer aprovação manual no GitHub
    steps:
      - run: |
          kubectl argo rollouts set image rollout/api \
            api=ghcr.io/${{ github.repository }}:${{ github.sha }}
          kubectl argo rollouts status rollout/api --timeout=10m
          # Argo analisa error rate — rollback automático se > 1%
```

### Rollback Automático via Métricas

```yaml
apiVersion: argoproj.io/v1alpha1
kind: AnalysisTemplate
metadata:
  name: error-rate-check
spec:
  metrics:
    - name: error-rate
      interval: 1m
      successCondition: result[0] < 0.01  # < 1% error rate
      failureLimit: 3                      # 3 falhas → rollback automático
      provider:
        prometheus:
          address: http://prometheus:9090
          query: |
            sum(rate(http_requests_total{status=~"5.."}[5m]))
            /
            sum(rate(http_requests_total[5m]))
```

```bash
# Rollback manual
kubectl rollout undo deployment/api

# Voltar para revisão específica
kubectl rollout undo deployment/api --to-revision=3
```

## Trade-offs

| Aspecto | Manual | Automatizado |
|---|---|---|
| **Velocidade** | Lento — deploys espaçados | Rápido — múltiplos deploys/dia |
| **Confiabilidade** | Inconsistente | Reproduzível — mesmo processo sempre |
| **Risco por deploy** | Alto — changes grandes | Baixo — changes pequenas e frequentes |
| **Rollback** | Manual e lento | Automático ou 1 comando |
| **Setup inicial** | Zero | Médio — pipelines, secrets, environments |

## Quando Usar / Quando Evitar

**Princípios de um pipeline saudável:**
```
1. Fail fast          → testes rápidos primeiro, lentos depois
2. Pipeline < 10 min  → feedback rápido para o dev
3. Determinístico     → mesmo input → mesmo resultado
4. Artefato único     → build uma vez, deploy em múltiplos ambientes
5. Secrets em vault   → nunca em código ou env vars hardcoded
6. Rollback testado   → não apenas planejado
```

**Gates que bloqueiam o merge:**
- Lint + typecheck
- Unit tests com coverage mínimo (70%)
- Integration tests
- Security scan (HIGH/CRITICAL)

## Conceitos Relacionados

[[fase-4-deploy-operacoes]] · [[zero-downtime-deploy]] · [[feature-flags]] · [[distributed-tracing]] · [[observabilidade]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-27*
