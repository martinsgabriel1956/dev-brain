---
type: entity
title: "Kong"
aliases: ["Kong Gateway"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 2
tags: [api-gateway, proxy, rate-limiting]
skill: tech-mentor-backend
status: stub
---

# Kong

Gateway/proxy de API amplamente usado para **centralizar políticas de rate limit**: vários serviços compartilham a mesma política sem implementá-la em cada aplicação ([[wiki/sources/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato]]). Ver [[wiki/concepts/api-gateway]], [[wiki/concepts/rate-limit-camadas-de-posicionamento]]. O vídeo cita também outro gateway ("ox", ambíguo no ASR).

Parte 2: segundo o vídeo, suporta fixed window (por consumidor, credencial, IP, serviço, rota), sliding window e leaky bucket como algoritmo avançado; a documentação contrasta sliding e fixed na transição entre janelas. Tudo relato do áudio, `[external, não verificado]`. Ver [[wiki/concepts/fixed-window-rate-limit]], [[wiki/concepts/sliding-window-rate-limit]], [[wiki/concepts/leaky-bucket]].

## Key Sources

- [[wiki/sources/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato]]
- [[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]] — algoritmos suportados citados na parte 2
