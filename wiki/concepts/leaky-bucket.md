---
type: concept
title: "Leaky Bucket"
aliases: ["balde furado"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 2
tags: [rate-limiting, algoritmo, suavizacao]
skill: tech-mentor-backend
status: draft
---

# Leaky Bucket

Balde que recebe água (requisições/pacotes) em ritmo irregular, mas tem saída controlada: a saída ocorre numa taxa previsível ([[wiki/sources/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato]]). Dá **fluxo previsível**, em oposição aos picos permitidos pelo [[wiki/concepts/token-bucket]].

`[skill: tech-mentor-backend]`: fila FIFO com saída a taxa constante; overflow descarta ou devolve 429; usado em gateways/proxies para proteger backends. O autor adia a comparação detalhada com fixed/sliding window para uma parte 2. Ver [[wiki/concepts/traffic-shaping-e-traffic-policing]], [[wiki/concepts/rate-limiting]].

Parte 2: transforma entrada irregular em saída previsível; indicado para recurso pouco elástico (legado, ~100 req/s) e para jobs (PDF, imagem, e-mail, relatório); a "fila" é didática, não processamento assíncrono. Base do [[wiki/concepts/client-rate-limit]]. Kong o lista como algoritmo avançado ([[wiki/entities/kong]]). Comparação: [[wiki/concepts/rate-limit-escolha-de-algoritmo]].

## Key Sources

- [[wiki/sources/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato]]
- [[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]] — uso com legado e jobs, client rate limit, fila didática
