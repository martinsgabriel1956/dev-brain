---
date: 2026-04-24
tags: [tech-mentor, lang-systems, go, concorrencia, goroutines, channels, context, sync]
skill: lang-systems/references/go
level: intermediário
---

# Go — Concorrência

## Contexto
O modelo de concorrência de Go é baseado em CSP (Communicating Sequential Processes). O slogan oficial: **"Don't communicate by sharing memory; share memory by communicating."** Goroutines custam ~2KB de stack inicial (vs ~1MB de thread OS) — escalam para milhões facilmente.

> Ver também [[go-core]] para goroutines, channels e context com exemplos detalhados.

---

## Goroutines

```go
go func() {
    // executa em goroutine separada
    fmt.Println("async")
}()

// Para aguardar conclusão: WaitGroup
var wg sync.WaitGroup

for i := range items {
    wg.Add(1)
    go func(item Item) {
        defer wg.Done()
        process(item)
    }(items[i]) // passar como parâmetro — evita closure capture bug
}

wg.Wait()
```

---

## Channels

```go
// Unbuffered — sincroniza sender e receiver
ch := make(chan int)

// Buffered — sender não bloqueia até cap ser atingida
ch := make(chan int, 100)

// Fechar channel sinaliza que não haverá mais envios
close(ch)

// Range sobre channel drena até ser fechado
for v := range ch {
    fmt.Println(v)
}

// Select — multiplexação
select {
case msg := <-ch1:
    handle(msg)
case msg := <-ch2:
    handle(msg)
case <-time.After(5 * time.Second):
    return ErrTimeout
case <-ctx.Done():
    return ctx.Err()
}
```

**Regra**: quem cria o channel é responsável por fechá-lo. Nunca feche do lado do receiver.

---

## sync — Mutex e Primitivos

```go
type SafeCounter struct {
    mu    sync.Mutex
    count int
}

func (c *SafeCounter) Increment() {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.count++
}

func (c *SafeCounter) Value() int {
    c.mu.RLock() // RWMutex para leitura concorrente
    defer c.mu.RUnlock()
    return c.count
}

// sync.Once — executa exatamente uma vez (singleton, init lazy)
var once sync.Once
var instance *DB

func GetDB() *DB {
    once.Do(func() {
        instance = connectDB()
    })
    return instance
}
```

---

## context.Context

Propagação de cancelamento e deadlines por toda a call chain.

```go
// Criar contexto com timeout
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel() // sempre chamar cancel para liberar recursos

// Passar pelo call chain — ctx sempre primeiro parâmetro
result, err := fetchData(ctx, userID)

// Verificar cancelamento
select {
case <-ctx.Done():
    return ctx.Err() // context.DeadlineExceeded ou context.Canceled
default:
    // continuar
}

// Valores no contexto — apenas para metadados de request (trace ID, auth)
type ctxKey string
ctx = context.WithValue(ctx, ctxKey("traceID"), "abc-123")
traceID := ctx.Value(ctxKey("traceID")).(string)
```

---

## Padrões de Concorrência

**Worker Pool:**
```go
func workerPool(ctx context.Context, jobs <-chan Job, numWorkers int) <-chan Result {
    results := make(chan Result, len(jobs))

    var wg sync.WaitGroup
    for i := 0; i < numWorkers; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            for job := range jobs {
                select {
                case <-ctx.Done():
                    return
                default:
                    results <- process(job)
                }
            }
        }()
    }

    go func() {
        wg.Wait()
        close(results)
    }()

    return results
}
```

**Fan-out / Fan-in:**
```go
// Fan-out: distribui trabalho para múltiplos workers
// Fan-in: merge de múltiplos channels em um

func merge(channels ...<-chan int) <-chan int {
    var wg sync.WaitGroup
    merged := make(chan int)

    output := func(c <-chan int) {
        defer wg.Done()
        for v := range c {
            merged <- v
        }
    }

    wg.Add(len(channels))
    for _, c := range channels {
        go output(c)
    }

    go func() {
        wg.Wait()
        close(merged)
    }()

    return merged
}
```

**Pipeline:**
```go
func pipeline(nums []int) <-chan int {
    out := make(chan int)
    go func() {
        defer close(out)
        for _, n := range nums {
            out <- n * 2 // transform stage
        }
    }()
    return out
}
```

---

## Race Detector

```bash
go test -race ./...
go run -race main.go
```

Sempre rodar em CI. O race detector tem ~5-10x overhead — não usar em produção.

---

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---------|----------|-------------|
| Goroutines | Baratas, fáceis de criar | Leak se não houver mecanismo de parada |
| Channels | Composição elegante de pipelines | Deadlock se sender/receiver não alinhados |
| Mutex | Simples para estado compartilhado | Risco de lock contention, deadlock |
| `sync.Map` | Thread-safe sem lock explícito | Menos ergonômico, performance específica |

## Quando Usar / Quando Evitar

**Channel vs Mutex:** use channel para transferir ownership de dados. Use mutex para proteger acesso a estado compartilhado. Não force channels onde mutex é mais simples.

**Goroutine leak:** toda goroutine precisa de uma condição de saída — ctx.Done(), channel fechado, ou erro. Goroutines sem saída vivem até o processo morrer.

## Conceitos Relacionados
[[go-core]] · [[go-fundamentos]] · [[go-producao]] · [[go-stdlib]]

---
*Fonte: tech-mentor skill · lang-systems · 2026-04-24*
