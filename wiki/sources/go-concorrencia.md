---
type: source
title: "Go — Concorrência"
aliases: ["go goroutines", "go channels", "go sync", "csp go"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/go-concorrencia.md
source_url: ""
author: "lang-systems skill"
date_published: 2026-04-24
date_ingested: 2026-04-24
source_count: 0
tags: [go, concorrencia, goroutines, channels, sync, context, csp]
skill: lang-systems
status: stable
---

# Go — Concorrência

## TL;DR

Go implementa CSP (Communicating Sequential Processes) — goroutines se comunicam via channels em vez de compartilhar memória. Goroutines são baratas (~2KB de stack inicial, multiplicadas por milhares). `sync.Mutex` para estado compartilhado quando channels seriam overengineering. `context.Context` propaga cancelamento e deadlines através de toda a call chain.

## Claims Principais

| Claim | Confiança |
|---|---|
| "Do not communicate by sharing memory; share memory by communicating" — mantra Go | Alta |
| Goroutines são ordens de magnitude mais baratas que threads OS | Alta |
| Channel unbuffered = sincronização; buffered = desacoplamento com limite | Alta |
| `context.Context` deve ser o primeiro parâmetro de toda função que pode ser cancelada | Alta |
| Race detector (`go test -race`) deve rodar em CI — detecta data races em tempo de execução | Alta |
| `select` com `default` cria non-blocking receive — usar com cuidado para evitar busy-loop | Média |

## Conceitos Abordados

- [[go-concorrencia]] · [[go-fundamentos]] · [[go-stdlib]] · [[distributed-locks]]
