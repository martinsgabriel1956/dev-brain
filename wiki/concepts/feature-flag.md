---
type: concept
title: "Feature Flag (Feature Toggle)"
aliases: ["feature toggle", "feature flags", "interruptor de funcionalidade"]
date_created: 2026-06-26
date_updated: 2026-08-13
source_count: 3
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

## Rollout Progressivo Como Substituto de Branch de Feature

[[wiki/sources/pull-requests-por-que-falham-alternativas-sem-pr]] descreve o papel da feature flag no pacote de empresas que operam sem [[wiki/concepts/code-review|pull request]]: como o código vai direto para a `main` via [[wiki/concepts/trunk-based-development|trunk-based development]], uma feature complexa e ainda incompleta fica escondida atrás de uma flag mesmo já estando commitada. A liberação segue uma ordem progressiva — primeiro para pessoas dentro da própria empresa, depois para um pequeno grupo de usuários, e só então para toda a base — removendo a flag ao final desse processo de validação. É a mesma lógica de canary/A/B já documentada acima, aqui descrita como peça específica que viabiliza trunk-based sem branch de feature nem PR de revisão prévia.

## Key Sources

- [[wiki/sources/arquitetura-de-sacrificio]] — Fowler aplica o princípio de sacrifício a *features*: construir de forma descartável e liberar a um subconjunto de usuários para validar antes de investir o esforço total
- [[wiki/sources/como-arquitetar-com-cache-e-redis]]
- [[wiki/sources/pull-requests-por-que-falham-alternativas-sem-pr]] — feature flag como peça que viabiliza trunk-based sem branch de feature nem PR; rollout progressivo interno → grupo pequeno → base toda
