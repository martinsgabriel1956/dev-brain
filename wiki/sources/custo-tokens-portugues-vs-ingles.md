---
type: source
title: "Você paga 62% a mais usando IA em português"
aliases: ["token tax português", "custo tokens idioma", "BPE multilingual"]
date_created: 2026-06-09
date_updated: 2026-06-09
source_count: 0
tags: [token-economics, tokenizacao, bpe, claude-code, custo-ia, portugues]
skill: tech-mentor-ai
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/custo-tokens-portugues-vs-ingles.md
source_url: ""
author: "PascaDev (não identificado por nome)"
date_published: "2025-2026"
date_ingested: 2026-06-09
---

# Você paga 62% a mais usando IA em português

## TL;DR

Escrever prompts, specs e `CLAUDE.md` em português custa **62% mais tokens** do que em inglês, devido ao algoritmo BPE (Byte Pair Encoding) dos tokenizadores de LLMs ser treinado predominantemente em dados em inglês. O Anthropic é o pior provedor nesse quesito entre os principais. A decisão de idioma é uma decisão de custo — e a maioria dos devs brasileiros não sabe disso.

---

## Key Claims

### 1. Toda IA cobra por tokens, não por palavras ou caracteres
**Evidência:** Claude, GPT, Gemini — todos usam tokens como unidade de cobrança. Palavras comuns em inglês viram um token só. Palavras longas ou incomuns (como "Palmeiras") são quebradas em múltiplos tokens.
**Confiança:** Alta (fato técnico bem estabelecido)

### 2. Português custa 62% mais tokens que inglês no Anthropic
**Evidência:** Estudo comparativo dos principais tokenizadores normalizando pelo inglês (multiplicador 1). Tabela publicada que ficou viral:
- Inglês: 1.04×
- Espanhol: ~1.1×
- Francês: ~1.3×
- **Português: ~1.62×**
- Chinês, Russo, Árabe: ainda maiores

**Confiança:** Alta (estudo citado, números consistentes com comportamento observável)

### 3. O Anthropic é o pior provedor para idiomas não-ingleses entre os principais
**Evidência:** Na comparação do estudo, Anthropic apresenta penalidade maior que OpenAI/Google para espanhol e francês.
**Confiança:** Média (fonte do estudo não linkada na transcrição; afirmação plausível dado BPE treinado em dados ingleses)

### 4. A causa técnica é o BPE (Byte Pair Encoding)
**Evidência:** BPE junta os pares de caracteres mais frequentes no corpus de treinamento em um único token. Como dados de treinamento são predominantemente em inglês, o vocabulário de tokens é otimizado para inglês. Não é um bug — é consequência direta dos dados de treinamento.
**Confiança:** Alta (mecanismo técnico bem documentado)

### 5. Impacto prático no Claude Code é substancial
**Evidência:** Um `CLAUDE.md` de 500 linhas em português consome 62% mais context budget por sessão do que em inglês. O efeito acumula em cada prompt, spec e documento no contexto.
**Confiança:** Alta (cálculo direto da multiplicação do token multiplier)

---

## Entities

- [[wiki/entities/anthropic]] — criadora do Claude; BPE do Claude é o mais penalizador para idiomas não-ingleses entre os principais provedores
- [[wiki/entities/pascadev]] — canal que produziu o vídeo (autor não identificado por nome)

---

## Concepts

- [[wiki/concepts/token-tax-multilingual]] — o fenômeno central: idiomas não-ingleses pagam mais tokens para expressar a mesma informação
- [[wiki/concepts/byte-pair-encoding]] — algoritmo que explica por que a token tax existe
- [[wiki/concepts/janela-de-contexto]] — idioma afeta diretamente o consumo do context budget
- [[wiki/concepts/claude-md]] — CLAUDE.md em português consome 62% mais contexto por sessão
- [[wiki/concepts/token-anxiety]] — token tax amplifica a ansiedade de devs não-anglófonos
- [[wiki/concepts/paradoxo-de-jevons]] — token mais barato + token tax = conta ainda maior para devs brasileiros
- [[wiki/concepts/spec-driven-development]] — specs em português custam 62% mais tokens que em inglês

---

## Três Opções para Lidar com a Token Tax

1. **Escreva tudo em inglês** — melhor custo-benefício se você já trabalha em inglês
2. **Artefatos em inglês, conversas em português** — equilíbrio para quem tem dificuldade com inglês técnico
3. **Ignore e aceite o custo** — válido se o projeto é pequeno, a empresa paga, ou a qualidade da comunicação importa mais que o custo

---

## Open Questions

- O estudo específico citado não foi linkado na transcrição — verificar fonte primária antes de usar os números como referência definitiva.
- Espera-se melhora à medida que modelos treinarem com mais dados multilíngues — quando isso se tornará perceptível no multiplier do português?
- Existe ferramenta que calcula automaticamente o custo extra por arquivo em português no contexto?

---

## Key Sources

_(este é o documento de origem)_
