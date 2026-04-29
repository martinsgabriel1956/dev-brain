---
type: concept
title: "Feature Flags"
aliases: ["feature toggles", "feature flags", "feature switches"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [devops, deploy, cicd, feature-flags, infra]
skill: tech-mentor-infra
status: stub
---

# Feature Flags

Mecanismo para ativar/desativar funcionalidades em produção sem novo deploy — desacopla deploy de release.

## Uso em Deploy

Complementa [[concepts/canary-release]] e [[concepts/blue-green-deploy]]: código da feature vai para produção desativado, ativado gradualmente por flag sem risco de deploy.

## Key Sources

- [[sources/blue-green-canary-rolling]]
