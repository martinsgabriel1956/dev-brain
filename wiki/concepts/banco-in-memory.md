---
type: concept
title: "Banco In-Memory"
aliases: ["in-memory database", "banco em memória", "armazenamento em memória"]
date_created: 2026-06-26
date_updated: 2026-06-26
source_count: 1
tags: [banco-in-memory, redis, cache, performance, backend]
skill: tech-mentor-backend
status: stable
---

# Banco In-Memory

## TL;DR

Banco de dados cujo armazenamento primário é a RAM — não o disco. Latência mínima porque elimina o I/O de disco. [[redis]] é o principal representante.

## Por Que é Mais Rápido

- Acesso à RAM: ~100ns
- Acesso ao SSD: ~100μs (1000× mais lento)
- Acesso ao HDD: ~10ms (100.000× mais lento)

Bancos tradicionais usam disco como fonte de verdade e RAM como cache de página. Bancos in-memory invertem: RAM é primária, disco é opcional.

## Persistência em Redis

[[redis]] oferece persistência opcional para sobreviver a reinicializações:

- **RDB** — snapshots periódicos em arquivo (padrão, compacto, pode perder N minutos)
- **AOF** — log de cada operação de escrita (mais durável, arquivo maior)
- **RDB + AOF** — combinação recomendada para produção

A persistência reduz um pouco o desempenho. Para uso puramente como [[cache]], desabilitar é aceitável — ao reiniciar, o cache se reconstrói via [[cache-aside]].

## Limitações

- **Tamanho** — limitado pela RAM disponível; escalar via [[escalabilidade-horizontal]] (cluster)
- **Durabilidade** — sem AOF, dados em memória são perdidos na falha de energia
- **Custo** — RAM é mais cara que disco por GB

## Key Sources

- [[wiki/sources/como-arquitetar-com-cache-e-redis]]
