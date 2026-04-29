---
type: source
title: "Conway's Law"
aliases: ["conways law", "inverse conway maneuver", "team topologies"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/conways-law.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [conways-law, inverse-conway, team-topologies, stream-aligned, platform-team, enabling-team, cognitive-load]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

"Organizações produzem sistemas que espelham suas estruturas de comunicação" (Conway, 1967). Implicação prática: se você quer microsserviços independentes, organize times independentes. Inverse Conway Maneuver: deliberadamente redesenhar o time para obter a arquitetura desejada. Team Topologies formaliza isso em 4 tipos de time (Stream-aligned, Platform, Enabling, Complicated Subsystem).

## Key Claims

**Claim:** A lei de Conway não é apenas observação — é uma força ativa que molda arquitetura.
**Evidence:** Time de backend monolítico = tendência a API monolítica. Time com fronteiras de comunicação fraca entre domínios = serviços acoplados. Tentar impor arquitetura contra a estrutura do time é lutar contra a gravidade.
**Confidence:** alta

**Claim:** Inverse Conway Maneuver: design o time para obter a arquitetura desejada.
**Evidence:** Quer microsserviço de payments independente? Crie um time dedicado a payments com ownership completo. Não tente criar o microsserviço primeiro e depois encontrar quem cuida dele.
**Confidence:** alta

**Claim:** Team Topologies reduz carga cognitiva como objetivo principal — não é sobre autonomia.
**Evidence:** Stream-aligned teams precisam entregar valor sem fricção. Platform team existe para reduzir a carga cognitiva dos stream-aligned (IDP). Enabling team existe temporariamente para transferir capacidade. Quando um time tem carga cognitiva alta, produz acoplamento acidental.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/conways-law]]
- [[concepts/inverse-conway-maneuver]]
- [[concepts/team-topologies]]
- [[concepts/cognitive-load]]
- [[concepts/platform-engineering]]

## Open Questions

- Como aplicar Team Topologies em empresas pequenas (< 10 devs) sem overhead organizacional?
- Qual o sinal de que a carga cognitiva de um time está alta demais antes que a qualidade degrade?
