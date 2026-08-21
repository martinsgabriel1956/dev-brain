---
type: concept
title: "Autoregressive Language Model"
aliases: ["modelo autorregressivo", "decoder-only", "causal LM"]
date_created: 2026-05-17
date_updated: 2026-08-17
source_count: 3
tags: [llm, transformer, arquitetura, autoregressive]
skill: tech-mentor-ai
status: draft
---

# Autoregressive Language Model

## Definição

Modelo que gera texto token a token, condicionando cada token nos tokens anteriores. Formalmente, modela a distribuição conjunta P(x₁, x₂, ..., xₙ) como produto de condicionais:

```
P(x₁...xₙ) = ∏ P(xᵢ | x₁...xᵢ₋₁)
```

## Arquitetura

Implementado tipicamente com um **Transformer decoder-only** (sem encoder):
- Atenção causal (masked self-attention) — cada posição só atende a posições anteriores.
- Treinado com objetivo de **next-token prediction** (language modeling loss).

GPT-3 ([[wiki/sources/gpt3-language-models-are-few-shot-learners]]) usa esta arquitetura com:
- Atenção alternando densa e esparsa (Sparse Transformer).
- Pré-normalização (LayerNorm antes da atenção, não depois).
- Tokenização reversível (BPE).

## Contraste com Encoder-Decoder

| Tipo | Exemplo | Melhor para |
|---|---|---|
| Decoder-only (autoregressive) | GPT-3, GPT-4, Llama | Geração de texto, ICL, completions |
| Encoder-only | BERT, RoBERTa | Classificação, extração |
| Encoder-decoder | T5, BART | Tradução, sumarização |

## Por que Decoder-only domina (2023+)

A descoberta de [[in-context-learning]] mostrou que modelos autorregressivos grandes são meta-aprendizes eficientes. O paradigma de fine-tuning encoder-decoder foi gradualmente substituído por ICL + instruction tuning em decoder-only.

## Por que a Autorregressão Torna o Token de Output Mais Caro que o de Input

A definição formal acima — cada token condicionado em todos os anteriores — tem uma consequência prática direta em custo de inferência. Diferente de um humano lendo uma história e guardando na memória só o que importa para responder uma pergunta pontual, o modelo autorregressivo **reprocessa toda a sequência gerada até ali a cada novo token**, porque não existe atalho: prever o token seguinte exige recolocar todo o contexto anterior (prompt + tokens já gerados) nas camadas da rede.

Exemplo didático em [[wiki/sources/tokens-o-que-sao-e-por-que-custam-caro]]: para completar "o gato" em "o gato senta no tapete", o modelo gera um token por vez, e a cada token novo reprocessa a sequência inteira acumulada (`o gato` → `o gato senta` → `o gato senta no` → `o gato senta no tapete`). A cada rodada, mais tokens entram no cálculo — daí o custo crescer com o tamanho da resposta gerada.

Isso explica por que **todo provider de LLM cobra mais caro por token de output que por token de input** (ex.: Claude Opus citado na fonte como ~5x mais caro no output que no input) — não é só política comercial, é reflexo direto do mecanismo: o processamento de input é feito uma única vez (tokenizar + codificar), enquanto a geração de output é recursiva por natureza. Técnicas como [[kv-cache]] existem justamente para amortizar parte desse custo, reaproveitando o que já foi computado em vez de recalcular do zero a cada token — mas o padrão de output-mais-caro-que-input persiste em toda a indústria mesmo com essas otimizações.

## Interpretabilidade das Ativações Residuais

A pesquisa de [[j-space-interpretabilidade]] da Anthropic (Jacobian Lens) opera diretamente sobre o mecanismo de previsão do próximo token que define esse tipo de modelo: calcula, via derivadas parciais (Jacobiano), a direção nas ativações residuais do stream que mais aumenta a probabilidade de cada palavra do vocabulário aparecer na próxima posição — tornando legível (e alterável) parte do processamento interno que antecede a escolha do token gerado.

## Fontes

- [[wiki/sources/gpt3-language-models-are-few-shot-learners]]
- [[wiki/sources/jspace-cerebro-cloud-antropic]]
- [[wiki/sources/tokens-o-que-sao-e-por-que-custam-caro]] — por que a geração autorregressiva torna o token de output estruturalmente mais caro que o de input
