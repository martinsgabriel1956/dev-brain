---
type: source
title: "Platform Engineering, DevEx e DORA Metrics"
aliases: ["platform engineering", "devex", "idp", "backstage", "dora metrics", "golden path"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/platform-engineering-devex.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [platform-engineering, devex, idp, backstage, dora-metrics, golden-path, space-metrics, inner-loop, outer-loop, cognitive-load]
skill: tech-mentor-infra
status: stable
---

## TL;DR

Platform Engineering cria um IDP (Internal Developer Platform) para reduzir carga cognitiva dos times de produto. Backstage é o software catalog padrão. Golden Path Templates eliminam decisões repetitivas. DORA Metrics (Deployment Frequency, Lead Time, MTTR, Change Failure Rate) são as métricas de entrega. DevEx mede satisfação do developer com SPACE framework.

## Key Claims

**Claim:** Platform Engineering existe para reduzir carga cognitiva — não para controle centralizado.
**Evidence:** Developer que gasta 40% do tempo com infra, pipelines e ambientes tem 40% menos tempo para produto. IDP resolve: self-service de ambientes, templates de projeto, observabilidade pré-configurada, secrets management. Métrica: tempo de onboarding de um novo serviço.
**Confidence:** alta

**Claim:** DORA Metrics são os 4 indicadores de elite de engenharia de software.
**Evidence:** Deployment Frequency (elite: múltiplos deploys/dia), Lead Time for Changes (elite: < 1h), MTTR (elite: < 1h), Change Failure Rate (elite: < 5%). Times elite combinam alta velocidade com alta estabilidade — não é trade-off.
**Confidence:** alta

**Claim:** Golden Path Templates eliminam decisões repetitivas e garantem padrões de segurança por default.
**Evidence:** Dev cria novo serviço via template: observabilidade, CI/CD, RBAC, secrets management, testes já configurados. Sem template: cada dev reinventa a roda de forma diferente e insegura.
**Confidence:** alta

**Claim:** Inner Loop (dev local) é o maior gargalo de produtividade — feedback lento mata o flow.
**Evidence:** Inner loop: código → build → teste → debug. Se cada iteração demora 5min, um dev faz 96 iterações/dia. Se demora 2min: 240 iterações. Investir em hot reload, testes rápidos, e dev containers tem ROI imediato.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/platform-engineering]]
- [[concepts/idp]]
- [[concepts/backstage]]
- [[concepts/golden-path]]
- [[concepts/dora-metrics]]
- [[concepts/space-metrics]]
- [[concepts/inner-loop]]
- [[concepts/cognitive-load]]

## Open Questions

- Como medir ROI de Platform Engineering sem métricas de satisfação de developer (SPACE) bem instrumentadas?
- Backstage software catalog — como mantê-lo atualizado sem virar documentação morta?
