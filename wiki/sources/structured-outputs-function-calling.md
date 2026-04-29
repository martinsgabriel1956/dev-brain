---
type: source
title: "Structured Outputs & Function Calling"
aliases: ["structured outputs", "function calling", "tool use", "json mode", "pydantic llm"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/structured-outputs-function-calling.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [structured-outputs, function-calling, tool-use, pydantic, zod, json-schema, instructor, constrained-decoding, parallel-tools, idempotencia]
skill: tech-mentor-ai
status: stable
---

## TL;DR

Structured Outputs garantem schema válido sem parsing frágil de texto livre. OpenAI: `response_format` com schema Pydantic. Claude: tool use forçado com `tool_choice`. Instructor library abstrai sobre qualquer LLM com retry automático. Para agentes: function calling em loop (LLM chama tool → observa resultado → decide próximo passo).

## Key Claims

**Claim:** JSON mode não garante schema — apenas JSON válido. Structured Outputs garante o schema.
**Evidence:** JSON mode pode retornar `{"name": null}` quando o campo é obrigatório. Structured Outputs com Pydantic/Zod garante que o JSON respeita o schema definido. Para extração crítica em produção, use Structured Outputs ou retry com validação de schema.
**Confidence:** alta

**Claim:** Retry com validação de schema é o fallback universal — cobre modelos sem Structured Outputs nativos.
**Evidence:** Tenta 3× com prompt progressivamente mais explícito se o schema falhar. Funciona com qualquer modelo (open-weight incluído). Instructor library implementa isso automaticamente com backoff e injection do erro de validação no prompt de retry.
**Confidence:** alta

**Claim:** Parallel Tool Calls reduzem latência em 50–70% quando tools são independentes.
**Evidence:** Claude e GPT-4o suportam multiple tool calls em uma resposta. Tools independentes rodam em Promise.all. Tool com dependência de resultado anterior deve ser sequencial. Identificar dependências no design das tools.
**Confidence:** alta

**Claim:** Tools devem ser idempotentes por design para suportar retry seguro.
**Evidence:** Agente pode fazer retry de tool call após falha. Se a tool não é idempotente (cria recurso duplicado, debita duas vezes), retry gera estado inconsistente. Idempotência via chave de idempotência ou check de existência antes de criar.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/structured-outputs]]
- [[concepts/function-calling]]
- [[concepts/tool-use-agents]]
- [[concepts/idempotencia]]
- [[concepts/parallel-tool-calls]]

## Open Questions

- Constrained decoding (Outlines) — qual o overhead de latência em GPU para compilação do grammar?
- Quando usar Instructor vs implementação própria de retry? Em quais casos o overhead do Instructor não vale?
