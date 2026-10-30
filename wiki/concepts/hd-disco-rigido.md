---
type: concept
title: "HD (Disco Rígido / HDD)"
aliases: ["HD", "HDD", "disco rígido", "hard disk drive", "disco magnético"]
date_created: 2026-08-13
date_updated: 2026-10-30
source_count: 3
tags: [storage, hardware, hdd, magnetico, cs-fundamentals]
skill: tech-mentor-data
status: stub
---

# HD (Disco Rígido / HDD)

Dispositivo de armazenamento tradicional que grava dados em **discos magnéticos giratórios** (pratos). Um braço atuador move uma cabeça de leitura/gravação sobre a superfície magnética para acessar as informações.

## Números

- **Capacidade:** 500 GB a 2 TB+ — melhor custo/GB para grande volume.
- **Velocidade:** medida em RPM. 5400/7200 RPM ≈ 100–160 MB/s; alto desempenho 10.000+ RPM.
- **Vida útil:** 3–5 anos.

## Trade-off

Barato e de alta capacidade, mas **tem partes mecânicas** — vulnerável a choque físico, superaquecimento e quedas de energia. É o oposto do [[wiki/concepts/ssd]] (rápido e sem partes móveis). Em [[wiki/concepts/storage-tiering]] ocupa a camada *warm*. O [[wiki/concepts/disquete]] e a [[wiki/concepts/fita-magnetica]] compartilham o mesmo princípio magnético.

## IBM RAMAC (1956)

[[wiki/sources/historia-do-computador-da-antikythera-ao-computador-quantico]]: o primeiro disco rígido foi o do IBM RAMAC 305, em 1956, com 50 discos magnéticos e ~5 MB. Na sequência do armazenamento: [[wiki/concepts/cartao-perfurado]] → fita magnética → disco → disquete → [[wiki/concepts/armazenamento-optico|óptico]] → nuvem.

## Key Sources

- [[wiki/sources/tipos-de-armazenamento-de-dados]] — HD como baseline de custo/capacidade vs. SSD
- [[wiki/sources/tipos-de-ssd-sata-ahci-m2-pci-express-nvme-explicados]]: SSD SATA reaproveitou portas e o protocolo [[wiki/concepts/ahci]], criado para HD

## Key sources (adição 2026-10-30)

- [[wiki/sources/historia-do-computador-da-antikythera-ao-computador-quantico]] — RAMAC 305 como primeiro HD (5 MB, 50 discos)
