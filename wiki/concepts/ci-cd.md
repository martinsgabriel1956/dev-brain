---
type: concept
title: "CI/CD"
aliases: ["CI/CD", "continuous integration", "continuous delivery", "continuous deployment", "pipeline de entrega"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [devops, cicd, deploy, automação, qualidade]
skill: tech-mentor-infra
status: stable
---

# CI/CD

Disciplina de entrega de software onde código é integrado, testado e entregue de forma contínua e automatizada. Não é uma ferramenta — é um conjunto de práticas.

## Os Três Níveis

| Nível | O que automatiza | Deploy é... |
|---|---|---|
| **Continuous Integration (CI)** | Integração + testes a cada push | Manual |
| **Continuous Delivery (CD)** | Tudo até produção estar *pronta* | Decisão humana |
| **Continuous Deployment** | Tudo, incluindo o deploy em produção | Automático |

A maioria das empresas opera em Continuous Delivery — todo commit está pronto, mas um humano decide quando vai para produção.

## Princípio Central: Fail Fast

Testes mais rápidos ficam primeiro no pipeline. Se algo vai quebrar, que quebre em 2 minutos (lint) e não em 20 (integration tests).

```
Lint (30s) → Unit (2min) → Build (3min) → Integration (5min) → Security (2min)
```

Se lint falhar, nada mais executa — economiza tempo e recursos.

## Por que CI/CD importa

Sem CI/CD:
- Changes grandes acumulam → risco alto por deploy
- "Funciona na minha máquina" → ambiente de deploy inconsistente
- Rollback = evento manual e estressante

Com CI/CD:
- Changes pequenas e frequentes → risco baixo por deploy
- Build reproduzível — mesmo processo sempre
- Rollback = 1 comando ou automático

## 6 Princípios de Pipeline Saudável

1. **Fail fast** — testes rápidos primeiro, lentos depois
2. **Pipeline < 10 min** — feedback em tempo útil para o dev
3. **Determinístico** — mesmo input, mesmo resultado (sem flaky tests)
4. **Artefato único** — build uma vez, deploy em múltiplos ambientes
5. **Secrets em vault** — nunca em código ou env vars hardcoded
6. **Rollback testado** — não apenas planejado

## Ver também

- [[concepts/pipeline-de-ci]] — estrutura detalhada dos stages
- [[concepts/github-actions]] — implementação com GitHub Actions
- [[concepts/argo-rollouts]] — progressive delivery no CD
- [[concepts/zero-downtime-deploy]] — objetivo final do pipeline
- [[concepts/feature-flags]] — desacopla deploy de release

## Key Sources

- [[sources/cicd-pipeline]]
