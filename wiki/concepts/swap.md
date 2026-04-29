---
type: concept
title: "Swap"
aliases: ["swap", "swap space", "paging to disk", "memória virtual em disco"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [sistema-operacional, memória, performance, cs-fundamentals]
skill: cs-fundamentals
status: stable
---

# Swap

Mecanismo onde o SO move páginas de memória RAM que não estão sendo usadas para o disco, liberando RAM para outros processos.

## Como funciona

```
RAM cheia → SO escolhe páginas "frias" (não acessadas recentemente)
         → Move essas páginas para swap no disco
         → Libera espaço na RAM para o processo que precisa
         
Processo acessa página que está em swap:
  → Page fault (major fault)
  → SO lê página do disco de volta para RAM
  → Execução retoma (com latência)
```

## O problema

Disco é **ordens de magnitude mais lento** que RAM:

```
RAM:      ~100 nanosegundos
SSD NVMe: ~100 microsegundos  (1.000× mais lento)
SSD SATA: ~500 microsegundos  (5.000× mais lento)
HDD:      ~10 milissegundos   (100.000× mais lento)
```

Se o sistema começa a fazer swap constantemente (**thrashing**), a performance despenca — o SO passa mais tempo movendo páginas do que executando código.

## Sinais de problema

- `vmstat` mostrando alto `si` (swap in) e `so` (swap out)
- `free -h` com swap usado consistentemente
- Sistema respondendo lentamente com disco em 100%

## Boas práticas

- Sistemas com workloads previsíveis (Redis, PostgreSQL) frequentemente **desativam swap** — preferem OOM killer a degradação silenciosa
- **Huge pages** reduzem o número de entradas na page table e TLB pressure
- Monitorar `pgmajfault` em métricas de produção

## Ver também

- [[concepts/memoria-virtual]] — mecanismo que viabiliza o swap
- [[concepts/processo]] — processos cujas páginas vão para swap ficam mais lentos

## Key Sources

- [[sources/sistema-operacional-por-baixo-dos-panos]]
