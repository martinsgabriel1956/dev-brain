---
type: concept
title: "Tokenização"
aliases: ["token", "tokens", "encode/decode llm", "vocabulário de tokens"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 1
tags: [tokenizacao, llm-fundamentals, tokens, vocabulario, bpe]
skill: tech-mentor-ai
status: stable
---

## Definição

Tokens são a unidade fundamental de processamento e cobrança dos LLMs. Cada modelo tem seu próprio **vocabulário de tokens** — palavras, subpalavras e caracteres conhecidos, cada um mapeado para um número. O LLM nunca processa texto diretamente: opera inteiramente sobre essas representações numéricas.

## O Pipeline Encode → Processamento → Decode

```
texto de entrada → encode (split em maiores chunks do vocabulário → lookup do número)
                 → tokens de entrada [numéricos]
                 → LLM processa (tudo em números)
                 → tokens de saída [numéricos]
                 → decode (lookup do chunk → concatenação)
                 → texto de saída
```

**Encode**: o texto é dividido nos maiores pedaços reconhecidos pelo vocabulário, depois cada pedaço vira o número correspondente.
**Decode**: o caminho inverso — números viram os chunks de texto correspondentes, concatenados em uma string.

## Vocabulário: o Trade-off Central

Quanto maior o vocabulário do tokenizer, menos tokens um mesmo texto produz — mas um vocabulário maior exige um modelo maior (mais memória, mais parâmetros) para "abrigá-lo". Exemplo didático com a palavra `"understanding"`:

| Tamanho do vocabulário | Tokenização | Nº de tokens |
|---|---|---|
| ~1.000 | `under` `st` `and` `ing` | 5 |
| ~50.000 | `under` `standing` | 3 |
| ~200.000 | 2 partes | 2 |

Um tokenizer puramente por caractere (vocabulário = só caracteres únicos) sempre produz `nº tokens == nº caracteres` — o pior caso possível, sem nenhum ganho de agrupamento.

## Por que Diferentes Provedores Produzem Contagens Diferentes

Cada LLM treina (ou herda) seu próprio tokenizer sobre seu próprio corpus. O mesmo prompt (`"Hello World"`) gera contagens diferentes em provedores diferentes — não é um bug, é consequência direta de vocabulários distintos. Ver [[byte-pair-encoding]] para o algoritmo mais usado para treinar esses vocabulários (GPT, Claude, Gemini).

## Palavras Raras Custam Mais Tokens

Palavras incomuns no corpus de treino (nomes inventados, jargão raro) são fragmentadas em mais tokens do que palavras frequentes, porque o vocabulário não tem um chunk único que as represente. O mesmo efeito penaliza idiomas pouco representados no corpus — ver [[token-tax-multilingual]] — e linguagens de programação menos populares.

## Conexões

- [[byte-pair-encoding]] — algoritmo de treinamento de vocabulário mais usado na prática
- [[token-tax-multilingual]] — consequência da tokenização para idiomas não-ingleses
- [[token-economics]] — custo é cobrado por token de entrada e saída, a taxas diferentes

## Key Sources

- [[wiki/sources/tokens-llm-fundamentos-typescript]]
