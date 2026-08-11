---
type: concept
title: "CI/CD"
aliases: ["CI/CD", "continuous integration", "continuous delivery", "continuous deployment", "pipeline de entrega"]
date_created: 2026-04-22
date_updated: 2026-08-11
source_count: 9
tags: [devops, cicd, deploy, automação, qualidade, projetos-novos, dora, trunk-based-development]
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

## Deploy Manual vs. Automático — a diferença é o gatilho

Um deploy manual (SSH na máquina, `git pull`, `npm start`) e um deploy automático (pipeline disparada por merge na `main`) podem executar exatamente os mesmos comandos por baixo. A diferença não é **o que** é executado, é **o que dispara** a execução: decisão humana pontual vs. regra automática. Deploy automático reduz erro humano e torna difícil esquecer de deployar, além de permitir gates adicionais (ex.: só deploya se os testes passarem).

**Exemplo concreto do lado manual:** um deploy [[concepts/blue-green-deploy]] numa VPS única, disparado inteiramente por SSH com uma sequência de scripts bash (clonar, subir instância, trocar roteamento do reverse proxy) rodados um a um pelo operador — sem CI, sem gate, sem gatilho automático. → [[wiki/sources/deploy-blue-green-na-pratica-vps-nginx]]

Qual **estratégia** de tráfego o deploy (manual ou automático) usa — [[concepts/recreate-deployment]], [[concepts/rolling-update]], [[concepts/blue-green-deploy]], [[concepts/canary-release]] — é uma decisão ortogonal. Continuous Deployment, em particular, tende a usar Rolling como padrão de fato, mas nada o obriga.

## Serverless

Em ambientes serverless, a estratégia de tráfego geralmente é administrada pela cloud, não pelo time: o provedor troca o roteamento para a versão nova de forma equivalente a um [[concepts/recreate-deployment]] instantâneo ou a um [[concepts/blue-green-deploy]] invisível. Nada impede configurar Canary ou A/B manualmente sobre serverless, mas serviços simples tendem a ficar no comportamento padrão da plataforma — inclusive rollback costuma ser rápido nesse modelo.

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

Essa prática é uma instância concreta do padrão [[walking-skeleton]] (esqueleto ambulante): uma fatia mínima que atravessa toda a arquitetura, em produção, antes de qualquer feature — o caso do LMAX (ver [[over-engineering]]) generaliza a mesma ideia além do boilerplate, para arquiteturas inteiras.

## CI/CD e a Correlação DORA entre Velocidade e Qualidade

A pesquisa [[dora-metrics|DORA]] (livro *Accelerate*) mostra que Deployment Frequency alta e Lead Time for Changes baixo se correlacionam com Change Failure Rate e MTTR *melhores*, não piores — refutando a intuição do "triângulo de ferro" (rápido/barato/bom, escolha dois). CI/CD é a prática que torna essa correlação possível: pipelines rápidos e determinísticos são o que permite manter deploys pequenos e frequentes sem acumular risco. Ver [[over-engineering]] para a discussão de como o medo de quebrar em produção leva ao efeito oposto — portões de deploy excessivos que atrasam feedback e aumentam risco por deploy.

Um exemplo real anterior à formalização do livro *Accelerate* (2018): o Facebook, em 2017, migrou de ~700 cherry-picks manuais/dia para push quase-contínuo direto da master, escalando o time em 15x sem degradar produtividade por engenheiro nem aumentar incidentes críticos — a mesma correlação "mais frequência, mesma ou melhor qualidade" que a DORA formalizaria depois, observada empiricamente em escala massiva. → [[wiki/sources/rapid-release-at-massive-scale-facebook]]

## 6 Princípios de Pipeline Saudável

1. **Fail fast** — testes rápidos primeiro, lentos depois
2. **Pipeline < 10 min** — feedback em tempo útil para o dev
3. **Determinístico** — mesmo input, mesmo resultado (sem flaky tests)
4. **Artefato único** — build uma vez, deploy em múltiplos ambientes
5. **Secrets em vault** — nunca em código ou env vars hardcoded
6. **Rollback testado** — não apenas planejado

## Fluxo de Branch com Ambiente Intermediário: feature → dev/staging → main

Padrão didático comum: `feature branch → dev/staging → main`. A feature vai primeiro para uma branch de dev/staging, onde QA (ou o próprio dev) testa antes de seguir para main — só o merge para main dispara o CD de fato. É uma forma concreta de inserir o gate humano de Continuous Delivery sem abandonar a automação: o pipeline roda igual em ambos os merges, mas só o de main termina em deploy para produção. → [[wiki/sources/continuous-integration-delivery-deploy-vs-release]]

## "CI" como *Single Command Deploy* em Times Pequenos

[[wiki/sources/git-flow-farsa-solucao-maturidade-rebase-lucas-montano]] oferece uma leitura pragmática de CI para **times pequenos** que não têm capacidade de manter um servidor de CI dedicado: o essencial não é o GitHub/GitLab Actions, é que **a entrega seja um único comando** — *single command deploy*, rodado até da máquina do dev. O objetivo é ser **frictionless** e eliminar o estado "código pronto mas não em produção". É a mesma ideia do "deploy manual vs. automático" acima (o que muda é o gatilho, não os comandos), aplicada como piso mínimo antes de haver pipeline.

Essa fonte também **contrasta** com o fluxo `feature → dev/staging → main` documentado acima: ela argumenta contra manter uma branch `dev` de **vida longa**, defendendo só a `main` como fonte de verdade ([[wiki/concepts/trunk-based-development]]) — com *staging* sendo um **ambiente** idêntico ao de produção (só muda URL/capacidade), não uma branch. Não é contradição de mérito: são trade-offs distintos (evitar manter conflitos entre uma `dev` atrasada e uma `prod` com hotfix, vs. ter um gate humano explícito por branch).

## Ver também

- [[wiki/concepts/trunk-based-development]] — o fluxo só-`main` com single command deploy
- [[concepts/pipeline-de-ci]] — estrutura detalhada dos stages
- [[concepts/github-actions]] — implementação com GitHub Actions
- [[concepts/argo-rollouts]] — progressive delivery no CD
- [[concepts/zero-downtime-deploy]] — objetivo final do pipeline
- [[concepts/feature-flags]] — desacopla deploy de release
- [[concepts/walking-skeleton]] — padrão que fundamenta o deploy imediato do boilerplate
- [[concepts/dora-metrics]] — como medir se o pipeline está de fato acelerando o time

## Key Sources

- [[sources/cicd-pipeline]]
- [[wiki/sources/5-ou-6-dicas-para-projetos-novos]]
- [[wiki/sources/integration-test-martin-fowler]]
- [[wiki/sources/tipos-de-deploy]]
- [[wiki/sources/como-evitar-over-engineering-david-farley]]
- [[wiki/sources/deploy-blue-green-na-pratica-vps-nginx]] — exemplo concreto de deploy 100% manual via SSH, sem pipeline
- [[wiki/sources/rapid-release-at-massive-scale-facebook]] — caso real (Meta/Facebook, 2017) de deploy quase-contínuo em escala massiva
- [[wiki/sources/continuous-integration-delivery-deploy-vs-release]] — aula didática reforçando os três níveis, com demo prática em GitHub Actions + VPS e fluxo de branch feature/dev-staging/main
- [[wiki/sources/git-flow-farsa-solucao-maturidade-rebase-lucas-montano]] — CI como single command deploy frictionless para times pequenos; contra a branch `dev` de vida longa
