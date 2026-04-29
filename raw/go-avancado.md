---
date: 2026-04-24
tags: [tech-mentor, lang-systems, go, avancado, generics, memory-model, reflection, wasm, cgo]
skill: lang-systems/references/go
level: arquiteto
---

# Go — Avançado

## Contexto
Generics (1.18), memory model refinado (1.19) e melhorias de GC (1.21+) tornaram Go mais expressivo sem abrir mão da simplicidade. Esses recursos resolvem problemas reais — mas cada um tem custo de legibilidade que precisa ser pesado.

---

## Generics (Go 1.18+)

```go
// Função genérica com constraint
func Map[T, U any](s []T, f func(T) U) []U {
    result := make([]U, len(s))
    for i, v := range s {
        result[i] = f(v)
    }
    return result
}

// Constraint customizada
type Number interface {
    ~int | ~int32 | ~int64 | ~float32 | ~float64
}

func Sum[T Number](nums []T) T {
    var total T
    for _, n := range nums {
        total += n
    }
    return total
}

// Tipo genérico
type Stack[T any] struct {
    items []T
}

func (s *Stack[T]) Push(v T) {
    s.items = append(s.items, v)
}

func (s *Stack[T]) Pop() (T, bool) {
    var zero T
    if len(s.items) == 0 {
        return zero, false
    }
    last := s.items[len(s.items)-1]
    s.items = s.items[:len(s.items)-1]
    return last, true
}
```

**Quando usar generics:**
- Estruturas de dados (Stack, Queue, Set, Result[T])
- Funções utilitárias (Map, Filter, Reduce, Contains)
- Clientes de API com resposta tipada

**Quando evitar:**
- Quando interfaces resolvem o problema com menos complexidade
- Lógica de negócio — generics aqui geralmente indicam abstração prematura
- Quando o tipo concreto seria mais legível

---

## Memory Model e Atomic Operations

Go tem um memory model baseado em happens-before. Leituras e escritas concorrentes sem sincronização são undefined behavior.

```go
// sync/atomic para operações simples sem Mutex
import "sync/atomic"

type AtomicCounter struct {
    value atomic.Int64
}

func (c *AtomicCounter) Increment() {
    c.value.Add(1)
}

func (c *AtomicCounter) Value() int64 {
    return c.value.Load()
}

// atomic.Value para valores arbitrários (read-heavy)
var config atomic.Value

func updateConfig(cfg Config) {
    config.Store(cfg) // atomic write
}

func getConfig() Config {
    return config.Load().(Config) // atomic read
}
```

**Regra:** use `sync/atomic` apenas para tipos simples (int, pointer, bool) ou `atomic.Value` para structs read-heavy. Para lógica mais complexa, `sync.Mutex` é mais legível e menos propenso a bugs.

---

## Reflection

```go
import "reflect"

func printFields(v any) {
    t := reflect.TypeOf(v)
    val := reflect.ValueOf(v)

    if t.Kind() == reflect.Ptr {
        t = t.Elem()
        val = val.Elem()
    }

    for i := 0; i < t.NumField(); i++ {
        field := t.Field(i)
        value := val.Field(i)
        tag := field.Tag.Get("json")
        fmt.Printf("%s (%s) = %v [json:%s]\n", field.Name, field.Type, value, tag)
    }
}
```

Reflection é como `encoding/json`, ORMs e frameworks de serialização funcionam internamente. **Na aplicação:** evitar — o custo de legibilidade e performance raramente vale. Prefira generics ou code generation (sqlc, protoc).

---

## cgo — Interface com C

```go
/*
#include <stdlib.h>
#include <string.h>

char* process(const char* input) {
    char* output = malloc(strlen(input) + 10);
    sprintf(output, "processed: %s", input);
    return output;
}
*/
import "C"
import "unsafe"

func processWithC(input string) string {
    cInput := C.CString(input)
    defer C.free(unsafe.Pointer(cInput))

    cOutput := C.process(cInput)
    defer C.free(unsafe.Pointer(cOutput))

    return C.GoString(cOutput)
}
```

**Custo do cgo:**
- Cross-compilation quebra (`CGO_ENABLED=0` para binários portáveis)
- Overhead de chamada CGo ~100ns vs ~1ns para Go puro
- GC não gerencia memória C — memory leaks manuais

**Quando usar:** libs nativas sem equivalente Go (SQLite embedded, crypto hardware, CUDA). Evitar se existir uma lib Go pura funcional.

---

## WebAssembly

```go
//go:build js && wasm

package main

import (
    "syscall/js"
)

func add(this js.Value, args []js.Value) any {
    return args[0].Int() + args[1].Int()
}

func main() {
    js.Global().Set("goAdd", js.FuncOf(add))
    select {} // mantém goroutine viva
}
```

```bash
GOOS=js GOARCH=wasm go build -o main.wasm main.go
cp "$(go env GOROOT)/misc/wasm/wasm_exec.js" .
```

Casos de uso: processamento pesado no browser, reutilização de lógica Go em frontend, plugins em ambientes WASM (Envoy, Extism).

---

## GC e Performance (Go 1.21+)

Go usa um GC tri-color mark-and-sweep concorrente. Melhorias no 1.21 reduziram pauses para sub-milissegundo na maioria dos casos.

```go
// GOGC — fator de agressividade do GC (padrão: 100%)
// GOGC=200 → GC roda quando heap dobra (menos frequente, mais memória)
// GOGC=off → desativa GC (para benchmarks, batch jobs curtos)

// GOMEMLIMIT (Go 1.19+) — limite absoluto de memória
// Mais seguro que GOGC para containers
// GOMEMLIMIT=512MiB

// Monitorar GC
import "runtime"

var stats runtime.MemStats
runtime.ReadMemStats(&stats)
fmt.Printf("GC runs: %d, Heap: %d MB\n", stats.NumGC, stats.HeapAlloc/1024/1024)
```

Para performance crítica: preferir pools de objetos com `sync.Pool`, evitar alocações no hot path, usar benchmarks com `go test -bench` antes de otimizar.

---

## Trade-offs

| Feature | Vantagem | Desvantagem |
|---------|----------|-------------|
| Generics | Elimina duplicação de código | Mensagens de erro complexas, compile time |
| sync/atomic | Sem lock overhead | Difícil de raciocinar corretamente |
| cgo | Acesso a libs C maduras | Quebra portabilidade, overhead, GC manual |
| WASM | Reutiliza lógica Go no browser | Bundle grande, performance vs JS nativo |
| Reflection | Flexibilidade máxima | Sem verificação em compile-time, lento |

## Conceitos Relacionados
[[go-concorrencia]] · [[go-fundamentos]] · [[go-producao]] · [[async-io-memory-management]]

---
*Fonte: tech-mentor skill · lang-systems · 2026-04-24*
