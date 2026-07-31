---
type: concept
title: "Feature Flags"
aliases: ["feature toggles", "feature flags", "feature switches"]
date_created: 2026-04-22
date_updated: 2026-07-31
source_count: 4
tags: [devops, deploy, cicd, feature-flags, infra]
skill: tech-mentor-infra
status: stub
---

# Feature Flags

Mecanismo para ativar/desativar funcionalidades em produção sem novo deploy — desacopla deploy de release. Ver [[concepts/deploy-vs-release]] para a distinção formal entre os dois eventos.

## Uso em Deploy

Complementa [[concepts/canary-release]] e [[concepts/blue-green-deploy]]: código da feature vai para produção desativado, ativado gradualmente por flag sem risco de deploy.

## Exemplo em Escala: Gatekeeper (Meta)

O Gatekeeper é o sistema interno de feature flag da Meta/Facebook, citado como peça central da transição para deploy contínuo em 2017: código chega a produção pelo push normal (já quase-contínuo), mas fica desligado até o Gatekeeper liberar a feature, gradualmente, para uma fração de usuários. Reduz risco por decisão de release (toggle) em vez de por decisão de deploy (reverter versão). *Não confundir com [[concepts/gatekeeper-pattern]] — mesmo nome, conceito de segurança não relacionado.* → [[wiki/sources/rapid-release-at-massive-scale-facebook]]

## Key Sources

- [[sources/blue-green-canary-rolling]]
- [[sources/tipos-de-deploy]]
- [[wiki/sources/rapid-release-at-massive-scale-facebook]] — Gatekeeper da Meta como exemplo de feature flag em escala massiva
- [[wiki/sources/continuous-integration-delivery-deploy-vs-release]] — feature flag citada como um dos dois mecanismos concretos de desacoplar deploy de release
