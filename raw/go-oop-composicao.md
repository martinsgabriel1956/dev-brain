---
date: 2026-04-24
tags: [tech-mentor, lang-systems, go, oop, interfaces, composicao, embedding]
skill: lang-systems/references/go
level: fundamento
---

# Go — OOP: Composição, Interfaces e Receivers

## Contexto
Go rejeita herança deliberadamente. Em vez disso, usa composição via embedding e interfaces implícitas. Isso elimina a fragilidade da hierarquia de classes e torna o código mais fácil de testar e trocar implementações.

---

## Composição via Embedding

```go
type Animal struct {
    Name string
}

func (a Animal) Speak() string {
    return a.Name + " faz barulho"
}

type Dog struct {
    Animal        // embedding — promove métodos e campos
    Breed string
}

d := Dog{
    Animal: Animal{Name: "Rex"},
    Breed:  "Labrador",
}

d.Speak()      // promovido de Animal
d.Animal.Name  // acesso explícito também funciona
```

Embedding não é herança: `Dog` não é um `Animal`. Você não pode passar `Dog` onde `Animal` é esperado — a menos que ambos implementem a mesma interface.

---

## Interfaces Implícitas

Go não tem `implements`. Um tipo satisfaz uma interface se tiver todos os métodos — em tempo de compilação.

```go
type Speaker interface {
    Speak() string
}

// Dog satisfaz Speaker sem declarar
func makeNoise(s Speaker) {
    fmt.Println(s.Speak())
}

makeNoise(d) // funciona
```

Interfaces pequenas são idiomáticas:

```go
// stdlib usa esse padrão extensivamente
type Reader interface {
    Read(p []byte) (n int, err error)
}

type Writer interface {
    Write(p []byte) (n int, err error)
}

type ReadWriter interface {
    Reader
    Writer
}
```

**Regra de ouro**: defina interfaces no pacote que as **consome**, não onde são implementadas. Isso inverte a dependência e facilita mocking.

---

## Value Receiver vs Pointer Receiver

```go
type Counter struct {
    count int
}

// Value receiver — recebe cópia
func (c Counter) Value() int {
    return c.count
}

// Pointer receiver — modifica o original
func (c *Counter) Increment() {
    c.count++
}
```

**Regra de decisão:**

| Situação | Receiver |
|----------|----------|
| Modifica o estado | `*T` |
| Struct grande (evitar cópia) | `*T` |
| Tipo precisa ser nil | `*T` |
| Imutável / valor pequeno | `T` |
| Consistência: se um método é `*T`, todos deveriam ser | `*T` |

Misturar value e pointer receivers num mesmo tipo é permitido mas confuso — evitar.

---

## Interface `error` e `fmt.Stringer`

```go
// error é apenas uma interface
type error interface {
    Error() string
}

// Erro customizado
type ValidationError struct {
    Field   string
    Message string
}

func (e ValidationError) Error() string {
    return fmt.Sprintf("validation error on %s: %s", e.Field, e.Message)
}

// fmt.Stringer — controla como o tipo é impresso
type User struct {
    Name  string
    Email string
}

func (u User) String() string {
    return fmt.Sprintf("User(%s <%s>)", u.Name, u.Email)
}

fmt.Println(u) // User(Alice <alice@example.com>)
```

---

## Type Assertions e Type Switches

```go
var s Speaker = Dog{Animal: Animal{Name: "Rex"}, Breed: "Lab"}

// Type assertion
dog, ok := s.(Dog)
if ok {
    fmt.Println(dog.Breed)
}

// Type switch — polimorfismo sem hierarquia
func describe(i interface{}) string {
    switch v := i.(type) {
    case int:
        return fmt.Sprintf("int: %d", v)
    case string:
        return fmt.Sprintf("string: %q", v)
    case Dog:
        return fmt.Sprintf("dog: %s", v.Name)
    default:
        return fmt.Sprintf("unknown: %T", v)
    }
}
```

---

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---------|----------|-------------|
| Interfaces implícitas | Desacoplamento natural, fácil mock | Difícil saber quem implementa sem IDE |
| Embedding | Reutilização sem herança frágil | Promoção de métodos pode surpreender |
| Sem herança | Hierarquias planas, testáveis | Padrões OO clássicos precisam ser reaprendidos |

## Quando Usar / Quando Evitar

**Embedding:** para composição real ("tem um"). Não use como atalho para "herdar" comportamento — isso quebra encapsulamento.

**Interface grande:** evitar. Se tiver > 3 métodos, provavelmente está tentando mapear uma classe OO para Go. Quebre em interfaces menores.

## Conceitos Relacionados
[[go-fundamentos]] · [[go-concorrencia]] · [[go-arquitetura]] · [[clean-architecture]]

---
*Fonte: tech-mentor skill · lang-systems · 2026-04-24*
