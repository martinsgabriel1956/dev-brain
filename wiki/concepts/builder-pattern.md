---
type: concept
title: "Builder Pattern"
aliases: ["builder", "method chaining"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 1
tags: [design-patterns, creational, builder, gof]
skill: tech-mentor-backend
status: stable
---

# Builder Pattern

Padrão [[creational-patterns|criacional]] que constrói objetos complexos **passo a passo**, separando a construção da representação final. Permite encadear métodos (method chaining) em qualquer ordem e omitir os opcionais.

## Como funciona

```typescript
class RequestBuilder {
  private url: string;
  private method: string;
  private headers: Record<string, string> = {};

  setUrl(url: string) { this.url = url; return this; }
  setMethod(method: string) { this.method = method; return this; }
  setHeaders(headers: Record<string, string>) { this.headers = headers; return this; }

  build() {
    return new HttpRequest(this.url, this.method, this.headers);
  }
}

const request = new RequestBuilder()
  .setUrl("https://api.exemplo.com")
  .setMethod("POST")
  .setHeaders({ "Content-Type": "application/json" })
  .build();
```

## Quando usar

- Construtores com mais de 4–5 parâmetros
- Objetos criados em etapas com dependências entre elas
- Quando a ordem de configuração importa (ex: query builders, SQL DSLs)

## Trade-offs

| ✅ | ❌ |
|---|---|
| Código legível como linguagem natural | Mais código up front |
| Adicionar opção nova = novo método, sem quebrar código existente | Mais classes/arquivos |
| Parâmetros opcionais ficam explícitos | |

## Exemplos no dia a dia

- Query builders (Knex, Prisma, TypeORM)
- `RequestBuilder` em HTTP clients
- `StringBuilder` em Java

## Key Sources

- [[sources/sete-padroes-de-design-de-software]]
