---
type: concept
title: "Positional Encoding"
aliases: ["positional embedding", "codificação posicional", "rope", "rotary position embedding"]
date_created: 2026-09-18
date_updated: 2026-09-18
source_count: 1
tags: [positional-encoding, transformers, self-attention, llm-fundamentals]
skill: tech-mentor-ai
status: stable
---

## Definição

Vetor adicional somado ao [[embedding-vectors|embedding]] de cada token para injetar informação sobre sua **posição/ordem** na sequência de input. É necessário porque o mecanismo de [[self-attention]], por si só, é invariante à posição — não distingue, sem essa informação extra, se um token veio antes ou depois de outro.

## Por que a Ordem Importa

A ordem das palavras muda o significado da frase inteira, mesmo mantendo o mesmo conjunto de tokens. Exemplo: "a mãe matou a filha" e "a filha matou a mãe" usam exatamente os mesmos tokens, mas têm significados opostos. Sem positional encoding, o Transformer trataria essas duas frases como equivalentes, já que self-attention calcula relevância entre pares de tokens sem noção nativa de sequência.

## Implementações

[external] — não coberto em profundidade na fonte que originou esta página, que apenas menciona o conceito e sua necessidade:

- **Sinusoidal** (paper original, [[wiki/entities/attention-is-all-you-need-paper]], 2017): funções seno/cosseno de frequências diferentes por dimensão, permitindo ao modelo extrapolar para sequências mais longas que as vistas em treino.
- **Aprendida**: vetor de posição treinado como parte dos parâmetros do modelo, junto com os embeddings de token.
- **RoPE (Rotary Position Embedding)**: usado em LLMs modernas (Llama, Mistral) — rotaciona os vetores Q/K em função da posição relativa entre tokens, em vez de somar um vetor fixo ao embedding.

## Conexões

- [[self-attention]] — mecanismo que depende de positional encoding para capturar ordem
- [[embedding-vectors]] — camada sobre a qual o vetor posicional é somado
- [[transformer-architecture]] — etapa do pipeline logo após a geração dos embeddings de token

## Key Sources

- [[wiki/sources/self-attention-mecanismo-transformers]] — explica a necessidade do positional encoding via exemplo de inversão de ordem que inverte o significado da frase ("a mãe matou a filha" vs. "a filha matou a mãe"); não detalha a implementação (sinusoidal vs. aprendida vs. RoPE)
