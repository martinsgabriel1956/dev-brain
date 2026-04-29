---
type: concept
title: "Monorepo Mobile"
aliases: ["monorepo apps mobile", "turborepo mobile", "pnpm workspaces mobile"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 1
tags: [mobile, monorepo, turborepo, platform-engineering, devex]
skill: tech-mentor-mobile
status: stable
---

# Monorepo Mobile

Estrutura de repositório único para múltiplos apps mobile que compartilham packages de infraestrutura. Recomendada quando os apps são mantidos pela mesma equipe.

## Estrutura

```
apps/
├── consumer/    → app B2C
├── driver/      → app de entregador
└── merchant/    → app de lojista
packages/
├── ui/          → design system compartilhado
├── networking/  → ApiClient base
├── analytics/   → adapter pattern
├── auth/        → autenticação
├── storage/     → MMKV, Keychain/Keystore
├── feature-flags/
└── eslint-config/
```

Toolchain: **Turborepo** (builds incrementais por package) + **pnpm workspaces** (gerenciamento de dependências).

## Trade-offs

| Aspecto | Monorepo | Repos Separados |
|---|---|---|
| Consistência de SDK | Alta | Baixa — cada app diverge |
| Setup inicial | Alto | Baixo |
| CI | Complexo | Simples |
| Compartilhamento | Trivial | Difícil |
| Blast radius de mudança | Alto (afeta todos) | Zero |

## Quando usar

Monorepo quando os apps são mantidos pelo mesmo time e compartilham UI. Repos separados quando os apps têm times independentes com ciclos de release diferentes.

## Relacionado

- [[concepts/shared-sdk]] — packages do monorepo formam o shared SDK
- [[sources/mobile-platform-engineering]]
