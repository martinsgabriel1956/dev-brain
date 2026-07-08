---
type: concept
title: "CI/CD"
aliases: ["CI/CD", "continuous integration", "continuous delivery", "continuous deployment", "pipeline de entrega"]
date_created: 2026-04-22
date_updated: 2026-07-07
source_count: 3
tags: [devops, cicd, deploy, automação, qualidade, projetos-novos]
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

O termo "Deployment Pipeline" é de [[wiki/entities/martin-fowler]]. Ele defende que [[teste-de-integracao-estreito-vs-amplo|testes de integração estreitos]] — por serem tão rápidos quanto unitários — devem rodar nos estágios iniciais do pipeline, dando feedback rápido; testes de integração amplos (system/E2E tests), sendo lentos, ficam melhor como gate de deploy do que de PR.

## Por que CI/CD importa

Sem CI/CD:
- Changes grandes acumulam → risco alto por deploy
- "Funciona na minha máquina" → ambiente de deploy inconsistente
- Rollback = evento manual e estressante

Com CI/CD:
- Changes pequenas e frequentes → risco baixo por deploy
- Build reproduzível — mesmo processo sempre
- Rollback = 1 comando ou automático

## Deploy Imediato do Boilerplate (Antes de Qualquer Funcionalidade)

Para um projeto novo, o CD não deve esperar a primeira feature. Recomendação prática, parte do [[wiki/concepts/checklist-primeiro-dia-projeto]]: assim que o framework gerar o boilerplate/Hello World, fazer o deploy dele imediatamente, com CD automático a cada merge para `main` (ex.: GitHub Actions apontando para uma VPS).

Motivo: é comum construir algo que só roda localmente (sem Docker, sem infraestrutura real) e descobrir na hora do primeiro deploy real que nada funciona no provedor escolhido — gerando horas de debugging tardio. Fazendo o deploy no dia 1, cada problema de ambiente aparece isolado e barato de corrigir, em vez de se acumular.

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
- [[wiki/sources/5-ou-6-dicas-para-projetos-novos]]
- [[wiki/sources/integration-test-martin-fowler]]
