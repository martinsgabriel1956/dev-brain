---
type: concept
title: "NVMe (Non-Volatile Memory Express)"
aliases: ["nvme", "nvm express"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_count: 1
tags: [storage, protocolo, ssd, nvme, hardware]
skill: cs-fundamentals
status: draft
---

# NVMe (Non-Volatile Memory Express)

Protocolo criado do zero para SSDs/flash, sobre [[wiki/concepts/pci-express]]. Suporta até **64.000 filas × 64.000 comandos** (vs. 1 × 32 do [[wiki/concepts/ahci]]) e latência menor (~10 µs vs. ~30 µs, números do vídeo, não verificados). Efeito: jogos e arquivos grandes carregam em segundos, multitarefa fluida; IOPS escala com a profundidade de fila, mas a latência não melhora com isso `[skill: cs-fundamentals — storage-filesystems.md]`. Padrão dos SSDs modernos de alta velocidade; comum no formato [[wiki/concepts/m2-formato-fisico|M.2]]. Ver [[wiki/concepts/ssd]].

## Key sources

- [[wiki/sources/tipos-de-ssd-sata-ahci-m2-pci-express-nvme-explicados]]
