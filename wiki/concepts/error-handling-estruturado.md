---
type: concept
title: "Error Handling Estruturado"
aliases: ["tratamento de erros", "error handler global", "classes de erro"]
date_created: 2026-04-25
date_updated: 2026-04-25
source_count: 1
tags: [error-handling, backend, http, portfolio, clean-code]
skill: tech-mentor-leadership
status: stable
---

# Error Handling Estruturado

Tratar erros de forma estruturada significa: erros específicos com HTTP codes corretos + handler global para erros inesperados.

## O padrão

### 1. Classes de erro para casos de negócio

```typescript
export class EmailAlreadyExistsError extends Error {
  constructor() {
    super("E-mail já cadastrado");
    this.name = "EmailAlreadyExistsError";
  }
}

export class UserNotFoundError extends Error {
  constructor(userId: string) {
    super("Usuário não encontrado");
    this.name = "UserNotFoundError";
  }
}
```

### 2. Tratativa na rota com HTTP code correto

```typescript
try {
  await createUser(data);
} catch (error) {
  if (error instanceof EmailAlreadyExistsError) {
    return reply.status(409).send({ error: error.message });
  }
  if (error instanceof UserNotFoundError) {
    return reply.status(404).send({ error: error.message });
  }
  throw error; // repassa para o handler global
}
```

### 3. Error handler global no servidor

```typescript
app.setErrorHandler((error, request, reply) => {
  // erro de validação (Zod, etc.)
  if (error.validation) {
    return reply.status(400).send({ error: "Dados inválidos", details: error.validation });
  }

  // erro inesperado
  if (process.env.NODE_ENV !== "production") {
    console.log({ error, stack: error.stack });
  } else {
    // envia para sistema de observabilidade (Sentry, Jaeger, etc.)
    observability.captureException(error);
  }

  return reply.status(500).send({ error: "Erro interno do servidor" });
});
```

## Por que importa

Retornar 500 para tudo (ou não tratar erros) é um sinal de descuido. HTTP codes corretos + mensagens de erro semânticas demonstram domínio do protocolo HTTP e cuidado com a experiência de quem consome a API.

## Relações

- [[portfolio-backend-junior]]
- [[observabilidade]] — handler global alimenta o sistema de observabilidade
- [[efeito-colateral]] — erros não tratados são efeitos colaterais silenciosos

## Key sources

- [[wiki/sources/diferenciais-portfolio-backend-junior]]
