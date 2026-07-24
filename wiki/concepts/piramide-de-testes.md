---
type: concept
title: "Pirâmide de Testes"
aliases: ["test pyramid", "ice cream cone", "testing trophy", "estratégia de testes"]
date_created: 2026-04-22
date_updated: 2026-07-24
source_count: 6
tags: [testes, pirâmide, estratégia, unitário, integração, e2e, projetos-novos]
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

## Testes Desde o Dia 1 de um Projeto Novo

Parte do [[wiki/concepts/checklist-primeiro-dia-projeto]]: configurar testes unitário e e2e na pipeline de CI **antes mesmo de existir qualquer funcionalidade real** — no ecossistema JS, um par comum é Vitest (unitário) + Cypress (e2e). Ter isso rodando desde cedo bloqueando merge garante que a base da pirâmide já existe quando a primeira feature real chega, em vez de virar dívida técnica para "depois".

## A camada de "Integração" tem duas variantes

[[teste-de-integracao-estreito-vs-amplo|Martin Fowler]] separa a camada de integração em duas práticas que a pirâmide costuma tratar como uma só:
- **estreita** — testa só a fatia de código que fala com um serviço externo, contra um double; roda quase na velocidade de um unitário e pode ficar no mesmo estágio deles no CI;
- **ampla** — ativa serviços reais; mais próxima do E2E em custo e fragilidade.

Isso explica por que times diferentes descrevem a "camada do meio" da pirâmide com expectativas de velocidade tão distintas.

## Não é bem uma pirâmide — é alocação de recursos

Uma leitura mais opinativa da pirâmide: a proporção "certa" entre camadas não é uma regra fixa, é um problema de **alocação de recursos**. Recursos de dev-time e infraestrutura não são infinitos; cada teste E2E a mais é uma semana que não foi gasta em outra coisa. As perguntas que decidem quanto investir em cada camada: qual custo você quer prevenir, qual erro não pode acontecer, quanto tempo seria poupado garantindo que um bug não volta após merge.

Dois contextos que empurram o balanço para fora da pirâmide "padrão":
- **Código legado sem dono conhecido:** aqui o valor de E2E é desproporcionalmente alto — um teste que cobre "usuário clicou, fez X, resultou em Y" dá liberdade para refatorar um monolito espaguete com confiança, mesmo sem entender o código por dentro.
- **Startup em pivot constante, mudando UI/fluxo com frequência:** aqui o valor de E2E cai — a UI muda rápido demais para os testes serem duráveis, e o custo não se justifica sem uma base de clientes que dependa da estabilidade.

Nessa leitura, o teste de maior valor por unidade de custo tende a ser um teste de integração que exercita uma regra de negócio de ponta a ponta — ex.: `POST /users` seguido de `GET /users/:id` confirmando que o dado persistiu — sem precisar da fragilidade e do custo de um E2E completo. Ver [[criterios-de-bom-teste]] para os critérios usados para julgar se um teste especifico vale o investimento.

## Base da pirâmide como pré-requisito de refatoração segura

[[wiki/concepts/refatoracao]] recorre explicitamente à base da pirâmide (unitário + integração estreita) como a rede de segurança para refatorar sem quebrar comportamento — E2E é citado como custoso e lento demais para o ciclo curto de refatorar em passos pequenos. Se a funcionalidade a ser refatorada não tem testes, a recomendação é escrevê-los primeiro, só para aquele escopo, antes de mexer na estrutura.

## Ver também

- [[tdd]] — prática que preenche a base da pirâmide
- [[contract-testing]] — camada entre integração e E2E em microsserviços
- [[test-doubles]] — como isolar dependências nos unitários
- [[testar-proprio-codigo]] — hábito de cobrir além do happy path
- [[teste-de-integracao-estreito-vs-amplo]] — a camada "Integração" desta pirâmide se divide em estreita e ampla
- [[criterios-de-bom-teste]] — determinístico, conciso, relevante, compreensível, durável

## E2E como Critério de Aceite em Loops Agênticos Longos

[[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]] relata um caso onde remover testes E2E (Playwright) da suíte — em favor de só integração/unidade, por questão de velocidade — fez erros se acumularem sem detecção ao longo de um [[wiki/concepts/loop-engineering|loop criador]] rodando autonomamente (jogo com muitas variáveis de estado). A correção não foi voltar à base ampla de sempre: manter os testes E2E como critério de entrega de cada fase do loop, mas sem persisti-los/acumulá-los — cada fase precisa rodar o Playwright ao vivo e provar a jornada ponta a ponta antes de ser considerada concluída. Caso concreto de tensão entre velocidade de feedback (favorece a base da pirâmide) e detecção de regressão em sistemas com muitas variáveis (favorece o topo).

## Key Sources

- [[sources/piramide-de-testes]]
- [[sources/roadmap-dev-senior-2026]] — testes como seguro contra decisões ruins da IA (pilar 5)
- [[wiki/sources/o-que-e-refatoracao-quando-usar]] — base da pirâmide como pré-requisito de segurança para refatorar
- [[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]] — E2E como critério de aceite (sem acumular testes) para não perpetuar erros em loop agêntico longo
- [[wiki/sources/5-ou-6-dicas-para-projetos-novos]]
- [[wiki/sources/integration-test-martin-fowler]]
- [[wiki/sources/teste-unitario-integracao-e2e-opiniao]] — releitura da pirâmide como problema de alocação de recursos; valor assimétrico de E2E entre legado e startup em pivot
