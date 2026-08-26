---
type: concept
title: "Elegibilidade de Chunks"
aliases: ["chunks elegíveis", "threshold de confiança rag", "eligible chunks"]
date_created: 2026-08-26
date_updated: 2026-08-26
source_count: 1
tags: [rag, retrieval, alucinacao, threshold, qualidade]
skill: tech-mentor-ai
status: stub
---

# Elegibilidade de Chunks

Busca vetorial com filtro de metadados não retorna necessariamente os [[wiki/concepts/chunking|chunks]] certos para responder a pergunta — retorna um **conjunto de chunks elegíveis**, isto é, candidatos que passam por um segundo critério (um score/threshold de confiança) antes de entrar de fato no prompt final.

## Como funciona

Exemplo em [[wiki/sources/rag-introducao-pipeline-completo]]: de 10 chunks retornados pela busca por proximidade, define-se que só entram no contexto os que atingem, por exemplo, 0,9 de confiança (escala 0–1). Nesse exemplo, apenas 3 dos 10 chunks sobrevivem ao filtro — são os chunks elegíveis.

## Zero chunks elegíveis → recusar responder

Se nenhum chunk recuperado atinge o threshold, a resposta correta do sistema é admitir que não tem a informação, em vez de responder com um chunk descontextualizado ou deixar o modelo "chutar". Essa é a mesma lógica documentada em [[wiki/concepts/alucinacao-llm]]: um LLM que reconhece incerteza é preferível a um que inventa uma resposta com confiança.

Uma vez definido o conjunto elegível, ainda é possível reordenar (reranking) esses chunks para dar mais ênfase a uns do que a outros dentro do prompt final.

## Key Sources

- [[wiki/sources/rag-introducao-pipeline-completo]] — introduz o conceito com o exemplo numérico do threshold de 0,9 e a recomendação de recusar responder quando não há chunk elegível
