---
type: source
title: "Sua RAG é Ruim? Busca Híbrida (Semântica + Palavra-chave) na Prática"
aliases: ["rag busca híbrida ronald hulk", "sua rag é ruim", "busca semântica não é suficiente"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 0
tags: [rag, busca-hibrida, busca-semantica, busca-textual, embeddings, top-k, fusion, retrieval, tech-mentor-ai]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/rag-busca-hibrida-semantica-e-textual-ronald-hulk.md
source_url: ""
author: "Ronald Hulk"
date_published: ""
date_ingested: 2026-09-29
---

# Sua RAG é Ruim? Busca Híbrida (Semântica + Palavra-chave) na Prática

## TL;DR

Vídeo de [[wiki/entities/ronald-hulk]] com a tese de que **busca semântica sozinha não basta** em RAG de produção. [[wiki/concepts/rag-como-ferramenta-de-busca]]: RAG é, acima de tudo, um problema de busca. A busca semântica ([[wiki/concepts/busca-semantica]]) compara o embedding da pergunta com os embeddings dos chunks por [[wiki/concepts/similaridade-de-cosseno]] e devolve os [[wiki/concepts/top-k-retrieval|top-K]] mais próximos; falha quando o usuário digita só uma ou duas palavras-chave, porque o vetor curto fica longe dos chunks. A solução é a [[wiki/concepts/hybrid-search|busca híbrida]]: rodar em paralelo a [[wiki/concepts/busca-por-palavra-chave|busca por palavra-chave]] e a semântica, e uni-las numa etapa de [[wiki/concepts/fusion-de-rankings|fusion]] que desempata e rankeia, com **pesos definidos por critério do engenheiro e validados por testes** do retrieval. Demonstração ao vivo na harness [[wiki/entities/rock-pro]]. Fecha com: o agente pode refazer a busca, mas deve ter limite de chamadas para não entrar em loop.

## Key Claims

**Claim:** RAG hoje é, na prática, dar ao agente uma ferramenta de busca; RAG é acima de tudo um problema de busca.
**Evidence:** Relato histórico do autor: no início as LLMs não chamavam ferramentas; depois que passaram a chamar de forma consistente, a "RAG" virou uma tool que busca no banco e devolve resultado à LLM.
**Confidence:** Alta — consistente com [[wiki/concepts/tool-use-agents]] e [[wiki/concepts/tool-call]], e com o tratamento de RAG como pipeline em [[wiki/sources/rag-introducao-pipeline-completo]]. [skill: tech-mentor-ai] `agentic-rag.md` trata exatamente o retrieval como ferramenta que o agente decide quando chamar.

**Claim:** Busca semântica não encontra o que o usuário quer quando ele digita só uma ou duas palavras-chave, porque essa consulta curta fica muito distante dos chunks (fatias de documento) no espaço vetorial.
**Evidence:** Argumento do autor + contraste em demo: pergunta longa e contextual funciona só com semântica; palavra isolada só é achada pela busca textual.
**Confidence:** Média-alta — mecanismo plausível e coerente com [skill: tech-mentor-ai] `ai-search.md` ("Embeddings melhor para conceito; BM25 melhor para siglas, códigos, termos técnicos e queries de usuário com jargão preciso"). A fonte não mostra medição, só demonstração.

**Claim:** Aumentar o top-K para "compensar" a falha da busca semântica polui o contexto, piora a resposta, gasta mais tokens e deixa mais lento; o K ótimo é achado por investigação (implementar, testar, coletar números, iterar).
**Evidence:** Raciocínio do autor sobre o "círculo" do top-K ao redor da pergunta no espaço vetorial.
**Confidence:** Alta como princípio — ver [[wiki/concepts/degradacao-de-contexto]] e [[wiki/concepts/janela-de-contexto]]; nenhum número de K ótimo é dado.

**Claim:** Busca híbrida = busca semântica e busca por palavra-chave rodando **em paralelo**, com uma etapa de **fusion** que consolida e rankeia as duas opiniões.
**Evidence:** Diagrama descrito: as duas buscas apontam chunks (ex.: uma dá prioridade ao chunk C, outra ao A) e o fusion desempata.
**Confidence:** Alta. [skill: tech-mentor-ai] `ai-search.md`: hybrid via **Reciprocal Rank Fusion** (`score = Σ 1/(k + rank)`, k=60) "consistentemente supera ambos individualmente". A fonte **não nomeia RRF** nem BM25 — só diz que o fusion é um critério do engenheiro.

**Claim:** O fusion não é "tecnologia alienígena": é um critério que o engenheiro define, inclusive o peso relativo entre palavra-chave e semântica conforme a natureza do dado.
**Evidence:** Afirmação direta do autor, com exemplo de dados que pedem mais peso a palavras-chave vs. mais peso a semântica.
**Confidence:** Alta. [skill: tech-mentor-ai] confirma a alternativa de combinação linear com α tunado por domínio (com o problema de normalização de scores) e o RRF como opção que dispensa pesos.

**Claim:** Os pesos e o K devem ser decididos por **testes que medem o retrieval** (o R da RAG), comparando configurações; "IA não é adivinhação, IA é trabalho".
**Evidence:** Método descrito: mudar peso para textual, medir; mudar para semântico, medir; ficar com o que melhora.
**Confidence:** Alta como princípio — alinhado a [[wiki/concepts/llm-evals-testing]] e [[wiki/concepts/evals-llm]]. A fonte não cita métricas (recall@K, MRR etc.) nem ferramentas de avaliação de retrieval.

**Claim:** A maioria das RAGs vistas na internet funciona na demo e não no mundo real.
**Evidence:** Afirmação do autor, ligada ao ciclo aprender → aplicar → produção → feedback.
**Confidence:** Média — opinião de praticante/consultor, sem dados. Ver [[wiki/concepts/rag-demo-vs-mundo-real]].

**Claim:** Um agente com RAG pode refazer a pergunta e buscar de novo quantas vezes for permitido, mas é boa prática limitar as chamadas para evitar loops.
**Evidence:** Recomendação final do autor ("não confie no modelo, confie na sua habilidade").
**Confidence:** Alta — [skill: tech-mentor-ai] `agents-runtime.md`/`agent-ops.md` (budget de tokens, loop detection).

**Claim:** A "memória semântica" de assistentes (lembrar preferências de sessões anteriores) exige entendimento de significado; na demo a busca por palavra-chave achou a aula sobre o tema porque a aula trata de embeddings.
**Evidence:** Exemplo da "aula 11 — implemente memória semântica" na harness do autor.
**Confidence:** Baixa-média — o uso do termo "memória semântica" aqui é informal e o trecho da transcrição é ambíguo (ver nota de limpeza no raw). Comparar com [[wiki/concepts/memoria-de-longo-prazo-ia]].

## Entidades e Conceitos Tocados

- [[wiki/entities/ronald-hulk]]
- [[wiki/entities/rock-pro]]
- [[wiki/concepts/hybrid-search]]
- [[wiki/concepts/busca-semantica]]
- [[wiki/concepts/busca-por-palavra-chave]]
- [[wiki/concepts/similaridade-de-cosseno]]
- [[wiki/concepts/top-k-retrieval]]
- [[wiki/concepts/fusion-de-rankings]]
- [[wiki/concepts/rag-como-ferramenta-de-busca]]
- [[wiki/concepts/rag-demo-vs-mundo-real]]
- [[wiki/concepts/chunking]]
- [[wiki/concepts/embedding-vectors]]
- [[wiki/concepts/bm25]]
- [[wiki/concepts/reranking]]
- [[wiki/concepts/janela-de-contexto]]
- [[wiki/concepts/degradacao-de-contexto]]
- [[wiki/concepts/tool-use-agents]]
- [[wiki/concepts/llm-evals-testing]]
- [[wiki/concepts/memoria-de-longo-prazo-ia]]
- [[wiki/concepts/harness]]
- [[wiki/sources/rag-introducao-pipeline-completo]]
- [[wiki/sources/rag-retrieval]]
- [[wiki/sources/prompt-caching-kv-cache-engenharia-de-contexto-ronald-hulk]] (mesmo autor e mesma harness)

## Open Questions

1. Qual algoritmo de fusion a Rock Pro usa (RRF, combinação linear com pesos)? A fonte só diz que é "um critério que você define".
2. Qual é o algoritmo da busca textual (BM25, `tsvector`/full-text do banco)? Não dito; ver [[wiki/concepts/full-text-search]].
3. Que valores de K e de pesos o autor usa, e que métricas de retrieval ele mede? Nenhum número é dado.
4. O limiar de "significância" (quão perto conta como relevante) é mencionado como controlável, mas sem detalhe de como se calibra.
5. "A partir de 120/150/200 milhões de tokens" o desempenho cai — provável erro de transcrição (mil tokens); a literatura de *lost in the middle* / [[wiki/concepts/degradacao-de-contexto]] deve ser consultada antes de citar o número.
6. Falta de menção a [[wiki/concepts/reranking]] (cross-encoder) após o fusion — etapa comum em [skill: tech-mentor-ai] `ai-search.md`, ausente no vídeo.

## Quotes

> "Busca semântica não é suficiente."

> "RAG acima de tudo é um problema de busca."

> "A gente não tá buscando um match absoluto... a ideia aqui não é igualdade exata, a ideia aqui é achar similaridade."

> "Você tem que achar esse círculo do top-K de maneira ótima. Isso é um trabalho de investigação."

> "As maiorias das RAGs que a gente vê na internet funcionam na demo... não funciona no mundo real."

> "Isso é um critério que você define."

> "IA não é adivinhação, IA é trabalho."

> "Não confie no modelo, confie na sua habilidade."
