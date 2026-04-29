---
type: source
title: "CI/CD Pipeline"
aliases: ["CI/CD", "pipeline de deploy", "continuous integration", "continuous delivery"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 0
tags: [cicd, devops, pipeline, github-actions, deploy, automação]
skill: tech-mentor-infra
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/cicd-pipeline.md
source_url:
author:
date_published: 2026-03-27
date_ingested: 2026-04-22
---

# CI/CD Pipeline

## TL;DR

CI/CD é uma disciplina, não uma ferramenta. O source cobre a estrutura completa de um pipeline em 7 stages, código de referência em GitHub Actions, deploy automatizado com Argo Rollouts, rollback via métricas Prometheus, e os 6 princípios de um pipeline saudável.

---

## Key Claims

**Distinção CI vs CD**
- **Continuous Integration**: todo código mergeado é testado automaticamente
- **Continuous Delivery**: todo commit que passa nos testes está *pronto* para produção (deploy é decisão humana)
- **Continuous Deployment**: vai automaticamente para produção (deploy é automático)
- Princípio central: **fail fast** — testes mais rápidos ficam primeiro

**Estrutura do pipeline em 7 stages**
```
CI:
  1. Fast Feedback (< 5 min) — lint, typecheck, unit tests, security scan de secrets
  2. Build — Docker image + push para registry
  3. Integration tests — com PostgreSQL e Redis reais
  4. Security gates — Trivy scan na imagem (bloqueia HIGH/CRITICAL)

CD:
  5. Deploy Staging + Smoke tests
  6. Deploy Produção — Canary / Rolling / Blue-Green + health check
  7. Rollback automático se error rate > threshold
```

**GitHub Actions — padrões chave**
- `needs:` para orquestrar dependências entre jobs
- `services:` para subir Postgres e Redis reais nos testes de integração
- `cache-from/cache-to: type=gha` para Docker layer caching
- Coverage threshold embutido no comando de test: `--coverageThreshold='{"global":{"lines":70}}'`
- Ambiente `production` com aprovação manual no GitHub antes do deploy

**Argo Rollouts — progressive delivery**
- `AnalysisTemplate` consulta Prometheus a cada 1m
- `successCondition: result[0] < 0.01` — bloqueia se error rate ≥ 1%
- `failureLimit: 3` — após 3 falhas consecutivas, rollback automático

**Rollback manual**
```bash
kubectl rollout undo deployment/api
kubectl rollout undo deployment/api --to-revision=3
```

**6 princípios de pipeline saudável**
1. Fail fast — rápidos primeiro
2. Pipeline < 10 min — feedback em tempo útil
3. Determinístico — mesmo input, mesmo resultado
4. Artefato único — build uma vez, deploy em múltiplos ambientes
5. Secrets em vault — nunca em código ou env vars hardcoded
6. Rollback testado — não apenas planejado

**Gates que bloqueiam merge**
- Lint + typecheck
- Unit tests com coverage ≥ 70%
- Integration tests
- Security scan (HIGH/CRITICAL)

**Trade-offs manual vs automatizado**

| Aspecto | Manual | Automatizado |
|---|---|---|
| Velocidade | Deploys espaçados | Múltiplos deploys/dia |
| Risco por deploy | Alto — changes grandes | Baixo — changes pequenas |
| Rollback | Manual e lento | Automático ou 1 comando |
| Setup inicial | Zero | Médio |

---

## Conceitos Tocados

- [[concepts/ci-cd]] — disciplina e distinção entre CI, CD e Continuous Deployment
- [[concepts/pipeline-de-ci]] — estrutura de stages e princípio fail fast
- [[concepts/github-actions]] — ferramenta de CI/CD com padrões de referência
- [[concepts/argo-rollouts]] — progressive delivery com analysis template e rollback automático
- [[concepts/canary-release]] — estratégia usada no deploy de produção
- [[concepts/blue-green-deploy]] — estratégia alternativa no deploy de produção
- [[concepts/feature-flags]] — mencionado como mecanismo de release desacoplado do deploy
- [[concepts/zero-downtime-deploy]] — objetivo do pipeline de CD
- [[concepts/observabilidade]] — métricas Prometheus usadas no rollback automático

---

## Open Questions

- Qual o threshold ideal de coverage para cada tipo de projeto?
- Quando usar Argo Rollouts vs Flagger para progressive delivery?
- Como estruturar pipelines em monorepos para evitar builds desnecessários?
