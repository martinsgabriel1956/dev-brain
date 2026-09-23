---
type: concept
title: "Pacelc"
aliases: []
date_created: 2026-09-22
date_updated: 2026-09-23
source_count: 3
tags: [pacelc, system-design, cap-theorem, latencia, consistencia]
skill: tech-mentor-system-design
status: draft
---

# PACELC

Extensão do [[wiki/concepts/cap-theorem]]: se há **P**artição, escolha **A** ou **C**; **E**lse (sem partição), escolha **L**atência ou **C**onsistência. Não invalida o CAP, acrescenta uma camada. Como partições são raras, o trade-off latência vs. consistência é o que se paga **na maior parte do tempo** ([[wiki/concepts/custo-da-leitura-forte-vs-local]]).

Base intuitiva: duas falácias, "a rede é confiável" e "a latência é zero" ([[wiki/concepts/falacias-da-computacao-distribuida]]).

[external] Formulado por Daniel Abadi; não verificado nesta sessão.

## Key sources

- [[wiki/sources/github-2018-cap-pacelc-particao-video]]
- [[wiki/sources/cap-pacelc-consistencia]]
- [[wiki/sources/cap-theorem]]
