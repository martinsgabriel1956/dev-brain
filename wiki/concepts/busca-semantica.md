---
type: concept
title: "Busca Semântica"
aliases: ["semantic search", "dense retrieval", "busca vetorial"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [rag, busca-semantica, embeddings, retrieval, dense-retrieval]
skill: tech-mentor-ai
status: draft
---

# Busca Semântica

Busca que se preocupa com **significado**, não com palavras exatas. Chunks são indexados como [[wiki/concepts/embedding-vectors|embeddings]]; a pergunta também vira embedding, e o sistema devolve os chunks mais próximos por [[wiki/concepts/similaridade-de-cosseno]], limitados pelo [[wiki/concepts/top-k-retrieval|top-K]].

## Propriedades

- Não busca igualdade, busca **similaridade**: a pergunta quase nunca é igual ao chunk.
- Funciona bem com perguntas longas e cheias de contexto.
- Falha com consultas de uma ou duas palavras (o vetor curto fica distante dos chunks), então "não achei nada significativo" ([[wiki/sources/rag-busca-hibrida-semantica-e-textual-ronald-hulk]]).
- Por isso não basta sozinha: complementa-se com [[wiki/concepts/busca-por-palavra-chave]] na [[wiki/concepts/hybrid-search]].

## Ligações

- Depende de [[wiki/concepts/chunking]]: a qualidade do corte define o que pode ser encontrado.
- A "memória semântica" de assistentes (lembrar preferências entre sessões) depende do mesmo princípio de entender significado; ver [[wiki/concepts/memoria-de-longo-prazo-ia]].

## Key sources

- [[wiki/sources/rag-busca-hibrida-semantica-e-textual-ronald-hulk]] — mecânica (pergunta → embedding → comparação) e limite com palavras-chave isoladas
