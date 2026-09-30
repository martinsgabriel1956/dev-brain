---
type: concept
title: "Mainframe as a Service (MaaS)"
aliases: ["maas", "zcloud", "mainframe na nuvem"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [mainframe, maas, cloud, kyndryl, zcloud, multitenancy, opex]
skill: tech-mentor-infra
status: stub
---

# Mainframe as a Service (MaaS)

Modelo em que a empresa **contrata capacidade de [[wiki/concepts/mainframe]] como serviço** de um provedor (ex.: [[wiki/entities/kyndryl]] com o zCloud) em vez de comprar/alugar e operar a máquina no data center próprio. O provedor mantém hardware, conectividade, segurança, DR/backup e boa parte dos especialistas (CICS, DB2, z/OS, storage, performance), e entrega ao cliente uma ou mais [[wiki/concepts/lpar|LPARs]] de um equipamento compartilhado com outros clientes ([[wiki/concepts/multi-tenancy|multitenant]]). O cliente não sabe em que máquina física seu workload roda — compra capacidade, não hardware.

## O que muda e o que não muda

- **Não muda:** os sistemas críticos (milhares de programas, milhões de linhas de [[wiki/concepts/cobol|COBOL]], DB2, CICS, JCL) seguem como estão — sem reescrita nem o risco dela.
- **Muda:** a forma de consumir a infraestrutura — de [[wiki/concepts/capex-vs-opex|CAPEX para OPEX]], com capacidade elástica no lugar de [[wiki/concepts/dimensionamento-para-o-pico|dimensionamento para o pico]], e com equipe de especialistas compartilhada entre clientes.

## Casos

[[wiki/entities/sulamerica]] (saúde, vida e previdência, 2023) e [[wiki/entities/casas-bahia]] (cerca de um ano depois, segundo a fonte). Ver [[wiki/concepts/cloud-como-modelo-de-consumo]].

## Ressalvas

Economia não quantificada na fonte; risco de dependência do provedor (cf. [[wiki/concepts/vendor-lock-in-cloud]]) não discutido. Ver Open Questions na fonte.

## Key Sources

- [[wiki/sources/mainframe-as-a-service-casas-bahia-sulamerica-kyndryl]] — define MaaS, mecanismo e casos Casas Bahia/SulAmérica
