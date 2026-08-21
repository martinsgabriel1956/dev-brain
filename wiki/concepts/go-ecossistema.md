---
type: concept
title: "Go — Ecossistema e Tooling"
aliases: ["go chi", "go sqlc", "go golangci-lint", "go modules", "go gin echo"]
date_created: 2026-04-24
date_updated: 2026-08-18
source_count: 4
tags: [go, ecossistema, chi, sqlc, sqlx, gorm, linting, modules]
skill: lang-systems
status: stable
---

# Go — Ecossistema e Tooling

A stdlib de Go é poderosa — o ecossistema complementa onde ela é verbosa. Escolher libs que estendem o padrão em vez de substituí-lo.

Isso não é só uma recomendação de tooling — é reflexo de uma ausência estrutural: segundo [[wiki/entities/lucas-badico]], não existe um framework dominante para Go equivalente a Rails (Ruby) ou Express (Node). A comunidade opera por recomendações e convenções, não por um padrão único — empresas diferentes combinam ferramentas diferentes (Chi vs. Gin vs. `net/http` puro, sqlc vs. GORM). O ditado da comunidade citado na fonte resume a filosofia: "é melhor repetir um pouquinho de código do que acoplar a uma grande biblioteca" — o que explica por que o Go nunca desenvolveu um framework "full-stack" à la Rails, e por que peças como autenticação e logging tendem a ser escritas à mão (via middleware/interceptor próprio) em vez de importadas de uma lib grande. Ver [[wiki/sources/golang-profissional-sem-grandes-frameworks]].

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

**Gorilla Mux:** roteador consolidado, com suporte a expressões regulares e matching por método/host/scheme nas rotas — usado em produção por [[wiki/entities/lucas-badico]] no seu sistema de mentoria em Go como uma das únicas três dependências externas do "Core" do projeto (ao lado do pacote gRPC do Google e do GORM). Ver [[wiki/sources/sistema-mentoria-golang-monolito-modular-live-lucas-badico]].

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

## Uso Declarado em Produção (Go Developer Survey)

Confirmando o encaixe da stdlib/ecossistema acima com o uso real reportado pelo Go Developer Survey do Google: 74% dos devs Go usam a linguagem para APIs e serviços RPC (com destaque para gRPC em comunicação serviço-a-serviço, não só REST), 63% para ferramentas CLI, e 45% já para frontend/sites via frameworks Go. Vagas reais no mercado brasileiro (checadas ao vivo no LinkedIn) combinam Go com Clean Architecture, Design Patterns, microsserviços, AWS/GCP e Git Flow — reforçando que o ecossistema Go não é usado isolado, sempre dentro de um conjunto maior de práticas de backend moderno. Ver [[wiki/sources/golang-mercado-salarios-pesquisa-2024]].

## Ver também

- [[go-stdlib]] — entender net/http antes de adicionar Chi
- [[go-arquitetura]] — como o ecossistema encaixa na clean architecture
- [[go-producao]] — linting + Docker + observabilidade

## Key Sources

- [[wiki/sources/go-ecossistema]]
- [[wiki/sources/golang-mercado-salarios-pesquisa-2024]]
- [[wiki/sources/golang-profissional-sem-grandes-frameworks]] — ausência de framework dominante em Go e o ditado "repetir é melhor que acoplar"
- [[wiki/sources/sistema-mentoria-golang-monolito-modular-live-lucas-badico]] — caso real de produção com apenas três libs externas (Gorilla Mux, gRPC do Google, GORM), confirmando a tese de dependência mínima na prática
