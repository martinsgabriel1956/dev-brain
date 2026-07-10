---
type: concept
title: "Hexagonal Architecture (Ports & Adapters)"
aliases: ["arquitetura hexagonal", "ports and adapters", "ports adapters", "hexagonal"]
date_created: 2026-05-04
date_updated: 2026-07-10
source_count: 3
tags: [arquitetura, hexagonal, ports-adapters, acoplamento, testabilidade]
skill: tech-mentor-backend
status: stable
---

# Hexagonal Architecture (Ports & Adapters)

Padrão arquitetural criado por Alistair Cockburn que isola o **domínio** de todas as dependências externas (banco, HTTP, e-mail, APIs) através de **Ports** (interfaces/contratos) e **Adapters** (implementações concretas).

A regra central: o domínio não conhece infraestrutura. Dependências sempre apontam para dentro.

## Componentes

### Port (Interface)
Define o contrato — o que um módulo pode fazer, sem dizer como.

```typescript
interface UserRepository {
  getAll(): Promise<User[]>;
  getUserById(id: string): Promise<User | null>;
  findByEmail(email: string): Promise<User | null>;
  create(data: CreateUserDTO): Promise<User>;
  delete(id: string): Promise<void>;
}
```

### Adapter (Implementação)
Implementa o contrato. Pode ser trocado sem quebrar o domínio.

Dentro de um adapter de persistência, a conversão campo-a-campo entre a entidade de domínio e o formato exigido pela tecnologia concreta (ex: Prisma) costuma ser isolada num [[wiki/concepts/mapper-pattern]] dedicado — mantém o adapter enxuto e concentra a lógica de conversão num único lugar, reaproveitável em todos os métodos do repositório.

```typescript
class InMemoryUserAdapter implements UserRepository {
  private users: Map<string, User> = new Map();
  // implementação em memória — para testes ou MVP
}

class PostgresUserAdapter implements UserRepository {
  // implementação com banco real — para produção
}

class ClerkUserAdapter implements UserRepository {
  // implementação com API externa — se migrar para Clerk
}
```

### Driving Ports (Primary)
O domínio é chamado de fora: HTTP, CLI, testes. Ex: controllers.

### Driven Ports (Secondary)
O domínio chama para fora: banco, e-mail, APIs externas. Ex: repositórios, gateways.

## Estrutura Típica

```
src/
├── domain/          — entidades, value objects, regras de domínio
├── repositories/    — ports (interfaces)
├── adapters/        — implementações concretas dos ports
├── services/        — casos de uso / regras de negócio
├── router/          — driving adapters (HTTP handlers)
└── index.ts         — composição root (instancia e injeta)
```

## Por Que Importa para IA

Arquitetura por camada (horizontal) obriga o agente a abrir 7–13 arquivos para uma única feature. Arquitetura hexagonal localiza cada feature em 2–3 arquivos com responsabilidade clara.

| Tarefa | Arquitetura horizontal | Hexagonal |
|---|---|---|
| "Altere criação de usuário" | domain + usecase + controller + validator + repository | `user.service.ts` + `user.adapter.ts` |
| "Troque o banco de users" | refatorar tudo | criar novo adapter + trocar uma linha |
| Contexto necessário | Alto | Baixo e localizado |

Ver [[concepts/codebase-legibilidade-ia]] para o princípio geral.

## Relação com Clean Architecture

São o mesmo princípio com terminologia diferente:

| Hexagonal | Clean Architecture |
|---|---|
| Port | Interface da camada Application |
| Adapter | Camada Frameworks/Infra |
| Driving Port | Controller |
| Driven Port | Repository, Gateway |

## In-Memory Adapters — Superpoder de Testabilidade

```typescript
// Teste ultrarrápido — sem banco, sem Docker, sem cleanup
const userRepo = new InMemoryUserAdapter();
const userService = new UserService(userRepo);

it("should throw when email already exists", async () => {
  await userService.create({ email: "a@b.com", name: "A" });
  await expect(userService.create({ email: "a@b.com", name: "B" }))
    .rejects.toThrow(UserAlreadyExistsError);
});
// executa em < 1ms
```

1000 testes com In-Memory Adapters rodam em < 1s. Sem flakiness de rede.

## Quando Vale

- Sistemas com lógica de negócio que vai mudar
- Times que precisam de testabilidade sem infra
- Partes do sistema que podem precisar ser substituídas (ex: migrar banco, trocar serviço externo)

## Quando É Over-engineering

- CRUDs simples sem lógica de negócio
- MVPs com uma pessoa e < 300 linhas

## Key Sources

- [[sources/hexagonal-architecture]] — referência técnica aprofundada (Alistair Cockburn, driving/driven ports)
- [[sources/ports-and-adapters-codebase-para-ia]] — antes/depois com exemplo de blog + ângulo de IA
- [[wiki/sources/mappers-conversao-entre-camadas]] — mapper como peça dentro do adapter de persistência
