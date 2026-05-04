---
type: concept
title: "ABI — Application Binary Interface"
aliases: ["ABI", "application binary interface", "interface binária"]
date_created: 2026-05-02
date_updated: 2026-05-02
source_count: 1
tags: [abi, sistemas, linking, ffi, interoperabilidade]
skill: lang-systems
status: stable
---

# ABI — Application Binary Interface

Define como componentes de código binário interagem entre si através do hardware. É o contrato de baixo nível que permite que code de linguagens diferentes coexista num único processo.

## Analogia com API

| | API | ABI |
|--|-----|-----|
| Nível | Código-fonte | Binário / hardware |
| Define | Assinaturas de funções | Como parâmetros são passados em registradores |
| Quem usa | Desenvolvedor | Compilador / linker |
| Quebra quando | Muda a assinatura | Muda a calling convention ou layout de memória |

## O que a ABI especifica

1. **[[concepts/calling-convention]]** — em quais registradores os parâmetros são passados, em qual ordem, quem salva/restaura registradores
2. **Layout de structs em memória** — alinhamento, padding, ordem dos campos
3. **Semântica de passagem de argumentos** — pass by value vs pass by reference
4. **Name mangling** — como o compilador renomeia símbolos (C++ e Rust fazem mangling; C não)
5. **Exceções / unwinding** — como exceções propagam através de frames de diferentes linguagens

## Exemplo de falha de ABI

**Problema 1 — Registradores errados:**
```
Linguagem A chama f(x, y):
  → coloca x em reg0, y em reg1

Linguagem B implementa f(x, y):
  → espera x em reg1, y em reg2

Resultado: comportamento indefinido — parâmetros errados nos registradores errados
```

**Problema 2 — Pass by reference vs pass by value:**
```
Linguagem X passa argumentos por referência (endereços de memória nos registradores)
Linguagem Y espera valores diretos nos registradores

Resultado: Linguagem Y interpreta endereços como valores → soma endereços em vez de valores
```

## Como conformar a ABI

Cada linguagem tem mecanismos para declarar que uma função deve seguir a ABI de outra:

| Linguagem | Mecanismo |
|----------|-----------|
| C | `extern` (declara função externa) |
| Rust | `extern "C"` + `#[no_mangle]` |
| Fortran | atributo `BIND(C)` |
| Go | bloco CGo com comentários especiais + `import "C"` |
| C++ | `extern "C" { ... }` (desativa name mangling) |

## ABI Estável vs Instável

- **C ABI** — estável há décadas, é o "esperanto" de interoperabilidade entre linguagens
- **C++ ABI** — instável entre compiladores e versões (motivo pelo qual `extern "C"` é necessário)
- **Rust ABI** — intencionalmente instável; use `extern "C"` para FFI estável
- **Go ABI** — mudou no Go 1.17 (register-based); CGo usa C ABI

## Key Sources

- [[sources/como-multiplas-linguagens-vivem-num-unico-binario]]
