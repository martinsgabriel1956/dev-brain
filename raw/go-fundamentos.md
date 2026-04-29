---
date: 2026-04-24
tags: [tech-mentor, lang-systems, go, fundamentos, tipos, slices, maps]
skill: lang-systems/references/go
level: fundamento
---

# Go — Fundamentos da Linguagem

## Contexto
Go tem um sistema de tipos deliberadamente simples. Zero values eliminam null pointers acidentais. Slices e maps são os workhorses da linguagem — entendê-los em profundidade evita bugs sutis de memória e performance.

---

## Tipos Primitivos e Zero Values

```go
var i int       // 0
var f float64   // 0.0
var s string    // ""
var b bool      // false
var p *int      // nil
```

`iota` para enumerações:

```go
type Direction int

const (
    North Direction = iota // 0
    East                   // 1
    South                  // 2
    West                   // 3
)

// Com bitmask
const (
    Read  = 1 << iota // 1
    Write             // 2
    Exec              // 4
)
```

---

## Arrays vs Slices

Array tem tamanho fixo e é **value type** — copiar um array copia todos os dados.

```go
arr := [3]int{1, 2, 3}
copy := arr // cópia completa
```

Slice é uma view sobre um array subjacente com três campos: `pointer`, `length`, `capacity`.

```go
s := make([]int, 3, 6) // len=3, cap=6

s = append(s, 4) // se len < cap: sem alocação
                  // se len == cap: novo array alocado, cap dobra

// Slice de slice compartilha o array subjacente
a := []int{1, 2, 3, 4, 5}
b := a[1:3] // [2, 3] — mesma memória
b[0] = 99  // modifica a também: a = [1, 99, 3, 4, 5]

// Para isolar: usar copy
c := make([]int, len(b))
copy(c, b)
```

**Regra**: ao passar slice para função, mutações no conteúdo são visíveis. Re-append pode ou não ser — depende de reusar o array subjacente.

---

## Maps

```go
m := make(map[string]int)
m["key"] = 1

// Verificar existência
v, ok := m["key"] // ok=false se ausente
if !ok {
    // chave não existe
}

// Deletar
delete(m, "key")

// Iterar (ordem não garantida)
for k, v := range m {
    fmt.Println(k, v)
}
```

Maps não são thread-safe. Use `sync.RWMutex` ou `sync.Map` em concorrência.

---

## Structs e Pointers

```go
type User struct {
    ID    int
    Name  string
    Email string
}

// Value vs Pointer
u1 := User{ID: 1, Name: "Alice"}
u2 := &User{ID: 2, Name: "Bob"} // pointer

// Pointer para evitar cópia em structs grandes
func updateName(u *User, name string) {
    u.Name = name // modifica original
}
```

---

## Controle de Fluxo

```go
// for como while
for condition { }

// for infinito
for { }

// range
for i, v := range slice { }
for k, v := range m { }
for i, r := range "string" { } // r é rune (Unicode)
```

`defer`: executa quando a função retorna, em ordem LIFO.

```go
func readFile(path string) error {
    f, err := os.Open(path)
    if err != nil {
        return err
    }
    defer f.Close() // garantido mesmo em panic

    // leitura...
    return nil
}
```

`panic` + `recover` para erros não recuperáveis e middleware de recovery:

```go
func safeDiv(a, b int) (result int, err error) {
    defer func() {
        if r := recover(); r != nil {
            err = fmt.Errorf("recovered: %v", r)
        }
    }()
    return a / b, nil
}
```

---

## Funções

```go
// Múltiplos retornos — idioma Go para erros
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("divisão por zero")
    }
    return a / b, nil
}

// Variadic
func sum(nums ...int) int {
    total := 0
    for _, n := range nums {
        total += n
    }
    return total
}

// First-class + closures
func counter(start int) func() int {
    count := start
    return func() int {
        count++
        return count
    }
}

next := counter(0)
next() // 1
next() // 2
```

Named returns: evitar — obscurece o fluxo. Aceitável em funções de 2-3 linhas com defer.

---

## Ferramentas Essenciais

```bash
go build ./...          # compila tudo
go run main.go          # compila e executa
go test ./...           # roda testes
go test -race ./...     # detecta race conditions
go vet ./...            # análise estática
go fmt ./...            # formata código
go mod init module/name # inicializa módulo
go mod tidy             # limpa dependências
go mod vendor           # vendoring local
```

---

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---------|----------|-------------|
| Zero values | Sem null pointers acidentais | Pode mascarar inicialização faltando |
| Slices | Flexíveis, performance previsível | Compartilhamento de memória surpreende |
| Maps | API simples | Não thread-safe por padrão |
| `defer` | Cleanup garantido | LIFO pode confundir em loops |

## Quando Usar / Quando Evitar

**Named returns:** evitar em funções longas. OK em `func (r Result) split() (x, y int)` com defer.

**Array vs Slice:** arrays para tamanho fixo e compilação-tempo (ex: hash de 32 bytes). Slice para tudo mais.

## Conceitos Relacionados
[[go-concorrencia]] · [[go-oop-composicao]] · [[go-stdlib]]

---
*Fonte: tech-mentor skill · lang-systems · 2026-04-24*
