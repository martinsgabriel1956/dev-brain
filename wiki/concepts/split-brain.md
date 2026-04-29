---
type: concept
title: "Split-Brain"
aliases: ["split brain", "partição de rede", "cérebro dividido"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [sistemas-distribuidos, consistencia, partição, split-brain, cap-theorem]
skill: tech-mentor-system-design
status: stub
---

# Split-Brain

Cenário onde uma partição de rede divide o cluster em dois grupos que tomam decisões conflitantes de forma independente — resultando em inconsistência.

## Exemplo com 3PC

```
Coordinator + Participant A  ←──✗──→  Participant B

A: viu PreCommit de todos → decide COMMIT
B: isolado, timeout       → decide ABORT
→ A commitou, B abortou — estado inconsistente
```

## Por que Acontece

[[concepts/three-phase-commit]] e [[concepts/two-phase-commit]] não distinguem "coordinator caiu" de "coordinator está particionado". Em ambos os casos, o participant fica sem resposta — e pode tomar a decisão errada.

## Como Resolver

Algoritmos com **quorum**: [[concepts/raft-paxos]]. Uma decisão só avança se a maioria (quorum) dos nós concordar. Partição que isola minoria não avança — evita split-brain.

## Key Sources

- [[sources/3pc]]
