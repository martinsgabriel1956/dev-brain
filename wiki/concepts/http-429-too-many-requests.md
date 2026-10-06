---
type: concept
title: "HTTP 429 Too Many Requests"
aliases: ["429", "RFC 6585", "Retry-After"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 2
tags: [http, rate-limiting, rfc-6585, retry]
skill: tech-mentor-backend
status: draft
---

# HTTP 429 Too Many Requests

Status code definido em **2012 pela RFC 6585**: o cliente enviou requisições demais num intervalo. A resposta pode trazer **Retry-After** (quanto esperar) ([[wiki/sources/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato]]).

- Rate limit **não obriga** a rejeitar; 429 é a resposta típica de uma política rígida ([[wiki/concepts/traffic-shaping-e-traffic-policing]]).
- O cliente precisa tratar o 429: backoff e política de retry ([[wiki/concepts/retry-backoff]]); implementar rate limit muda a experiência dos consumidores da API.
- `[skill: tech-mentor-backend]`: tratar `Retry-After` como obrigatório na prática (sem ele clientes entram em retry apertado e agravam o problema); 429 = limite do cliente, 503 = sobrecarga do sistema.
- Catálogo geral: [[wiki/concepts/http-status-code]]. Política: [[wiki/concepts/rate-limiting]].

Parte 2: no caso real, os 429 tiveram efeito pedagógico — clientes ajustaram suas sincronizações ([[wiki/concepts/rate-limit-pesos-por-endpoint]]).

## Key Sources

- [[wiki/sources/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato]]
- [[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]] — 429 como sinal que levou clientes a ajustar processos
