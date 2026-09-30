---
type: concept
title: "Busca por Palavra-chave"
aliases: ["busca textual", "keyword search", "lexical search", "sparse retrieval"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [rag, busca-textual, keyword-search, retrieval, bm25]
skill: tech-mentor-ai
status: draft
---

# Busca por Palavra-chave

Busca que casa **termos** da consulta com termos dos documentos. No contexto de RAG, é o complemento da [[wiki/concepts/busca-semantica]]: acha o chunk certo quando o usuário só sabe uma palavra-chave e o embedding curto ficaria longe do contexto.

## Papel na busca híbrida

- Na demo de [[wiki/sources/rag-busca-hibrida-semantica-e-textual-ronald-hulk]], uma única palavra bastou para a [[wiki/entities/rock-pro]] achar a aula certa, decisão tomada só pela palavra-chave. Só com semântica, a mesma consulta poderia retornar zero.
- Roda em paralelo com a semântica e se une a ela no [[wiki/concepts/fusion-de-rankings|fusion]] ([[wiki/concepts/hybrid-search]]).

## Implementações

A fonte não diz qual algoritmo usa. Opções conhecidas: [[wiki/concepts/bm25]] e busca de texto integral em banco ([[wiki/concepts/full-text-search]]). [skill: tech-mentor-ai] BM25 é forte em siglas, códigos, versões e nomes próprios.

## Key sources

- [[wiki/sources/rag-busca-hibrida-semantica-e-textual-ronald-hulk]] — papel da palavra-chave e demo
