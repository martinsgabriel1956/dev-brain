---
type: concept
title: "PCI Express (PCIe)"
aliases: ["pcie", "pci-e", "pci express"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_count: 1
tags: [storage, hardware, barramento, pcie]
skill: cs-fundamentals
status: draft
---

# PCI Express (PCIe)

Barramento de múltiplas **pistas (lanes)** paralelas entre dispositivos e processador, usado pelos SSDs mais rápidos. Com 4 pistas, valores aproximados: **3.0 ≈ 3.500 MB/s; 4.0 ≈ 7.500 MB/s; 5.0 ≈ 14.000 MB/s** (dobra a cada geração), contra ~550 MB/s do [[wiki/concepts/ssd-sata]]. Trade-offs: preço e consumo maiores; CPU e placa-mãe têm **número limitado de pistas**, e muitos dispositivos dividem banda. Normalmente carrega o protocolo [[wiki/concepts/nvme]]; encaixe físico comum: [[wiki/concepts/m2-formato-fisico|M.2]].

## Key sources

- [[wiki/sources/tipos-de-ssd-sata-ahci-m2-pci-express-nvme-explicados]]
