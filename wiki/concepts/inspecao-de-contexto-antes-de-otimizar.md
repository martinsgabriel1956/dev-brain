---
type: concept
title: "Inspeção de Contexto Antes de Otimizar"
aliases: ["context inspector", "medir o contexto"]
date_created: 2026-10-07
date_updated: 2026-10-07
source_count: 1
tags: [context-engineering, observabilidade, tokens, agentes]
skill: tech-mentor-ai
status: stub
---

# Inspeção de Contexto Antes de Otimizar

Regra de método: **engenharia de contexto começa na análise**. Instrumentar cada chamada ao LLM para registrar (1) nº de mensagens, (2) estimativa de tokens, (3) lista de tools disponíveis no turno. Só então decidir o que cortar. Na demo de [[wiki/sources/engenharia-de-contexto-write-select-compress-isolate-felipe-fagundes]], foi isso que revelou ferramentas inúteis repetidas em todo turno e o salto para 8.339 tokens.

Análogo manual no [[wiki/entities/claude-code]]: `/context` ([[wiki/concepts/context-compaction]]). Parte do [[wiki/concepts/write-select-compress-isolate]].

## Key sources

- [[wiki/sources/engenharia-de-contexto-write-select-compress-isolate-felipe-fagundes]]
