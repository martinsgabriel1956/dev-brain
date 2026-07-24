---
type: concept
title: "Go — Standard Library Essencial"
aliases: ["go net/http server", "go encoding json", "go database/sql", "go table-driven tests", "go slog"]
date_created: 2026-04-24
date_updated: 2026-07-22
source_count: 2
tags: [go, stdlib, net-http, json, database-sql, testing, slog, unicode-utf8]
skill: lang-systems
status: stable
---

# Go — Standard Library Essencial

A stdlib de Go é intencionalmente abrangente. Para a maioria dos serviços, `net/http`, `encoding/json`, `database/sql` e `testing` são suficientes sem dependências externas.

## net/http — Server

```go
mux := http.NewServeMux()
mux.HandleFunc("GET /users/{id}", func(w http.ResponseWriter, r *http.Request) {
    id := r.PathValue("id") // Go 1.22+
    // ...
})

server := &http.Server{
    Addr:         ":8080",
    Handler:      mux,
    ReadTimeout:  5 * time.Second,
    WriteTimeout: 10 * time.Second,
    IdleTimeout:  60 * time.Second,
}
```

Middleware como função `func(http.Handler) http.Handler` — composable sem framework.

## encoding/json

```go
type User struct {
    ID    int    `json:"id"`
    Name  string `json:"name"`
    Email string `json:"email,omitempty"`
}

// Serializar
data, err := json.Marshal(user)

// Deserializar
var user User
err := json.Unmarshal(data, &user)

// Stream (mais eficiente para payloads grandes)
json.NewDecoder(r.Body).Decode(&user)
json.NewEncoder(w).Encode(user)
```

## database/sql

```go
db, err := sql.Open("pgx", os.Getenv("DATABASE_URL"))
db.SetMaxOpenConns(25)
db.SetMaxIdleConns(5)

// Sempre usar context com timeout
ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
defer cancel()

row := db.QueryRowContext(ctx, "SELECT id, name FROM users WHERE id = $1", id)
err := row.Scan(&user.ID, &user.Name)
```

## testing — Table-Driven Tests

```go
func TestAdd(t *testing.T) {
    tests := []struct {
        name string
        a, b int
        want int
    }{
        {"positive", 1, 2, 3},
        {"negative", -1, -2, -3},
        {"zero", 0, 0, 0},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            t.Parallel()
            got := Add(tt.a, tt.b)
            if got != tt.want {
                t.Errorf("Add(%d, %d) = %d, want %d", tt.a, tt.b, got, tt.want)
            }
        })
    }
}
```

## unicode/utf8

Pacote de referência para tudo relacionado a codificação/decodificação [[utf-8]] em Go — `utf8.RuneCountInString`, `utf8.DecodeRune`. [[wiki/sources/algoritmo-decode-utf8-com-tdd]] reimplementa `DecodeRune` do zero como exercício didático e **importa a própria suite de testes desse pacote** da stdlib como oráculo de corretude — validando a implementação própria contra os mesmos edge cases (sequências inválidas, overlong encoding, surrogate pairs) que o time do Go já mapeou. Ver [[tdd]] para a técnica geral de importar testes de uma implementação de referência.

## log/slog (Go 1.21+)

```go
logger := slog.New(slog.NewJSONHandler(os.Stdout, nil))
logger.Info("user created", "user_id", id, "email", email)

// Output: {"time":"...","level":"INFO","msg":"user created","user_id":"...","email":"..."}
```

Substitui `log` padrão — structured logging nativo sem dependência externa.

## Ver também

- [[go-ecossistema]] — Chi, sqlc quando stdlib não é suficiente
- [[go-concorrencia]] — `context` e `sync` são parte da stdlib
- [[go-producao]] — `net/http/pprof` e `log/slog` em produção

## Key Sources

- [[wiki/sources/go-stdlib]]
- [[wiki/sources/algoritmo-decode-utf8-com-tdd]] — `unicode/utf8` como referência e fonte de testes para uma reimplementação didática de `DecodeRune`
