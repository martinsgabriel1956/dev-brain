---
type: source
title: "Feature Flags"
aliases: ["feature toggle", "feature switch", "kill switch", "unleash", "launchdarkly"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 0
tags: [feature-flags, feature-toggle, rollout, ab-testing, unleash, launchdarkly, deploy]
skill: tech-mentor-backend
status: draft
source_file: /home/nemomartins/Documentos/new/dev-study/raw/feature-flags.md
source_url:
author:
date_published:
date_ingested: 2026-04-23
---

# Feature Flags

## TL;DR

Feature flags desacoplam deploy de release — você pode deployar código desativado e ativá-lo progressivamente sem novo deploy. Quatro tipos: Release Toggle (feature em progresso), Ops Toggle (kill switch), Experiment Toggle (A/B), Permission Toggle (plano/papel). O maior risco é flag debt: flags antigas que nunca são removidas. Ferramentas: Unleash, GrowthBook (open source), LaunchDarkly (SaaS).

## Key Claims

| Claim | Evidência |
|---|---|
| Flag debt é o maior risco — flags acumuladas = complexidade de branch em runtime | Martin Fowler — Feature Toggles |
| Rollout gradual: hash do userId % 100 para consistência | Mesmo usuário sempre vê o mesmo estado |
| Ops Toggle (kill switch) deve ser o mais simples — sem dependências | Deve funcionar mesmo se o Redis estiver down |
| Migrar para ferramenta dedicada quando > 10 flags ativas simultaneamente | Env vars + Redis manual não escala |
| Não usar feature flags para bugfix ou refactoring interno | Deploy direto é o correto |

## Conceitos

- [[concepts/feature-flags]] — mecanismo e tipos de toggle
- [[concepts/canary-release]] — rollout gradual alternativo via infra
- [[concepts/deploy-strategies]] — flags complementam blue/green e canary
- [[concepts/ab-testing]] — Experiment Toggle para análise de conversão

## Key Sources

_Este é o documento primário._
