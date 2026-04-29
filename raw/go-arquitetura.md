---
date: 2026-04-24
tags: [tech-mentor, lang-systems, go, arquitetura, clean-architecture, repository, di, functional-options]
skill: lang-systems/references/go
level: avançado
---

# Go — Arquitetura e Patterns

## Contexto
Clean Architecture em Go é mais simples do que em Java ou C# — sem frameworks DI, sem annotations, sem magic. O wiring é feito manualmente em `main.go`. Isso parece verboso, mas torna o grafo de dependências explícito e auditável.

---

## Clean Architecture em Go

```
cmd/
└── server/
    └── main.go           ← wiring manual

internal/
├── domain/               ← entities, value objects, erros de domínio
│   └── user.go
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

```go
// main.go — wiring explícito
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

---

## Repository Pattern com Interfaces

```go
// internal/features/users/repository.go
type UserRepository interface {
    FindByID(ctx context.Context, id string) (*domain.User, error)
    FindByEmail(ctx context.Context, email string) (*domain.User, error)
    Save(ctx context.Context, user *domain.User) error
    Delete(ctx context.Context, id string) error
}

// internal/infrastructure/postgres/user_repo.go
type userRepository struct {
    db *sqlx.DB
}

func NewUserRepository(db *sqlx.DB) users.UserRepository {
    return &userRepository{db: db}
}

func (r *userRepository) FindByID(ctx context.Context, id string) (*domain.User, error) {
    var u domain.User
    err := r.db.GetContext(ctx, &u, "SELECT * FROM users WHERE id = $1", id)
    if errors.Is(err, sql.ErrNoRows) {
        return nil, nil // UseCase trata nil como NotFound
    }
    return &u, err
}
```

---

## Dependency Injection via Construtores

```go
// UseCase depende da interface, não da implementação
type UserUseCase struct {
    repo   UserRepository
    mailer EmailService // interface para infra
    logger *slog.Logger
}

func NewUserUseCase(repo UserRepository, mailer EmailService, logger *slog.Logger) *UserUseCase {
    return &UserUseCase{repo: repo, mailer: mailer, logger: logger}
}

func (uc *UserUseCase) CreateUser(ctx context.Context, dto CreateUserDTO) (*domain.User, error) {
    existing, err := uc.repo.FindByEmail(ctx, dto.Email)
    if err != nil {
        return nil, fmt.Errorf("checking existing user: %w", err)
    }
    if existing != nil {
        return nil, ErrEmailAlreadyExists
    }

    user := domain.NewUser(dto.Name, dto.Email)
    if err := uc.repo.Save(ctx, user); err != nil {
        return nil, fmt.Errorf("saving user: %w", err)
    }

    uc.mailer.SendWelcome(ctx, user.Email) // fire-and-forget ou goroutine
    return user, nil
}
```

---

## Error Handling Explícito

```go
// Erros de domínio tipados
var (
    ErrUserNotFound      = errors.New("user not found")
    ErrEmailAlreadyExists = errors.New("email already exists")
)

// Wrapping com contexto
return nil, fmt.Errorf("createUser: %w", ErrEmailAlreadyExists)

// Unwrapping
if errors.Is(err, ErrUserNotFound) {
    http.Error(w, "not found", http.StatusNotFound)
    return
}

// Para erros com dados
type ValidationError struct {
    Field   string
    Message string
}

func (e *ValidationError) Error() string {
    return fmt.Sprintf("%s: %s", e.Field, e.Message)
}

var ve *ValidationError
if errors.As(err, &ve) {
    // acessar ve.Field, ve.Message
}
```

---

## Functional Options Pattern

Para configuração de structs com muitos parâmetros opcionais — alternativa a builders e constructors com 10 parâmetros.

```go
type Server struct {
    port         int
    timeout      time.Duration
    maxConns     int
    tlsEnabled   bool
}

type Option func(*Server)

func WithPort(p int) Option {
    return func(s *Server) { s.port = p }
}

func WithTimeout(d time.Duration) Option {
    return func(s *Server) { s.timeout = d }
}

func WithTLS() Option {
    return func(s *Server) { s.tlsEnabled = true }
}

func NewServer(opts ...Option) *Server {
    s := &Server{
        port:     8080,
        timeout:  30 * time.Second,
        maxConns: 100,
    }
    for _, o := range opts {
        o(s)
    }
    return s
}

// Uso
srv := NewServer(
    WithPort(9090),
    WithTLS(),
    WithTimeout(60*time.Second),
)
```

---

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---------|----------|-------------|
| Wiring manual | Explícito, auditável, sem magic | Verboso em projetos grandes |
| Repository com interface | Mockável, testável, trocar implementação | Boilerplate de interface para cada entidade |
| Functional options | API extensível sem breaking changes | Menos descobrível que struct config |
| Erros explícitos | Rastreável, tipado | Verboso vs exceções |

## Quando Usar / Quando Evitar

**Functional options:** para libs e pacotes públicos onde a API de configuração vai evoluir. Para structs internas com 2-3 campos, um struct simples é mais legível.

**Repository interface no mesmo pacote:** define a interface onde é consumida (UseCase), não onde é implementada (postgres). Isso é o princípio da inversão de dependência em Go.

## Conceitos Relacionados
[[clean-architecture]] · [[go-ecossistema]] · [[go-producao]] · [[hexagonal-architecture]]

---
*Fonte: tech-mentor skill · lang-systems · 2026-04-24*
