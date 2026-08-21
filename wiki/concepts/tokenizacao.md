---
type: concept
title: "Tokenização"
aliases: ["token", "tokens", "encode/decode llm", "vocabulário de tokens"]
date_created: 2026-07-03
date_updated: 2026-08-17
source_count: 3
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

## Por que Não Tokenizar Letra-por-Letra nem Palavra-por-Palavra

Os dois extremos de granularidade têm problemas opostos: tokenização por caractere explode o custo computacional (mais tokens por frase, e o modelo precisa "descobrir" a cada cálculo que letras adjacentes formam uma única palavra, desperdiçando raciocínio); tokenização por palavra completa explode o vocabulário necessário, porque seria preciso mapear não só toda palavra de toda língua, mas todas as suas flexões (ex.: "corre", "corria", "corríamos" viram entradas separadas). Subword tokens (via [[byte-pair-encoding]]) resolvem os dois problemas ao quebrar palavras em pedaços reaproveitáveis entre flexões — o prefixo "corr" é comum a todas as variações de "corre", só o sufixo muda. Ver [[wiki/sources/tokens-o-que-sao-e-por-que-custam-caro]].

## Palavras Raras Custam Mais Tokens

Palavras incomuns no corpus de treino (nomes inventados, jargão raro) são fragmentadas em mais tokens do que palavras frequentes, porque o vocabulário não tem um chunk único que as represente. O mesmo efeito penaliza idiomas pouco representados no corpus — ver [[token-tax-multilingual]] — e linguagens de programação menos populares.

## Conexões

- [[byte-pair-encoding]] — algoritmo de treinamento de vocabulário mais usado na prática
- [[token-tax-multilingual]] — consequência da tokenização para idiomas não-ingleses
- [[token-economics]] — custo é cobrado por token de entrada e saída, a taxas diferentes

## Consequência Prática: Análise por Token ≠ Leitura Linha a Linha

[[wiki/sources/ia-nao-substitui-sistemas-corporativos-deterministicos]] traz um exemplo concreto do custo de a IA operar sobre tokens em vez de texto: um LLM não lê um programa fonte linha a linha como um humano — ele tokeniza o conteúdo, monta contexto e gera resposta por probabilidade. Isso explicou, no relato do autor, por que três LLMs diferentes (ChatGPT, Claude, Gemini) falhavam de forma inconsistente em uma checagem sintática trivial (identificar se um programa COBOL estava em free format ou fixed format) — uma tarefa que um parser determinístico resolve sem ambiguidade, mas que depende de reconstrução probabilística a partir de tokens para um LLM. Ver [[wiki/concepts/determinismo-vs-probabilismo-em-ia]].

## Key Sources

- [[wiki/sources/tokens-llm-fundamentos-typescript]]
- [[wiki/sources/ia-nao-substitui-sistemas-corporativos-deterministicos]] — caso real de falha em checagem sintática trivial por processamento via tokens em vez de leitura linha a linha
- [[wiki/sources/tokens-o-que-sao-e-por-que-custam-caro]] — por que subword tokens vencem letra-por-letra e palavra-por-palavra; experimento comparando GPT-4o vs. Claude Opus 5
