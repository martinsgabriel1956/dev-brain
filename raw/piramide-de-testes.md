---
date: 2026-03-27
tags: [tech-mentor, testes, pirâmide, estratégia, ci]
skill: tech-mentor-testing/references/test-strategy.md
level: fundamento
---
# Pirâmide de Testes

## Contexto

A pirâmide é um modelo de distribuição de testes que define **quantos** testes ter em cada nível e **por quê**. A lógica central: quanto mais alto na pirâmide, mais lento, mais caro e mais frágil é o teste. Inverter a pirâmide é um anti-pattern chamado **ice cream cone** — suite lenta, flaky e sem confiança.

## Como Funciona

```
           /\
          /  \
         / E2E\          Poucos — happy paths críticos
        /______\
       /        \
      /Integração \      Moderados — contratos e I/O
     /______________\
    /                \
   /    Unitários     \  Muitos — lógica de negócio isolada
  /____________________\
```

### Unitários — base

Testam lógica de negócio pura, sem I/O. Rápidos (ms), baratos, fáceis. Devem ser a maioria.

```typescript
describe("Order", () => {
  it("should not allow discount above 50%", () => {
    const order = new Order({ items: [{ price: 100, quantity: 1 }] });
    expect(() => order.applyDiscount(0.6)).toThrow("Discount cannot exceed 50%");
  });

  it("should calculate total correctly", () => {
    const order = new Order([
      { price: 100, quantity: 2 },
      { price: 50, quantity: 1 },
    ]);
    expect(order.total).toBe(250);
  });
});
```

### Integração — meio

Testam integração com banco real, filas, APIs internas. Mocks de banco são frágeis e enganosos — use banco real via Testcontainers.

```typescript
it("should persist order and return id", async () => {
  const result = await orderRepository.create({
    customerId: "c-123",
    items: [{ productId: "p-1", quantity: 2, price: 50 }],
  });

  const saved = await db("orders").where({ id: result.id }).first();
  expect(saved).toBeDefined();
  expect(saved.status).toBe("pending");
});
```

### E2E — topo

Testam o fluxo completo — da request HTTP até o banco. Lentos (segundos), caros, frágeis. Apenas happy paths críticos.

```typescript
// Playwright — fluxo de checkout completo
test("user can complete checkout", async ({ page }) => {
  await page.goto("/cart");
  await page.click('[data-testid="checkout-btn"]');
  await page.fill('[name="card-number"]', "4111111111111111");
  await page.click('[data-testid="pay-btn"]');
  await expect(page.locator(".order-confirmation")).toBeVisible();
});
```

## Trade-offs

| Característica | Unitário | Integração | E2E |
|---|---|---|---|
| **Velocidade** | ~ms | ~segundos | ~10-30s |
| **Flakiness** | Quase zero | Baixo | Alto |
| **Feedback loop** | Imediato | Rápido | Lento |
| **Custo de manutenção** | Baixo | Médio | Alto |
| **O que valida** | Lógica isolada | Contratos com I/O | Fluxo do usuário |

## Desvios Válidos

**Testing Trophy** (Kent C. Dodds) — para sistemas com muito I/O e lógica de negócio rasa (Next.js, CRUD APIs), o centro de gravidade sobe: mais integração, menos unitário.

```
    /\
   /E2E\
  /-----\
 / Integ \   ← centro de gravidade
/----------\
/ Unitários \
/____________\
    Static      ← TypeScript, ESLint, Zod = testes "gratuitos"
```

**Por domínio**: sistemas financeiros com pricing complexo → base pesada de unitários. CRUD admin panel → mais integração.

## Quando Usar / Quando Evitar

**Cada camada não substitui a outra — blind spots específicos:**
- Unitário sem integração → lógica correta, mas query SQL errada
- Integração sem unitário → edge cases do domínio descobertos
- E2E sem integração/unitário → fluxo passa, mas não sabe *por quê* falhou

**E2E no CI:**
```yaml
stages:
  - unit         # roda em segundos, bloqueia PR imediatamente
  - integration  # roda em < 2 min, bloqueia PR
  - e2e          # roda em staging, bloqueia release — não PR
```

E2E não bloqueia merge de PR — é lento demais. Bloqueia o **deploy para produção**.

## Conceitos Relacionados

[[tdd]] · [[test-doubles]] · [[testcontainers]] · [[flaky-tests]] · [[contract-testing]]
