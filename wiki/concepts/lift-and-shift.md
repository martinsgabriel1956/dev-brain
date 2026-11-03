---
type: concept
title: "Lift and Shift"
aliases: ["rehost", "rehosting", "migração lift and shift"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_count: 1
tags: [cloud, migracao, legado, infra]
skill: tech-mentor-infra
status: stub
---

# Lift and Shift

Estratégia de migração que leva a aplicação do ambiente tradicional para a nuvem sem reestruturá-la. A fonte a cita como uma das estratégias, sem detalhar, e aponta o caso típico: produto de prateleira não conteinerizado vai para máquina virtual. [[wiki/sources/utilizar-ou-nao-kubernetes-fluxo-de-decisao-cloud]]

A VM é o ambiente mais parecido com um data center. Você deixa de cuidar do hardware, mas não aproveita "todo o potencial" da nuvem. Ver [[wiki/concepts/virtualizacao]] e [[wiki/concepts/ec2]].

`[skill: tech-mentor-infra]` Nos 7Rs de migração (`cloud/cloud-agnostic.md`), corresponde a *Rehost*: pouco esforço e pouco benefício de nuvem. A sequência prática é Retire, Rehost rápido, Replatform iterativo e Refactor onde o retorno justifica.

## Key Sources

- [[wiki/sources/utilizar-ou-nao-kubernetes-fluxo-de-decisao-cloud]]
