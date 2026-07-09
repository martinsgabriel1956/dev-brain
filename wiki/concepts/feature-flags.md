---
type: concept
title: "Feature Flags"
aliases: ["feature toggles", "feature flags", "feature switches"]
date_created: 2026-04-22
date_updated: 2026-07-09
source_count: 2
tags: [devops, deploy, cicd, feature-flags, infra]
skill: tech-mentor-infra
status: stub
---

# Feature Flags

Mecanismo para ativar/desativar funcionalidades em produção sem novo deploy — desacopla deploy de release. Ver [[concepts/deploy-vs-release]] para a distinção formal entre os dois eventos.

## Uso em Deploy

Complementa [[concepts/canary-release]] e [[concepts/blue-green-deploy]]: código da feature vai para produção desativado, ativado gradualmente por flag sem risco de deploy.

## Key Sources

- [[sources/blue-green-canary-rolling]]
- [[sources/tipos-de-deploy]]
