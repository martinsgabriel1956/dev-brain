---
type: concept
title: "Go — Arquitetura e Patterns"
aliases: ["go clean architecture", "go repository pattern", "go DI", "go functional options"]
date_created: 2026-04-24
date_updated: 2026-08-18
source_count: 2
tags: [go, arquitetura, clean-architecture, repository, dependency-injection, functional-options]
skill: lang-systems
status: stable
---

# Go — Arquitetura e Patterns

Clean Architecture em Go sem frameworks de DI — wiring manual explícito, interfaces no domínio, implementações na infraestrutura.

## Estrutura de Pastas

```
cmd/
└── server/
    └── main.go           ← wiring manual

internal/
├── domain/               ← entities, value objects, erros de domínio
├── features/
│   └── users/
│       ├── handler.go    ← HTTP (controller)
│       ├── usecase.go    ← regras de negócio
│       ├── repository.go ← interface
│       └── errors.go
└── infrastructure/
    └── postgres/
        └── user_repo.go  ← implementação do repository
```

## Wiring Explícito

```go
func main() {
    db := postgres.Connect(cfg.DatabaseURL)
    userRepo := postgres.NewUserRepository(db)
    userUseCase := users.NewUserUseCase(userRepo)
    userHandler := users.NewUserHandler(userUseCase)

    r := chi.NewRouter()
    r.Mount("/users", userHandler.Routes())
    http.ListenAndServe(":8080", r)
}
```

Sem reflection, sem tags mágicas — o grafo de dependências é legível em `main.go`.

## Repository Pattern com Interfaces

A interface fica no pacote do domínio, implementação na infraestrutura. Permite trocar Postgres por SQLite em testes sem mudar o UseCase.

## Functional Options Pattern

```go
type ServerOption func(*Server)

func WithTimeout(t time.Duration) ServerOption {
    return func(s *Server) { s.timeout = t }
}

func NewServer(opts ...ServerOption) *Server {
    s := &Server{timeout: 30 * time.Second} // defaults
    for _, opt := range opts {
        opt(s)
    }
    return s
}
```

Substitui structs de configuração com campos opcionais que explodem construtores.

## Error Handling

```go
type UserNotFoundError struct{ ID string }
func (e UserNotFoundError) Error() string {
    return fmt.Sprintf("user %s not found", e.ID)
}

// No UseCase:
user, err := repo.FindByID(ctx, id)
if err != nil {
    return nil, UserNotFoundError{ID: id}
}
```

## Guard Clauses

```go
func processUser(user *User) error {
    if user == nil { return ErrNilUser }
    if !user.IsActive { return ErrInactiveUser }
    // lógica principal sem aninhamento
}
```

## Wiring Multi-Módulo (Monolito Modular)

Variação do wiring explícito acima quando o projeto não é um único serviço "feature-based", mas um [[wiki/concepts/monolito-modular]] com vários módulos independentes (`modules/appointment`, `modules/payment`, ...). Cada módulo expõe uma função `Register(router)` que traduz seu próprio conjunto de rotas — o `main.go` de cada entry point só instancia dependências (DB, HTTP server) e injeta o handler de cada módulo que aquele entry point deve servir:

```go
func main() {
    db := postgres.Connect(cfg.DatabaseURL)
    db.Migrate()

    httpServer := server.NewHTTPServer()
    appointmentHandler := appointment.NewHTTPHandler(db)
    appointmentHandler.Register(httpServer.Router())

    httpServer.Start()
}
```

Extrair um módulo para um serviço próprio, nesse desenho, é remover a linha de injeção (`appointmentHandler.Register(...)`) do entry point atual e criar um `main.go` novo, exclusivo, só para esse módulo — sem tocar na lógica de negócio interna. Caso real documentado por [[wiki/entities/lucas-badico]] em [[wiki/sources/sistema-mentoria-golang-monolito-modular-live-lucas-badico]], onde cada módulo também expõe handler HTTP e [[wiki/concepts/grpc|gRPC]] em paralelo — HTTP para clientes externos, gRPC para comunicação interna entre módulos.

## Ver também

- [[clean-architecture]] — princípios gerais
- [[hexagonal-architecture]] — ports & adapters
- [[go-ecossistema]] — Chi, sqlc, golangci-lint
- [[go-producao]] — graceful shutdown, health checks
- [[wiki/concepts/monolito-modular]] — quando "feature" vira "módulo" com fronteira de extração explícita

## Key Sources

- [[wiki/sources/go-arquitetura]]
- [[wiki/sources/sistema-mentoria-golang-monolito-modular-live-lucas-badico]] — wiring multi-módulo com entry points HTTP e gRPC separados, injeção de handler por módulo
