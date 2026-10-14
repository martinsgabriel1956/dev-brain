---
type: concept
title: "Recurrent Neural Network (RNN)"
aliases: ["RNN", "rede neural recorrente"]
date_created: 2026-10-09
date_updated: 2026-10-14
source_count: 3
tags: [ai, llm-fundamentals, rnn, sequence-models]
skill: tech-mentor-ai
status: draft
---

## Definição

Rede neural que processa a sequência **passo a passo**, carregando um **estado oculto** (memória de tamanho fixo) de um token para o próximo. Custo linear no comprimento (O(L)), mas o estado fixo faz o início da sequência ser sobrescrito/esquecido em contextos longos. Na metáfora da fonte: a **formiga** que lê palavra por palavra e esquece o começo, contra o Transformer "super-homem" que olha a página inteira.

## Conexões

- [[wiki/concepts/transformer-architecture]] — substituiu RNN/LSTM ao processar tudo em paralelo com [[wiki/concepts/self-attention]]; paga custo quadrático
- [[wiki/concepts/memory-caching-rnn]] — técnica que dá memória crescente à RNN
- [[wiki/concepts/needle-in-a-haystack]] — tarefa em que RNNs de memória fixa falham
- [external] SSMs/Mamba e Titans são descendentes recorrentes modernos (ver skill tech-mentor-ai `llm-architectures-2026`)

## Adição (2026-10-14)

Contexto histórico: o Transformer substituiu o processamento sequencial palavra a palavra (típico de arquiteturas anteriores, como RNNs) por análise simultânea, permitindo treino paralelo em GPUs. [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]

## Key Sources

- [[wiki/sources/google-nao-esta-perdendo-corrida-ia-memory-caching-gemini-live]]
- [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]] — Transformer vs. processamento sequencial das arquiteturas anteriores

## Adição (2026-10-14)

Para imagens, a arquitetura clássica é a [[wiki/concepts/cnn-rede-neural-convolucional]].

- [[wiki/sources/gemini-embedding-2-embedding-multimodal-google]] — contraste com CNN (imagens) usada para vetores de busca visual
