---
date: 2026-03-27
tags: [tech-mentor, testes, test-doubles, mock, stub, fake, spy]
skill: tech-mentor-testing/references/test-tooling.md
level: intermediário
---

# Test Doubles

## Contexto

Test Double é o termo genérico para qualquer objeto que substitui uma dependência real nos testes — como um dublê de ator. Os termos são usados de forma intercambiável no dia a dia, mas têm significados distintos. Confundir Mock com Stub leva a testes frágeis acoplados à implementação. Taxonomia de Gerard Meszaros em *xUnit Test Patterns* (2007).

## Como Funciona

```
Dummy  → passa, mas nunca é usado
Stub   → retorna valor fixo, não verifica chamada
Fake   → implementação funcional simplificada
Spy    → observa sem alterar comportamento
Mock   → controla retorno E verifica como foi chamado
```

## Código de Referência

### Dummy — satisfaz assinatura, nunca é usado

```typescript
const dummyLogger = {} as Logger;
const service = new OrderService(repo, dummyLogger);
```

### Stub — retorna resposta pré-determinada

```typescript
const stubRepo = {
  findById: async () => ({ id: "1", name: "João", email: "joao@email.com" }),
};

const useCase = new GetUserUseCase(stubRepo);
const user = await useCase.execute("1");
expect(user.name).toBe("João");
```

Use quando o teste se importa com o **resultado**, não com quem foi chamado.

### Fake — implementação funcional simplificada

```typescript
class InMemoryUserRepository implements IUserRepository {
  private users = new Map<string, User>();

  async findById(id: string) {
    return this.users.get(id) ?? null;
  }

  async save(user: User) {
    this.users.set(user.id, user);
  }

  async findByEmail(email: string) {
    return [...this.users.values()].find(u => u.email === email) ?? null;
  }
}
```

Fake é o melhor tipo para repositórios e serviços com estado — reutilizável, sem acoplamento à implementação.

### Spy — registra chamadas sem alterar comportamento

```typescript
const spy = jest.spyOn(emailService, "send");

await createUser({ name: "João", email: "joao@email.com" });

expect(spy).toHaveBeenCalledOnce();
expect(spy).toHaveBeenCalledWith(
  "joao@email.com",
  expect.stringContaining("bem-vindo")
);
```

Use quando quer verificar que um efeito colateral aconteceu **sem substituir** o comportamento real.

### Mock — controla retorno E verifica interação

```typescript
const mockPayment = {
  charge: jest.fn().mockResolvedValue({ id: "charge_123", status: "succeeded" }),
};

const useCase = new CheckoutUseCase(orderRepo, mockPayment);
await useCase.execute({ orderId: "order-1", amount: 250 });

expect(mockPayment.charge).toHaveBeenCalledWith({
  amount: 250,
  currency: "BRL",
});
```

### MSW — Test Double de Rede

Substitui APIs externas no nível da rede — o código nem sabe que está sendo interceptado.

```typescript
import { setupServer } from "msw/node";
import { http, HttpResponse } from "msw";

const server = setupServer(
  http.get("https://api.payments.com/charge", () => {
    return HttpResponse.json({ id: "ch_123", status: "succeeded" });
  })
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

## Trade-offs

| Tipo | Use quando | Evite quando |
|---|---|---|
| **Dummy** | Dependência exigida mas irrelevante para o teste | Há risco de ser chamado acidentalmente |
| **Stub** | Teste importa com resultado, não com quem foi chamado | Precisa verificar que algo foi chamado |
| **Fake** | Repositório, broker, cache com estado entre chamadas | Objeto simples demais para justificar implementação |
| **Spy** | Verificar efeitos colaterais sem substituir comportamento | Comportamento original causa I/O indesejado |
| **Mock** | Controlar retorno E verificar a interação | Substituir colaboradores de domínio — use Fake |

## Quando Usar / Quando Evitar

**Regra de ouro: prefira Fakes sobre Mocks.**

Mock acopla o teste à implementação interna — renomear o método quebra o teste sem o comportamento ter mudado.

```typescript
// ❌ Mock frágil — quebra se renomear "charge" para "processPayment"
expect(mockPayment.charge).toHaveBeenCalledWith(250);

// ✅ Fake robusto — testa o contrato, não o nome do método
const fakePayment = new InMemoryPaymentGateway();
await useCase.execute({ amount: 250 });
expect(fakePayment.getLastCharge().amount).toBe(250);
```

**Mocks excessivos são code smell**: se um teste precisa mockar 5 dependências, o código tem acoplamento alto demais — refatore antes de continuar.

## Conceitos Relacionados

[[tdd]] · [[piramide-de-testes]] · [[contract-testing]] · [[testcontainers]]

---
*Fonte: tech-mentor skill · tech-mentor-testing · 2026-03-27*
