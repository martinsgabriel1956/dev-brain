---
type: concept
title: "Rate Limit Distribuído: Estado Compartilhado"
aliases: ["rate limit distribuído", "contador compartilhado"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 2
tags: [rate-limiting, sistemas-distribuidos, redis, consistencia, spof]
skill: tech-mentor-backend
status: draft
---

# Rate Limit Distribuído: Estado Compartilhado

Com N instâncias e contador em memória por instância, o limite se multiplica: 3 instâncias × 100 req/min = até **300** para o mesmo usuário ([[wiki/sources/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato]]). Solução: **armazenamento compartilhado externo** consultado e atualizado por todas as instâncias ([[wiki/concepts/estado-compartilhado]]).

**Custos:** latência (ida ao store a cada requisição), concorrência (atualização atômica), consistência, disponibilidade; o store vira dependência crítica e, se mal dimensionado, **gargalo/SPOF do sistema que deveria proteger** ([[wiki/concepts/single-point-of-failure]]). Precisa ser tão escalável e resiliente quanto a aplicação.

**Opções citadas:** [[wiki/concepts/redis]], Google Memorystore, Azure Cache for Redis, DynamoDB, ou banco tradicional; não equivalentes (`[external, não verificado]` além de Redis). `[skill: tech-mentor-backend]`: Lua script atômico no Redis (`rate-limiting.md`).

Lacunas do vídeo: política de falha do store (fail-open × fail-closed), sincronização local+global, custo de latência. Ver [[wiki/concepts/rate-limiting]].

Parte 2 antecipa o tema como a terceira decisão (Redis/cache compartilhado, concorrência, indisponibilidade do limiter); sliding window e token bucket exigem mais estado que fixed window. Ver [[wiki/questions/rate-limit-producao-atomicidade-fail-open-e-janela-distribuida]].

## Key Sources

- [[wiki/sources/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato]]
- [[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]] — fecho: produção distribuída como terceira parte; mais estado em sliding/token
