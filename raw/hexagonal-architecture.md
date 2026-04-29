---
date: 2026-04-13
tags: [tech-mentor, arquitetura, hexagonal, ports-and-adapters]
skill: tech-mentor-system-design/references/architecture-patterns
level: intermediário
---
# Hexagonal Architecture (Ports & Adapters)

## Contexto

Criada por Alistair Cockburn em 2005. O nome vem do hexágono usado nos diagramas — as 6 faces não têm significado literal, representam que o sistema pode ter múltiplos "lados" de entrada e saída. O nome alternativo **Ports & Adapters** é mais preciso.

O objetivo central: **isolar o núcleo da aplicação de tudo que é I/O**. O domínio não sabe se está sendo chamado via HTTP, CLI, fila de mensagens, ou teste unitário.

Relação com Clean Architecture: são complementares. Clean Architecture é uma hierarquia de camadas; Hexagonal é um modelo de interação entre o domínio e o mundo externo. Na prática, muitos projetos usam ambos.
## Como Funciona

### Ports (Interfaces)

**Primary Ports (Driving side)** — como o mundo chama o sistema:
- Definem operações que o domínio expõe
- Implementados pelo domínio, chamados por adapters primários

**Secondary Ports (Driven side)** — como o sistema chama o mundo:
- Definem dependências que o domínio precisa
- Implementados por adapters secundários

```typescript
// Primary Port — o que a aplicação expõe ao mundo
type UserService = {
  registerUser(input: RegisterUserInput): Promise<User>;
  getUserById(id: string): Promise<User>;
};

// Secondary Port — o que a aplicação precisa do mundo
type UserRepository = {
  save(user: User): Promise<void>;
  findById(id: string): Promise<User | null>;
  findByEmail(email: string): Promise<User | null>;
};

type EmailPort = {
  sendWelcomeEmail(to: string, name: string): Promise<void>;
};
```
### Adapters

**Primary Adapters (Driving)** — traduzem o mundo externo para o domínio:

```typescript
// HTTP Adapter — Express controller
class UserHttpAdapter {
  constructor(private userService: UserService) {}

  async register(req: Request, res: Response): Promise<void> {
    const result = await this.userService.registerUser({
      name: req.body.name,
      email: req.body.email,
      password: req.body.password
    });
    res.status(201).json({ data: result });
  }
}

// CLI Adapter — mesmo domínio, interface diferente
class UserCliAdapter {
  constructor(private userService: UserService) {}

  async run(args: string[]): Promise<void> {
    const [name, email, password] = args;
    const user = await this.userService.registerUser({ name, email, password });
    console.log({ message: "User registered", userId: user.id });
  }
}
```

**Secondary Adapters (Driven)** — adaptam o domínio para infraestrutura:

```typescript
// Adapter real para produção
class PrismaUserRepository implements UserRepository {
  async save(user: User): Promise<void> {
    await prisma.user.upsert({
      where: { id: user.id },
      update: { name: user.name, email: user.email },
      create: { id: user.id, name: user.name, email: user.email }
    });
  }

  async findByEmail(email: string): Promise<User | null> {
    const raw = await prisma.user.findUnique({ where: { email } });
    return raw ? UserMapper.toDomain(raw) : null;
  }
}

// In-Memory Adapter para testes — mesmo Port, implementação fake
class InMemoryUserRepository implements UserRepository {
  private store = new Map<string, User>();

  async save(user: User): Promise<void> {
    this.store.set(user.id, user);
  }

  async findByEmail(email: string): Promise<User | null> {
    return [...this.store.values()].find(u => u.email === email) ?? null;
  }
}
```

### A Magia dos In-Memory Adapters para Testes

Com Ports & Adapters, seus testes de domínio ficam completamente isolados de infraestrutura:

```typescript
describe("registerUser", () => {
  let userService: UserService;
  let userRepository: InMemoryUserRepository;
  let emailAdapter: InMemoryEmailAdapter;

  beforeEach(() => {
    userRepository = new InMemoryUserRepository();
    emailAdapter = new InMemoryEmailAdapter();
    userService = new UserServiceImpl(userRepository, emailAdapter);
  });

  it("should register user and send welcome email", async () => {
    const input = { name: "Alice", email: "alice@example.com", password: "Secure123!" };

    const user = await userService.registerUser(input);

    expect(user.email).toBe("alice@example.com");
    expect(emailAdapter.sentEmails).toHaveLength(1);
    expect(emailAdapter.sentEmails[0].to).toBe("alice@example.com");
  });

  it("should throw when email already exists", async () => {
    const input = { name: "Alice", email: "alice@example.com", password: "Secure123!" };
    await userService.registerUser(input);

    await expect(userService.registerUser(input)).rejects.toThrow(EmailAlreadyExistsError);
  });
});
```

Sem banco real, sem HTTP, sem mocks frágeis. **Os testes rodam em milissegundos.**

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Testabilidade | In-memory adapters permitem testes ultra-rápidos | Manter In-Memory sincronizado com o real |
| Flexibilidade | Múltiplas interfaces (HTTP, CLI, Worker) sem tocar o domínio | Mais interfaces e arquivos |
| Isolamento | Infraestrutura não vaza para o domínio | Overhead de mapeamento |
| Substituibilidade | Troca de Prisma por TypeORM sem afetar regras | DI manual pode ser verboso sem container |

## Quando Usar / Quando Evitar

**Usar quando:**
- Domínio precisa ser testável de forma isolada (prioridade máxima)
- Múltiplos tipos de entrada/saída (HTTP + Worker + CLI)
- Expectativa de trocar infraestrutura ao longo do tempo

**Evitar quando:**
- Aplicação é puramente CRUD sem lógica de domínio
- Protótipo rápido ou sistema descartável

## Conceitos Relacionados

[[clean-architecture]] · [[dependency-injection]] · [[ddd-tactical]] · [[solid]] · [[test-doubles]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-13*
