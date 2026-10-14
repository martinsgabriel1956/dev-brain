---
type: concept
title: "Aritmética de Vetores Semânticos"
aliases: ["rei menos homem mais mulher", "analogia de embeddings", "direções semânticas"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [embeddings, intuicao, espaco-latente, algebra-linear]
skill: tech-mentor-ai
status: draft
---

# Aritmética de Vetores Semânticos

Propriedade do espaço de embeddings em que **relações de significado viram deslocamentos (direções)**: vetor(rei) − vetor(homem) + vetor(mulher) ≈ vetor(rainha). No exemplo 3D do vídeo: rei (2, 1.3, 0) − homem (0, 0.5, 0) + mulher (0, 0.1, 0.1) = (2, 0.9, 0.1), próximo de "rainha".

## Ponto-chave

O significado não está em cada dimensão isolada (não há um eixo "masculinidade"), mas nas **direções** do espaço; modelos reais usam milhares de dimensões (3072 no [[wiki/entities/gemini-embedding-2]]). Valores do exemplo são didáticos/inventados e a analogia é aproximada, não exata (confiança: alta como intuição; [external] o resultado clássico vem de word embeddings).

Base de por que [[wiki/concepts/similaridade-de-cosseno]] e [[wiki/concepts/busca-semantica]] funcionam. Ver [[wiki/concepts/embedding-vectors]].

## Key sources

- [[wiki/sources/gemini-embedding-2-embedding-multimodal-google]]
