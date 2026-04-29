---
type: source
title: "Go — Goroutines, Channels, Context, Interfaces e Error Handling"
aliases: ["go", "golang", "goroutines", "channels", "context go", "interfaces go", "error handling go", "csp"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/go-core.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [go, golang, goroutines, channels, context, interfaces, error-handling, csp, concurrency, sync]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Go: linguagem para sistemas distribuídos com concorrência nativa via CSP (Communicating Sequential Processes). Goroutines são threads leves (~2KB stack). Channels para comunicação segura entre goroutines. Context para cancelamento e deadlines propagados pela call chain. Interfaces implícitas (duck typing). Error handling explícito: `if err != nil` é intencional — erros são valores, não exceções.

## Key Claims

**Claim:** Goroutines com channels seguem "share memory by communicating" — não locks em memória compartilhada.
**Evidence:** Go philosophy: ao invés de mutex para proteger estado compartilhado, passar o dado via channel. Channel é o ponto de sincronização. Goroutines leves (~2KB vs ~1MB de thread OS): pode ter 100k+ goroutines simultâneas. M:N scheduling: N goroutines mapeadas em M threads OS via Go runtime.
**Confidence:** alta

**Claim:** Context é obrigatório em toda chamada de I/O — propaga cancelamento e timeout pela chain de chamadas.
**Evidence:** `context.WithTimeout(ctx, 5*time.Second)`: todas as chamadas filhas (HTTP, DB, Redis) são canceladas quando o timeout expira. Sem Context: timeout na borda não se propaga — queries DB continuam executando mesmo após o cliente desistir. Convenção Go: `ctx context.Context` é sempre o primeiro parâmetro.
**Confidence:** alta

**Claim:** Interfaces implícitas em Go permitem polimorfismo sem herança — qualquer tipo que implementa os métodos satisfaz a interface.
**Evidence:** `type Writer interface { Write([]byte) (int, error) }`. `os.File` implementa `Write` → satisfaz `Writer` sem declaração explícita. Vantagem: pode criar interface que agrupa métodos de tipos de bibliotecas externas sem modificá-las. Diferente de Java/C# onde `implements` é declarado explicitamente.
**Confidence:** alta

**Claim:** Error handling explícito em Go é uma escolha de design — erros são valores, não exceções que saltam a call stack.
**Evidence:** `val, err := doSomething(); if err != nil { return nil, fmt.Errorf("context: %w", err) }`. `%w` wraps o erro original para `errors.Is/As`. Benefício: o caminho de erro é legível no código. Custo: verbosidade. Em Go, ignorar um erro é uma decisão explícita (`_ = doSomething()`), não acidental.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/goroutines]]
- [[concepts/channels-go]]
- [[concepts/context-go]]
- [[concepts/interfaces-go]]
- [[concepts/error-handling-go]]
- [[concepts/csp]]
- [[concepts/go-concurrency]]

## Open Questions

- Goroutine leaks em produção — como detectar goroutines que nunca terminam sem overhead de pprof contínuo?
- Generics em Go 1.18+ vs interfaces para abstrações reutilizáveis — quando cada abordagem é mais legível?
