---
type: concept
title: "Indexação vetorial (fase offline do RAG)"
aliases: ["indexação RAG", "ingestão de documentos RAG", "indexar no vector store"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [rag, indexacao, embeddings, vector-store, chunking, metadados]
skill: tech-mentor-ai
status: draft
---

# Indexação vetorial

Preparação da base antes de qualquer consulta [[wiki/concepts/rag-tres-etapas|RAG]]: transformar dados próprios em registros pesquisáveis por similaridade.

## Passos

1. **Escolher o que indexar:** regras de negócio/políticas, catálogo de produtos, histórico de pedidos.
2. **[[wiki/concepts/chunking]]:** quebrar em trechos.
3. **Escrever o texto em linguagem natural**, próximo de como a pergunta será feita (nome, localização, categoria, descrição). É o texto que vira embedding, então a redação importa.
4. **Embedding:** converter o texto em vetor com um modelo de embedding (OpenAI, Gemini etc.).
5. **Gravar** no [[wiki/concepts/vector-store]] com **id, conteúdo, metadados e embedding**.

## Metadados

Gravados já na indexação, viram filtros na consulta ([[wiki/concepts/recuperacao-com-filtro-de-metadados]]); no demo, separam "catálogo" de "histórico do cliente".

## Contínua, não só inicial

Com eventos, o agente indexa conforme chegam: novo produto entra no catálogo; nova order entra no histórico ([[wiki/concepts/microagente]]). Ligação com invalidação/sincronização: [[wiki/concepts/rag-arquitetura-avancada]].

## No Spring AI

`vectorStore.add(List<Document>)`; o embedding é gerado "por baixo dos panos" ([[wiki/entities/spring-ai]]).

## Key Sources

- [[wiki/sources/rag-spring-ai-microagente-recomendacao-michele-brito]]
