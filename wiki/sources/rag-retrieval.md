---
type: source
title: "RAG & Retrieval"
aliases: ["rag", "retrieval augmented generation", "embeddings", "vector store", "hybrid search", "reranking"]
date_created: 2026-04-23
date_updated: 2026-08-26
source_file: /home/nemomartins/Documentos/new/dev-study/raw/rag-retrieval.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 3
tags: [rag, retrieval, embeddings, vector-store, chunking, hybrid-search, reranking, hyde, contextual-retrieval, graphrag, agentic-rag, ragas, hnsw]
skill: tech-mentor-ai
status: stable
---

## TL;DR

RAG injeta contexto relevante no prompt para reduzir alucinações e manter conhecimento atualizado. Pipeline: chunking → embedding → vector store → busca → prompt + LLM. Chunking é o gargalo de qualidade. Hybrid Search (vetorial + BM25) é o padrão de produção. Re-ranking melhora precisão pós-busca. RAGAS para avaliação.

## Key Claims

**Claim:** Chunking é o fundamento do recall — a maioria das falhas de RAG começa aqui.
**Evidence:** Chunk muito grande = embedding diluído, retrieval impreciso. Chunk muito pequeno = sem contexto suficiente para responder. Sweet spot: 512–1024 tokens com 10–20% overlap. Chunking semântico (por parágrafo ou seção) supera chunking por caracteres fixos em docs técnicos.
**Confidence:** alta

**Claim:** Hybrid Search (vetorial + BM25) é o padrão de produção — superior a cada técnica isolada.
**Evidence:** Vetorial captura semântica (sinônimos, paráfrases). BM25 captura correspondência exata (nomes próprios, siglas, termos técnicos). RRF (Reciprocal Rank Fusion) combina os rankings sem precisar calibrar pesos. Melhora recall em 15–25% vs pure-vector.
**Confidence:** alta

**Claim:** Re-ranking com CrossEncoder melhora precisão Top-K sem custo de re-embedding.
**Evidence:** Retrieval retorna Top-50. CrossEncoder re-ranqueia com modelo mais preciso (mas mais lento). Top-5 final tem 20–30% mais relevância que Top-5 direto do retrieval. BGE-reranker e Cohere Rerank são as opções principais.
**Confidence:** alta

**Claim:** HyDE (Hypothetical Document Embeddings) resolve queries complexas que não casam com documentos diretamente.
**Evidence:** Em vez de embedar a query, gera um documento hipotético que responderia a query, depois embeda esse documento. A distribuição do embedding de um doc hipotético é mais próxima dos docs reais do que a query crua.
**Confidence:** média-alta

**Claim:** Contextual Retrieval (Anthropic) reduz retrieval failures em 49% ao adicionar contexto do documento a cada chunk.
**Evidence:** Antes de indexar, prefixar cada chunk com "Este trecho faz parte de [documento X] que trata de [contexto Y]". Custo: 1 LLM call por chunk no momento de indexação. Melhora significativa em bases com muitos documentos similares.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/rag-retrieval]]
- [[concepts/chunking]]
- [[concepts/hybrid-search]]
- [[concepts/reranking]]
- [[concepts/hyde]]
- [[concepts/contextual-retrieval]]
- [[concepts/graphrag]]
- [[concepts/hnsw]]

## Key Sources

- [[wiki/sources/porque-nunca-confiar-em-llm-alucinacao]] — reforça RAG como mitigação de [[wiki/concepts/alucinacao-llm]], mas explicita o limite: RAG melhora eficiência sem chegar a "hallucination zero", pois o modelo ainda pode ignorar ou distorcer o documento injetado no contexto.
- [[wiki/sources/harness-explicado-function-calling-hag-evals]] — relato pessoal de um pipeline RAG corporativo (chunking → vector DB → busca KNN/BM25 → prompt restrito aos documentos) construído antes da terminologia atual (hybrid search, RAGAS) existir; mesma arquitetura descrita de forma informal.
- [[wiki/sources/rag-introducao-pipeline-completo]] — versão introdutória/pedagógica do mesmo tema (Full Cycle): pipeline básico de ingestão/consulta, chunking, metadados e o conceito de "chunks elegíveis" com threshold de confiança; sem contradição, granularidade menor que esta fonte.

## Open Questions

- Qual chunk size é ideal para código fonte vs documentação vs transcrições de reunião?
- GraphRAG tem custo de construção alto — quando o grafo de conhecimento justifica vs hybrid search simples?
