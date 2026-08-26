---
type: concept
title: "Chunking"
aliases: ["chunk", "divisão de documentos", "fatiamento de documentos"]
date_created: 2026-08-26
date_updated: 2026-08-26
source_count: 1
tags: [rag, chunking, embeddings, retrieval]
skill: tech-mentor-ai
status: stub
---

# Chunking

Processo de dividir um documento (markdown, PDF, planilha, transcrição etc.) em pedaços menores antes de gerar embeddings, para que uma busca vetorial não precise — nem consiga — trazer o documento inteiro como contexto. É o passo do pipeline de ingestão de [[wiki/concepts/rag-arquitetura-avancada|RAG]] que mais determina a qualidade do retrieval: chunk mal cortado gera busca ruim independente da qualidade do modelo de embedding ou do LLM usado depois.

## O problema central

Chunking não é uma unidade de busca 100% eficaz — cortar por tamanho fixo pode separar um pedaço do seu contexto original. Exemplo citado em [[wiki/sources/rag-introducao-pipeline-completo]]: a palavra "preço" aparece em vários lugares de uma base de conhecimento; um chunk isolado contendo só essa palavra pode ser recuperado para a pergunta errada, trazendo o preço de um produto que não é o perguntado.

## Cada chunk carrega

- **ID** — identificador único.
- **Texto cru** — o conteúdo do pedaço, salvo junto ao vetor (dado duplicado por design: vetor para busca, texto para uso no prompt).
- **Metadados** — origem, produto, tipo de documento, status de publicação — usados para filtrar antes/durante a busca vetorial.
- **Embedding** — a representação vetorial do texto, gerada por um modelo de embedding.

## Key Sources

- [[wiki/sources/rag-introducao-pipeline-completo]] — descrição do chunking como o fundamento do pipeline de ingestão, com exemplo de descontextualização por corte ruim
