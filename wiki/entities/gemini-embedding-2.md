---
type: entity
title: "Gemini Embedding 2"
aliases: ["Gemini Embedding 2", "embedding 2 do Gemini"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [gemini, google, embeddings, multimodal, produto]
skill: tech-mentor-ai
status: draft
---

# Gemini Embedding 2

Modelo de [[wiki/concepts/embedding-multimodal]] do [[wiki/entities/google]], lançado na semana do vídeo (outubro/2026, segundo a fonte), via API/Vertex.

- Modalidades: texto, imagens, vídeo, áudio, documentos (com [[wiki/concepts/ocr]]) num único espaço; 100+ idiomas, inclusive português.
- Limites por chamada: texto 8.192 tokens; 6 imagens; vídeo 120 s (MP4/MOV); PDF 6 páginas; áudio sem limite informado. Acima disso: [[wiki/concepts/chunking]].
- Até 3072 dimensões; menos via projeção ([[wiki/concepts/reducao-de-dimensoes-de-embedding]]).
- Desvantagens: [[wiki/concepts/custo-e-privacidade-de-embedding-via-api]].

Não testado pelo apresentador; números vêm da página do Google relatada no vídeo.

## Key sources

- [[wiki/sources/gemini-embedding-2-embedding-multimodal-google]]
