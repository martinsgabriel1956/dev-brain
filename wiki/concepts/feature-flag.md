---
type: concept
title: "Feature Flag (Feature Toggle)"
aliases: ["feature toggle", "feature flags", "interruptor de funcionalidade"]
date_created: 2026-06-26
date_updated: 2026-06-26
source_count: 1
tags: [feature-flag, feature-toggle, redis, cache, trunk-based-development, backend]
skill: tech-mentor-backend
status: stable
---

# Feature Flag (Feature Toggle)

## TL;DR

Interruptores dentro do código que habilitam ou desabilitam trechos de funcionalidade em runtime, sem deploy. Permitem Trunk-Based Development sem branches de feature e viabilizam dark launches, canary releases e A/B tests.

## Para Que Serve

- Evitar branches de feature (habilitar Trunk-Based Development)
- Desligar funcionalidades com problema em produção sem rollback
- Lançar features para subconjunto de usuários (canary, A/B)
- Controlar acesso a features por tenant ou plano

## Por Que Redis é Ideal

Feature flags ficam **no meio do fluxo de execução do código** — toda request consulta os toggles. A latência precisa ser mínima. Um banco relacional introduz latência perceptível; [[redis]] responde em sub-milissegundo.

## Arquitetura com Redis

```
[Tela de Gestão]
       ↓
[Microsserviço de Manutenção]
       ↓
   [Banco SQL]       ← fonte de verdade
       ↓
   [Batch Job]       ← sincroniza periodicamente
       ↓
    [Redis]          ← consulta ultra-rápida
       ↑
[Microsserviço Feature Toggle]
       ↑
   [Aplicação]
```

O batch pode ser substituído por [[cache-aside]]: ao não encontrar a flag no Redis, o microsserviço busca no SQL, popula o Redis com TTL e retorna.

## Ferramentas de Mercado

- **LaunchDarkly** — SaaS com SDKs, targeting, analytics
- **Unleash** — open source, self-hosted
- **Flagsmith** — open source/cloud
- Redis + código próprio — simples chave-valor; adequado para casos básicos

## Key Sources

- [[wiki/sources/como-arquitetar-com-cache-e-redis]]
