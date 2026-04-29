---
type: concept
title: "Pirâmide de Testes"
aliases: ["test pyramid", "ice cream cone", "testing trophy", "estratégia de testes"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [testes, pirâmide, estratégia, unitário, integração, e2e]
skill: tech-mentor-testing
status: stable
---

# Pirâmide de Testes

Modelo que define **quantos testes ter em cada nível e por quê**. Quanto mais alto na pirâmide, mais lento, caro e frágil o teste.

```
           /\
          /E2E\          Poucos — happy paths críticos
         /______\
        /        \
       /Integração \     Moderados — contratos e I/O
      /______________\
     /                \
    /    Unitários     \ Muitos — lógica de negócio isolada
   /____________________\
```

## As Três Camadas

| Camada | Velocidade | Flakiness | O que valida |
|---|---|---|---|
| Unitário | ~ms | Quase zero | Lógica isolada |
| Integração | ~segundos | Baixo | Contratos com I/O real |
| E2E | ~10-30s | Alto | Fluxo do usuário |

**Blind spots de cada camada:**
- Unitário sem integração → lógica correta, SQL errado
- Integração sem unitário → edge cases do domínio descobertos tarde
- E2E sem as outras → não sabe *por quê* falhou

## Exemplos

**Unitário:**
```typescript
describe("Order", () => {
  it("should not allow discount above 50%", () => {
    const order = new Order({ items: [{ price: 100, quantity: 1 }] });
    expect(() => order.applyDiscount(0.6)).toThrow("Discount cannot exceed 50%");
  });
});
```

**Integração (banco real):**
```typescript
it("should persist order and return id", async () => {
  const result = await orderRepository.create({
    customerId: "c-123",
    items: [{ productId: "p-1", quantity: 2, price: 50 }]
  });
  const saved = await db("orders").where({ id: result.id }).first();
  expect(saved.status).toBe("pending");
});
```

**E2E (Playwright):**
```typescript
test("user can complete checkout", async ({ page }) => {
  await page.goto("/cart");
  await page.click('[data-testid="checkout-btn"]');
  await page.fill('[name="card-number"]', "4111111111111111");
  await page.click('[data-testid="pay-btn"]');
  await expect(page.locator(".order-confirmation")).toBeVisible();
});
```

## Anti-pattern: Ice Cream Cone

Inverter a pirâmide — maioria de E2E, poucos unitários. Suite lenta, flaky, sem confiança, feedback loop de horas.

## Variante: Testing Trophy (Kent C. Dodds)

Para sistemas com muito I/O e lógica de domínio rasa (Next.js, CRUD APIs), o centro de gravidade sobe para integração:

```
    /E2E\
   /------\
  / Integr \  ← centro de gravidade
 /----------\
/ Unitários  \
/____________\
   Static      ← TypeScript + ESLint + Zod = testes "gratuitos"
```

## E2E no CI

```yaml
- unit         # roda em segundos, bloqueia PR
- integration  # roda em <2min, bloqueia PR
- e2e          # roda em staging, bloqueia DEPLOY — não PR
```

E2E não bloqueia merge de PR — é lento demais. Bloqueia o **deploy para produção**.

## Ver também

- [[tdd]] — prática que preenche a base da pirâmide
- [[contract-testing]] — camada entre integração e E2E em microsserviços
- [[test-doubles]] — como isolar dependências nos unitários
- [[testar-proprio-codigo]] — hábito de cobrir além do happy path

## Key Sources

- [[sources/piramide-de-testes]]
- [[sources/roadmap-dev-senior-2026]] — testes como seguro contra decisões ruins da IA (pilar 5)
