---
type: concept
title: "Busca Visual por Similaridade"
aliases: ["busca por imagem", "visual search", "busca visual com CNN"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [embeddings, visao-computacional, cnn, e-commerce, similaridade]
skill: tech-mentor-ai
status: draft
---

# Busca Visual por Similaridade

Buscar itens parecidos a partir de uma **imagem de consulta**. Receita leve citada no vídeo: usar uma [[wiki/concepts/cnn-rede-neural-convolucional]] (ex.: VGG16) **sem a cabeça de classificação**, extrair o vetor da camada anterior (representação no espaço latente), pré-calcular os vetores de todo o catálogo e comparar a consulta por [[wiki/concepts/similaridade-de-cosseno]], devolvendo o mais parecido (não necessariamente idêntico). Roda em hardware modesto.

## Evolução descrita

1. Busca por **metadados/termos** (descrição, marca, tamanho): [[wiki/concepts/busca-por-palavra-chave]].
2. **Busca visual** (estilo Google Lens) com CNN: grande upgrade, só imagem.
3. **Busca textual semântica** via modelos visão-linguagem/[[wiki/concepts/embedding-multimodal]]: "blusa azul de telinha com botões" mesmo sem esses termos nos metadados; e consulta por voz direta.

Quando o caso é só imagem-imagem, a CNN leve basta; migrar para [[wiki/entities/gemini-embedding-2]] compensa se o cliente exige texto/áudio e aceita o [[wiki/concepts/custo-e-privacidade-de-embedding-via-api|custo e a privacidade]]. Cenário hipotético, sem benchmark.

## Key sources

- [[wiki/sources/gemini-embedding-2-embedding-multimodal-google]]
