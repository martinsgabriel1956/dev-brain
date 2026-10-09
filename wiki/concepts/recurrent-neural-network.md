---
type: concept
title: "Recurrent Neural Network (RNN)"
aliases: ["RNN", "rede neural recorrente"]
date_created: 2026-10-09
date_updated: 2026-10-09
source_count: 1
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

## Key Sources

- [[wiki/sources/google-nao-esta-perdendo-corrida-ia-memory-caching-gemini-live]]
