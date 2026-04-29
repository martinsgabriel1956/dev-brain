---
type: source
title: "Go — Standard Library Essencial"
aliases: ["go net/http", "go encoding/json", "go database/sql", "go testing", "go slog"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_file: /home/nemomartins/Documentos/new/dev-study/raw/go-stdlib.md
source_url: ""
author: "lang-systems skill"
date_published: 2026-04-24
date_ingested: 2026-04-24
source_count: 0
tags: [go, stdlib, net-http, json, database-sql, testing, slog]
skill: lang-systems
status: stable
---

# Go — Standard Library Essencial

## TL;DR

A stdlib de Go é intencionalmente abrangente — `net/http`, `encoding/json`, `database/sql` e `testing` cobrem a maioria dos serviços sem dependências externas. `log/slog` (Go 1.21+) é o padrão para structured logging. Table-driven tests com `t.Run` são o idioma de testes em Go. Entender a stdlib antes de adicionar frameworks evita abstrações desnecessárias.

## Claims Principais

| Claim | Confiança |
|---|---|
| `net/http` com middleware chain (funções que recebem e retornam `http.Handler`) é suficiente sem framework | Alta |
| `encoding/json` usa reflection — structs com tags `json:` controlam serialização | Alta |
| `database/sql` é interface genérica — driver específico (pgx, lib/pq) registrado via `sql.Register` | Alta |
| Table-driven tests com `t.Run` e `t.Parallel()` são o padrão idiomático | Alta |
| `log/slog` substituiu `log` — structured logging com handlers JSON/Text | Alta |
| `context.WithTimeout` em chamadas de DB e HTTP evita goroutine leaks | Alta |

## Conceitos Abordados

- [[go-stdlib]] · [[go-fundamentos]] · [[go-concorrencia]] · [[go-ecossistema]] · [[go-producao]]
