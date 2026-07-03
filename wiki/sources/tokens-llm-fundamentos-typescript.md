---
type: source
title: "Tokens em LLMs — Fundamentos com TypeScript"
aliases: ["tokens llm typescript", "token deep dive matt pocock", "o que é um token llm"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_file: /home/nemomartins/Documentos/new/dev-study/raw/tokens-llm-fundamentos-typescript.md
source_url: ""
author: "Matt Pocock (AI Hero)"
date_published: ""
date_ingested: 2026-07-03
source_count: 0
tags: [tokens, tokenizacao, bpe, llm-fundamentals, typescript, ai-sdk, tiktoken, vocabulario]
skill: tech-mentor-ai
status: stable
---

## TL;DR

Deep dive didático sobre tokens em LLMs usando TypeScript: por que o mesmo prompt gera contagens de tokens diferentes entre Anthropic e Google, como funciona o pipeline encode → processamento → decode, e como tokenizers são treinados incrementalmente (nível-caractere → nível-subpalavra → BPE real) a partir de um corpus, com o tamanho do vocabulário como trade-off central entre eficiência de tokens e tamanho do modelo.

## Key Claims

**Claim:** O mesmo prompt (`"Hello World"`) produz contagens de tokens diferentes em provedores diferentes porque cada LLM usa seu próprio vocabulário de tokenizer.
**Evidence:** Via AI SDK: Claude 3.5 Haiku (Anthropic) reporta 11 tokens de entrada / 20 de saída; Gemini 2.0 Flash Lite (Google) reporta 4 tokens de entrada / 11 de saída para o mesmo prompt.
**Confidence:** alta

**Claim:** Tokens são sempre menos numerosos que caracteres, porque um token agrupa múltiplos caracteres — exceto em tokenizers puramente por caractere.
**Evidence:** Demonstração com `js-tiktoken` (`o200k_base`, tokenizer do GPT-4o): um parágrafo de ~2.300 caracteres vira menos de 500 tokens; `"Hello World"` (12 caracteres) vira 3 tokens.
**Confidence:** alta

**Claim:** O tamanho do vocabulário de um tokenizer é o trade-off central entre eficiência de tokens (menos tokens por texto) e tamanho/memória do modelo.
**Evidence:** Exemplo didático com a palavra `"understanding"`: vocabulário de ~1.000 tokens → 5 tokens (`under`/`st`/`and`/`ing`); ~50.000 tokens → 3 tokens (`under`/`standing`); ~200.000 tokens → 2 tokens. Vocabulário maior exige modelo maior para "abrigar" as entradas.
**Confidence:** alta

**Claim:** Tokenizers são treinados identificando grupos de caracteres frequentes no corpus de treino, de forma recursiva (grupos de grupos), não apenas caracteres isolados.
**Evidence:** Implementação didática comparando um `CharacterLevelTokenizer` (11 caracteres → 11 tokens, sem ganho) com um `SubwordLevelTokenizer` treinado no mesmo corpus (`"the cat sat on the mat"`), que reduz `"cats sat mat"` de 11 para 8 tokens ao identificar subwords como `th`, `he`, ` a`. Tokenizers reais (BPE) vão além de um nível de agrupamento.
**Confidence:** alta

**Claim:** Palavras raras/incomuns e idiomas ou linguagens de programação pouco representados no corpus de treino são quebrados em mais tokens, encarecendo e ocupando mais janela de contexto.
**Evidence:** A palavra inventada `"frabjous"` (do poema *Jabberwocky*, de Lewis Carroll) é dividida em 4 tokens separados pelo `o200k_base`, muito mais que uma palavra comum receberia. O mesmo raciocínio se aplica a idiomas pouco representados e a linguagens de programação menos populares (ex. Haskell vs. JavaScript).
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/byte-pair-encoding]]
- [[concepts/token-tax-multilingual]]
- [[concepts/tokenizacao]]
- [[entities/anthropic]]
- [[entities/openai]]
- [[entities/google]]
- [[entities/matt-pocock]]
- [[entities/vercel-ai-sdk]]

## Open Questions

- O exemplo do vídeo usa um tokenizer didático de apenas um nível de agrupamento — como o BPE real decide quando parar de mesclar pares (critério de parada do treinamento, além do tamanho-alvo do vocabulário)?
- Qual o multiplicador real de tokens do Gemini/Google para português, comparável ao ~1.62× documentado para Anthropic em [[token-tax-multilingual]]? A fonte não cobre isso.
