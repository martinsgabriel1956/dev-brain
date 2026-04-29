---
type: concept
title: "Go — Fundamentos da Linguagem"
aliases: ["golang fundamentos", "go tipos", "go slices", "go zero values"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [go, fundamentos, tipos, slices, maps, structs, zero-values]
skill: lang-systems
status: stable
---

# Go — Fundamentos da Linguagem

Linguagem compilada, estaticamente tipada, com GC e concorrência nativa. Projetada para sistemas distribuídos modernos: compilação rápida, binário único sem runtime externo, modelo de tipos simples e poderoso.

## Zero Values

Toda variável declarada tem um zero value definido — sem uninitialized bugs:

```go
var i int       // 0
var f float64   // 0.0
var s string    // ""
var b bool      // false
var p *int      // nil
```

## Slices vs Arrays

Arrays têm tamanho fixo em compile-time — raramente usados diretamente. **Slices são views de arrays** com comprimento e capacidade separados:

```go
s := make([]int, 3, 5) // len=3, cap=5
s = append(s, 4)       // len=4, cap=5 — sem realocação
```

Cuidado: slices compartilham memória com o array original até `append` forçar realocação.

## Maps

```go
m := map[string]int{"a": 1, "b": 2}
val, ok := m["key"] // two-value idiom — ok=false se não existe
delete(m, "key")
```

Maps não são thread-safe — use `sync.RWMutex` ou `sync.Map` em concorrência.

## Structs e Pointers

```go
type User struct {
    ID    int
    Name  string
    Email string
}

u := &User{ID: 1, Name: "Alice"} // pointer — modifica original
```

## Enumerações com iota

```go
type Direction int
const (
    North Direction = iota // 0
    East                   // 1
    South                  // 2
)

// Bitmask
const (
    Read  = 1 << iota // 1
    Write             // 2
    Exec              // 4
)
```

## Controle de Fluxo

- `for` é o único loop — substitui `while`, `do-while` e `for`
- `for range` sobre slices, maps, channels e strings
- `defer` executa na saída da função — LIFO, útil para cleanup

## Ver também

- [[go-oop-composicao]] — como structs evoluem para OOP via composição
- [[go-concorrencia]] — goroutines e channels
- [[go-stdlib]] — net/http, json, database/sql

## Key Sources

- [[wiki/sources/go-fundamentos]]
