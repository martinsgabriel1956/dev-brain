---
type: concept
title: "RAG em Escala — Além de Buscar e Injetar no Contexto"
aliases: ["rag arquitetura", "retrieval augmented generation avancado", "rag em producao"]
date_created: 2026-08-14
date_updated: 2026-08-14
source_count: 1
tags: [rag, retrieval-augmented-generation, embeddings, banco-vetorial, arquitetura, versionamento]
skill: tech-mentor-ai
status: stub
---

# RAG em Escala — Além de Buscar e Injetar no Contexto

A percepção comum de RAG (Retrieval Augmented Generation) — "buscar num banco de dados vetorial e trazer o dado para o contexto" — está correta, mas incompleta. Trazer informação **acurada** de verdade em produção e em escala exige lidar com:

- **Metadado** — de onde veio o dado, quando foi criado/atualizado, nível de confiança
- **Estruturação** — como o documento é fatiado (chunking) antes de virar embedding
- **Tipos de documento** — tratar PDF, código, transcrição e planilha como fontes com necessidades de parsing diferentes
- **Fontes** — rastreabilidade de qual sistema/documento originou o trecho recuperado
- **Versões e compatibilidade de embeddings** — trocar de provider de modelo de embedding pode invalidar o índice vetorial existente; embeddings de modelos diferentes não são diretamente comparáveis
- **Invalidação** — quando o documento-fonte muda, o embedding correspondente precisa ser recalculado
- **Sincronização** — manter o índice vetorial atualizado em relação à fonte de verdade (banco de dados, CMS, wiki interna)

## Bancos Vetoriais

Bancos de dados vetoriais fazem consulta por proximidade/similaridade de embeddings. Alguns bancos tradicionais (ex.: [[wiki/concepts/redis|Redis]]) oferecem suporte a vetor, funcionando como uma camada adicional de cache/busca em vez de exigir um banco vetorial dedicado. Cloud providers oferecem RAG "pronto para uso" combinando modelo + banco vetorial gerenciado (ex.: Vertex AI da Google).

## Relação com Outros Conceitos

- [[wiki/concepts/cache]] — cache de contexto/embeddings é a otimização de custo/latência mais citada para pipelines de RAG.
- [[wiki/concepts/context-engineering-harness]] — RAG é um dos mecanismos concretos de trazer contexto real-time (em vez de só documentação estática) para o modelo.
- [[wiki/concepts/observabilidade]] — rastrear qual chunk/fonte foi usado numa resposta depende da mesma disciplina de tracing aplicada a chamadas de LLM.

## Key Sources

- [[wiki/sources/8-pontos-arquitetura-de-software-na-era-da-ia]] — RAG citado como ponto de system design com IA, com a ressalva de que a complexidade real está em metadado, versionamento, invalidação e sincronização, não na busca vetorial em si
