---
type: concept
title: "Token Bucket"
aliases: ["balde de fichas"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 2
tags: [rate-limiting, algoritmo, bursts]
skill: tech-mentor-backend
status: draft
---

# Token Bucket

Balde com capacidade máxima de tokens, reposto a taxa fixa (ex.: 2 ou 100 por segundo). Cada requisição consome um token; sem tokens, é rejeitada ou adiada. **Permite picos controlados** até a capacidade do balde ([[wiki/sources/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato]]).

- Contraste: [[wiki/concepts/leaky-bucket]] suaviza a saída; token bucket tolera rajadas.
- Usado por [[wiki/entities/spring-cloud-gateway]] (RequestRateLimiter com Redis) e [[wiki/entities/bucket4j]].
- `[skill: tech-mentor-backend]` (`rate-limiting.md`): implementação atômica em Redis com Lua; O(1) de memória; escolha padrão quando bursts controlados são desejáveis.
- Contexto geral: [[wiki/concepts/rate-limiting]], [[wiki/concepts/traffic-shaping-e-traffic-policing]].

Parte 2: exemplo 100 tokens/s de reposição e balde de 200 (até 200 requisições de uma vez); admite burst e controla a taxa média; suporta [[wiki/concepts/rate-limit-pesos-por-endpoint]] (caso real: 10.000 tokens/h por cliente, 1 vs. ~1000 por requisição). Falha que ele mitiga: [[wiki/concepts/burst-na-fronteira-da-janela]]. Comparação: [[wiki/concepts/rate-limit-escolha-de-algoritmo]].

## Key Sources

- [[wiki/sources/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato]]
- [[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]] — exemplo numérico, pesos por endpoint e caso real da sincronização
