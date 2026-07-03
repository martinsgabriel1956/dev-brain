---
type: concept
title: "Token Tax Multilingual"
aliases: ["token tax", "imposto do token", "custo idioma tokens", "multilingual token penalty"]
date_created: 2026-06-09
date_updated: 2026-07-03
source_count: 2
tags: [token-economics, tokenizacao, bpe, custo-ia, portugues, llm]
skill: tech-mentor-ai
status: stable
---

## Definição

Penalidade de custo que idiomas não-ingleses pagam ao usar LLMs, causada pelo [[byte-pair-encoding]] ser treinado predominantemente em dados em inglês. A mesma informação expressa em português custa mais tokens do que em inglês — não porque é mais longa, mas porque é tokenizada de forma menos eficiente.

---

## Multiplicadores por Idioma (Anthropic)

Normalizando pelo inglês como baseline (1×):

| Idioma     | Multiplicador |
|------------|--------------|
| Inglês     | 1.04×        |
| Espanhol   | ~1.1×        |
| Francês    | ~1.3×        |
| **Português** | **~1.62×** |
| Chinês, Russo, Árabe | >1.62× |

> Fonte: estudo comparativo de tokenizadores; números do Anthropic (Claude). Outros provedores apresentam penalidades menores para idiomas não-ingleses.

**Português paga 62% a mais em tokens para expressar a mesma informação que em inglês.**

---

## Por que Isso Existe

O algoritmo [[byte-pair-encoding]] cria um vocabulário de tokens baseado na frequência de padrões no corpus de treinamento. Como esse corpus é predominantemente em inglês:

- Palavras comuns em inglês → 1 token
- Palavras em inglês menos comuns → 2–3 tokens
- Palavras em português → quebradas em mais pedaços porque aparecem com menor frequência no corpus

Não é um bug de design intencional — é consequência direta de onde os dados de treinamento estão concentrados. Melhora à medida que os modelos treinam com mais dados multilíngues.

O mesmo efeito ocorre com qualquer padrão pouco frequente no corpus, não só idiomas: a palavra inventada `"frabjous"` (poema *Jabberwocky*, Lewis Carroll) é dividida em 4 tokens separados pelo tokenizer `o200k_base` (GPT-4o) — muito mais que uma palavra comum receberia. Idiomas não-ingleses pagam essa mesma penalidade de forma sistemática porque, em bloco, seus padrões são menos frequentes no corpus de treino. O efeito também penaliza linguagens de programação menos populares (ex. Haskell) frente às mais usadas (ex. JavaScript): menos tokens por linha de código é mais uma vantagem de adoção na era da IA.

---

## Impacto Prático no Dia a Dia

### No Claude Code

Um `CLAUDE.md` de 500 linhas em português:
- Consome **62% mais context budget** por sessão do que em inglês
- O custo se repete em **toda sessão**, não só na primeira vez

### Em Specs e Documentação

Cada spec em português = 62% mais tokens por spec. Em um mês de uso intenso com [[spec-driven-development]], o acúmulo é significativo.

### No Budget de Contexto

A [[janela-de-contexto]] se esgota mais rápido quando o conteúdo está em português. O fenômeno agrava [[token-anxiety]] em devs não-anglófonos.

---

## Estratégias de Mitigação

| Estratégia | Quando usar | Trade-off |
|---|---|---|
| Tudo em inglês | Você já trabalha em inglês | Nenhum |
| Artefatos em inglês, conversas em português | Inglês técnico é barreira | Menor ganho que "tudo em inglês" |
| Ignorar e aceitar o custo | Projeto pequeno / empresa paga | Custo real em uso intenso |

A decisão depende do contexto — não há resposta universalmente certa.

---

## Conexões

- [[byte-pair-encoding]] — o algoritmo que causa a token tax
- [[janela-de-contexto]] — se esgota mais rápido em português
- [[claude-md]] — CLAUDE.md em português custa 62% mais por sessão
- [[token-anxiety]] — token tax amplifica a ansiedade de devs não-anglófonos
- [[paradoxo-de-jevons]] — token mais barato + token tax = custo ainda relevante para devs brasileiros
- [[spec-driven-development]] — specs em português custam 62% mais tokens
- [[tokenizacao]] — conceito geral de token e vocabulário; palavras raras em qualquer idioma sofrem o mesmo efeito

---

## Key Sources

- [[wiki/sources/custo-tokens-portugues-vs-ingles]]
- [[wiki/sources/tokens-llm-fundamentos-typescript]]
