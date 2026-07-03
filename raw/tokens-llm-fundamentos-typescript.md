# Tokens em LLMs — Fundamentos com TypeScript

**Fonte:** Vídeo (canal de Matt Pocock, AI Hero — conteúdo de AI + TypeScript)
**Tema:** O que são tokens, como tokenizers são treinados, e por que diferentes provedores de LLM produzem contagens de tokens diferentes para o mesmo texto

---

## Motivação

O autor estava ministrando um workshop de IA na Polônia e pediu para quem soubesse o que é um token levantar a mão — apenas um terço da sala levantou. Isso motivou este deep dive: muitos devs usam LLMs no dia a dia sem entender o que acontece "por baixo do capô". Todos os exemplos de código são em TypeScript (o autor promete nunca mostrar uma linha de Python no canal).

---

## Tokens são a moeda dos LLMs

Ao enviar `"Hello World"` para um LLM, o texto é quebrado em tokens constituintes. Para a OpenAI, `"Hello World"` vira 3 tokens, cobrados a uma fração de centavo por 1.000 tokens (exemplo usando preços do GPT-5).

Fluxo de custo:
1. O LLM recebe os tokens de entrada (input tokens) e "pensa".
2. Produz tokens de saída (output tokens), cobrados a uma taxa diferente da entrada.
3. Custo total = (tokens de entrada / 1000 × preço de entrada) + (tokens de saída / 1000 × preço de saída).

### Demonstração com o AI SDK

Usando o AI SDK (Vercel) para gerar texto:

**Claude 3.5 Haiku (Anthropic)** — prompt: `"Hello World"`
- Resposta: *"Hello! How are you doing today? Is there anything I can help you with?"*
- Uso: **11 tokens de entrada**, **20 tokens de saída**
- Estranho: 11 tokens de entrada para apenas duas palavras.

**Gemini 2.0 Flash Lite (Google)** — mesmo prompt
- Uso: **4 tokens de entrada**, **11 tokens de saída**

Mesmo prompt, dois provedores, contagens de tokens completamente diferentes — o que motiva a pergunta central do vídeo: qual é a relação entre tokens e texto, e por que ela varia entre modelos?

---

## O que são tokens, de fato

Cada LLM tem seu próprio **vocabulário de tokens**: todas as palavras, subpalavras e caracteres que o modelo conhece. Cada item do vocabulário recebe um número — esse número é o token.

Processo de **encoding**:
1. O texto de entrada (`"Hello World!"`) é dividido nos maiores pedaços (chunks) reconhecidos pelo vocabulário — por exemplo `Hello`, ` World`, `!`.
2. Cada chunk é mapeado para o número correspondente no vocabulário.

### Exemplo em código com `js-tiktoken`

Usando o tokenizer `o200k_base` (tokenizer do GPT-4o) via `js-tiktoken`, a implementação JS do `tiktoken` da OpenAI:

- Texto de teste: um parágrafo de ~2.300 caracteres ("The wise owl of Moonlight Forest...") → menos de 500 tokens.
- Texto `"Hello World"`: 12 caracteres → apenas 3 tokens.

Ou seja, o número de tokens é sempre menor (ou igual) ao número de caracteres, porque tokens agrupam múltiplos caracteres.

### O pipeline completo do LLM

```
"Hello World" → encode (split em chunks do vocabulário → lookup do número)
             → tokens de entrada [numéricos]
             → LLM processa/"pensa" (tudo em números, não em texto)
             → tokens de saída [numéricos]
             → decode (lookup do chunk correspondente → concatenação)
             → texto de saída ("Hi")
```

O LLM **nunca processa texto diretamente** — ele opera inteiramente sobre representações numéricas (tokens). `tokenizer.decode()` faz o caminho inverso: recebe um array de números e retorna a string concatenada.

---

## Como os vocabulários de tokenizers são treinados

Vocabulários são construídos a partir de um **corpus de texto** (na prática, gigabytes/terabytes — geralmente os mesmos dados usados para treinar o modelo).

### Tokenizer nível-caractere (exemplo didático)

Usando o corpus mínimo `"the cat sat on the mat"`:

- Um `CharacterLevelTokenizer` extrai os caracteres únicos do corpus e monta um vocabulário só com eles (ex.: `space` = 3, `n` = 8, `o` = 7 etc.).
- Ao codificar `"cat sat mat"`: **11 caracteres → 11 tokens**. Como só existem caracteres no vocabulário, a contagem de tokens é sempre igual à contagem de caracteres.

Isso é ruim: quanto mais tokens na entrada, mais trabalho o LLM tem que fazer para processá-la. O **tamanho do vocabulário** é um fator crítico:

| Tamanho do vocabulário | `"understanding"` vira |
|---|---|
| ~1.000 tokens | `under` `st` `and` `ing` (5 tokens) |
| ~50.000 tokens | `under` `standing` (3 tokens) |
| ~200.000 tokens | 2 tokens |

Vocabulários maiores → menos tokens por texto → mais eficiência de processamento. Mas não escala ao infinito: vocabulários maiores exigem modelos maiores (mais memória, mais parâmetros) para "abrigar" o vocabulário.

### Tokenizer nível-subpalavra (exemplo didático)

Para reduzir a contagem de tokens, identifica-se grupos de caracteres que ocorrem juntos com frequência — ex.: `th` aparece em "the"; `he` também aparece em "the"; `at` aparece em "cat", "sat", "mat".

Com um `SubwordLevelTokenizer` (implementação simplificada, "vibe coded", segundo o autor) treinado no mesmo corpus:

- `"cat sat mat"` (11 caracteres) → **8 tokens** (contra 11 do tokenizer de caractere).
- O vocabulário resultante tem 15 tokens, incluindo `th`, `he`, ` a`, `t `, etc.
- O `encode()` fica mais complexo: precisa casar o **maior subword possível** a cada posição para tokenizar com eficiência.

Tokenizers reais vão além de um nível: identificam "grupos de grupos" recursivamente. Por exemplo, `th` + `e` formam `the` como um único token de 3 caracteres. O tokenizer de exemplo do vídeo só vai um nível fundo, então fica limitado a grupos de 2 caracteres.

Ao final, cada token do vocabulário é apenas um número — exatamente como visto na demonstração inicial com `o200k_base`.

---

## Palavras incomuns geram mais tokens

Teste com `"frabjous day"` (palavra inventada por Lewis Carroll, do poema *Jabberwocky*):

- Rodando via `o200k_base`: `"frabjous"` é dividido em **4 tokens separados** — muito mais que uma palavra comum receberia.

Implicações:
- Palavras raras/incomuns no corpus de treino → mais tokens.
- **Idiomas pouco representados** no corpus de treino do modelo tendem a ser quebrados em mais tokens (custo maior, mais lento).
- O mesmo vale para **linguagens de programação**: linguagens mais usadas (ex. JavaScript) tendem a ter menos tokens por linha de código do que linguagens menos usadas (ex. Haskell) — mais uma vantagem para linguagens populares na era da IA (menos tokens para enviar o mesmo código).

---

## Resumo

- Tokens são a moeda dos LLMs — você paga por token, e cada provedor cobra taxas diferentes para tokens de entrada e saída.
- Provedores diferentes usam tokenizers diferentes, então o mesmo prompt gera contagens de tokens diferentes entre eles.
- **Encoding**: texto → maiores chunks reconhecidos pelo vocabulário → números (tokens).
- **Decoding**: números (tokens) → chunks correspondentes → concatenação → texto.
- O LLM "pensa" inteiramente em tokens (números), nunca em texto bruto.
- O tamanho do vocabulário é um trade-off: vocabulários maiores = menos tokens por texto = mais eficiência, mas exigem modelos maiores.
- Tokenizers são treinados identificando subpalavras/grupos de caracteres frequentes no corpus, de forma incremental (grupos de grupos).
- Palavras raras, idiomas pouco representados e linguagens de programação menos populares tendem a gerar mais tokens por causa da baixa frequência no corpus de treino.

---

## Ferramentas e recursos citados

- **AI SDK** (Vercel) — usado para chamar Anthropic e Google e comparar `usage` (tokens de entrada/saída).
- **`tiktoken`** — tokenizer da OpenAI; **`js-tiktoken`** é a implementação JavaScript usada nos exemplos (`o200k_base`, tokenizer do GPT-4o).
- **AI Hero** (aihero.dev) — site/curso do autor sobre AI + TypeScript, com tutorial gratuito do AI SDK e newsletter.
