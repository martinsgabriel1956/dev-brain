---
type: concept
title: "Deploy vs. Release"
aliases: ["deploy vs release", "separar deploy de release", "deploy diferente de release"]
date_created: 2026-07-09
date_updated: 2026-08-23
source_count: 4
tags: [devops, deploy, cicd, feature-flags, infra]
skill: tech-mentor-infra
status: stable
---

# Deploy vs. Release

Deploy e release são eventos diferentes, mesmo que em times pouco maduros aconteçam juntos.

```
Deploy:   colocar o binário/código na máquina de produção
Release:  ligar o comportamento para o usuário
```

Um deploy pode acontecer **sem** release: o código já está na máquina, mas nenhum usuário está sendo afetado por ele. Duas formas de conseguir isso:

- **Feature flag** — o código novo está escondido atrás de uma flag desligada; todo o tráfego chega ao servidor, mas as linhas novas não executam.
- **Tráfego direcionado** — duas instâncias rodando em paralelo, uma com código antigo e outra com código novo, mas 100% do tráfego real ainda vai para a antiga (base do [[concepts/canary-release]] e do [[concepts/shadow-deployment]] antes do cutover).

## Por que separar

- Deploy vira um evento de baixo risco e frequente — pode acontecer múltiplas vezes ao dia sem afetar usuários.
- Release vira uma decisão de produto/negócio, independente do ritmo de deploy — pode ser instantânea (flip de flag) e não exige novo build.
- Rollback de release (desligar a flag) é muito mais rápido que rollback de deploy (reverter código e redeployar).

## Relação com Feature Flags

[[concepts/feature-flags]] é o mecanismo mais comum para essa separação. Ver também a categoria "Release toggle" no framework de Martin Fowler já documentado ali.

## Relação com Deploy Manual vs. Automático

Ortogonal a essa distinção: independente de o deploy ser manual (SSH + `git pull` + `npm start`, decisão humana pontual) ou automático (pipeline "triggada" por regra, ex.: merge na `main`), deploy e release continuam sendo eventos separáveis. A diferença entre manual e automático não é o que é executado, é qual o gatilho que dispara a execução — ver [[concepts/ci-cd]].

## O mesmo raciocínio, um nível acima: Continuous Delivery vs. Continuous Deployment

[[wiki/sources/continuous-delivery-martin-fowler]] aplica a mesma lógica de separar capacidade de ato a um nível acima do deploy individual: Continuous Delivery é a **capacidade** de lançar para produção a qualquer momento, enquanto Continuous Deployment é o **ato** automático de fazê-lo a cada mudança que passa no pipeline. Assim como um deploy pode acontecer sem release (feature flag desligada), um pipeline pode ser capaz de ir para produção a qualquer commit sem que isso de fato aconteça a cada vez — a decisão de exercer essa capacidade costuma ser do negócio, não uma limitação técnica. Ver [[wiki/concepts/ci-cd]] para os quatro indicadores concretos de que um time tem essa capacidade.

## Key Sources

- [[sources/tipos-de-deploy]]
- [[wiki/sources/rapid-release-at-massive-scale-facebook]] — Gatekeeper (Meta) como implementação real dessa separação em escala
- [[wiki/sources/continuous-integration-delivery-deploy-vs-release]] — reforço didático da distinção com os mesmos dois mecanismos (feature flag e tráfego direcionado)
- [[wiki/sources/continuous-delivery-martin-fowler]] — a mesma distinção capacidade-vs-ato aplicada a Continuous Delivery vs. Continuous Deployment
