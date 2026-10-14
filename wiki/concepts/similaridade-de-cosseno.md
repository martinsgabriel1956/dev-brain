---
type: concept
title: "Similaridade de Cosseno"
aliases: ["cosine similarity", "distância de cosseno"]
date_created: 2026-09-29
date_updated: 2026-10-14
source_count: 2
tags: [embeddings, busca-semantica, similaridade, algebra-linear]
skill: tech-mentor-ai
status: stub
---

# Similaridade de Cosseno

Métrica que compara dois vetores pelo ângulo entre eles (quanto mais alinhados, mais similares). Na [[wiki/concepts/busca-semantica]], compara o embedding da pergunta com os embeddings dos chunks; os mais próximos formam o [[wiki/concepts/top-k-retrieval|top-K]].

A fonte ([[wiki/sources/rag-busca-hibrida-semantica-e-textual-ronald-hulk]]) só a nomeia como "a conta, no geral", e nota que o tema pede noção de álgebra linear. Sem detalhes de fórmula na fonte.

Ver [[wiki/concepts/embedding-vectors]] para o que os vetores representam.

## Key sources

- [[wiki/sources/rag-busca-hibrida-semantica-e-textual-ronald-hulk]]

## Adição (2026-10-14)

O vídeo afirma que o cosseno é a métrica normalmente usada; vale para vetores multimodais ([[wiki/concepts/embedding-multimodal]]) e para vetores de CNN ([[wiki/concepts/busca-visual-por-similaridade]]).

- [[wiki/sources/gemini-embedding-2-embedding-multimodal-google]] — cosseno (ou euclidiana) como métrica usual entre vetores de mídias distintas e em busca visual com CNN
