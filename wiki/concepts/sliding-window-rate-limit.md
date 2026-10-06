---
type: concept
title: "Sliding Window (rate limit)"
aliases: ["janela deslizante de rate limit", "sliding window rate limiting"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [rate-limiting, algoritmo, sliding-window]
skill: tech-mentor-backend
status: draft
---

# Sliding Window (rate limit)

Em vez de blocos fixos, a janela **acompanha o momento atual**: "100 requisições nos últimos 60 s". A cada requisição conta-se quantas o cliente fez nos 60 s anteriores, então não existe fronteira onde o contador zera ([[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]]). Reduz o [[wiki/concepts/burst-na-fronteira-da-janela]] do [[wiki/concepts/fixed-window-rate-limit]].

**Custo:** precisa guardar mais informação por requisição (um contador simples não basta): mais memória, mais I/O no armazenamento, lógica mais complexa, pior ainda se distribuído. Vale quando a **distribuição** das requisições importa tanto quanto a quantidade (recursos limitados de infra). A documentação do [[wiki/entities/kong]] contrasta sliding (taxa dentro do limite) com fixed (mais volume na transição) — relato do áudio, `[external, não verificado]`.

`[skill: tech-mentor-backend]`: duas variantes — **Log** (timestamp por requisição, exato, O(N)) e **Counter** (média ponderada da janela anterior e da atual, O(1), ~90%, padrão recomendado para APIs gerais). O vídeo descreve o custo da variante Log.

Homônimo: [[wiki/concepts/sliding-window]] é a técnica de algoritmos (dois ponteiros), outro assunto. Comparação: [[wiki/concepts/rate-limit-escolha-de-algoritmo]]; visão geral: [[wiki/concepts/rate-limiting]].

## Key Sources

- [[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]]
