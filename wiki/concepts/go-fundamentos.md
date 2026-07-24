---
type: concept
title: "Go — Fundamentos da Linguagem"
aliases: ["golang fundamentos", "go tipos", "go slices", "go zero values"]
date_created: 2026-04-24
date_updated: 2026-07-22
source_count: 5
tags: [go, fundamentos, tipos, slices, maps, structs, zero-values, cloud-native, filosofia-de-linguagem, bitwise]
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

O mesmo trio de operadores por trás do bitmask acima (`&`, `|`, `<<`) é a base de qualquer parsing binário em Go — ver [[bitwise-operations]] para o padrão geral e [[wiki/sources/algoritmo-decode-utf8-com-tdd]] para um caso real: reconstruir uma `rune` (também um tipo próprio, forte, alias de `int32`) a partir de bytes UTF-8.

## Controle de Fluxo

- `for` é o único loop — substitui `while`, `do-while` e `for`
- `for range` sobre slices, maps, channels e strings
- `defer` executa na saída da função — LIFO, útil para cleanup

## Filosofia: Pragmatismo vs. Expressividade (Go vs. Rust)

Segundo [[wiki/entities/lucas-badico]], a diferença central na filosofia de design entre Go e Rust não é técnica, é de propósito: Rust é pensado para soluções *clever* — muitas features, muitas formas de resolver o mesmo problema. Go tem poucas formas de fazer cada coisa, o que força uma solução mais crua e menos "bonita", mas consistente e fácil de manter. Programar em Go pensando como Rust tende a não funcionar bem; o caminho inverso (Rust pensando como Go) funciona, mas fica aquém do ideal na linguagem mais expressiva.

Essa diferença de propósito aparece concretamente na decisão de memória: Go usa garbage collector (menos controle, mais conforto), Rust usa ownership/borrow checker (mais controle e previsibilidade, mais decisões explícitas exigidas desde o primeiro programa). Ver [[wiki/concepts/rust-ownership-borrowing-lifetimes]] e [[wiki/concepts/rust-fundamentos]] para o detalhamento do lado Rust dessa comparação.

## Design Cloud Native

Go foi desenhado desde o início para sustentar a infraestrutura em cloud do Google — não uma linguagem de propósito geral adaptada depois para cloud, como aconteceu com outras. Isso é apontado como o principal motivo da adoção consolidada do Go em empresas brasileiras como Mercado Livre, Mercado Pago e Stone, e como diferencial frente a tecnologias que tiveram forte influência histórica mas nunca escalaram para adoção em massa (ex.: Ruby on Rails). Ver [[wiki/concepts/ciclo-de-mercado-tech]].

O Go Developer Survey oficial do Google confirma esse padrão de adoção com dados de uso: 74% dos devs Go usam a linguagem para APIs e serviços RPC (destaque para gRPC), 63% para CLIs, e a maior fatia de experiência profissional entre respondentes está em 16+ anos de codificação — reforçando que Go tende a ser adotado por devs experientes migrando de outra stack para casos de uso de cloud/microsserviços, não como primeira linguagem. Ver [[wiki/sources/golang-mercado-salarios-pesquisa-2024]].

## Ver também

- [[go-oop-composicao]] — como structs evoluem para OOP via composição
- [[go-concorrencia]] — goroutines e channels
- [[go-stdlib]] — net/http, json, database/sql
- [[wiki/concepts/ponte-fullstack-para-especializacao]] — estratégia de carreira para quem quer entrar no ecossistema Go vindo de outra stack
- [[wiki/concepts/rust-fundamentos]] — o lado Rust do contraste pragmatismo vs. expressividade

## Key Sources

- [[wiki/sources/go-fundamentos]]
- [[wiki/sources/golang-mercado-trabalho-frontend-para-backend]]
- [[wiki/sources/golang-mercado-salarios-pesquisa-2024]]
- [[wiki/sources/rust-por-que-tanto-hype-ownership-borrowing-lifetimes]] — contraponto Rust: ownership/borrow checker em vez de GC, mais expressividade ao custo de mais decisões explícitas
- [[wiki/sources/algoritmo-decode-utf8-com-tdd]] — bitmask/bitwise (`&`, `\|`, `<<`) aplicado a um caso real: decode de UTF-8 byte a byte
