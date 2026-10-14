---
type: concept
title: "Custo e Privacidade de Embedding via API"
aliases: ["trade-off embedding proprietário", "enviar dados à API de embedding"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [embeddings, privacidade, custo, api, seguranca, lgpd]
skill: tech-mentor-ai
status: draft
---

# Custo e Privacidade de Embedding via API

Duas desvantagens de adotar um embedding proprietário como o [[wiki/entities/gemini-embedding-2]]:

1. **Custo por chamada** de API (vs. modelos open source separados, sem custo por chamada mas com mais pipeline para manter).
2. **Dados saem da empresa:** documentos precisam ser enviados à API do provedor. O apresentador suspeita que os termos autorizem uso para treino, mas **não os leu** (especulação; conferir os ToS). Para documentos sensíveis ele descarta o uso ("não dá para confiar nas big techs").

Relaciona-se a [[wiki/concepts/confidencialidade-de-dados-em-prompts-ia]] e [[wiki/concepts/lgpd]]. Em RAG, embeddings de documentos também vazam conteúdo ao provedor; alternativa: modelo de embedding self-hosted ([skill: tech-mentor-ai] cita BGE-M3, gratuito, em `embeddings-semantic-search.md`). Ver [[wiki/concepts/embedding-multimodal]].

## Key sources

- [[wiki/sources/gemini-embedding-2-embedding-multimodal-google]]
