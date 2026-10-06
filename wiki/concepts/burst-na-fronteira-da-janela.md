---
type: concept
title: "Burst na Fronteira da Janela"
aliases: ["boundary burst", "rajada na fronteira da janela"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [rate-limiting, fixed-window, bursts]
skill: tech-mentor-backend
status: draft
---

# Burst na Fronteira da Janela

Falha clássica do [[wiki/concepts/fixed-window-rate-limit]]: o cliente fica ocioso até o fim da janela, manda 100 requisições em 1 s (10:00:59), e logo após o reset manda mais 100 (10:01:00). Resultado: **200 requisições em ~2 s** sem violar a regra ([[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]]). Se todos os clientes fizerem o mesmo, há pico perigoso na infra. Aceitável se o limite for só contratual; problema se há limite de recursos.

Mitigações: [[wiki/concepts/sliding-window-rate-limit]] (sem fronteira fixa) ou [[wiki/concepts/token-bucket]] (burst limitado pela capacidade do balde). `[skill: tech-mentor-backend]` usa o mesmo exemplo ("boundary burst"). Ver [[wiki/concepts/rate-limiting]].

## Key Sources

- [[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]]
