---
type: concept
title: "Fita Magnética (LTO)"
aliases: ["fita magnética", "magnetic tape", "LTO", "tape backup", "cartucho de fita"]
date_created: 2026-08-13
date_updated: 2026-08-13
source_count: 1
tags: [storage, hardware, magnetico, fita, lto, backup, arquivamento, cold-storage, cs-fundamentals]
skill: tech-mentor-data
status: stub
---

# Fita Magnética (LTO)

Meio de armazenamento que grava dados em uma fita de plástico magnetizada. Considerada "ultrapassada", mas **ainda em uso por grandes empresas ([[wiki/entities/ibm|IBM]]), governos e data centers** para backup de longo prazo — porque vence em eixos que o SSD não cobre.

## Por que sobrevive

- **Barata** e de **alta capacidade** — cartuchos LTO modernos guardam vários TB.
- **Durável:** 30+ anos.
- **Segura:** fica **offline** (fora da rede), então é menos vulnerável a invasão/ransomware — o argumento central do air gap.

## Trade-off: acesso sequencial

Dados são lidos **na ordem em que foram gravados** — sem acesso aleatório rápido. Isso a torna lenta para uso interativo, mas ideal para arquivamento de grande volume, onde a leitura é rara. É o equivalente físico da camada *cold* em [[concepts/storage-tiering]] (análogo ao S3 Glacier). Compartilha o princípio magnético com o [[concepts/hd-disco-rigido]] e o [[concepts/disquete]].

## Key Sources

- [[wiki/sources/tipos-de-armazenamento-de-dados]] — fita como cold storage barato, durável e offline
