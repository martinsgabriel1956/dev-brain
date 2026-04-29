---
type: concept
title: "Go — OOP: Composição, Interfaces e Receivers"
aliases: ["go embedding", "go duck typing", "go interfaces implícitas", "go pointer receiver"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [go, oop, composicao, embedding, interfaces, receivers, duck-typing]
skill: lang-systems
status: stable
---

# Go — OOP: Composição, Interfaces e Receivers

Go não tem herança. Substitui com **composição via embedding** e **interfaces implícitas (duck typing)**.

## Composição via Embedding

```go
type Animal struct{ Name string }
func (a Animal) Speak() string { return a.Name + " faz barulho" }

type Dog struct {
    Animal        // embedding — promove métodos e campos
    Breed string
}

d := Dog{Animal: Animal{Name: "Rex"}, Breed: "Labrador"}
d.Speak()      // promovido de Animal
d.Animal.Name  // acesso explícito também funciona
```

**Embedding não é herança:** `Dog` não é um `Animal`. Não pode ser passado onde `Animal` é esperado — a menos que ambos implementem a mesma interface.

## Interfaces Implícitas

Nenhum `implements` necessário. Qualquer tipo que satisfaz os métodos da interface a implementa:

```go
type Writer interface {
    Write(p []byte) (n int, err error)
}

// Qualquer struct com método Write([]byte)(int,error) é um Writer
// Isso permite satisfazer interfaces de stdlib sem modificá-las
```

Interfaces pequenas são preferidas — `io.Reader`, `io.Writer`, `fmt.Stringer` têm 1 método cada.

## Value Receiver vs Pointer Receiver

```go
// Value receiver — opera em cópia, não modifica original
func (u User) String() string { return u.Name }

// Pointer receiver — modifica original
func (u *User) Activate() { u.IsActive = true }
```

**Regra:** se qualquer método precisa de pointer receiver, todos devem ser pointer receiver para consistência.

## fmt.Stringer e error

```go
type Color int
func (c Color) String() string {
    switch c {
    case Red: return "red"
    default:  return "unknown"
    }
}
```

`fmt.Stringer` (`String() string`) e `error` (`Error() string`) são as interfaces mais importantes da stdlib.

## Type Switch

```go
switch v := value.(type) {
case string:  fmt.Println("string:", v)
case int:     fmt.Println("int:", v)
default:      fmt.Println("unknown type")
}
```

Mais idiomático que múltiplos type assertions sequenciais.

## Ver também

- [[go-fundamentos]] — structs e tipos base
- [[go-arquitetura]] — interfaces como contratos de repository
- [[clean-architecture]] — inversão de dependência via interfaces

## Key Sources

- [[wiki/sources/go-oop-composicao]]
