---
type: concept
title: "C como linguagem-alvo de código gerado por IA"
aliases: ["c volta a ser o rei", "c na era da ia"]
date_created: 2026-10-02
date_updated: 2026-10-05
source_count: 2
tags: [linguagem-c, ia, codigo-gerado-por-ia, desempenho, memory-safety, opiniao]
skill: lang-systems
status: draft
---

# C como linguagem-alvo de código gerado por IA

**Tese** (artigo lido em [[wiki/sources/c-linguagem-do-futuro-na-era-da-ia-bora-tomar-cafe]]): se a IA escreve o código, o custo cognitivo de [[wiki/concepts/linguagem-c]] (ponteiros, memória manual, segfaults) deixa de importar, e sobra só a vantagem: zero overhead de runtime, binários mínimos, controle de hardware ([[wiki/concepts/custo-de-abstracao-em-runtime]]). Logo, C seria a melhor linguagem para código gerado.

## Onde a tese é forte

- O argumento de desempenho é real: C não tem GC, VM nem interpretador; roda de microcontroladores a supercomputadores [skill: lang-systems].
- Remove a premissa que justificava o alto nível: [[wiki/concepts/abstracoes-como-protecao-cognitiva-humana]].

## Onde é fraca (tensões)

- **"A IA não esquece de liberar memória"** é forte demais: instruções se perdem na janela de contexto (ressalva da apresentadora na fonte).
- **Segurança:** código de IA já tem mais falhas que o humano e degrada com iterações ([[wiki/sources/codigo-gerado-por-ia-mais-falhas-seguranca-degradacao-iterativa]]); em C, falhas viram corrupção de memória/UB. [inferência]
- **Humanos ainda leem e mantêm** o código gerado ([[wiki/concepts/governanca-de-codigo-gerado-por-ia]]); o argumento do "prédio vazio" ignora isso.
- **Alternativas:** linguagens com segurança de memória sem GC ([[wiki/concepts/rust-fundamentos]]) ou uma linguagem desenhada para IA ([[wiki/concepts/linguagem-de-programacao-pensada-para-ia]]). Para a maioria dos sistemas, o gargalo é I/O, não CPU [inferência, não verificado].

## Status

Tese de opinião sem benchmark ou caso real; confiança baixa-média.

## Key sources

- [[wiki/sources/c-linguagem-do-futuro-na-era-da-ia-bora-tomar-cafe]] — tese central e contrapontos da apresentadora
- [[wiki/sources/c-linguagem-do-futuro-ia-assembly-opcode-safe-source-ricardo-albuquerque]] — endosso do desempenho + dois contra-argumentos: por que não assembly/opcode ([[wiki/concepts/ia-gerando-binario-direto]]) e legibilidade como controle ([[wiki/concepts/legibilidade-humana-do-codigo-gerado-por-ia]])
