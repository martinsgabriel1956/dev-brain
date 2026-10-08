---
type: concept
title: "Jev para Ramificar, LLM para Ler"
aliases: ["regra jev vs llm"]
date_created: 2026-10-08
date_updated: 2026-10-08
source_count: 1
tags: [ia, decisao, arquitetura, heuristica]
skill: tech-mentor-ai
status: draft
---

# Jev para ramificar, LLM para ler

Heurística do vídeo: se a saída da etapa é um **valor que o código usa para ramificar** (rotear, classificar, aprovar), use um [[wiki/concepts/system-one-model]] como o [[wiki/entities/jev]]; se é **texto que uma pessoa vai ler**, use um LLM. Em agentes: LLM no raciocínio aberto; decisões como "chamo a ferramenta?" ([[wiki/concepts/tool-call]], [[wiki/concepts/agente-ia]]) viram perguntas tipadas. Parente de roteamento por custo/complexidade em [[wiki/concepts/cascade-pattern-llm]].

## Key sources
- [[wiki/sources/jev-typesafe-ai-system-one-model-decisoes-tipadas-codigo-fonte-tv]]
