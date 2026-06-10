# Você paga 62% a mais usando IA em português

**Fonte:** transcrição de vídeo (canal PascaDev)
**Idioma original:** Português (Brasil)
**Data estimada:** 2025–2026

---

## O que é um token

Você está pagando mais caro para usar IA do que um dev americano — não porque você tem um plano diferente ou porque a moeda é diferente, mas porque você está escrevendo em português.

Toda IA cobra por **tokens**, não por caracteres nem por palavras. Claude, GPT, Gemini — todos usam essa unidade de cobrança. Você pode visualizar os tokens na página do Hugging Face (tokenizer playground), que exibe os tokens com cores.

Exemplo em inglês:

> "Palmeiras don't have a world championship"

Cada palavra comum vira **um token**: `don't`, `have`, `road`, `championship`. Já `Palmeiras`, por ser menos comum, é quebrado em **três tokens**.

A regra geral: palavras comuns em inglês = 1 token. Palavras longas ou incomuns são quebradas em pedaços.

---

## O imposto do português

A mesma frase em português usa **mais tokens** para expressar a mesma informação. Isso é chamado de **token tax** (imposto do token).

Um estudo comparou os principais tokenizadores normalizando pelo inglês (multiplicador 1):

| Idioma     | Multiplicador (Anthropic) |
|------------|--------------------------|
| Inglês     | 1.04                     |
| Espanhol   | ~1.1                     |
| Francês    | ~1.3                     |
| Português  | **~1.62**                |
| Chinês, Russo, Árabe | ainda maiores |

**Português custa 62% a mais em tokens** do que o inglês.

---

## Por que isso acontece

Os modelos usam um algoritmo chamado **BPE (Byte Pair Encoding)**. A ideia é pegar um corpo enorme de texto e juntar os pares de caracteres mais frequentes em um único token. O resultado é um vocabulário que reflete a frequência desses padrões nos dados de treinamento.

- Palavras muito comuns em inglês → um token só
- Palavras menos comuns (como "Palmeiras") → quebradas em partes
- Palavras em português → quebradas em pedaços menores porque aparecem menos nos dados de treinamento

**Não é um bug.** É consequência direta de onde os dados de treinamento estão concentrados. O Anthropic é o pior dentre os principais provedores nesse quesito — não por má intenção, mas porque o foco do treinamento favorece menos idiomas não-ingleses.

À medida que os modelos treinarem com mais dados multilíngues, isso vai melhorando. Mas hoje é assim.

---

## Impacto prático no Claude Code

Se você usa Claude Code e tem um `CLAUDE.md` com 500 linhas em português:

- Aquele arquivo consome **62% mais context budget** do que se fosse em inglês
- Cada sessão, cada spec escrita em português: **62% mais tokens**
- Cada prompt em português: **62% mais tokens**
- Em um mês de uso intenso: **dinheiro real ou context budget desperdiçado**

---

## Suas três opções

### Opção 1 — Escreva tudo em inglês
Se você já trabalha com inglês, manter prompts, código, documentação e `CLAUDE.md` em inglês é o mais natural e o de melhor custo-benefício.

### Opção 2 — Artefatos em inglês, conversas em português
Seu `CLAUDE.md`, specs e documentação ficam em inglês (onde você tem ganho de contexto o tempo todo). Suas conversas do dia a dia com o agente ficam em português, se preferir. É o equilíbrio para quem tem dificuldade com o inglês técnico.

### Opção 3 — Ignore e aceite o custo
Se você usa um plano com limite generoso, se a empresa está pagando, se o projeto é pequeno ou se a comunicação em inglês comprometeria a qualidade do trabalho — use português e aceite que está pagando mais. A decisão depende do seu contexto.

---

## O que o autor faz

- `CLAUDE.md` e specs em inglês
- Conversas com o agente em inglês (por trabalhar em inglês)
- Para ele, é o melhor dos dois mundos

---

## Contexto maior

Esse vídeo faz parte de uma série sobre **como trabalhar com IA de forma eficiente** — não só barata, mas eficiente de verdade:

- Specs e como planejar contextos
- Testes que guiam o agente a saber quando o trabalho terminou
- Paralelismo de agentes

O canal (PascaDev) está preparando um treinamento completo: **Spec Driven com Claude Code**, do básico até paralelizar agentes.
