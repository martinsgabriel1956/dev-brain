---
type: concept
title: "Redução de Dimensões de Embedding"
aliases: ["projeção de embedding", "dimensões de embedding", "matryoshka embeddings"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [embeddings, dimensoes, custo, armazenamento]
skill: tech-mentor-ai
status: draft
---

# Redução de Dimensões de Embedding

Pedir ao modelo de embedding **menos dimensões** do que o máximo (ex.: metade ou um quarto de 3072). No [[wiki/entities/gemini-embedding-2]], segundo o vídeo, o modelo sempre calcula as 3072 e **projeta** para o tamanho pedido; o Google recomenda o máximo porque mais dimensões = mais informação, ao custo de mais armazenamento e busca mais pesada em [[wiki/concepts/vector-store]].

## Trade-off

Menos dimensões → menos memória/latência e menor recall. [skill: tech-mentor-ai] `embeddings-semantic-search.md` traz o padrão *Matryoshka Embeddings (MRL)* no `text-embedding-3-large` (3072 → 256 dims, ~12× menos storage, recall@10 de 0,92 → 0,81 no exemplo da skill); medir no próprio dataset. Não foi dito no vídeo que o Gemini use MRL. Ver [[wiki/concepts/embedding-vectors]].

## Key sources

- [[wiki/sources/gemini-embedding-2-embedding-multimodal-google]]
