---
type: source
title: "Platform Engineering Mobile — Shared SDK, Módulos Nativos, DX da Equipe"
aliases: ["mobile platform engineering", "shared sdk mobile"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 0
tags: [mobile, platform-engineering, shared-sdk, native-module, monorepo, analytics, devex, react-native]
skill: tech-mentor-mobile
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/mobile-platform-engineering.md
source_url: ""
author: "tech-mentor-mobile"
date_published: 2026-04-23
date_ingested: 2026-04-23
---

# Platform Engineering Mobile — Shared SDK, Módulos Nativos, DX da Equipe

## TL;DR

Platform Engineering mobile é a camada de infraestrutura consumida por múltiplos times de produto sem que eles precisem entender os detalhes. O output não é um app — é o SDK e ferramental que suportam múltiplos apps. Inclui Auth, Networking, Storage, Analytics, FeatureFlags, Crash, Push e Utils padronizados.

## Key Claims

**Claim:** O erro mais custoso em analytics mobile é chamar providers (Firebase, Amplitude, Mixpanel) diretamente em 200 lugares — quando você troca de provider, o PR tem 500 linhas.
**Evidence:** A solução é o Adapter Pattern: um `AnalyticsService` registra múltiplos `AnalyticsProvider`, e o app chama apenas `analytics.track()`.
**Source:** raw/mobile-platform-engineering.md
**Confidence:** Alta

**Claim:** Módulos nativos custom (React Native) devem ser criados apenas quando não existe lib matura — o custo de manter código nativo iOS + Android é alto.
**Evidence:** Exemplo completo de `SecureStorage` com Android Keystore (Kotlin) + iOS Keychain (Swift) + TypeScript typed wrapper.
**Source:** raw/mobile-platform-engineering.md
**Confidence:** Alta

**Claim:** Monorepo com Turborepo + pnpm workspaces é a estrutura recomendada para múltiplos apps mobile da mesma empresa.
**Evidence:** Estrutura `apps/consumer`, `apps/driver`, `apps/merchant` + `packages/ui`, `packages/networking`, etc.
**Source:** raw/mobile-platform-engineering.md
**Confidence:** Alta

**Claim:** O `ApiClient` base deve receber `getToken` e `onUnauthorized` como injeção de dependência via construtor — não chamar o store diretamente.
**Evidence:** Código do `ApiClient` com `getToken: () => useAuthStore.getState().token`.
**Source:** raw/mobile-platform-engineering.md
**Confidence:** Média (singleton com acesso direto ao store é acoplamento implícito)

## Entities

- [[entities/turborepo]] — build incremental em monorepo
- [[entities/expo]] — plataforma React Native (EAS Build referenciado)

## Concepts

- [[concepts/shared-sdk]] — SDK compartilhado entre apps mobile
- [[concepts/adapter-pattern-analytics]] — Adapter Pattern para troca de provider de analytics
- [[concepts/native-module]] — módulo nativo React Native (iOS + Android)
- [[concepts/monorepo-mobile]] — estrutura de monorepo para múltiplos apps mobile
- [[concepts/analytics-pipeline]] — pipeline assíncrono de analytics

## Open Questions

- O `ApiClient` singleton com `useAuthStore.getState()` cria acoplamento oculto ao estado global — como isolar melhor para testes unitários?
- Qual é o limite de tamanho de SDK antes de justificar split em pacotes separados com versionamento independente?

## Raw Quotes

> "Platform Engineering mobile é a camada de infraestrutura que a equipe de produto consome sem precisar entender os detalhes."

> "Quando não existe uma lib npm para funcionalidade nativa específica... o custo de manutenção de código nativo iOS + Android é alto."

> "Módulos nativos custom apenas quando não existe lib matura para a funcionalidade."
