---
type: question
title: "Rate limit: contar requisições com falha e escolher a chave"
aliases: ["o que conta no rate limit"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 2
tags: [rate-limiting, design, pergunta-aberta]
skill: tech-mentor-backend
status: draft
---

# Rate limit: contar requisições com falha e escolher a chave

Perguntas levantadas e **não respondidas** em [[wiki/sources/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato]]: (1) limitar por usuário, API key ou IP? (2) a requisição conta só depois de um 200 ou também quando falha? (3) o que fazer ao atingir o limite (rejeitar, adiar)? (4) limite em alguns endpoints ou no sistema todo?

Pistas fora do vídeo: [[wiki/concepts/rate-limiting]] registra que só IP não cobre ataque distribuído nem NAT; `[skill: tech-mentor-backend]` trata limites por tier/API key e rate limit por custo de operação. Contar também falhas protege login contra brute force (ver [[wiki/concepts/ataque-online-vs-offline-senha]]). Continuar na parte 2 do vídeo, se publicada.

Parte 2 não responde; fornece o exemplo de login com fixed window (força bruta) e limite por cliente/consumidor/credencial/IP no Kong.

## Key Sources

- [[wiki/sources/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato]]
- [[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]] — exemplos de chave de identificação (consumidor, credencial, IP, rota)
