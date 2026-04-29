---
type: concept
title: "Go — Ecossistema e Tooling"
aliases: ["go chi", "go sqlc", "go golangci-lint", "go modules", "go gin echo"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [go, ecossistema, chi, sqlc, sqlx, gorm, linting, modules]
skill: lang-systems
status: stable
---

# Go — Ecossistema e Tooling

A stdlib de Go é poderosa — o ecossistema complementa onde ela é verbosa. Escolher libs que estendem o padrão em vez de substituí-lo.

## HTTP: Roteadores

**`net/http` puro (Go 1.22+):** suporta path parameters nativos com `{id}` — suficiente para APIs simples.

**Chi (recomendado):** wrapper fino sobre `net/http`, composable middleware, sem mágica:

```go
r := chi.NewRouter()
r.Use(middleware.Logger)
r.Use(middleware.Recoverer)
r.Route("/users", func(r chi.Router) {
    r.Get("/{id}", handler.GetUser)
    r.Post("/", handler.CreateUser)
})
```

**Gin / Echo:** mais features, reflection interno, overhead vs Chi para serviços que já usam `net/http`.

## SQL: Acesso a Dados

**sqlc (recomendado):** escreva SQL real → gera código Go type-safe. Zero `interface{}`, zero N+1 acidental:

```sql
-- query.sql
-- name: GetUser :one
SELECT id, name, email FROM users WHERE id = $1;
```

```go
// gerado automaticamente
user, err := queries.GetUser(ctx, id)
```

**sqlx:** extensão leve de `database/sql` com `StructScan` e named queries — bom para queries dinâmicas.

**GORM:** conveniente para prototipagem, migrations automáticas. Gera queries imprevisíveis em relacionamentos complexos — evitar em produção com queries críticas.

## Config e Ambiente

```go
// viper ou envconfig
type Config struct {
    DatabaseURL string `env:"DATABASE_URL,required"`
    Port        int    `env:"PORT" envDefault:"8080"`
}
```

Sempre validar com Zod-equivalente (envconfig, viper) — nunca `os.Getenv` direto sem fallback.

## Linting

```yaml
# .golangci.yml
linters:
  enable:
    - staticcheck   # bugs e performance
    - errcheck      # erros não checados
    - gosimple      # simplificações idiomáticas
    - govet         # análise do compilador
```

`golangci-lint run` em CI — bloqueia merge em novas violações.

## Ver também

- [[go-stdlib]] — entender net/http antes de adicionar Chi
- [[go-arquitetura]] — como o ecossistema encaixa na clean architecture
- [[go-producao]] — linting + Docker + observabilidade

## Key Sources

- [[wiki/sources/go-ecossistema]]
