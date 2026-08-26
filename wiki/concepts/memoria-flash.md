---
type: concept
title: "Memória Flash (NAND)"
aliases: ["memória flash", "flash memory", "NAND", "célula NAND"]
date_created: 2026-08-13
date_updated: 2026-08-26
source_count: 2
tags: [storage, hardware, flash, nand, cs-fundamentals]
skill: tech-mentor-data
status: stub
---

# Memória Flash (NAND)

Memória de estado sólido não volátil que retém dados sem energia, gravando-os em **células NAND**. É o substrato comum de três mídias que parecem diferentes mas são a mesma tecnologia:

- [[concepts/ssd]] — flash como disco interno de alta performance
- Pen drive (flash drive) — flash portátil via USB
- Cartão de memória (SD/microSD) — flash para câmeras, smartphones, consoles

## Por que importa

Sem partes móveis → acesso eletrônico rápido, resistência a choque e vibração, e vida útil maior que mídias mecânicas como o [[concepts/hd-disco-rigido]]. A velocidade final depende da **interface**, não só do chip: USB 2.0/3.0/3.1 no pen drive, SATA/NVMe no SSD, classe de velocidade no cartão.

## Flash vs. RAM

Flash é **não volátil** (retém dado sem energia) mas ordens de magnitude mais lenta que [[wiki/concepts/memoria-ram|RAM]] — por isso o SO nunca executa código diretamente da flash, sempre carrega para a RAM primeiro. É essa diferença de latência (RAM ~dezenas/centenas de ns, flash/SSD ~dezenas/centenas de µs) que torna [[wiki/concepts/swap|swap]] tão custoso: mover páginas "frias" de RAM para uma mídia flash ainda é ordens de magnitude mais lento que mantê-las em RAM, mesmo sendo mais rápido que HD mecânico.

## Key Sources

- [[wiki/sources/tipos-de-armazenamento-de-dados]] — NAND como base comum de SSD, pen drive e cartão
- [[wiki/sources/evolucao-memorias-ram-ddr1-a-ddr5]] — contraste com RAM volátil (DDR), que é a camada de trabalho acima da flash na hierarquia de memória
