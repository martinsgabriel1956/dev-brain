---
type: concept
title: "AHCI (Advanced Host Controller Interface)"
aliases: ["ahci"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_count: 1
tags: [storage, protocolo, sata, hardware]
skill: cs-fundamentals
status: draft
---

# AHCI (Advanced Host Controller Interface)

Protocolo de comunicação do SATA, criado para discos rígidos e reaproveitado em SSDs. Suporta **uma fila de até 32 comandos**: suficiente para HD mecânico, gargalo para flash capaz de milhares de requisições paralelas (analogia: supermercado com um caixa). Latência ~30 µs citada contra ~10 µs do [[wiki/concepts/nvme]]. Todo [[wiki/concepts/ssd-sata]] usa AHCI. Contexto de SO/storage: `storage-filesystems.md` `[skill: cs-fundamentals]`.

## Key sources

- [[wiki/sources/tipos-de-ssd-sata-ahci-m2-pci-express-nvme-explicados]]
