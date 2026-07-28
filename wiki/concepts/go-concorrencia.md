---
type: concept
title: "Go — Concorrência"
aliases: ["goroutines", "go channels", "go csp", "go sync", "go context"]
date_created: 2026-04-24
date_updated: 2026-07-28
source_count: 2
tags: [go, concorrencia, goroutines, channels, sync, context, csp]
skill: lang-systems
status: stable
---

# Go — Concorrência

Go implementa **CSP (Communicating Sequential Processes)** — goroutines comunicam-se via channels em vez de compartilhar memória. Mantra: *"Do not communicate by sharing memory; share memory by communicating."*

## Goroutines

Goroutines têm stack inicial de ~2KB (threads OS: ~1MB). Multiplexadas pelo runtime Go sobre threads OS. Custo de criação próximo de zero:

```go
go func() {
    // executa concorrentemente
}()
```

## Channels

```go
ch := make(chan int)       // unbuffered — sincroniza sender e receiver
ch := make(chan int, 10)   // buffered — desacopla com limite

ch <- 42        // send (bloqueia se unbuffered e sem receiver)
val := <-ch     // receive
close(ch)       // sinaliza fim — receivers recebem zero value após fechar
```

**Regra:** unbuffered = sincronização; buffered = desacoplamento controlado.

## context.Context

Deve ser o primeiro parâmetro de toda função que pode ser cancelada:

```go
func fetchUser(ctx context.Context, id string) (*User, error) {
    // ctx.Done() sinaliza cancelamento
}
```

`context.WithTimeout`, `context.WithCancel`, `context.WithDeadline` — sempre chamar `cancel()` com `defer`.

## sync Primitives

- `sync.Mutex` / `sync.RWMutex` — estado compartilhado quando channels seriam overengineering
- `sync.WaitGroup` — aguardar N goroutines concluírem
- `sync.Once` — inicialização garantida uma única vez
- `sync/atomic` — operações atômicas sem lock (cuidado: difícil de raciocinar)

## Padrões

- **Fan-out:** uma goroutine distribui trabalho para N workers via channel
- **Pipeline:** goroutines encadeadas via channels, cada estágio transforma dados
- **Done channel:** canal de sinalização para cancelamento manual
- **Semaphore:** channel buffered como limitador de concorrência

## Race Detector

```bash
go test -race ./...
go run -race main.go
```

Obrigatório em CI — detecta data races em tempo de execução.

## Biblioteca `conc` (Sourcegraph)

Biblioteca da Sourcegraph que encapsula padrões comuns de concorrência em Go (fan-out, error groups, panics recuperados) sobre uma API mais simples que goroutines/channels/mutexes crus. [[wiki/sources/aprenda-a-programar-do-jeito-dificil]] cita seu próprio uso como o caminho recomendado por terceiros para resolver um problema de performance (bot de Tibia), mas relata ter escolhido implementar concorrência do zero antes de recorrer à biblioteca pronta, para entender o mecanismo subjacente — ver [[wiki/concepts/aprendizado-por-luta]].

## Ver também

- [[go-fundamentos]] — tipos e structs
- [[go-stdlib]] — `context`, `sync` fazem parte da stdlib
- [[distributed-locks]] — concorrência distribuída além de uma instância

## Key Sources

- [[wiki/sources/go-concorrencia]]
- [[wiki/sources/aprenda-a-programar-do-jeito-dificil]] — biblioteca `conc` da Sourcegraph; caso de otimização de bot de Tibia (20min → 2-3s)
