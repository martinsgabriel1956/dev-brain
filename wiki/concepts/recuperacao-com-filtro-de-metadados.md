---
type: concept
title: "Recuperação com filtro de metadados"
aliases: ["similarity search com filtro", "filter expression", "busca vetorial filtrada"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [rag, retrieval, metadados, filtro, busca-semantica, top-k]
skill: tech-mentor-ai
status: draft
---

# Recuperação com filtro de metadados

Primeira etapa do [[wiki/concepts/rag-tres-etapas|RAG]]: uma busca por similaridade recebe **três parâmetros**:

- **query** em linguagem natural (como se fosse a pergunta no chat), convertida em embedding;
- **topK**: quantos resultados trazer ([[wiki/concepts/top-k-retrieval]]); 4 no exemplo;
- **filtro** sobre metadados gravados na [[wiki/concepts/indexacao-vetorial]].

No demo há duas buscas com filtros diferentes: **catálogo de produtos** (restringe a tipo/localização) e **histórico do consumidor** (restringe ao cliente). Retorno: lista de `Document`.

## Por quê

Similaridade sozinha não separa "o que é do catálogo" de "o que é deste usuário". O filtro faz isso, e também é o mecanismo de controle de acesso apontado em [[wiki/sources/rag-introducao-pipeline-completo]]. Complementos de produção (threshold, [[wiki/concepts/elegibilidade-de-chunks]], [[wiki/concepts/hybrid-search]]) não aparecem no vídeo.

Ver [[wiki/concepts/busca-semantica]] e [[wiki/concepts/vector-store]].

## Key Sources

- [[wiki/sources/rag-spring-ai-microagente-recomendacao-michele-brito]]
