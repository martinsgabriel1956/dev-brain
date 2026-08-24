---
type: concept
title: "Pipeline de CI"
aliases: ["CI pipeline", "pipeline de integração contínua", "stages de CI", "build pipeline"]
date_created: 2026-04-22
date_updated: 2026-08-23
source_count: 3
tags: [devops, cicd, pipeline, testes, build]
skill: tech-mentor-infra
status: stable
---

# Pipeline de CI

Sequência de stages automatizados que validam cada commit antes de chegar à produção. Organizado do mais rápido ao mais lento.

O princípio geral por trás dessa ordenação — estágios progressivos que trocam tempo extra por confiança crescente — vem de [[wiki/entities/martin-fowler]] ([[wiki/sources/deployment-pipeline-martin-fowler]]): estágios iniciais (lint, unit tests) pegam a maioria dos problemas rápido; estágios finais (integration tests, security gates) fazem uma checagem mais lenta e minuciosa. Os 7 estágios abaixo são uma implementação concreta desse princípio.

## Estrutura de 7 Stages

```
Push
│
├── 1. Fast Feedback (< 5 min)
│    ├── Lint + type check         ← falha em segundos se tem erro óbvio
│    ├── Unit tests + coverage     ← cobertura mínima 70%
│    └── Security scan (secrets)  ← detecta credenciais expostas
│
├── 2. Build
│    ├── Docker image              ← multi-stage, distroless
│    └── Push para registry       ← tag com git SHA
│
├── 3. Integration tests           ← banco e Redis reais (services)
│
└── 4. Security gates
     └── Trivy scan na imagem     ← bloqueia HIGH e CRITICAL
          │
          ▼ (se passar tudo)
          CD Pipeline
```

## Gates que bloqueiam o merge

- Lint + typecheck
- Unit tests com coverage ≥ 70%
- Integration tests passando
- Nenhuma CVE HIGH/CRITICAL nas dependências

## Padrões de implementação

**Coverage threshold embutido no comando:**
```bash
npm run test:unit -- --coverage \
  --coverageThreshold='{"global":{"lines":70}}'
```

**Services para integration tests (GitHub Actions):**
```yaml
services:
  postgres:
    image: postgres:16
    env: { POSTGRES_DB: testdb, POSTGRES_PASSWORD: test }
    options: --health-cmd pg_isready --health-retries 5
  redis:
    image: redis:7
    options: --health-cmd "redis-cli ping" --health-retries 5
```

**Docker layer cache no CI:**
```yaml
cache-from: type=gha
cache-to: type=gha,mode=max
```

**Artefato único:** build uma vez com a tag do git SHA, usar a mesma imagem em staging e produção — garante que o que foi testado é o que vai para produção.

## Antipadrões

- Rodar integration tests antes dos unit tests (viola fail fast)
- Build separado por ambiente (viola artefato único)
- Secrets em variáveis de ambiente hardcoded no YAML
- Pipeline > 10 min sem paralelização

## Ver também

- [[concepts/ci-cd]] — disciplina e princípios
- [[concepts/github-actions]] — implementação de referência
- [[concepts/argo-rollouts]] — o que acontece depois que o CI passa

## Key Sources

- [[sources/cicd-pipeline]]
- [[wiki/sources/deployment-pipeline-martin-fowler]] — origem do princípio de estágios progressivos por confiança
- [[wiki/sources/continuous-delivery-martin-fowler]] — o deployment pipeline como um dos dois requisitos de Continuous Delivery, ao lado da cultura colaborativa ([[wiki/concepts/devops-culture]])
