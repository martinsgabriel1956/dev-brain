---
type: concept
title: "Calling Convention"
aliases: ["convenção de chamada", "calling conventions", "call convention"]
date_created: 2026-05-02
date_updated: 2026-05-02
source_count: 1
tags: [abi, sistemas, assembly, registradores]
skill: lang-systems
status: stable
---

# Calling Convention

Conjunto de regras que define **como uma função é chamada a nível de hardware**: quais registradores carregam os parâmetros, em qual ordem, quem salva e restaura registradores, e onde o valor de retorno é depositado.

Faz parte da [[concepts/abi]] e é o ponto mais comum de falha ao misturar linguagens.

## O problema

Duas linguagens podem gerar assembly válido para a mesma CPU e ainda assim falhar ao interoperar:

```
Chamador (Linguagem A):           Chamado (Linguagem B):
  mov rdi, arg1                     ; espera arg1 em rsi
  mov rsi, arg2                     ; espera arg2 em rdx
  call funcao                       mov rax, [rsi + rdx]  ← lê valores errados
```

Nenhum dos dois está "errado" — eles simplesmente seguem convenções diferentes.

## Convenções comuns (x86-64)

### System V AMD64 ABI (Linux, macOS)
- Parâmetros inteiros: `rdi`, `rsi`, `rdx`, `rcx`, `r8`, `r9` (nessa ordem)
- Parâmetros float: `xmm0`–`xmm7`
- Valor de retorno: `rax` (inteiro), `xmm0` (float)
- Callee-saved: `rbx`, `rbp`, `r12`–`r15`

### Microsoft x64 ABI (Windows)
- Parâmetros: `rcx`, `rdx`, `r8`, `r9`
- Valor de retorno: `rax`
- Shadow space: 32 bytes reservados na stack antes de qualquer call

## Por que C é o "esperanto"

A C ABI é estável e bem documentada. Quando uma linguagem quer interoperar com outra, o caminho mais fácil é ambas adotarem a C calling convention — é o que `extern "C"` faz em C++ e Rust.

## Relação com name mangling

C++ e Rust renomeiam símbolos internamente (ex: `namespace::Foo::bar` vira `_ZN9namespace3Foo3barEv`). Para expor uma função com nome previsível para o linker:
- C++: `extern "C" void minha_func() { ... }`
- Rust: `#[no_mangle] pub extern "C" fn minha_func() { ... }`

## Key Sources

- [[sources/como-multiplas-linguagens-vivem-num-unico-binario]]
