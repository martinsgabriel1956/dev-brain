---
type: concept
title: "Needle in a Haystack"
aliases: ["agulha no palheiro", "NIAH"]
date_created: 2026-10-09
date_updated: 2026-10-09
source_count: 1
tags: [ai, long-context, benchmark, recall]
skill: tech-mentor-ai
status: stub
---

## Definição

Teste de recuperação em contexto longo: esconde-se um fato (a "agulha") em qualquer posição de um documento enorme (o "palheiro") e pergunta-se por ele. [[wiki/concepts/transformer-architecture|Transformers]] se saem bem (atenção sobre tudo, custo alto); [[wiki/concepts/recurrent-neural-network|RNNs]] de memória fixa falham por esquecer. [[wiki/concepts/memory-caching-rnn]] busca fechar esse gap. Ver [[wiki/concepts/context-window]].

## Key Sources

- [[wiki/sources/google-nao-esta-perdendo-corrida-ia-memory-caching-gemini-live]]
