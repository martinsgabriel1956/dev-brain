---
type: concept
title: "FFI — Foreign Function Interface"
aliases: ["FFI", "foreign function interface", "interop", "interoperabilidade de linguagens"]
date_created: 2026-05-02
date_updated: 2026-05-02
source_count: 1
tags: [ffi, abi, interoperabilidade, sistemas, rust, c, go]
skill: lang-systems
status: stable
---

# FFI — Foreign Function Interface

Mecanismo que permite chamar funções de uma linguagem a partir de outra dentro do **mesmo processo**. É a camada de código que faz a [[concepts/abi]] funcionar na prática.

## Como funciona

1. Uma linguagem compila sua função para um [[concepts/object-file]] seguindo a C ABI
2. A outra linguagem declara a assinatura da função externa
3. O linker conecta as duas — o caller sabe onde encontrar o callee
4. Em runtime, os parâmetros são passados conforme a [[concepts/calling-convention]] acordada

## Mecanismos por linguagem

### C
```c
// Declara função implementada em outra linguagem
extern int calcular_primos(int limite);

// Usa normalmente
int resultado = calcular_primos(1000);
```

### Rust
```rust
// Expor função Rust para C:
#[no_mangle]  // desativa name mangling — nome previsível para o linker
pub extern "C" fn calcular_primos(limite: i32) -> i32 {
    // ...
}

// Chamar função C a partir de Rust:
extern "C" {
    fn funcao_em_c(x: i32) -> i32;
}

unsafe { funcao_em_c(42) }
```

### Go (CGo)
```go
// #include <stdlib.h>
// int calcular_primos(int limite);
import "C"

result := C.calcular_primos(1000)
```
CGo permite inclusive escrever código C inline nos comentários acima do `import "C"`.

### Fortran
```fortran
! Usar BIND(C) para conformar com C ABI
function calcular_primos(limite) BIND(C, NAME='calcular_primos')
  use iso_c_binding
  integer(c_int), value :: limite
  integer(c_int) :: calcular_primos
end function
```

## Direção mais comum

**C → Rust** e **Rust → C** são os casos mais frequentes. C é mais antigo — bibliotecas maduras de gráficos, criptografia e APIs de SO estão em C. Rust precisa acessar esse ecossistema.

**Python → C** via `ctypes` ou `cffi` também é extremamente comum (NumPy, PyTorch são extensions C/C++).

## Custo de FFI

Chamar através da FFI tem overhead:
- Conversão de tipos (especialmente strings — cada linguagem tem sua representação)
- `unsafe` em Rust — o compilador não pode verificar invariants além da fronteira
- Marshal/unmarshal de dados complexos

Para chamadas frequentes em hot paths, considere minimizar cruzamentos de fronteira ou usar memória compartilhada.

## Projetos reais que usam FFI

- **Linux kernel:** C + assembly (FFI via chamada direta, mesma C ABI)
- **ffmpeg:** C + assembly para codecs de vídeo de alta performance
- **OpenSSL:** C + assembly para operações criptográficas

## Key Sources

- [[sources/como-multiplas-linguagens-vivem-num-unico-binario]]
