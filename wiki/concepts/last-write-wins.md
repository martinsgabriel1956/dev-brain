---
type: concept
title: "Last Write Wins (LWW)"
aliases: ["lww", "ultima escrita vence"]
date_created: 2026-09-04
date_updated: 2026-09-04
source_count: 2
tags: [lww, conflict-resolution, local-first, crdt, sistemas-distribuidos]
skill: tech-mentor-system-design
status: stub
---

# Last Write Wins (LWW)

**Estratégia de resolução de conflito em sistemas de réplicas: quando duas escritas concorrentes chegam para o mesmo dado, a mais recente (por timestamp) sobrescreve as demais.**

Surge tipicamente em arquiteturas [[wiki/concepts/local-first]], onde múltiplas réplicas (ex.: notebook e celular) podem editar o mesmo dado offline e depois convergir — alguma regra precisa decidir o que sobra quando duas edições concorrentes se encontram.

## Tradeoff

- **A favor**: é a estratégia mais simples de implementar, geralmente a primeira escolhida.
- **Contra**: perda silenciosa de dados — a escrita vencedora sobrescreve alterações anteriores sem aviso, sem merge, sem detecção de conflito para o usuário.

## Alternativa

[[wiki/concepts/crdt]] resolve o mesmo problema com convergência matemática (comutatividade, associatividade, idempotência das operações de merge), evitando a perda de dados do LWW ao custo de maior complexidade de implementação.

## Key sources

- [[wiki/sources/local-first-vs-offline-first]]
- [[wiki/sources/vector-clocks]] — já citava LWW como "a resolução mais simples mas descarta dados", sem página própria até esta ingestão
