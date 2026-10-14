---
type: concept
title: "Embedding Multimodal"
aliases: ["espaço de embedding unificado", "multimodal embedding", "cross-modal retrieval"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [embeddings, multimodal, busca-semantica, rag]
skill: tech-mentor-ai
status: draft
---

# Embedding Multimodal

Modelo de embedding que coloca **várias modalidades (texto, imagem, vídeo, áudio, documento) no mesmo espaço vetorial**, de modo que conteúdos de mesmo significado ficam próximos mesmo em mídias diferentes: foto, vídeo e som de um cachorro latindo e o texto "o cachorro está latindo" formam um cluster. Permite **busca cross-modal** (texto → imagem, áudio → imagem) com um único tipo de índice, e dispensa transcrever áudio para texto antes de indexar. Exemplo: [[wiki/entities/gemini-embedding-2]].

## Efeitos práticos

- **Pipeline unificado:** em vez de um modelo por modalidade + conversões, um só modelo e um só [[wiki/concepts/vector-store]]; troca-se complexidade por custo ([[wiki/concepts/custo-e-privacidade-de-embedding-via-api]]).
- **Vários vetores por item:** na indexação, um produto pode ter vetores de imagem e de metadados; a consulta é comparada com todos por [[wiki/concepts/similaridade-de-cosseno]].
- **Limites por chamada** forçam [[wiki/concepts/chunking]] de vídeos longos e PDFs grandes (um vetor por pedaço).
- Nem sempre é necessário: [[wiki/concepts/busca-visual-por-similaridade]] com CNN leve resolve casos só-imagem.

[skill: tech-mentor-ai] `embeddings-semantic-search.md` cobre alternativas anteriores (CLIP, ImageBind) para o mesmo objetivo; ver também [[wiki/concepts/embedding-vectors]] e [[wiki/concepts/busca-semantica]].

## Key sources

- [[wiki/sources/gemini-embedding-2-embedding-multimodal-google]]
