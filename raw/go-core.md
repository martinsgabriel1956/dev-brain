---
date: 2026-04-17
tags: [tech-mentor, linguagens, go, goroutines, channels, context, interfaces, concorrencia]
skill: tech-mentor-backend/references/go
level: intermediário
---

# Go — Goroutines, Channels, Context, Interfaces e Error Handling

## Contexto

Go foi projetado para ser a linguagem dos sistemas distribuídos modernos: concorrência nativa com goroutines/channels, compilação rápida, binary único sem runtime externo, e um sistema de tipos simples mas poderoso. O diferencial central é o modelo de concorrência CSP (Communicating Sequential Processes) — goroutines se comunicam através de channels, não memória compartilhada.

---

## Goroutines — Concorrência Leve

```go
package main

import (
    "fmt"
    "sync"
    "time"
)

// Goroutine: função executada concorrentemente com `go` keyword
// Go runtime multiplexa goroutines em threads do OS (M:N threading)
// Custo: ~2KB de stack inicial (vs ~1MB para threads OS)
func worker(id int, jobs <-chan int, results chan<- int, wg *sync.WaitGroup) {
    defer wg.Done()
    for job := range jobs {
        // Simular trabalho
        time.Sleep(10 * time.Millisecond)
        results <- job * 2
        fmt.Printf("Worker %d processou job %d\n", id, job)
    }
}

func main() {
    const numWorkers = 5
    const numJobs = 20

    jobs := make(chan int, numJobs)     // buffered: sender não bloqueia até cheio
    results := make(chan int, numJobs)

    var wg sync.WaitGroup

    // Iniciar worker pool
    for w := 1; w <= numWorkers; w++ {
        wg.Add(1)
        go worker(w, jobs, results, &wg)
    }

    // Enviar jobs
    for j := 1; j <= numJobs; j++ {
        jobs <- j
    }
    close(jobs)  // fechar channel sinaliza que não há mais jobs

    // Aguardar workers e fechar results
    go func() {
        wg.Wait()
        close(results)
    }()

    // Coletar resultados
    total := 0
    for result := range results {
        total += result
    }
    fmt.Printf("Total: %d\n", total)
}
```

---

## Channels — Comunicação entre Goroutines

```go
package main

import (
    "fmt"
    "time"
)

// Unbuffered channel: sincronização (send bloqueia até recv estar pronto)
// Buffered channel:  fila (send bloqueia apenas quando buffer está cheio)

// Fan-out: distribuir trabalho para múltiplos workers
func fanOut[T any](input <-chan T, numWorkers int) []<-chan T {
    outputs := make([]<-chan T, numWorkers)
    for i := range numWorkers {
        ch := make(chan T)
        outputs[i] = ch
        go func() {
            defer close(ch)
            for v := range input {
                ch <- v
            }
        }()
    }
    return outputs
}

// Fan-in: agregar múltiplos channels em um
func fanIn[T any](channels ...<-chan T) <-chan T {
    merged := make(chan T)
    var done sync.WaitGroup

    pipe := func(c <-chan T) {
        defer done.Done()
        for v := range c {
            merged <- v
        }
    }

    done.Add(len(channels))
    for _, c := range channels {
        go pipe(c)
    }

    go func() {
        done.Wait()
        close(merged)
    }()

    return merged
}

// Select: multiplexação sobre múltiplos channels
func processWithTimeout(jobs <-chan string, timeout time.Duration) {
    timer := time.NewTimer(timeout)
    defer timer.Stop()

    for {
        select {
        case job, ok := <-jobs:
            if !ok {
                fmt.Println("Canal fechado, encerrando")
                return
            }
            fmt.Printf("Processando: %s\n", job)

        case <-timer.C:
            fmt.Println("Timeout atingido")
            return

        default:
            // Non-blocking check: executa se nenhum outro case estiver pronto
            // Útil para polling sem bloquear
            time.Sleep(1 * time.Millisecond)
        }
    }
}

// Pipeline pattern: encadear transformações como channels
func generate(nums ...int) <-chan int {
    out := make(chan int)
    go func() {
        defer close(out)
        for _, n := range nums {
            out <- n
        }
    }()
    return out
}

func square(in <-chan int) <-chan int {
    out := make(chan int)
    go func() {
        defer close(out)
        for n := range in {
            out <- n * n
        }
    }()
    return out
}

// Uso: pipeline := square(square(generate(1, 2, 3, 4)))
```

---

## Context — Cancelamento e Deadlines

```go
package main

import (
    "context"
    "fmt"
    "net/http"
    "time"
)

// Context propaga cancelamento, deadline e valores através de call stacks
// Regra: sempre o primeiro parâmetro, nunca armazenar em struct

type UserService struct {
    db DatabasePool
}

func (s *UserService) GetUser(ctx context.Context, userID string) (*User, error) {
    // Verificar se contexto já foi cancelado antes de iniciar trabalho
    select {
    case <-ctx.Done():
        return nil, ctx.Err()
    default:
    }

    // Passar context para todas as operações downstream
    row := s.db.QueryRowContext(ctx,
        "SELECT id, name, email FROM users WHERE id = $1", userID,
    )

    var u User
    if err := row.Scan(&u.ID, &u.Name, &u.Email); err != nil {
        return nil, fmt.Errorf("scanning user %s: %w", userID, err)
    }

    return &u, nil
}

// HTTP handler: context da request já inclui cancelamento
func handleGetUser(w http.ResponseWriter, r *http.Request) {
    ctx := r.Context()  // context cancelado quando cliente desconecta

    // Adicionar timeout à operação específica
    ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
    defer cancel()  // SEMPRE defer cancel para evitar context leak

    userID := r.PathValue("id")
    user, err := userService.GetUser(ctx, userID)
    if err != nil {
        if ctx.Err() == context.DeadlineExceeded {
            http.Error(w, "Request timeout", http.StatusGatewayTimeout)
            return
        }
        http.Error(w, "Internal error", http.StatusInternalServerError)
        return
    }

    _ = user  // usar user normalmente
}

// Context com valores — apenas para dados de request-scoped (tracing, auth)
type contextKey string

const (
    requestIDKey contextKey = "requestID"
    userIDKey    contextKey = "userID"
)

func withRequestID(ctx context.Context, requestID string) context.Context {
    return context.WithValue(ctx, requestIDKey, requestID)
}

func getRequestID(ctx context.Context) (string, bool) {
    v, ok := ctx.Value(requestIDKey).(string)
    return v, ok
}

// Context hierarchy:
// context.Background() → raiz de todos os contexts
// context.TODO()       → placeholder temporário (deve ser substituído)
// WithCancel:          cancelamento manual
// WithTimeout:         deadline relativo
// WithDeadline:        deadline absoluto
// WithValue:           dados de request scope
```

---

## Interfaces — Duck Typing Implícito

```go
package main

import (
    "context"
    "fmt"
    "io"
    "os"
)

// Interfaces são implementadas implicitamente — sem `implements`
// Interface pequena > interface grande (Interface Segregation)

type UserRepository interface {
    FindByID(ctx context.Context, id string) (*User, error)
    Save(ctx context.Context, user *User) error
}

type EmailSender interface {
    SendEmail(to, subject, body string) error
}

// Composição de interfaces
type Notifier interface {
    EmailSender
    SendSMS(to, message string) error
}

// Interface para testabilidade — mock facilmente
type PostgresUserRepo struct{ /* db */ }

func (r *PostgresUserRepo) FindByID(ctx context.Context, id string) (*User, error) {
    return nil, nil  // implementação real
}

func (r *PostgresUserRepo) Save(ctx context.Context, user *User) error {
    return nil
}

// InMemory mock para testes
type InMemoryUserRepo struct {
    users map[string]*User
}

func (r *InMemoryUserRepo) FindByID(ctx context.Context, id string) (*User, error) {
    u, ok := r.users[id]
    if !ok {
        return nil, fmt.Errorf("user %s not found", id)
    }
    return u, nil
}

func (r *InMemoryUserRepo) Save(ctx context.Context, user *User) error {
    r.users[user.ID] = user
    return nil
}

// interface{} / any — usar com moderação, preferir generics (Go 1.18+)

// Blank interface para funções que aceitam qualquer tipo
func printAny(v any) {
    fmt.Printf("%T: %v\n", v, v)
}

// Type assertion e type switch
func describe(i any) string {
    switch v := i.(type) {
    case string:
        return fmt.Sprintf("string: %q (len=%d)", v, len(v))
    case int:
        return fmt.Sprintf("int: %d", v)
    case []string:
        return fmt.Sprintf("[]string: %v (len=%d)", v, len(v))
    default:
        return fmt.Sprintf("unknown type: %T", v)
    }
}

// io.Reader / io.Writer — as interfaces mais importantes da stdlib
func copyFile(src, dst string) error {
    srcFile, err := os.Open(src)
    if err != nil {
        return fmt.Errorf("opening source: %w", err)
    }
    defer srcFile.Close()

    dstFile, err := os.Create(dst)
    if err != nil {
        return fmt.Errorf("creating destination: %w", err)
    }
    defer dstFile.Close()

    // io.Copy funciona com qualquer io.Reader → io.Writer
    if _, err := io.Copy(dstFile, srcFile); err != nil {
        return fmt.Errorf("copying: %w", err)
    }

    return nil
}
```

---

## Error Handling — Explícito e Composável

```go
package main

import (
    "errors"
    "fmt"
)

// Go não tem exceptions — erros são valores retornados explicitamente

// Erros customizados com contexto
type NotFoundError struct {
    Resource string
    ID       string
}

func (e *NotFoundError) Error() string {
    return fmt.Sprintf("%s with id %s not found", e.Resource, e.ID)
}

type ValidationError struct {
    Field   string
    Message string
}

func (e *ValidationError) Error() string {
    return fmt.Sprintf("validation error on %s: %s", e.Field, e.Message)
}

// Wrap de erros — preserva a stack de contexto
func findUserOrder(userID, orderID string) (*Order, error) {
    user, err := findUser(userID)
    if err != nil {
        return nil, fmt.Errorf("finding user for order lookup: %w", err)
    }

    order, err := findOrder(orderID)
    if err != nil {
        return nil, fmt.Errorf("finding order %s for user %s: %w", orderID, userID, err)
    }

    if order.UserID != user.ID {
        return nil, &NotFoundError{Resource: "order", ID: orderID}
    }

    return order, nil
}

// errors.Is — verificar tipo de erro na cadeia de wrap
// errors.As — extrair erro específico da cadeia

func handleOrderRequest(userID, orderID string) {
    order, err := findUserOrder(userID, orderID)
    if err != nil {
        var notFound *NotFoundError
        var validation *ValidationError

        switch {
        case errors.As(err, &notFound):
            fmt.Printf("Not found: %s\n", notFound.Error())

        case errors.As(err, &validation):
            fmt.Printf("Validation: %s\n", validation.Error())

        default:
            fmt.Printf("Internal error: %v\n", err)
        }
        return
    }

    _ = order
}

// Sentinel errors — erros predefinidos para comparação com errors.Is
var (
    ErrNotFound    = errors.New("not found")
    ErrUnauthorized = errors.New("unauthorized")
    ErrConflict    = errors.New("conflict")
)

// Wrap com sentinel
func getUser(id string) (*User, error) {
    if id == "" {
        return nil, fmt.Errorf("user lookup: %w", ErrNotFound)
    }
    return nil, nil
}

// Verificar com errors.Is (funciona mesmo com wrapping)
func main() {
    _, err := getUser("")
    if errors.Is(err, ErrNotFound) {
        fmt.Println("usuário não encontrado")
    }
}
```

---

## Sync Primitives

```go
package main

import (
    "sync"
    "sync/atomic"
)

// Mutex — exclusão mútua para acesso a estado compartilhado
type SafeCounter struct {
    mu    sync.Mutex
    count int64
}

func (c *SafeCounter) Increment() {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.count++
}

func (c *SafeCounter) Value() int64 {
    c.mu.RLock()  // RLock: múltiplos readers simultâneos
    defer c.mu.RUnlock()
    return c.count
}

// sync.atomic — operações atômicas sem mutex (mais performático)
type AtomicCounter struct {
    count atomic.Int64
}

func (c *AtomicCounter) Increment() { c.count.Add(1) }
func (c *AtomicCounter) Value() int64 { return c.count.Load() }

// sync.Once — executar uma vez (inicialização lazy thread-safe)
type Config struct {
    once     sync.Once
    settings map[string]string
}

func (c *Config) Get(key string) string {
    c.once.Do(func() {
        c.settings = loadFromEnv()  // executado uma única vez
    })
    return c.settings[key]
}

// sync.Pool — reutilização de objetos (reduz GC pressure)
var bufferPool = sync.Pool{
    New: func() any {
        return make([]byte, 0, 4096)
    },
}

func processRequest(data []byte) {
    buf := bufferPool.Get().([]byte)
    defer bufferPool.Put(buf[:0])  // reset e devolver ao pool

    buf = append(buf, data...)
    // usar buf...
}

func loadFromEnv() map[string]string { return map[string]string{} }
```

---

## Trade-offs

| Feature | Go | Trade-off vs Alternativas |
|---|---|---|
| **Goroutines** | 2KB stack, M:N threading | vs threads OS (1MB cada) — Go vence em escala |
| **Channels** | Comunicação sem lock explícito | vs mutex — channels são mais seguros, mutex é mais performático |
| **Error handling** | Explícito, sem exceptions | vs exceptions — mais verboso, mas impossível ignorar errors |
| **Interfaces** | Implícitas (duck typing) | vs Java explicit implement — mais flexível, menos documentado |
| **Generics** | Go 1.18+, básicos | vs TypeScript/Rust — menos poderoso, mas suficiente |

## Quando Usar / Quando Evitar

**Go para:** serviços de alta performance, CLIs, tooling de infraestrutura, networking (proxies, gateways), microsserviços com requirements de latência baixa e binary pequeno.

**Evitar Go para:** scripting rápido (use Python), aplicações com muita lógica de domínio complexa onde a verbosidade do error handling é custo alto, prototipagem rápida.

**Goroutines vs async/await:** Go é sincrono na aparência mas concorrente na execução. Muito mais simples de raciocinar que callbacks ou async/await encadeados.

## Conceitos Relacionados

[[go-avancado]] · [[grpc]] · [[kubernetes-operators]] · [[distributed-locks]]

---
*Fonte: tech-mentor skill · lang-systems · 2026-04-17*
