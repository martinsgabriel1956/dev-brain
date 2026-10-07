---
type: concept
title: "Seleção de Memória e Tools por Turno (Select)"
aliases: ["select", "filtro de memória", "tool selection dinâmica"]
date_created: 2026-10-07
date_updated: 2026-10-07
source_count: 1
tags: [context-engineering, memoria, tools, agentes, rag]
skill: tech-mentor-ai
status: draft
---

# Seleção de Memória e Tools por Turno (Select)

## Memória: três filtros na leitura

- **Janela de tempo** (horas): só memórias recentes.
- **Importância** 0–1, atribuída pelo LLM na escrita.
- **Meia-vida** (ex.: 72 h): a importância cai pela metade a cada período (1 → 0,5 → 0,25). Mesma lógica de envelhecimento que combate [[wiki/concepts/memory-rot]] `[inferência]`.
- Alternativa: RAG ou palavras-chave. A memória **não é fonte completa da verdade** — sempre se filtra.

## Tools: lista dinâmica por turno

Mapear palavras-chave da **última mensagem do usuário** para domínios e expor só as tools desse domínio (ex.: "traduzir texto" some para um agente SRE). Reduz decisões do agente ([[wiki/concepts/superficie-probabilistica-do-agente]]). Ver [[wiki/concepts/tool-use-agents]]. Limite `[inferência]`: palavra-chave simples falha se a pergunta não contiver o termo.

Parte do [[wiki/concepts/write-select-compress-isolate]].

## Key sources

- [[wiki/sources/engenharia-de-contexto-write-select-compress-isolate-felipe-fagundes]]
