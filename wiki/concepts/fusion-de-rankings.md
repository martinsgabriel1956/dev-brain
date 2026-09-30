---
type: concept
title: "Fusion de Rankings"
aliases: ["fusion", "rank fusion", "RRF", "reciprocal rank fusion"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [rag, hybrid-search, fusion, ranking, retrieval]
skill: tech-mentor-ai
status: draft
---

# Fusion de Rankings

Etapa da [[wiki/concepts/hybrid-search]] que recebe os resultados da [[wiki/concepts/busca-semantica]] e da [[wiki/concepts/busca-por-palavra-chave]], **desempata** as duas "opiniões" e produz um ranking único.

## Na fonte

- É um **critério que o engenheiro define**, não tecnologia externa.
- O critério inclui o **peso** de cada busca, conforme a natureza dos dados.
- Pesos se escolhem medindo o retrieval: mudar, comparar, manter o que melhora ([[wiki/sources/rag-busca-hibrida-semantica-e-textual-ronald-hulk]]).

## Técnicas conhecidas [skill: tech-mentor-ai]

- **Reciprocal Rank Fusion (RRF):** `score = Σ 1/(k + rank)`, k=60 funciona sem ajuste; usa só posições, não scores absolutos.
- **Combinação linear:** `α·bm25 + (1-α)·dense`; exige normalizar escalas e ajustar α por domínio.

A fonte não diz qual das duas a [[wiki/entities/rock-pro]] usa.

## Key sources

- [[wiki/sources/rag-busca-hibrida-semantica-e-textual-ronald-hulk]]
