---
type: source
title: "RAG — Introdução e Pipeline Completo"
aliases: ["rag introdução", "rag pipeline ingestão consulta", "rag não é agente"]
date_created: 2026-08-26
date_updated: 2026-08-26
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/rag-introducao-pipeline-completo.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-08-26
source_count: 0
tags: [rag, retrieval, embeddings, chunking, pgvector, metadados, agente-ia, full-cycle]
skill: tech-mentor-ai
status: stable
---

## TL;DR

Aula introdutória (estilo Full Cycle) explicando RAG do zero: o que significa cada letra da sigla, por que é preciso injetar contexto externo no prompt em vez de treinar um modelo específico, os dois pipelines (ingestão e consulta), o papel de chunking/embeddings/metadados, o conceito de "chunks elegíveis" com threshold de confiança, e a distinção explícita entre RAG e agente de IA. Complementa [[wiki/sources/rag-retrieval]] (mais técnico/avançado) com uma explicação pedagógica do "arroz com feijão" do RAG.

## Key Claims

**Claim:** RAG não é uma tecnologia, é um padrão arquitetural de pipeline — e não é sinônimo de agente de IA.
**Evidence:** RAG é definido como formato de pipeline (busca → contexto → geração), não como uma tool ou biblioteca específica. Um agente pode usar RAG como parte do seu processo, mas simplesmente chamar um modelo de LLM (mesmo com contexto injetado) é "uma consulta de API", não um agente — falta o loop de ação autônomo que caracteriza [[wiki/concepts/agente-ia]].
**Confidence:** alta

**Claim:** Existem dois pipelines distintos em todo sistema RAG: ingestão (fonte de dados → chunking → embedding → vector store) e consulta (query → embedding da query → busca por proximidade → prompt → LLM).
**Evidence:** Descrição passo a passo de ambos os fluxos, com Postgres + extensão PG Vector como exemplo concreto de vector store, citando que a extensão "aguenta bastante carga" e é viável em produção mesmo havendo bancos vetoriais dedicados.
**Confidence:** alta

**Claim:** Cada registro vetorial no banco carrega dado duplicado por design: o embedding (vetor) e o texto cru do chunk, mais metadados.
**Evidence:** Justificativa prática — o vetor sozinho não é legível/citável; o texto cru é o que efetivamente entra no prompt depois de recuperado. Os metadados (origem, produto, status de publicação, tipo de documento) existem para filtrar antes da busca vetorial e evitar varrer milhões de registros.
**Confidence:** média-alta (claim descritivo/prático, sem benchmark citado)

**Claim:** Metadados são o mecanismo de controle de acesso do RAG — sem eles, o pipeline pode vazar dado sensível (ex.: salário) para qualquer usuário que faça a pergunta certa.
**Evidence:** Exemplo dado: um RAG corporativo sem filtro de metadado pode retornar chunks contendo salário de funcionário para qualquer pessoa que pergunte. A aula trata isso como responsabilidade obrigatória da camada de aplicação/banco, não como detalhe opcional de qualidade.
**Confidence:** alta — ponto de segurança levantado sem citar incidente real, mas coerente com [[wiki/concepts/rag-arquitetura-avancada]] (metadado como parte do trabalho real de RAG em produção)

**Claim:** Busca vetorial + filtro retorna "chunks elegíveis", não necessariamente os chunks corretos — e recusar responder é preferível a responder com base em chunk não elegível.
**Evidence:** Exemplo numérico: de 10 chunks retornados pela busca, aplicando um threshold de confiança (ex.: 0,9 de 0 a 1), apenas 3 podem restar como elegíveis. Se nenhum for elegível, a resposta correta é admitir que não se tem a informação, evitando alucinação com contexto descontextualizado.
**Confidence:** alta — mesma lógica de "melhor recusar que alucinar" já documentada em [[wiki/concepts/alucinacao-llm]]

**Claim:** A dificuldade real de RAG não é buscar-e-injetar (fácil, dá pra fazer com um arquivo), mas garantir qualidade de resposta em produção — isso exige decisões arquiteturais, não só uma chamada de API.
**Evidence:** Contraste explícito entre um RAG de demo (funciona com um arquivo) e um RAG de produção (fonte de dados apurada, metadados bem organizados) — sem isso, "sai tudo errado" ou a busca varre milhões de registros por consulta.
**Confidence:** média-alta — afirmação qualitativa de instrutor, sem métrica, mas consistente com o resto da wiki sobre RAG avançado

## Entities & Concepts Touched

- [[wiki/entities/full-cycle]]
- [[wiki/concepts/rag-arquitetura-avancada]]
- [[wiki/concepts/agente-ia]]
- [[wiki/concepts/alucinacao-llm]]
- [[wiki/concepts/postgresql]]
- [[wiki/concepts/chunking]]
- [[wiki/concepts/elegibilidade-de-chunks]]

## Key Sources

- [[wiki/sources/rag-retrieval]] — fonte técnica/avançada já existente na wiki (hybrid search, reranking, HyDE, contextual retrieval, GraphRAG, RAGAS); esta fonte cobre o mesmo domínio em nível introdutório/pedagógico, sem contradição — apenas granularidade diferente
- [[wiki/sources/porque-nunca-confiar-em-llm-alucinacao]] — reforça, de forma independente, que RAG mitiga mas não elimina alucinação, e que admitir incerteza é preferível a inventar resposta

## Open Questions

- Qual o valor de threshold de "elegibilidade" (0,9 no exemplo da aula) é realista em produção, e como ele se relaciona com as métricas de `context_precision`/`context_recall` do RAGAS já documentadas em [[wiki/sources/rag-retrieval]]?
- A aula não detalha como versionar ou invalidar metadados quando o documento-fonte muda — ponto que [[wiki/concepts/rag-arquitetura-avancada]] já identifica como o "trabalho real" do RAG em escala.
