---
type: concept
title: "Virtualização"
aliases: ["virtualization", "virtualização de servidores"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [virtualizacao, mainframe, cloud, hypervisor, isolamento]
skill: tech-mentor-infra
status: stub
---

# Virtualização

Particionar e compartilhar os recursos de uma máquina física entre ambientes isolados. A fonte defende que a virtualização **não nasceu com a AWS**, e sim no [[wiki/concepts/mainframe]] ([[wiki/concepts/lpar|LPARs]]), onde compartilhamento e elasticidade de capacidade já existiam há décadas — cloud pública massificou o que o mainframe já fazia. [external] Origem histórica: VM/CP-67 da IBM, anos 1960 (https://en.wikipedia.org/wiki/Hardware_virtualization).

Consequência conceitual: numa instância de hyperscaler, o cliente compra **capacidade computacional, não hardware** — a mesma ideia do [[wiki/concepts/mainframe-as-a-service]]. Não confundir com [[wiki/concepts/memoria-virtual]] (mecanismo de SO distinto).

## Key Sources

- [[wiki/sources/mainframe-as-a-service-casas-bahia-sulamerica-kyndryl]] — virtualização e compartilhamento nasceram no mainframe
