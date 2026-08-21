---
type: concept
title: "Byte Pair Encoding"
aliases: ["BPE", "tokenização BPE", "byte pair encoding"]
date_created: 2026-06-09
date_updated: 2026-08-17
source_count: 3
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

### Tamanho do Vocabulário como Trade-off

Vocabulário maior → menos tokens por texto (mais eficiência), mas exige modelo maior para "abrigar" o vocabulário. Exemplo didático com a palavra `"understanding"`:

| Tamanho do vocabulário | Tokens |
|---|---|
| ~1.000 | `under` `st` `and` `ing` (5) |
| ~50.000 | `under` `standing` (3) |
| ~200.000 | 2 |

Um tokenizer que treina só até o nível de caractere (sem merges) sempre produz `nº tokens == nº caracteres` — a versão sem nenhum ganho do algoritmo, útil para entender por que o passo iterativo de merge importa. Ver [[tokenizacao]] para o pipeline completo de encode/decode.

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

## Experimento: Vocabulário Menor Observado Empiricamente (GPT-4o vs. Claude Opus 5)

[[wiki/sources/tokens-o-que-sao-e-por-que-custam-caro]] compara a mesma frase tokenizada por dois modelos: em português, o GPT-4o (vocabulário público, ~200k tokens) gastou 22 tokens contra 42 do Claude Opus 5 (vocabulário privado, não divulgado pela Anthropic) — quase o dobro. Em inglês, a mesma frase caiu para 15 tokens (GPT-4o) e 35 (Claude Opus). O autor infere que o tokenizer da Anthropic tem vocabulário menor, mas essa é uma suposição não confirmada por fonte primária — a Anthropic não publica o tamanho do vocabulário do tokenizer do Opus. O padrão qualitativo (inglês sempre mais barato que português, no mesmo modelo) confirma a Token Tax em ambos os providers.

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
- [[tokenizacao]] — conceito geral de token, vocabulário e pipeline encode/decode

---

## Key Sources

- [[wiki/sources/custo-tokens-portugues-vs-ingles]]
- [[wiki/sources/tokens-llm-fundamentos-typescript]]
- [[wiki/sources/tokens-o-que-sao-e-por-que-custam-caro]] — comparação empírica GPT-4o vs. Claude Opus 5 e palavra inventada vs. real
