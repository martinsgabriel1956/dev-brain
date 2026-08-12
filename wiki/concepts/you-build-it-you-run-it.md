---
type: concept
title: "You Build It, You Run It"
aliases: ["you build it you run it", "voce constroi voce opera", "ownership operacional", "team managed infrastructure"]
date_created: 2026-08-12
date_updated: 2026-08-12
source_count: 1
tags: [devops, platform-engineering, ownership, on-call, autonomia, aws]
skill: tech-mentor-infra
status: draft
---

# You Build It, You Run It

## TL;DR

Mantra operacional (origem Amazon/Werner Vogels, popularizado no movimento DevOps) que aparece no caso de plataformas de [[wiki/entities/evan-bottcher]] ([[wiki/sources/talk-about-platforms-evan-bottcher]]): **quem constrói um serviço também o opera** — deploy, monitoração e plantão (on-call). Fecha o loop entre decisão e consequência, gerando ownership real.

## Como surgiu no artigo

Na BigCo, os times fugiram da infra centralizada travada para a **AWS** (self-service real + fronteiras de responsabilidade claras), trazendo junto o *you build it, you run it*. Na WebBiz, "Team Managed Infrastructure" deu autonomia total — e responsabilização pelos deploys foi estabelecida rapidamente.

## Aplica-se aos dois lados da plataforma

Feito de forma ruim, um "time de plataforma" vira só mais um silo de DevOps. A divisão correta ([[plataforma-como-produto]]):

- **Times de aplicação** — constroem, fazem deploy, monitoram e ficam on-call por componentes de aplicação + a infra que provisionam;
- **Times de plataforma** — constroem, operam e ficam on-call pela plataforma e sua infra subjacente; idealmente **nem sabem** quais apps rodam em cima — respondem só pela disponibilidade do serviço de plataforma.

O princípio vale para os dois.

## DevOps não é um cargo

Citação de [[wiki/entities/phil-calcado]] no artigo: perdeu-se a batalha do "DevOps não é cargo/time/ferramentas". *You build it, you run it* é a prática cultural; virar "time de DevOps" isolado a trai.

## Relacionados

- [[plataforma-como-produto]] — a fronteira de responsabilidade
- [[autonomia-responsabilidade]] — o par autonomia + accountability
- [[sensible-defaults-paved-road]] — quem sai da estrada assume o custo de operar

## Key sources

- [[wiki/sources/talk-about-platforms-evan-bottcher]] — Evan Bottcher, *What I Talk About When I Talk About Platforms* (2018)
