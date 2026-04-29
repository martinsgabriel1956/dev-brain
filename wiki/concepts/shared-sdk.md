---
type: concept
title: "Shared SDK Mobile"
aliases: ["sdk compartilhado", "mobile sdk", "platform sdk"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 1
tags: [mobile, platform-engineering, shared-sdk, monorepo]
skill: tech-mentor-mobile
status: stable
---

# Shared SDK Mobile

SDK compartilhado é o conjunto de módulos de infraestrutura que múltiplos apps mobile da mesma empresa consomem sem reimplementar. É o output central do [[concepts/monorepo-mobile]].

## Módulos típicos

```
packages/
├── auth/          → tokens, refresh, biometria, login social
├── networking/    → ApiClient base, retry, timeout, interceptors
├── storage/       → MMKV/Keychain/Keystore abstraídos
├── analytics/     → adapter pattern (troca provider sem mudar chamadas)
├── logging/       → estruturado, com contexto, sanitizado
├── feature-flags/ → abstração sobre Remote Config / LaunchDarkly
├── crash/         → Sentry configurado + wrappers
├── push/          → FCM/APNs token management
└── utils/         → date formatting, currency, validators
```

## Quando usar

- 2+ apps mobile da mesma empresa precisam de auth, analytics e networking idênticos
- Times diferentes precisam evoluir features de produto sem reinventar infra

## Trade-off principal

**Blast radius alto**: uma mudança quebrada no SDK afeta todos os apps simultaneamente. Mitigar com versionamento semântico e testes de integração por pacote.

## Key sources

- [[sources/mobile-platform-engineering]]
