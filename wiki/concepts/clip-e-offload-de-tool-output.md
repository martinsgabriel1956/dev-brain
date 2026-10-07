---
type: concept
title: "Clip e Offload de Tool Output"
aliases: ["clipar e offload", "compress de tool result"]
date_created: 2026-10-07
date_updated: 2026-10-07
source_count: 1
tags: [context-engineering, compressao, tokens, logs, agentes]
skill: tech-mentor-ai
status: draft
---

# Clip e Offload de Tool Output

Camada de **Compress** em duas partes ([[wiki/sources/engenharia-de-contexto-write-select-compress-isolate-felipe-fagundes]]):

1. **Clip + offload**: se um resultado passa de um limite (demo: **1.200 tokens**), o original completo vai para memória ([[wiki/concepts/escrever-memoria-fora-da-janela]]) e o contexto mantém só o sinal (demo: últimas linhas com `error`/`warn` de logs).
2. **Sumarização**: ao chegar a **3.500 tokens** de conversa, resumir, opcionalmente com system prompt próprio que define o que preservar. Ver [[wiki/concepts/context-compaction]].

Diferença de truncar: nada é excluído, apenas retirado da janela. Limites escolhidos pelo autor, a adaptar por aplicação; o corte de "últimas linhas" perde o que veio antes do erro `[inferência]`.

## Key sources

- [[wiki/sources/engenharia-de-contexto-write-select-compress-isolate-felipe-fagundes]]
