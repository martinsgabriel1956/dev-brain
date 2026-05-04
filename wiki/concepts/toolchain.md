---
type: concept
title: "Toolchain"
aliases: ["compiler toolchain", "build toolchain", "gcc toolchain"]
date_created: 2026-05-02
date_updated: 2026-05-02
source_count: 1
tags: [compilacao, gcc, sistemas, build]
skill: lang-systems
status: stable
---

# Toolchain

Um **pipeline de ferramentas** executadas em sequência, onde cada etapa consome o output da anterior. O que chamamos casualmente de "compilador" geralmente é uma toolchain inteira.

## Por que importa

Pensar em "compilador" como caixa preta esconde a modularidade real. Entender que é uma toolchain explica:
- Por que podemos misturar linguagens (cada uma produz um [[concepts/object-file]], o linker une tudo)
- Por que podemos inspecionar fases intermediárias (`gcc -S` para ver o assembly)
- Por que podemos substituir componentes (trocar o linker, usar Clang como frontend do LLVM)

## GCC como exemplo

GCC = **GNU Compiler Collection** (não "GNU C Compiler" — o nome foi expandido).

| Ferramenta | Fase | Input → Output |
|-----------|------|---------------|
| `cpp` | Pré-processamento | `.c` → `.i` (C processado) |
| `cc1` | Compilação | `.i` → `.s` (assembly) |
| `as` | Montagem | `.s` → `.o` (object file) |
| `ld` | Linking | `.o` + libs → executável |

GCC suporta: C, C++, Objective-C, Fortran, Ada, D, Go (dependendo da configuração).

## Toolchains de outras linguagens

| Linguagem | Toolchain | Backend |
|----------|-----------|---------|
| Rust | rustc + cargo | LLVM |
| C/C++ (Clang) | clang + lld | LLVM |
| Swift | swiftc | LLVM |
| Go | gc (compilador próprio) | SSA próprio |
| Zig | zig build | LLVM |

## Plugabilidade

O último passo de qualquer toolchain passa pelo **linker** — e é aí que linguagens diferentes se encontram. Rust pode linkar com object files produzidos pelo GCC, e vice-versa, porque o formato de object file (ELF no Linux, Mach-O no macOS, PE no Windows) é um padrão neutro.

## Key Sources

- [[sources/como-multiplas-linguagens-vivem-num-unico-binario]]
