---
type: concept
title: "Hybrid Search"
aliases: ["busca híbrida", "busca híbrida em RAG", "semantic + keyword search"]
date_created: 2026-09-22
date_updated: 2026-09-29
source_count: 2
tags: [hybrid-search, rag, retrieval, busca-semantica, busca-textual, fusion]
skill: tech-mentor-ai
status: draft
---

# Hybrid Search

Busca que combina [[wiki/concepts/busca-semantica]] (significado, via embeddings) e [[wiki/concepts/busca-por-palavra-chave]] (termos exatos, ex.: [[wiki/concepts/bm25]]) para recuperar chunks em [[wiki/concepts/rag-como-ferramenta-de-busca|RAG]]. Uma cobre o que a outra perde.

## Por que existe

- Busca semântica sozinha falha com consultas de uma ou duas palavras: o vetor curto fica longe dos chunks (fatias de documento) e a busca conclui "nada significativo" ([[wiki/sources/rag-busca-hibrida-semantica-e-textual-ronald-hulk]]).
- Alargar o [[wiki/concepts/top-k-retrieval|top-K]] para compensar traz lixo, polui o contexto e piora custo e latência da resposta.
- [skill: tech-mentor-ai] BM25 costuma vencer embeddings em nomes próprios, siglas, códigos, versões e jargão preciso; embeddings vencem em paráfrase e conceito.

## Como funciona

1. A consulta roda **em paralelo** nas duas buscas.
2. Cada uma devolve seu ranking de chunks (as duas podem discordar).
3. Uma etapa de [[wiki/concepts/fusion-de-rankings|fusion]] consolida e rankeia.
4. Os melhores resultados vão ao agente, que gera a resposta. Opcionalmente há um passo de [[wiki/concepts/reranking]] [skill: tech-mentor-ai].

## Decisões que são suas

- **Peso** entre palavra-chave e semântica: depende da natureza do dado.
- **K** e limiar de significância.
- Ambos se definem **medindo o retrieval** (mudar peso, comparar, manter só o que melhora), não por intuição.

## Key sources

- [[wiki/sources/rag-busca-hibrida-semantica-e-textual-ronald-hulk]] — explicação com demo (busca por uma palavra achando a aula certa só pela palavra-chave) e o papel do fusion
- [[wiki/sources/rag-retrieval]]
