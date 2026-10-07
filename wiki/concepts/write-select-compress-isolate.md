---
type: concept
title: "Write, Select, Compress, Isolate"
aliases: ["wsci", "quatro estratégias de contexto", "write select compress isolate"]
date_created: 2026-10-07
date_updated: 2026-10-07
source_count: 1
tags: [context-engineering, agentes, tokens, memoria, subagentes]
skill: tech-mentor-ai
status: draft
---

# Write, Select, Compress, Isolate

## TL;DR

Quatro estratégias para controlar o que entra na [[wiki/concepts/janela-de-contexto]] de um agente, na formulação de [[wiki/entities/felipe-fagundes]] ([[wiki/sources/engenharia-de-contexto-write-select-compress-isolate-felipe-fagundes]]):

| Estratégia | Ideia | Página |
|---|---|---|
| **Write** | Salvar fora da janela o que precisa sobreviver (sem perder) | [[wiki/concepts/escrever-memoria-fora-da-janela]] |
| **Select** | Trazer de volta só o relevante (memórias e tools), com filtros | [[wiki/concepts/selecao-de-memoria-e-tools-por-turno]] |
| **Compress** | Manter o sinal, descartar o resto (sumarizar; clip + offload) | [[wiki/concepts/clip-e-offload-de-tool-output]], [[wiki/concepts/context-compaction]] |
| **Isolate** | Delegar tarefa pesada a subagente que devolve só um resumo | [[wiki/concepts/subagentes]] |

Pré-requisito: medir antes ([[wiki/concepts/inspecao-de-contexto-antes-de-otimizar]]). Objetivo final: reduzir ruído ([[wiki/concepts/superficie-probabilistica-do-agente]]), não só tokens.

## Como se combinam (demo do autor)

Write guarda o diagnóstico de cada serviço; Select recupera só essas linhas no resumo final e filtra as tools; Compress faz clip/offload dos logs grandes; Isolate manda o processamento dos logs para subagentes. Resultado na demo: último turno de 8.339 para 2.426 tokens.

## Nota

A nomenclatura em quatro verbos aparece em material público sobre context engineering `[external, não verificado: atribuição de origem não conferida]`; a fonte aqui não cita origem.

## Key sources

- [[wiki/sources/engenharia-de-contexto-write-select-compress-isolate-felipe-fagundes]]
