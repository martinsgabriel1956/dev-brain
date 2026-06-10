---
type: concept
title: "Byte Pair Encoding"
aliases: ["BPE", "tokenização BPE", "byte pair encoding"]
date_created: 2026-06-09
date_updated: 2026-06-09
source_count: 1
tags: [tokenizacao, bpe, llm, token-economics, nlp]
skill: tech-mentor-ai
status: stable
---

## Definição

Algoritmo de tokenização usado pelos principais LLMs (GPT, Claude, Gemini) para converter texto em tokens — as unidades fundamentais de processamento e cobrança dos modelos.

O BPE funciona de forma iterativa:
1. Começa com todos os caracteres individuais como tokens
2. Identifica os pares de caracteres/tokens adjacentes mais frequentes no corpus
3. Mescla esse par em um único token
4. Repete até atingir o tamanho de vocabulário desejado (tipicamente 32k–100k tokens)

O resultado é um vocabulário de tokens que reflete **os padrões mais frequentes no corpus de treinamento**.

---

## Por que BPE Causa a Token Tax

Como o corpus de treinamento dos LLMs é predominantemente em inglês:

- Palavras e padrões comuns em inglês → fundidos em tokens únicos
- Padrões de idiomas não-ingleses → menos frequentes → menos mesclados → mais fragmentados

**Exemplo concreto:**
- `"championship"` em inglês → 1 token (palavra comum nos dados de treino)
- `"mundial"` em português → 2+ tokens (menos frequente no corpus)

Isso explica a [[token-tax-multilingual]]: a mesma informação em português requer mais tokens que em inglês.

---

## Visualização

O Hugging Face oferece um playground de tokenização interativo que permite visualizar como qualquer texto é dividido em tokens por diferentes modelos. Útil para comparar a eficiência de tokenização entre idiomas.

---

## Melhora Esperada

À medida que modelos treinarem com corpora mais multilíngues (dados balanceados por idioma), a eficiência do BPE para idiomas não-ingleses deve melhorar. Ainda assim, em 2025–2026, o multiplicador do português no Anthropic é ~1.62×.

---

## Conexões

- [[token-tax-multilingual]] — consequência direta do BPE treinado em corpus inglês
- [[janela-de-contexto]] — tokens são a unidade que preenche e esgota a janela de contexto
- [[completion]] — output do modelo também é cobrado por tokens gerados via BPE

---

## Key Sources

- [[wiki/sources/custo-tokens-portugues-vs-ingles]]
