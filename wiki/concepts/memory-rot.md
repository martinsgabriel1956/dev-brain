---
type: concept
title: "Memory Rot"
aliases: ["memória obsoleta", "apodrecimento de memória"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [memory-rot, memoria, agentes, harness, documentacao]
skill: tech-mentor-ai
status: stub
---

# Memory Rot

Quando a memória do agente (CLAUDE.md, notas, memórias persistidas) **envelhece e deixa de refletir o estado real do software**, passando a induzir erro em vez de evitá-lo. Termo usado em [[wiki/sources/pilares-desenvolvimento-com-ia-contrato-de-revisao-waves]] para explicar por que "lidar com memória é complexo": a memória serve para o agente não repetir o mesmo erro, mas precisa ser mantida.

## Lacunas

A fonte só **nomeia** o problema; não propõe mitigação. Práticas plausíveis (validar memórias contra o código antes de agir, expirar/atualizar entradas) são [inferência] — ver [[wiki/concepts/agent-memory-tres-camadas]], [[wiki/concepts/drift-detection]] e [[wiki/concepts/closed-loop-skill-learning]].

## Key sources

- [[wiki/sources/pilares-desenvolvimento-com-ia-contrato-de-revisao-waves]]
