---
type: concept
title: "GitHub Actions"
aliases: ["GitHub Actions", "GHA", "actions workflow", "github workflow"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [devops, cicd, github, automação]
skill: tech-mentor-infra
status: stable
---

# GitHub Actions

Plataforma de CI/CD integrada ao GitHub. Pipelines definidos como YAML em `.github/workflows/`.

## Conceitos Chave

- **Workflow**: arquivo YAML que define o pipeline
- **Job**: unidade de execução (roda num runner, em paralelo por padrão)
- **Step**: comando ou action dentro de um job
- **Runner**: máquina que executa o job (`ubuntu-latest`, `macos-latest`, self-hosted)
- **Action**: step reutilizável publicado no marketplace (`actions/checkout@v4`)

## Orquestração com `needs`

Jobs rodam em paralelo por padrão. `needs:` cria dependência:

```yaml
jobs:
  lint:         # roda imediatamente
  unit-tests:
    needs: lint  # aguarda lint passar
  build:
    needs: unit-tests
  integration-tests:
    needs: unit-tests  # roda em paralelo com build
  security-scan:
    needs: build
```

## Serviços para integration tests

Sobe containers auxiliares (banco, cache) junto com o job:

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

## Docker cache com GHA

```yaml
- uses: docker/build-push-action@v5
  with:
    push: true
    tags: ghcr.io/${{ github.repository }}:${{ github.sha }}
    cache-from: type=gha    # lê do cache do Actions
    cache-to: type=gha,mode=max  # salva para próximos runs
```

## Environments com aprovação manual

```yaml
deploy-production:
  environment: production  # requer aprovação no GitHub antes de executar
```

Útil para Continuous Delivery: pipeline automático até staging, deploy para produção exige confirmação humana.

## Triggers comuns

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:  # trigger manual via UI
  schedule:
    - cron: "0 2 * * *"  # nightly
```

## Ver também

- [[concepts/ci-cd]] — disciplina que o GitHub Actions implementa
- [[concepts/pipeline-de-ci]] — estrutura de stages de referência
- [[concepts/argo-rollouts]] — ferramenta usada no CD após o CI passar

## Key Sources

- [[sources/cicd-pipeline]]
