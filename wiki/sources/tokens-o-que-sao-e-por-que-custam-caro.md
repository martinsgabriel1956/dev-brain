---
type: source
title: "Tokens: o Que São e Por Que Custam Tão Caro"
aliases: ["por que output custa mais que input", "tokens de verdade explicado", "GPT-4o vs Claude Opus tokens"]
date_created: 2026-08-17
date_updated: 2026-08-17
source_count: 0
tags: [tokens, tokenizacao, llm-fundamentals, token-economics, autoregressive, bpe, vocabulario, precificacao-llm]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/tokens-o-que-sao-e-por-que-custam-caro.md
source_url: ""
author: "desconhecido (canal de vídeo)"
date_published: ""
date_ingested: 2026-08-17
---

# Tokens: o Que São e Por Que Custam Tão Caro

## TL;DR

Explica desde a base por que LLMs precisam converter texto em tokens (elas só operam sobre números via multiplicação de matrizes), por que subword tokens vencem tanto letra-por-letra (explode cálculo) quanto palavra-por-palavra (explode vocabulário), e como o tamanho do vocabulário do tokenizer determina a granularidade da quebra — demonstrado com um experimento prático comparando GPT-4o e Claude Opus 5 na mesma frase em português e inglês. A segunda metade explica, via autorregressão, por que o token de **output** custa estruturalmente mais caro que o de **input** em todos os providers: cada novo token gerado exige reprocessar todo o contexto anterior mais o token novo, tornando a geração cumulativamente mais cara conforme a resposta cresce.

## Key Claims

**Claim:** LLMs operam exclusivamente sobre números (multiplicação de matrizes); tokens existem como unidade de tradução entre linguagem humana e representação numérica.
**Evidence:** Explicação conceitual do pipeline: texto → tokenização (split em pedaços do vocabulário) → encoding (pedaço → número) → matrizes → inferência → decoding.
**Confidence:** alta — consistente com [[wiki/concepts/tokenizacao]] e [[wiki/sources/tokens-llm-fundamentos-typescript]].

**Claim:** Tokenização letra-por-letra explode o custo computacional (mais tokens por frase, mais cálculo para o modelo entender que letras adjacentes formam uma única palavra); tokenização palavra-por-palavra explode o vocabulário necessário (precisaria mapear todas as palavras de todas as línguas e todas as suas flexões).
**Evidence:** Exemplo didático com "cat" (C-A-T como 3 tokens desperdiça raciocínio) e com as flexões de "corre" (corria, corríamos, correndo) — cada flexão como palavra nova explodiria o vocabulário.
**Confidence:** alta — argumento didático coerente com o algoritmo de [[wiki/concepts/byte-pair-encoding]].

**Claim:** GPT-4o (vocabulário ~200k tokens, público) tokeniza a mesma frase em português com menos da metade dos tokens que o Claude Opus 5 (vocabulário não divulgado, presumidamente menor).
**Evidence:** Frase "a raposa marrom rápida pula sobre o cão preguiçoso": 22 tokens no GPT-4o vs. 42 tokens no Claude Opus 5. Em inglês ("the quick brown fox..."): 15 tokens no GPT-4o vs. 35 no Claude Opus. Autor reconhece que não pode confirmar o tamanho exato do vocabulário da Anthropic porque o tokenizer deles é privado — é inferência, não fato verificado.
**Confidence:** média — o resultado numérico (22 vs. 42, 15 vs. 35) é reproduzível/observável, mas a causa atribuída (vocabulário menor) é suposição do autor, não confirmada por fonte primária da Anthropic.

**Claim:** Uma palavra inventada sem correspondência nos dados de treino ("Ubazu", 5 letras) consome muito mais tokens que uma palavra real do mesmo comprimento ("carro", 5 letras) no mesmo tokenizer.
**Evidence:** "Ubazu" → 10 tokens no Claude Opus / 2 tokens no GPT-4o; "carro" → 8 tokens no Claude Opus. Mesmo número de caracteres, contagem de tokens muito diferente.
**Confidence:** alta — consistente com o efeito de token tax já documentado em [[wiki/concepts/token-tax-multilingual]] para o exemplo "frabjous".

**Claim:** O token de output custa estruturalmente mais que o de input em todos os providers de LLM porque a geração é autorregressiva: cada novo token exige reprocessar todo o contexto gerado até ali, enquanto o processamento do input é feito uma única vez (tokenizar + codificar), sem repetição.
**Evidence:** Passo a passo didático gerando "o gato senta no tapete" token a token, mostrando que a cada novo token o modelo precisa reimputar toda a sequência anterior. Preços citados: Claude Opus ~$5/M tokens input vs. ~$25/M tokens output (5x); padrão de output mais caro repetido em Sonnet, Haiku e em outros providers (OpenAI, modelos chineses).
**Confidence:** alta para o mecanismo (autorregressão é comportamento documentado de LLMs decoder-only, ver [[wiki/concepts/autoregressive-language-model]]); os valores de preço específicos citados não foram verificados contra a tabela oficial da Anthropic nesta ingestão.

## Entities & Concepts Touched

- [[wiki/concepts/tokenizacao]]
- [[wiki/concepts/byte-pair-encoding]]
- [[wiki/concepts/token-tax-multilingual]]
- [[wiki/concepts/autoregressive-language-model]]
- [[wiki/concepts/context-window]]
- [[wiki/entities/anthropic]]
- [[wiki/entities/openai]]

## Open Questions

- O autor assume que o vocabulário do tokenizer da Anthropic é menor que o do GPT-4o com base apenas na contagem de tokens observada — a Anthropic não divulga publicamente o tamanho do vocabulário nem o algoritmo exato do tokenizer. Fica em aberto se a diferença observada (quase 2x mais tokens) vem só do tamanho do vocabulário ou também de outras decisões de tokenização (ex.: tratamento de espaços, maiúsculas, acentuação em português).
- Os valores de preço citados (Opus ~$5/$25 por milhão de tokens input/output) não foram cross-checados contra a tabela de preços oficial vigente da Anthropic nesta ingestão — tratar como aproximação da fonte, não como preço confirmado.
- A fonte não menciona [[wiki/concepts/kv-cache]] nem prompt caching como técnicas que mitigam parcialmente o custo do reprocessamento autorregressivo descrito — é uma lacuna frente ao que já está registrado em [[wiki/concepts/kv-cache]] e em `references/ai/token-economics.md` (skill tech-mentor-ai).

## Raw Quotes

> "A LLM ela só consegue lidar com números, ela não lida com palavras, ela não lida com letras, ela está lidando com números."

> "O token é uma maneira eficiente de traduzir a nossa linguagem para algo entendível para as LLMs."

> "Isso aqui gastou um total de 22 tokens... agora quando a gente analisa o Cloud Opus, a gente vai ver que ele gastou 42 tokens."

> "Para cada novo token que a LLM vai gerar, ela vai precisar reprocessar todo o texto imputado anteriormente e mais o novo token gerado."

> "O processo de geração do output ele é recursivo... e é por isso que o preço de output é aqui o dobro no caso dos modelos da Antropic, mas nos outros modelos também muito mais elevado do que o custo do input."
