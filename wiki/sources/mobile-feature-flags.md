---
type: source
title: "Feature Flags + A/B Testing Mobile — LaunchDarkly, Firebase Remote Config"
aliases: ["mobile feature flags", "mobile remote config", "mobile ab testing", "mobile rollout"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-feature-flags.md
source_url: ""
author: "tech-mentor-mobile skill"
date_published: 2026-04-23
date_ingested: 2026-04-24
source_count: 0
tags: [mobile, feature-flags, ab-testing, remote-config, launchdarkly, firebase, rollout]
skill: tech-mentor-mobile
status: stable
---

# Feature Flags Mobile

## TL;DR

Feature flags dissociam deploy de release — código vai para produção, ativação é controlada remotamente sem nova versão na store. Habilita rollout gradual (5% → 100%), A/B testing, kill switch imediato e canary releases. Firebase Remote Config gratuito para casos simples; LaunchDarkly para targeting avançado por usuário. Cache local obrigatório para funcionar offline.

## Claims Principais

| Claim | Confiança |
|---|---|
| Flags dissociam deploy de release — reverter bug é desativar flag, sem hotfix na store | Alta |
| Firebase Remote Config gratuito e suficiente para rollout por percentual | Alta |
| Cache local de flags obrigatório — app não pode depender de fetch bem-sucedido para funcionar | Alta |
| A/B testing via flags exige métricas de conversão atreladas — sem métrica, sem A/B | Alta |

## Conceitos Abordados

- [[mobile-feature-flags]] · [[mobile-cicd]] · [[feature-flags]] · [[mobile-monitoramento]]
