---
type: concept
title: "Transformer Architecture"
aliases: ["transformers", "arquitetura transformer"]
date_created: 2026-09-18
date_updated: 2026-09-18
source_count: 2
tags: [transformers, llm-fundamentals, self-attention, embeddings, attention-is-all-you-need]
skill: tech-mentor-ai
status: stable
---

## Definição

Arquitetura de rede neural introduzida no paper [[wiki/entities/attention-is-all-you-need-paper]] (2017), base de praticamente todas as LLMs generativas modernas (GPT, Claude, Gemini). Substituiu arquiteturas recorrentes (RNN/LSTM) ao processar a sequência inteira em paralelo, usando [[self-attention]] para capturar relações entre tokens independentemente da distância entre eles.

## Pipeline de Alto Nível

```
Input tokens → Token Embeddings + Positional Encoding
             → N × [Multi-Head Attention → Add & Norm → FFN → Add & Norm]
             → Output logits
```

1. **Tokenização**: input vira [[tokenizacao|tokens]], cada um mapeado a um ID no vocabulário do modelo.
2. **Embeddings**: cada ID é traduzido em um [[embedding-vectors|embedding vector]] — representação numérica do significado geral do token.
3. **Positional Encoding**: um vetor extra é somado ao embedding para injetar informação de ordem, já que a atenção por si só é invariante à posição.
4. **Self-Attention** (N camadas, cada uma com múltiplas "heads"): cada token gera vetores Q/K/V e calcula sua relação de importância com todos os outros tokens da sequência — ver [[self-attention]].
5. **FFN (Feed-Forward Network)**: aplicado independentemente a cada token após a atenção; responsável por boa parte da "memória" factual do modelo.
6. **Output**: logits sobre o vocabulário inteiro, usados para prever o próximo token.

## Por que Substituiu Arquiteturas Anteriores

Antes do Transformer, modelos já usavam embedding vectors para representar significado de tokens, mas tinham dificuldade em capturar **contexto** — a relação entre um token e os demais na mesma sequência. O mecanismo de self-attention resolveu isso computando, para cada par de tokens, um score de relevância mútua, processado em paralelo (não sequencialmente como em RNNs). Isso é o que permitiu o salto de qualidade em modelos generativos a partir de 2017-2018.

## Custo Computacional

Self-attention é O(n²) no comprimento da sequência — para n tokens, a matriz de atenção é n×n. Isso é o gargalo físico por trás do limite de [[context-window|context window]] e motivou arquiteturas alternativas como [[mamba-ssm]] (O(n)) e otimizações como [[flash-attention]] (mesmo resultado matemático, muito mais eficiente em memória).

## Conexões

- [[self-attention]] — o componente central da arquitetura; mecanismo de cálculo de contexto
- [[embedding-vectors]] — a representação de significado sobre a qual a atenção opera
- [[positional-encoding]] — como a ordem dos tokens é injetada, já que atenção pura é invariante à posição
- [[tokenizacao]] — etapa anterior que transforma texto em tokens/IDs
- [[wiki/entities/attention-is-all-you-need-paper]] — paper de origem (2017)
- [[mixture-of-experts]] — variação que substitui o FFN denso por experts esparsos
- [[flash-attention]] — otimização de implementação do cálculo de atenção
- [[mamba-ssm]] — arquitetura alternativa O(n) para sequências longas

## Key Sources

- [[wiki/sources/como-llms-funcionam]] — visão geral da arquitetura, complexidade O(n²), FlashAttention, MoE, Mamba/SSM como alternativas
- [[wiki/sources/self-attention-mecanismo-transformers]] — deep dive no mecanismo de self-attention especificamente (tokens → embeddings → Q/K → attention score)
