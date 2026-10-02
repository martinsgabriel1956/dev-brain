---
type: concept
title: "Custo de abstração em runtime"
aliases: ["runtime overhead", "sobrecarga de linguagem de alto nível"]
date_created: 2026-10-02
date_updated: 2026-10-02
source_count: 1
tags: [lang-systems, desempenho, runtime, abstracao, gc, interpretador]
skill: lang-systems
status: draft
---

# Custo de abstração em runtime

Cada camada que uma linguagem adiciona entre a lógica e o hardware tem preço: interpretador (CPython), motor/JIT (V8), VM (JVM), coletor de lixo (Go, Java, JS). O artigo em [[wiki/sources/c-linguagem-do-futuro-na-era-da-ia-bora-tomar-cafe]] resume: "C roda na velocidade do hardware; o resto roda na velocidade da camada de abstração".

## Comparativo (skill: lang-systems, `languages-transversal.md`)

| Modelo de memória | Linguagens | Overhead/pausa GC |
|---|---|---|
| Tracing GC | Java, C#, Go, JS, Python | variável |
| Ownership | Rust | zero |
| Manual | C, C++ | zero |

Ver [[wiki/concepts/gerenciamento-de-memoria]] e [[wiki/concepts/compilador]] (compilado vs interpretado vs bytecode+VM).

## Alegações da fonte

- Python 10–100× mais lento que C [external, ordem de grandeza plausível para CPU-bound em CPython puro; **não verificado**; muda com I/O-bound ou libs nativas].
- Binário C em KB vs. runtime de ~50 MB [alegação; a apresentadora nota que comparar runtime com binário é retórico].

## Contraponto

O custo é a contrapartida de [[wiki/concepts/abstracao]] e segurança. Quando vale pagar? Quando o gargalo é CPU/memória/embarcado; em serviços I/O-bound o custo costuma ser irrelevante [inferência].

## Key sources

- [[wiki/sources/c-linguagem-do-futuro-na-era-da-ia-bora-tomar-cafe]] — o argumento de overhead de Python/JS/Java/Go/Rust vs C
