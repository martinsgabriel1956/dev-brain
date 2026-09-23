---
type: concept
title: "Disponibilidade no teorema CAP"
aliases: ["availability no CAP", "disponibilidade formal"]
date_created: 2026-09-23
date_updated: 2026-09-23
source_count: 1
tags: [system-design, sistemas-distribuidos, cap-theorem, disponibilidade]
skill: tech-mentor-system-design
status: draft
---

# Disponibilidade no teorema CAP

No senso comum, disponível = "o sistema está no ar". No [[wiki/concepts/cap-theorem]], significa: **todo nó que não caiu responde sem erro**, inclusive o nó isolado do lado errado da partição.

Consequências:
- Um sistema pode estar "disponível" no CAP e ainda assim entregar dados desatualizados ou divergentes, como o [[wiki/concepts/github-incidente-2018-particao-de-rede]] durante as 24 h.
- Um nó que recusa responder por não conseguir garantir consistência é "indisponível" no CAP, mesmo com o processo saudável.
- É diferente da noção operacional de [[wiki/concepts/alta-disponibilidade]] (uptime, SLA, failover).

## Key sources

- [[wiki/sources/github-2018-cap-pacelc-particao-video]]
