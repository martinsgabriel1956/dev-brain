---
date: 2026-03-27
tags: [tech-mentor, testes, tdd, design, qualidade]
skill: tech-mentor-testing/references/test-patterns.md
level: intermediário
---
# TDD — Test-Driven Development

## Contexto

TDD é uma prática onde o teste é escrito *antes* do código de produção. O benefício principal não é cobertura — é que você **sente o acoplamento antes de criá-lo**. Código testável por definição tende a ter baixo acoplamento e responsabilidades claras. TDD não garante boa arquitetura, mas garante que o código é testável.

## Como Funciona

O ciclo tem três fases obrigatórias:

```
RED → GREEN → REFACTOR → RED → GREEN → REFACTOR → ...
```

- **RED**: escreva um teste que falha. O comportamento ainda não existe.
- **GREEN**: escreva o *mínimo* de código para o teste passar. Sem over-engineering.
- **REFACTOR**: melhore o código sem quebrar os testes.

Sem o Refactor, TDD vira apenas "testes primeiro" — acumula débito técnico junto com os testes.

## Código de Referência

```typescript
// 1. RED — falha porque Order não existe
it("should calculate order total with discount", () => {
  const order = new Order([
    { price: 100, quantity: 2 },
    { price: 50, quantity: 1 },
  ]);
  expect(order.totalWithDiscount(0.1)).toBe(225); // 250 - 10%
});

// 2. GREEN — implementação mínima
class Order {
  constructor(private items: { price: number; quantity: number }[]) {}

  totalWithDiscount(discount: number): number {
    const subtotal = this.items.reduce((sum, i) => sum + i.price * i.quantity, 0);
    return subtotal * (1 - discount);
  }
}

// 3. REFACTOR — extrai responsabilidade sem quebrar o teste
class Order {
  constructor(private items: { price: number; quantity: number }[]) {}

  private get subtotal(): number {
    return this.items.reduce((sum, i) => sum + i.price * i.quantity, 0);
  }

  totalWithDiscount(discount: number): number {
    return this.subtotal * (1 - discount);
  }
}
```

### Armadilha: testar implementação, não comportamento

```typescript
// ❌ Frágil — quebra se renomear método interno
it("should call calculateSubtotal", () => {
  const spy = jest.spyOn(order, "calculateSubtotal");
  order.totalWithDiscount(0.1);
  expect(spy).toHaveBeenCalled();
});

// ✅ Robusto — testa o resultado observável
it("should return correct total", () => {
  expect(order.totalWithDiscount(0.1)).toBe(225);
});
```

## As Duas Escolas

### Detroit (Inside-Out / Classicist)

Começa pelas unidades internas do domínio. Usa objetos reais, mocka apenas I/O real (DB, HTTP, filesystem).

```typescript
it("expired coupon should throw", () => {
  const coupon = new Coupon({ code: "SAVE10", expiresAt: pastDate });
  const order = new Order({ items: [...] });

  expect(() => order.applyCoupon(coupon)).toThrow(ExpiredCouponError);
});
```

### London (Outside-In / Mockist)

Começa pelo comportamento externo. Mocka todos os colaboradores ainda não existentes — o design emerge das interfaces que o teste exige.

```typescript
it("checkout should charge correct amount with coupon", async () => {
  const mockCoupon = { validate: jest.fn().mockResolvedValue({ discount: 0.1 }) };
  const mockPayment = { charge: jest.fn().mockResolvedValue({ id: "ch_123" }) };

  const useCase = new CheckoutUseCase(mockCoupon, mockPayment);
  await useCase.execute({ orderId: "1", couponCode: "SAVE10" });

  expect(mockPayment.charge).toHaveBeenCalledWith(225);
});
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| **Design** | Acoplamento percebido antes de ser criado | Requer disciplina — fácil de pular o refactor |
| **Cobertura** | Alta cobertura como subproduto natural | Pode dar falsa sensação de segurança sem testes de integração |
| **Velocidade** | Feedback loop curto por ciclo | Mais lento inicialmente para devs não acostumados |
| **Mocks (London)** | Design emerge de fora para dentro | Mocks podem mascarar integração quebrada |
| **Objetos reais (Detroit)** | Integração validada nas unidades | Falhas de integração aparecem mais tarde |

## Quando Usar / Quando Evitar

**Use TDD quando:**
- Lógica de negócio com múltiplos caminhos
- Algoritmos onde o comportamento correto é claro antes da implementação
- Refatorando legado: escreve testes antes de mudar qualquer linha
- Quer que o design emerja guiado pelos testes

**Evite TDD quando:**
- Exploração de APIs externas desconhecidas (spike primeiro, testes depois)
- Protótipos descartáveis
- UI visual onde o "correto" é subjetivo
- IaC (Terraform, K8s manifests)

## Conceitos Relacionados

[[bdd]] · [[piramide-de-testes]] · [[test-doubles]] · [[property-based-testing]]
