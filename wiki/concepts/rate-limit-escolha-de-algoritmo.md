---
type: concept
title: "Escolha do Algoritmo de Rate Limit"
aliases: ["fixed vs sliding vs token vs leaky"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [rate-limiting, comparativo, trade-off]
skill: tech-mentor-backend
status: draft
---

# Escolha do Algoritmo de Rate Limit

Segundo [[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]], os quatro algoritmos não são melhores/piores: cada um produz um comportamento. Decidir pelo problema, não pela sofisticação.

| Algoritmo | Controla | Bom para | Custo |
|---|---|---|---|
| [[wiki/concepts/fixed-window-rate-limit]] | cota por janela | cota contratual, barreira simples, login | burst na fronteira |
| [[wiki/concepts/sliding-window-rate-limit]] | cota nos últimos 60 s | distribuição uniforme, infra limitada | mais estado e I/O |
| [[wiki/concepts/token-bucket]] | taxa média + pico controlado | clientes com rajadas legítimas, pesos por endpoint | dois parâmetros (taxa, capacidade) |
| [[wiki/concepts/leaky-bucket]] | saída a taxa constante | backend pouco elástico (legado), jobs | latência de fila |

Duas decisões (vídeos 1 e 2): **onde** ([[wiki/concepts/rate-limit-camadas-de-posicionamento]]) e **como** (esta tabela); a terceira é produção distribuída ([[wiki/concepts/rate-limit-estado-compartilhado]]).

`[skill: tech-mentor-backend]`: padrão geral = Sliding Window Counter; Token Bucket para bursts controlados. Não contradiz o autor, que não dá padrão. Ver [[wiki/concepts/rate-limiting]].

## Key Sources

- [[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]]
