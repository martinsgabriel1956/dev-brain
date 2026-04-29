---
date: 2026-04-24
tags: [tech-mentor, lang-systems, go, stdlib, net-http, json, database-sql, testing, slog]
skill: lang-systems/references/go
level: intermediário
---

# Go — Standard Library Essencial

## Contexto
A stdlib de Go é intencionalmente abrangente. Para a maioria dos serviços, `net/http`, `encoding/json`, `database/sql` e `testing` são suficientes sem nenhuma dependência externa. Entender a stdlib antes de adicionar frameworks evita abstrações desnecessárias.

---

## net/http — Server e Client

```go
// Server
mux := http.NewServeMux()

mux.HandleFunc("GET /users", listUsersHandler)
mux.HandleFunc("POST /users", createUserHandler)
mux.HandleFunc("GET /users/{id}", getUserHandler) // path params Go 1.22+

srv := &http.Server{
    Addr:         ":8080",
    Handler:      mux,
    ReadTimeout:  5 * time.Second,
    WriteTimeout: 10 * time.Second,
    IdleTimeout:  120 * time.Second,
}

log.Fatal(srv.ListenAndServe())
```

```go
// Handler
func listUsersHandler(w http.ResponseWriter, r *http.Request) {
    users, err := repo.FindAll(r.Context())
    if err != nil {
        http.Error(w, "internal error", http.StatusInternalServerError)
        return
    }

    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(users)
}

// Middleware — wrapper de http.Handler
func withLogging(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        start := time.Now()
        next.ServeHTTP(w, r)
        log.Printf("%s %s %v", r.Method, r.URL.Path, time.Since(start))
    })
}
```

```go
// Client com timeout
client := &http.Client{Timeout: 10 * time.Second}

req, err := http.NewRequestWithContext(ctx, http.MethodGet, url, nil)
if err != nil {
    return err
}

resp, err := client.Do(req)
if err != nil {
    return err
}
defer resp.Body.Close()
```

---

## encoding/json

```go
type User struct {
    ID        int       `json:"id"`
    Name      string    `json:"name"`
    Email     string    `json:"email"`
    Password  string    `json:"-"`          // nunca serializar
    CreatedAt time.Time `json:"created_at"`
    Bio       *string   `json:"bio,omitempty"` // omite se nil
}

// Marshal
data, err := json.Marshal(user)

// Unmarshal
var u User
err = json.Unmarshal(data, &u)

// Streaming (mais eficiente para HTTP)
json.NewEncoder(w).Encode(user)
json.NewDecoder(r.Body).Decode(&u)

// Custom marshaler
func (u User) MarshalJSON() ([]byte, error) {
    type Alias User
    return json.Marshal(&struct {
        Alias
        CreatedAt string `json:"created_at"`
    }{
        Alias:     Alias(u),
        CreatedAt: u.CreatedAt.Format(time.RFC3339),
    })
}
```

---

## database/sql

```go
db, err := sql.Open("postgres", dsn)
if err != nil {
    return err
}
defer db.Close()

// Connection pool
db.SetMaxOpenConns(25)
db.SetMaxIdleConns(25)
db.SetConnMaxLifetime(5 * time.Minute)

// Query com context
rows, err := db.QueryContext(ctx, "SELECT id, name FROM users WHERE active = $1", true)
if err != nil {
    return err
}
defer rows.Close()

var users []User
for rows.Next() {
    var u User
    if err := rows.Scan(&u.ID, &u.Name); err != nil {
        return err
    }
    users = append(users, u)
}
if err := rows.Err(); err != nil {
    return err
}

// Transação
tx, err := db.BeginTx(ctx, nil)
if err != nil {
    return err
}
defer tx.Rollback() // no-op se já commitado

_, err = tx.ExecContext(ctx, "UPDATE accounts SET balance = balance - $1 WHERE id = $2", amount, fromID)
if err != nil {
    return err
}
_, err = tx.ExecContext(ctx, "UPDATE accounts SET balance = balance + $1 WHERE id = $2", amount, toID)
if err != nil {
    return err
}

return tx.Commit()
```

---

## testing — Table-Driven Tests

```go
func TestDivide(t *testing.T) {
    tests := []struct {
        name    string
        a, b    float64
        want    float64
        wantErr bool
    }{
        {name: "normal division", a: 10, b: 2, want: 5},
        {name: "division by zero", a: 10, b: 0, wantErr: true},
        {name: "negative numbers", a: -6, b: 2, want: -3},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got, err := divide(tt.a, tt.b)
            if (err != nil) != tt.wantErr {
                t.Errorf("divide() error = %v, wantErr %v", err, tt.wantErr)
                return
            }
            if got != tt.want {
                t.Errorf("divide() = %v, want %v", got, tt.want)
            }
        })
    }
}

// Benchmark
func BenchmarkDivide(b *testing.B) {
    for i := 0; i < b.N; i++ {
        divide(10, 3)
    }
}
```

---

## log/slog — Structured Logging (Go 1.21+)

```go
// Setup
logger := slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{
    Level: slog.LevelInfo,
}))
slog.SetDefault(logger)

// Uso
slog.Info("user created", "user_id", userID, "email", email)
slog.Error("database error", "err", err, "query", query)

// Com context (para trace propagation)
slog.InfoContext(ctx, "request completed",
    "method", r.Method,
    "path", r.URL.Path,
    "duration_ms", time.Since(start).Milliseconds(),
)
```

---

## Trade-offs

| Pacote | Vantagem | Desvantagem |
|--------|----------|-------------|
| `net/http` puro | Zero deps, controle total | Verbose para rotas complexas |
| `encoding/json` | Simples, rápido | Reflection-based, lento vs alternatives |
| `database/sql` | Genérico, connection pool embutido | Verbose, sem query builder |
| `testing` | Sem deps, paralelismo nativo | Assertions manuais (sem testify) |

## Quando Usar / Quando Evitar

**`net/http` puro:** use para serviços simples ou quando performance é crítica. Para APIs REST com muitas rotas e middlewares, Chi ou Gin reduzem boilerplate sem custo significativo.

**`database/sql` direto:** prefira sqlx (extensão mínima) ou sqlc (geração de código). GORM esconde complexidade que você vai precisar entender quando der errado.

## Conceitos Relacionados
[[go-fundamentos]] · [[go-ecossistema]] · [[go-concorrencia]] · [[go-producao]]

---
*Fonte: tech-mentor skill · lang-systems · 2026-04-24*
