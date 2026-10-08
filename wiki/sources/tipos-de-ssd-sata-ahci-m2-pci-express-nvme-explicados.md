---
type: source
title: "Tipos de SSD explicados: SATA, AHCI, M.2, PCI Express e NVMe"
aliases: ["tipos de ssd", "sata vs nvme"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/tipos-de-ssd-sata-ahci-m2-pci-express-nvme-explicados.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-10-08
source_count: 0
tags: [storage, hardware, ssd, nvme, sata, pcie, ahci, m2, cs-fundamentals]
skill: cs-fundamentals
status: draft
---

# Tipos de SSD explicados: SATA, AHCI, M.2, PCI Express e NVMe

## TL;DR

"SSD" não diz nada sobre velocidade: ela depende de **três camadas independentes**: formato físico ([[wiki/concepts/m2-formato-fisico]]), barramento ([[wiki/concepts/ssd-sata]] ~550 MB/s vs. [[wiki/concepts/pci-express]] 3.0/4.0/5.0 ≈ 3.500/7.500/14.000 MB/s com 4 pistas) e protocolo ([[wiki/concepts/ahci]], 1 fila × 32 comandos, vs. [[wiki/concepts/nvme]], até 64.000 filas × 64.000 comandos). M.2 não implica NVMe nem rapidez; é preciso conferir se o drive é SATA ou NVMe.

## Key Claims

| Claim | Evidência | Confiança |
|---|---|---|
| SSD SATA satura em ~550 MB/s | Limite da interface SATA III (600 MB/s brutos, ~550 úteis) | Alta; confere com [[wiki/sources/tipos-de-armazenamento-de-dados]] (~600 MB/s) |
| AHCI: 1 fila, 32 comandos; NVMe: 64.000 filas × 64.000 comandos | Especificações AHCI/NVMe; coerente com `storage-filesystems.md` `[skill: cs-fundamentals]` | Alta |
| M.2 é só formato; pode ser SATA ou NVMe | Descrição do vídeo | Alta |
| PCIe x4: 3.5 / 7.5 / 14 GB/s (3.0/4.0/5.0) | Valores práticos arredondados (teórico 3.9/7.9/15.8) | Média-alta; arredondado |
| Latência AHCI ~30 µs → NVMe ~10 µs | Citada sem fonte | Baixa-média; ordem de grandeza plausível, número não verificado |
| Número de pistas PCIe é limitado e pode dividir banda | Argumento do vídeo | Alta |

## Entidades

[[wiki/entities/alura]] (patrocinadora; plano Pro, IA "Lu", Tech Guide).

## Conceitos

[[wiki/concepts/ssd-sata]], [[wiki/concepts/ahci]], [[wiki/concepts/m2-formato-fisico]], [[wiki/concepts/pci-express]], [[wiki/concepts/nvme]], [[wiki/concepts/ssd]], [[wiki/concepts/hd-disco-rigido]], [[wiki/concepts/memoria-flash]], [[wiki/concepts/storage-tiering]].

## Perguntas em aberto

- Canal não identificado; o vídeo remete a outro sobre tipos de armazenamento, provavelmente [[wiki/sources/tipos-de-armazenamento-de-dados]].
- Fonte não cobre durabilidade (TBW), controladora, DRAM cache ou QLC/TLC, que explicam por que dois NVMe do mesmo PCIe têm desempenhos distintos.
- "Lu" (ASR "Luri") e Alura: grafia incerta `[?]`.

## Citações

> "M.2 é apenas o formato físico."
> "Se o AHCI era um supermercado com um único caixa, o NVMe é como abrir mil caixas ao mesmo tempo."
