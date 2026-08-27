---
type: concept
title: "Sistemas Operacionais (Conceito Central)"
aliases: ["SO", "operating system", "OS"]
date_created: 2026-08-27
date_updated: 2026-08-27
source_count: 1
tags: [cs-fundamentals, sistemas-operacionais, baixo-nivel, aprendizado]
skill: cs-fundamentals
status: stub
---

# Sistemas Operacionais (Conceito Central)

Camada de software que atua como **interface entre o hardware e as aplicações**: responsável por troca de tarefas, execução concorrente aparente de múltiplos programas, sistema de arquivos, gerenciamento de memória (incluindo `malloc` e proteção de memória) e gerenciamento de processos. Ver também páginas específicas do wiki como [[wiki/sources/como-sistemas-operacionais-funcionam]] e [[wiki/sources/8-sistemas-operacionais-explicados]] para panoramas complementares.

## Como porta de entrada para baixo nível

Em [[wiki/sources/guia-programacao-baixo-nivel-c-arquitetura-so-embarcados]], construir um sistema operacional do zero é apontado como uma das melhores formas práticas de aprender [[wiki/concepts/linguagem-c|programação de baixo nível]] — não precisa ser um Unix ou Windows completo, apenas algo funcional o suficiente para rodar em um dispositivo embarcado (Arduino, ESP). Um SO de estudo costuma exigir aplicar na prática [[wiki/concepts/gerenciamento-de-memoria|gerenciamento de memória]] manual, [[wiki/concepts/interrupcao-de-hardware|interrupções]] e conceitos de [[wiki/concepts/arquitetura-de-computadores|arquitetura de computadores]].

Diferença apontada frente a [[wiki/concepts/sistemas-embarcados]]: ao estudar SO, muitas vezes é possível abstrair a arquitetura específica (x86, ARM) do processador; em embarcados, isso não é possível.

## Fonte recomendada (português)

[[wiki/entities/carlos-maziero]] (UFPR) — livro de sistemas operacionais com projeto acompanhante de construção de SO do zero (citado como "PingOS", baseado em POSIX/Unix), citado como usado pelo autor de [[wiki/sources/guia-programacao-baixo-nivel-c-arquitetura-so-embarcados]] durante a graduação.

## Key sources

- [[wiki/sources/guia-programacao-baixo-nivel-c-arquitetura-so-embarcados]]
