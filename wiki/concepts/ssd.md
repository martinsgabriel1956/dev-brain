---
type: concept
title: "SSD (Solid State Drive)"
aliases: ["SSD", "solid state drive", "NVMe", "SATA SSD", "disco de estado sólido"]
date_created: 2026-08-13
date_updated: 2026-08-13
source_count: 1
tags: [storage, hardware, ssd, nvme, sata, flash, cs-fundamentals]
skill: tech-mentor-data
status: stub
---

# SSD (Solid State Drive)

Armazenamento que grava dados eletronicamente em [[concepts/memoria-flash]] (células NAND), **sem partes móveis**. Por isso é muito mais rápido, mais durável (~5–10 anos) e mais resistente a choque/vibração que o [[concepts/hd-disco-rigido]].

## SATA vs. NVMe

| Tipo | Velocidade | Uso |
|---|---|---|
| **SATA** | até ~600 MB/s | mais lento, ainda muito acima de HD |
| **NVMe** | vários GB/s | alto desempenho (jogos, edição de vídeo) |

> **Cuidado com form factor:** NVMe tem formatos físicos diferentes — verifique a compatibilidade com o dispositivo antes de comprar.

## Trade-off

Mais rápido e resistente, mas custo/GB maior que HD. Capacidades típicas de 256/512 GB (1–2 TB+ em setups avançados). Em [[concepts/storage-tiering]] ocupa a camada *hot*. Compartilha a tecnologia flash com [[concepts/memoria-flash]], pen drive e cartão de memória. A migração de HD para SSD marcou sistemas de arquivos modernos como o [[concepts/apfs]].

## Key Sources

- [[wiki/sources/tipos-de-armazenamento-de-dados]] — SSD (SATA/NVMe), NAND e form factors
