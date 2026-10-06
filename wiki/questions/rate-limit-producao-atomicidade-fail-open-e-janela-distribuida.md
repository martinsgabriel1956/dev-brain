---
type: question
title: "Rate limit em produção: atomicidade, fail-open e janela distribuída"
aliases: []
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [rate-limiting, producao, redis, concorrencia]
skill: tech-mentor-backend
status: draft
---

# Rate limit em produção: atomicidade, fail-open e janela distribuída

Lacunas deixadas pela parte 2 ([[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]]), que propõe uma parte 3:

1. **Atomicidade:** como implementar token bucket e sliding window no [[wiki/concepts/redis]] sem corrida entre instâncias? `[skill: tech-mentor-backend]` mostra INCR/EXPIRE (fixed) e Lua (token bucket).
2. **Fail-open ou fail-closed** se o store cair ([[wiki/concepts/rate-limit-estado-compartilhado]]); o skill sugere fallback permissivo, mas isso abre mão da proteção justo sob estresse.
3. **Custo do sliding window** distribuído: Log (O(N)) vs. Counter (O(1)); o vídeo não distingue ([[wiki/concepts/sliding-window-rate-limit]]).
4. **Leaky bucket:** é fila real (latência, tamanho máximo, descarte) ou só medidor? O vídeo trata como fila didática.
5. **Pesos por endpoint:** como definir e revisar os pesos ([[wiki/concepts/rate-limit-pesos-por-endpoint]])?

Relacionada: [[wiki/questions/rate-limit-contabilizar-requisicao-falha-e-chave-de-identificacao]].

## Key Sources

- [[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]]
