---
date: 2026-04-23
tags: [go, arquitetura, clean-architecture, simplicidade, interfaces, struct, pragmatismo]
skill: tech-mentor-backend
level: intermediário
source_url: https://blog.vertigrated.com/go-is-not-java
author: vertigrated.com
date_published: desconhecida
nota: fetch falhou com HTTP 429 — nota baseada na transcrição do vídeo clean-architecture-ia-custo-real
---

# Go is not Java

## TL;DR

Go prova que os princípios fundamentais de Clean Architecture — lógica de negócio isolada, injeção de dependência, testabilidade — são separáveis do ritual de camadas físicas, interfaces para cada coisa e frameworks de DI. Go não tem classes, não tem herança, não tem anotações. Tem struct, interface implícita e função. E ainda assim todo sistema Go sério em produção implementa esses princípios.

## O Argumento Central

**O erro não é defender princípios de Clean Architecture. O erro é confundir os princípios com a prática ritualística.**

Princípios válidos (separáveis da cerimônia):
- Lógica de negócio isolada de infra
- Injeção de dependência para testabilidade
- Separação de responsabilidades

Cerimônia questionável:
- Interface para cada repositório mesmo com uma única implementação
- Use case para cada operação CRUD
- Mappers entre todas as camadas
- DTOs em todas as direções

Go eliminou a cerimônia e manteve os princípios. O resultado: Kubernetes, Docker, a infraestrutura inteira do Cloudflare — todos implementam os fundamentos de Clean Architecture sem nenhum ritual.

## Como Go Faz

### Interfaces Implícitas

```go
// Não tem `implements`. Se seu struct tem os métodos, implementa a interface.
type UserRepository interface {
    FindByID(ctx context.Context, id string) (*User, error)
    Save(ctx context.Context, user *User) error
}

// PostgresUserRepo implementa UserRepository implicitamente
type PostgresUserRepo struct{ db *sql.DB }

func (r *PostgresUserRepo) FindByID(ctx context.Context, id string) (*User, error) {
    // implementação
}
```

Sem `implements UserRepository`. Sem anotação. Sem registro em container de DI. A interface é definida onde é *usada*, não onde é *implementada* — isso é inversão real.

### Sem Framework de DI

Em Go, DI é feita via construtor. Sem container, sem magic, sem XML, sem reflection:

```go
func NewOrderService(repo UserRepository, email EmailSender) *OrderService {
    return &OrderService{repo: repo, email: email}
}
```

O próprio compilador garante que a dependência está satisfeita. É testável por construção.

### Sem Herança — Composição Direta

```go
// Em vez de herança, Go usa composição de structs
type AdminUser struct {
    User                  // embed — herda todos os métodos
    Permissions []string
}
```

## A Lição Para Qualquer Linguagem

Go não inventou nada novo em termos de princípios. Ele apenas removeu os mecanismos que tornavam a cerimônia possível e forçou a usar soluções mais diretas.

A implicação: se você está em TypeScript/Java/C# e usa uma arquitetura complexa, a pergunta válida é — **isso está aqui porque resolve um problema real, ou porque a linguagem/framework torna possível e os blog posts normalizam?**

## Implicações para IA

Codebases no estilo Go são mais fáceis para agentes navegarem:
- Interfaces implícitas → AST estático consegue rastrear (sem DI container oculto)
- Sem camadas físicas separadas → menos arquivos para a mesma feature
- Funções em vez de hierarquias de classe → menos indireção para o agente seguir

É exatamente o oposto do problema documentado no [[sources/navigation-paradox-2026]].

## Conceitos Relacionados

- [[sources/clean-architecture-ia-custo-real]] — o caso real que motiva essa discussão
- [[sources/navigation-paradox-2026]] — por que DI containers são problemáticos para agentes
- [[sources/go-core]] — goroutines, channels, interfaces Go em profundidade

---

*Fonte: blog.vertigrated.com/go-is-not-java (fetch falhou 429) · nota baseada em transcrição de vídeo · 2026-04-23*
