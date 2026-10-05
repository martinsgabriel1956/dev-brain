---
type: concept
title: "Memory safety (segurança de memória)"
aliases: ["segurança de memória", "buffer overflow", "use-after-free"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_count: 1
tags: [seguranca, lang-systems, memoria, rust, linguagem-c, vulnerabilidades]
skill: lang-systems
status: stub
---

# Memory safety

Propriedade de impedir acessos inválidos à memória — **buffer overflow**, **uso após o free** (use-after-free), ponteiros soltos, leaks. Em C/C++ a responsabilidade é do programador (comportamento indefinido); [[wiki/sources/c-linguagem-do-futuro-ia-assembly-opcode-safe-source-ricardo-albuquerque]] lembra que humanos "fatalmente erram" nisso e que isso abre ataques, razão da migração para alto nível e [[wiki/concepts/rust-fundamentos]].

## Abordagens [skill: lang-systems, `languages-transversal.md`]

| Abordagem | Exemplos | Overhead | Segurança |
|---|---|---|---|
| GC | Java, Go, Python | alto (pausas) | excelente |
| ARC | Swift | médio | boa (ciclos) |
| Ownership | Rust | zero | total em compile-time |
| Manual | C, C++ | zero | ruim (UB) |

Tema central da disputa em [[wiki/concepts/c-como-linguagem-alvo-de-codigo-gerado-por-ia]]: o ganho de desempenho do C devolve o risco. Ver [[wiki/concepts/gerenciamento-de-memoria]], [[wiki/concepts/aritmetica-de-ponteiros]].

## Key sources

- [[wiki/sources/c-linguagem-do-futuro-ia-assembly-opcode-safe-source-ricardo-albuquerque]] — erros humanos de memória e ataques decorrentes
