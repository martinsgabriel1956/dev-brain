---
date: 2026-04-24
tags: [tech-mentor, lang-systems, go, ecossistema, chi, gin, sqlc, sqlx, linting]
skill: lang-systems/references/go
level: intermediário
---

# Go — Ecossistema e Tooling

## Contexto
Go tem uma stdlib poderosa, mas o ecossistema complementa onde ela é verbosa. A chave é escolher libs que estendem o padrão em vez de substituí-lo — você ainda deve entender `net/http` e `database/sql` antes de adicionar qualquer abstração.

---

## Web Frameworks e Roteadores

### net/http puro (Go 1.22+)

Go 1.22 adicionou path params e method routing nativos:

```go
mux := http.NewServeMux()
mux.HandleFunc("GET /users/{id}", getUserHandler)
mux.HandleFunc("POST /users", createUserHandler)
```

Suficiente para APIs simples sem dependências externas.

### Chi — recomendado

Leve, 100% compatível com `net/http`. Middlewares do ecossistema padrão funcionam direto.

```go
r := chi.NewRouter()

r.Use(middleware.Logger)
r.Use(middleware.Recoverer)
r.Use(middleware.Timeout(60 * time.Second))

r.Route("/users", func(r chi.Router) {
    r.Get("/", listUsersHandler)
    r.Post("/", createUserHandler)
    r.Route("/{id}", func(r chi.Router) {
        r.Use(userCtxMiddleware) // middleware específico de rota
        r.Get("/", getUserHandler)
        r.Delete("/", deleteUserHandler)
    })
})

// Path param
func getUserHandler(w http.ResponseWriter, r *http.Request) {
    id := chi.URLParam(r, "id")
    // ...
}
```

### Gin vs Echo

| | Gin | Echo |
|--|-----|------|
| Performance | Alta (custom router) | Alta |
| API | Própria (não stdlib-compatible) | Própria |
| Mágico | Mais | Menos |
| Stars/maturidade | Maior | Menor |

**Trade-off:** Gin e Echo têm contextos próprios, o que rompe compatibilidade com middlewares stdlib. Chi mantém `http.Handler` padrão — mais longo prazo.

---

## ORM e SQL

### sqlc — recomendado

Gera código Go tipado a partir de queries SQL. Sem reflection, sem magic.

```sql
-- query.sql
-- name: GetUser :one
SELECT id, name, email, created_at
FROM users
WHERE id = $1;

-- name: ListActiveUsers :many
SELECT id, name, email
FROM users
WHERE active = true
ORDER BY created_at DESC;

-- name: CreateUser :one
INSERT INTO users (name, email, password_hash)
VALUES ($1, $2, $3)
RETURNING *;
```

```go
// gerado automaticamente
queries := db.New(conn)

user, err := queries.GetUser(ctx, userID)
users, err := queries.ListActiveUsers(ctx)
user, err := queries.CreateUser(ctx, sqlcdb.CreateUserParams{
    Name:         "Alice",
    Email:        "alice@example.com",
    PasswordHash: hash,
})
```

Configuração (`sqlc.yaml`):
```yaml
version: "2"
sql:
  - engine: "postgresql"
    queries: "./queries"
    schema: "./migrations"
    gen:
      go:
        package: "sqlcdb"
        out: "./internal/db"
```

### sqlx — extensão leve de database/sql

```go
db, _ := sqlx.Connect("postgres", dsn)

// Scan direto para struct
var user User
err := db.GetContext(ctx, &user, "SELECT * FROM users WHERE id = $1", id)

// Slice de structs
var users []User
err = db.SelectContext(ctx, &users, "SELECT * FROM users WHERE active = true")

// Named params
_, err = db.NamedExecContext(ctx,
    "INSERT INTO users (name, email) VALUES (:name, :email)",
    user,
)
```

### GORM — quando usar

Prototipagem rápida, equipes vindas de Rails/Django. Evitar em produção com queries complexas — o SQL gerado surpreende, migrations automáticas são perigosas.

---

## Config e Ambiente

```go
// Validação com Zod-equivalente Go: manualmente ou com envconfig/viper
type Config struct {
    DBHost     string
    DBPort     int
    DBName     string
    DBUser     string
    DBPassword string
    JWTSecret  string
    Port       int
}

func LoadConfig() (Config, error) {
    cfg := Config{
        DBHost: os.Getenv("DB_HOST"),
        Port:   8080,
    }

    portStr := os.Getenv("PORT")
    if portStr != "" {
        p, err := strconv.Atoi(portStr)
        if err != nil {
            return cfg, fmt.Errorf("PORT inválida: %w", err)
        }
        cfg.Port = p
    }

    if cfg.DBHost == "" {
        return cfg, errors.New("DB_HOST é obrigatório")
    }

    return cfg, nil
}
```

Alternativa: `github.com/kelseyhightower/envconfig` para mapear env vars para structs com tags.

---

## Linting

```bash
# golangci-lint — agrega múltiplos linters
golangci-lint run ./...

# Linters úteis para habilitar:
# - errcheck: garante que erros não são ignorados
# - gosec: segurança
# - revive: substituto do golint
# - staticcheck: análise estática avançada
# - gofumpt: fmt mais estrito
```

`.golangci.yml` mínimo:
```yaml
linters:
  enable:
    - errcheck
    - gosimple
    - govet
    - staticcheck
    - unused
    - gosec
    - revive

linters-settings:
  revive:
    rules:
      - name: exported
        severity: warning
```

---

## Trade-offs

| Escolha | Trade-off |
|---------|-----------|
| Chi vs stdlib puro | Chi: menos boilerplate, mais deps. stdlib: zero deps, mais verboso |
| sqlc vs sqlx | sqlc: type-safe, precisa de geração. sqlx: mais flexível, menos seguro |
| envconfig vs manual | envconfig: menos código. manual: sem dep, mais explícito |

## Conceitos Relacionados
[[go-stdlib]] · [[go-arquitetura]] · [[go-producao]]

---
*Fonte: tech-mentor skill · lang-systems · 2026-04-24*
