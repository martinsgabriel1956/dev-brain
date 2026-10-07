---
type: concept
title: "Escrever Memória Fora da Janela (Write)"
aliases: ["write", "memória externa de agente"]
date_created: 2026-10-07
date_updated: 2026-10-07
source_count: 1
tags: [context-engineering, memoria, agentes, langchain]
skill: tech-mentor-ai
status: draft
---

# Escrever Memória Fora da Janela (Write)

Em vez de apagar contexto sem volta, **persistir** o que importa ou é grande num store externo, organizado por **namespace** (como pasta), **id** e conteúdo (demo com `store.put`, [[wiki/entities/langchain]]). A informação sai da janela mas não se perde. Só vale a pena com recuperação filtrada: [[wiki/concepts/selecao-de-memoria-e-tools-por-turno]].

Tipos de memória: [[wiki/concepts/tipos-de-memoria-de-agente]]. Comparar com [[wiki/concepts/memoria-de-longo-prazo-ia]] (plano em `.md`) e [[wiki/concepts/agent-memory-tres-camadas]]. Exemplo da demo: o diagnóstico de cada serviço foi salvo e o resumo final o leu da memória, sem reler logs. Risco: acúmulo sem curadoria ([[wiki/concepts/memory-rot]]).

## Key sources

- [[wiki/sources/engenharia-de-contexto-write-select-compress-isolate-felipe-fagundes]]
