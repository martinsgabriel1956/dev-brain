---
type: concept
title: "Top-K Retrieval"
aliases: ["top-k", "top K", "número de chunks retornados"]
date_created: 2026-09-29
date_updated: 2026-10-06
source_count: 2
tags: [rag, retrieval, top-k, busca-semantica, contexto]
skill: tech-mentor-ai
status: draft
---

# Top-K Retrieval

Parâmetro que define **quantos chunks** a busca devolve ao agente (a fonte cita 3, 4, 5 ou 10). Nunca se retorna um resultado só; o K certo é descoberto por teste.

## Trade-off

- **K pequeno demais:** consultas curtas ou ambíguas ficam sem o chunk relevante ("não achei nada significativo").
- **K grande demais:** entra material irrelevante, polui o contexto, gasta mais tokens, deixa mais lento e piora a resposta; ver [[wiki/concepts/degradacao-de-contexto]] e [[wiki/concepts/janela-de-contexto]].
- A fonte também fala de um limiar de **significância** que o engenheiro controla.

Achar o K ótimo é "trabalho de investigação": implementar, testar, coletar números, iterar ([[wiki/concepts/llm-evals-testing]]). A [[wiki/concepts/hybrid-search]] ataca a causa em vez de inflar K.

## Key sources

- [[wiki/sources/rag-busca-hibrida-semantica-e-textual-ronald-hulk]] — o "círculo" do top-K em torno da pergunta e o custo de alargá-lo
- [[wiki/sources/rag-spring-ai-microagente-recomendacao-michele-brito]] — topK fixo em 4 no exemplo, com a observação de que bases maiores pedem K maior; usado em [[wiki/concepts/recuperacao-com-filtro-de-metadados]]
