---
date: 2026-04-17
tags: [tech-mentor, platform, devex, dora, backstage, golden-path]
skill: tech-mentor-platform/references/platform-engineering
level: arquiteto
---

# Platform Engineering, DevEx e DORA Metrics

## Platform Engineering

### Contexto
Platform Engineering é a disciplina de construir e operar **plataformas internas** que aumentam a produtividade dos times de produto. Em vez de cada squad configurar seu próprio CI/CD, Kubernetes, observabilidade e segurança, o time de plataforma oferece um **Internal Developer Platform (IDP)** com experiência consistente.

```
Sem Platform Engineering:
Squad A: configura CI/CD (3 dias)
Squad B: configura CI/CD (3 dias, diferente do A)
Squad C: configura CI/CD (2 dias, diferente dos dois)
...
Todos reinventam a roda, de forma inconsistente.

Com Platform Engineering:
Time de Plataforma → Golden Path template
Squad A: `npx create-service order-api` → CI/CD + K8s + alertas prontos em 30 min
```

### IDP — Internal Developer Platform

```
Developer Experience
       │
  ┌────▼──────────────────────────────────────┐
  │          Developer Portal (Backstage)      │
  │  Software Catalog | Templates | Docs | TechRadar│
  └────┬──────────────────────────────────────┘
       │
  ┌────▼──────────────────────────────────────┐
  │           Self-Service Layer               │
  │  CI/CD │ Envs │ Secrets │ Feature Flags    │
  └────┬──────────────────────────────────────┘
       │
  ┌────▼──────────────────────────────────────┐
  │        Shared Infrastructure               │
  │  K8s │ Observabilidade │ Service Mesh      │
  └───────────────────────────────────────────┘
```

### Backstage — Software Catalog

```yaml
# catalog-info.yaml — em cada repositório de serviço
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: order-api
  title: Order API
  description: Handles order creation, updates and fulfillment
  annotations:
    github.com/project-slug: myorg/order-api
    grafana/dashboard-selector: "service=order-api"
    pagerduty.com/service-id: P123456
    backstage.io/techdocs-ref: dir:.
  tags: [backend, orders, critical]
spec:
  type: service
  lifecycle: production
  owner: group:payments-team
  system: order-management
  dependsOn:
    - component:payment-api
    - resource:orders-postgres
    - resource:orders-kafka-topic
  providesApis:
    - order-api-rest
```

### Golden Path Template

```yaml
# Template Backstage que cria repositório, CI/CD e infraestrutura
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
  name: nodejs-service-template
spec:
  parameters:
    - title: Service Info
      properties:
        name: { type: string }
        owner: { type: string }
        description: { type: string }
  steps:
    - id: fetch-template
      action: fetch:template
      input:
        url: ./skeleton
        values: { name: "${{ parameters.name }}" }
    - id: create-repo
      action: publish:github
      input:
        repoUrl: "github.com?repo=${{ parameters.name }}&owner=myorg"
    - id: register-catalog
      action: catalog:register
      input:
        repoContentsUrl: "${{ steps['create-repo'].output.repoContentsUrl }}"
```

---

## DevEx — Developer Experience

### SPACE Metrics (GitHub Research)

Framework para medir DevEx — evita focar só em velocidade:

| Dimensão | O que mede | Exemplo de métrica |
|---|---|---|
| **S**atisfaction | Felicidade com ferramentas e processos | NPS interno, surveys trimestrais |
| **P**erformance | Qualidade e impacto do output | % de features sem bug em prod em 30 dias |
| **A**ctivity | Volume de trabalho (não produtividade!) | PRs merged, deploys |
| **C**ommunication | Colaboração e integração | Review time, PR comments |
| **E**fficiency | Fluxo de trabalho sem interrupções | Tempo de CI, onboarding time |

**Armadilha:** SPACE não é sobre maximizar "Activity" — developer que faz menos PRs mas entrega mais impacto tem melhor performance.

### Inner Loop vs. Outer Loop

```
Inner Loop (acontece centenas de vezes por dia):
  edit → build → test → debug
  Otimização: compilação incremental, hot reload, testes rápidos

Outer Loop (acontece dezenas de vezes por semana):
  PR → review → CI → deploy → observe
  Otimização: CI rápido, deploys confiáveis, observabilidade boa
```

---

## DORA Metrics

Quatro métricas de engenharia correlacionadas com desempenho de negócio (pesquisa DevOps Research & Assessment):

| Métrica | Elite | High | Medium | Low |
|---|---|---|---|---|
| **Deploy Frequency** | Várias vezes/dia | 1x/dia–1x/semana | 1x/semana–1x/mês | < 1x/mês |
| **Lead Time for Changes** | < 1 hora | 1 dia–1 semana | 1 semana–1 mês | > 1 mês |
| **Change Failure Rate** | < 5% | 5-10% | 10-15% | > 15% |
| **MTTR** | < 1 hora | < 1 dia | 1 dia–1 semana | > 1 semana |

```typescript
// Calculando DORA via GitHub API + dados de incidente
async function calculateDORAMetrics(repo: string, period: DateRange) {
  const deployments = await github.listDeployments(repo, period);
  const incidents = await pagerduty.listIncidents(period);

  const deployFrequency = deployments.length / period.days;

  const leadTimes = deployments.map(d =>
    differenceInHours(d.deployedAt, d.firstCommitAt)
  );
  const leadTime = median(leadTimes);

  const failedDeploys = deployments.filter(d => d.rollbackedAt);
  const changeFailureRate = failedDeploys.length / deployments.length;

  const mttr = median(incidents.map(i =>
    differenceInMinutes(i.resolvedAt, i.startedAt)
  ));

  return { deployFrequency, leadTime, changeFailureRate, mttr };
}
```

## Conceitos Relacionados
[[cicd-pipeline]] · [[kubernetes-core]] · [[observabilidade]] · [[architecture-fitness-functions]] · [[tech-debt]]

---
*Fonte: tech-mentor skill · tech-mentor-platform · 2026-04-17*
