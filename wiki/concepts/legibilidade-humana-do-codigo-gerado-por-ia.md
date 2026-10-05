---
type: concept
title: "Legibilidade humana do código gerado por IA como controle"
aliases: ["código legível como segurança", "humano no loop de leitura de código"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_count: 1
tags: [ia, codigo-gerado-por-ia, seguranca, revisao-de-codigo, legibilidade, governanca]
skill: lang-systems
status: draft
---

# Legibilidade humana do código gerado por IA como controle

Tese de [[wiki/entities/ricardo-albuquerque]] em [[wiki/sources/c-linguagem-do-futuro-ia-assembly-opcode-safe-source-ricardo-albuquerque]]: mesmo quando a IA escreve o código, **o código precisa continuar legível por humanos** porque a leitura é um mecanismo de controle — permite pegar algoritmos ineficientes ou errados ("muda esse algoritmo") e auditar os passos da IA. Contrapõe-se a [[wiki/concepts/abstracoes-como-protecao-cognitiva-humana]], que trata a legibilidade só como custo.

## Gradiente de auditabilidade

Linguagem de alto nível > C (grande base de leitores) > [[wiki/concepts/assembly]] (pouquíssimos) > opcode (ninguém). Quanto mais baixo o alvo, menor o conjunto de revisores e mais difícil a revisão — o que limita [[wiki/concepts/ia-gerando-binario-direto]].

## Ressalvas

- O autor admite que, com IA melhor, a revisão humana pode deixar de importar.
- Legível ≠ revisável: em C, falhas de memória sutis ([[wiki/concepts/memory-safety]]) escapam a leitores experientes; revisão deve somar-se a ferramentas — ver [[wiki/concepts/governanca-de-codigo-gerado-por-ia]], [[wiki/concepts/code-review]] [inferência].

## Key sources

- [[wiki/sources/c-linguagem-do-futuro-ia-assembly-opcode-safe-source-ricardo-albuquerque]] — leitura do código como característica de segurança
