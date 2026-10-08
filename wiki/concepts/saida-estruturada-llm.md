---
type: concept
title: "Saída Estruturada (Structured Output)"
aliases: ["structured output", "structured outputs", "output estruturado"]
date_created: 2026-09-30
date_updated: 2026-10-08
source_count: 2
tags: [llm, saida-estruturada, json-schema, zod, pydantic, sdk]
skill: tech-mentor-ai
status: draft
---

# Saída Estruturada (Structured Output)

## TL;DR

Em vez de receber texto livre, a aplicação define o **formato exato** da resposta do modelo (schema), e valida o retorno com uma biblioteca de schema. Descrito em [[wiki/sources/claude-code-dicas-worktrees-paralelismo-rotinas-sessoes-remotas-output-estruturado]] no contexto do SDK da [[wiki/entities/anthropic]].

## Fluxo descrito

1. Definir o schema com **Zod** (TypeScript) ou **Pydantic** (Python), por exemplo um `feature plan` com `feature name`, `summary`, `steps`.
2. Converter para **JSON Schema** e enviá-lo na request.
3. O modelo responde nesse formato.
4. Validar a resposta com a mesma biblioteca.

## Quando faz sentido

- **Sim:** aplicações e backends que consomem a resposta programaticamente, como orquestradores de agentes ou decomposição de tarefas complexas.
- **Pouco útil:** uso interativo local do [[wiki/entities/claude-code]] (opinião do autor).

## Complemento [skill: tech-mentor-ai]

A skill trata o tema em `references/ai/structured-outputs-function-calling.md`: o problema é que o formato livre varia entre chamadas e quebra o parsing; Pydantic/Zod fazem o papel de contrato tipado. Relaciona-se com function calling (ver [[wiki/concepts/tool-call]]) e com geração restrita por gramática. Não é afirmação da fonte.

## Key Sources

- [[wiki/sources/claude-code-dicas-worktrees-paralelismo-rotinas-sessoes-remotas-output-estruturado]]

- [[wiki/sources/jev-typesafe-ai-system-one-model-decisoes-tipadas-codigo-fonte-tv]] — alternativa: [[wiki/concepts/system-one-model]] devolve tipos nativos com confiança; ver [[wiki/concepts/zero-erro-de-schema-nao-e-correcao-semantica]]
