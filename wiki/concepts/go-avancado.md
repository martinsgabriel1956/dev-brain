---
type: concept
title: "Go — Avançado"
aliases: ["go generics", "go reflection", "go cgo", "go wasm", "go gc tuning"]
date_created: 2026-04-24
date_updated: 2026-07-31
source_count: 2
tags: [go, avancado, generics, reflection, cgo, wasm, memory-model, gc]
skill: lang-systems
status: stable
---

# Go — Avançado

Recursos além do uso diário — generics, reflection, cgo, WASM e tuning de GC.

## Generics (Go 1.18+)

```go
func Map[T, U any](s []T, f func(T) U) []U {
    result := make([]U, len(s))
    for i, v := range s {
        result[i] = f(v)
    }
    return result
}
```

Type constraints via interfaces:

```go
type Number interface { int | float64 }

func Sum[T Number](nums []T) T {
    var total T
    for _, n := range nums { total += n }
    return total
}
```

**Trade-off:** elimina duplicação, mas mensagens de erro em compile-time são complexas.

### Filosofia de Uso: Generics Pequenos, Não Abstrações Grandes

Segundo [[wiki/entities/lucas-badico]], mesmo com generics disponíveis desde a 1.18, a cultura da comunidade Go não migrou para abstração generalizada — o padrão observado em código profissional é usar generics em pontos pequenos e isolados (ex.: trocar o tipo em uma única peça de dados), não para construir um "mapper" ou pipeline genérico universal que substitua repetição em larga escala. O argumento é de estabilidade: uma abstração genérica grande e "inteligente" concentra risco — se ela quebra ou precisa mudar, quebra tudo que depende dela — enquanto handlers repetitivos, ainda que verbosos, falham de forma isolada e são triviais de entender e alterar um por um. Essa preferência por repetição estável sobre abstração frágil é a mesma lógica documentada em [[wiki/concepts/go-ecossistema]] e [[wiki/concepts/go-stdlib]] para dependências externas — "repetir é melhor que acoplar" se aplica tanto a bibliotecas quanto a abstrações internas via generics. Ver [[wiki/sources/golang-profissional-sem-grandes-frameworks]].

## Reflection

Como `encoding/json`, ORMs e frameworks de serialização funcionam internamente. **Na aplicação: evitar.** O custo de legibilidade e performance raramente vale. Prefira generics ou code generation (sqlc, protoc).

```go
t := reflect.TypeOf(v)
val := reflect.ValueOf(v)
```

## Memory Model e Atomic Operations

Operações atômicas sem lock para contadores e flags:

```go
var counter int64
atomic.AddInt64(&counter, 1)
atomic.LoadInt64(&counter)
```

Difícil de raciocinar corretamente — usar apenas para hot paths com medição de benchmark.

## cgo

Permite interop com bibliotecas C maduras. **Desvantagens críticas:**
- Quebra portabilidade (cross-compilation requer CGO_ENABLED=0)
- Desativa race detector
- Overhead de context switch entre runtimes Go e C
- GC não gerencia memória C — vazamentos manuais

## GC Tuning (Go 1.21+)

```bash
GOGC=100        # percentual de crescimento do heap antes de GC (default: 100)
GOMEMLIMIT=4GiB # limite hard de memória — evita OOM antes de GC
```

Pausas < 1ms com configurações padrão para a maioria dos workloads.

## Ver também

- [[go-fundamentos]] — base de tipos e structs
- [[go-concorrencia]] — sync/atomic em contexto de concorrência
- [[go-producao]] — pprof para profiling de GC em produção

## Key Sources

- [[wiki/sources/go-avancado]]
- [[wiki/sources/golang-profissional-sem-grandes-frameworks]] — filosofia de generics pequenos vs. abstração grande, direto de um dev Go profissional (Lucas Badico)
