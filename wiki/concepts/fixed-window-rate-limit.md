---
type: concept
title: "Fixed Window (rate limit)"
aliases: ["janela fixa", "fixed window counter"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [rate-limiting, algoritmo, fixed-window]
skill: tech-mentor-backend
status: draft
---

# Fixed Window (rate limit)

Divide o tempo em **janelas fixas** (10:00–10:01, 10:01–10:02...), conta as requisições do cliente em cada uma e bloqueia ao atingir o limite (ex.: 100/min) até o início da próxima, quando o contador zera ([[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]]). É o algoritmo mais simples (um contador por cliente e janela).

**Fraqueza:** [[wiki/concepts/burst-na-fronteira-da-janela]] (até 2× o limite em ~2 s).

**Quando usar:** cota contratual (X por minuto/hora/dia, sem preocupação de infra, comum em SaaS e API gateways) e barreira simples em APIs públicas e login contra força bruta. [[wiki/entities/kong]] suporta o modelo por consumidor, credencial, IP, serviço e rota (relato do áudio, `[external, não verificado]`).

`[skill: tech-mentor-backend]`: O(1) de memória, precisão média. Alternativa: [[wiki/concepts/sliding-window-rate-limit]]. Comparação: [[wiki/concepts/rate-limit-escolha-de-algoritmo]]. Visão geral: [[wiki/concepts/rate-limiting]].

## Key Sources

- [[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]]
