---
date: 2026-03-27
tags: [tech-mentor, testes, bdd, gherkin, cucumber, living-docs]
skill: tech-mentor-testing/references/test-patterns.md
level: intermediário
---
# BDD — Behavior-Driven Development

## Contexto

BDD é uma extensão do TDD que usa **linguagem de domínio** (Gherkin) para descrever comportamentos do sistema como especificações executáveis — que são simultaneamente documentação e testes. O ponto central: elimina o gap entre o que o negócio especifica e o que o time implementa. PO, QA e Dev trabalham na mesma fonte de verdade.

## Como Funciona

```
PO/QA escreve cenário em Gherkin
         ↓
Dev mapeia os steps para código (step definitions)
         ↓
Testes executam os cenários
         ↓
Relatório vira living documentation — sempre sincronizada com o código
```

### Gherkin — A Linguagem

- **Given**: estado inicial (pré-condição)
- **When**: ação executada
- **Then**: resultado esperado

```gherkin
# features/checkout.feature
Feature: Checkout com cupom de desconto
  Como cliente registrado
  Quero aplicar um cupom de desconto no checkout
  Para pagar menos pelo meu pedido

  Background:
    Given que estou autenticado como "joao@email.com"
    And tenho itens no carrinho no valor de R$ 250,00

  Scenario: Cupom válido aplica desconto
    When aplico o cupom "SAVE10"
    Then o total deve ser R$ 225,00
    And vejo a mensagem "Cupom aplicado com sucesso"

  Scenario: Cupom expirado é rejeitado
    Given o cupom "EXPIRED20" está vencido
    When tento aplicar o cupom "EXPIRED20"
    Then vejo o erro "Cupom expirado"
    And o total permanece R$ 250,00

  Scenario Outline: Descontos variados
    When aplico o cupom "<cupom>"
    Then o total deve ser "<total>"

    Examples:
      | cupom   | total     |
      | SAVE5   | R$ 237,50 |
      | SAVE10  | R$ 225,00 |
      | SAVE20  | R$ 200,00 |
```

`Background` executa antes de cada cenário — equivalente ao `beforeEach`.
`Scenario Outline` + `Examples` gera um teste por linha da tabela.

## Código de Referência

### Step Definitions (TypeScript + Cucumber)

```typescript
// steps/checkout.steps.ts
import { Given, When, Then } from "@cucumber/cucumber";

Given("tenho itens no carrinho no valor de {string}", async function(value: string) {
  this.cart = await CartFactory.create({ total: parseAmount(value) });
});

When("aplico o cupom {string}", async function(couponCode: string) {
  this.result = await this.checkoutService.applyCoupon(this.cart.id, couponCode);
});

Then("o total deve ser {string}", async function(expectedTotal: string) {
  expect(this.result.total).toBe(parseAmount(expectedTotal));
});

Then("vejo a mensagem {string}", async function(message: string) {
  expect(this.result.message).toContain(message);
});
```

### Living Documentation no CI

```yaml
- name: Run Cucumber Tests
  run: npx cucumber-js --format json:reports/cucumber.json

- name: Generate Living Docs
  run: npx living-documentation --input reports/cucumber.json --output docs/specs/

- name: Deploy to GitHub Pages
  uses: peaceiris/actions-gh-pages@v3
  with:
    github_token: ${{ secrets.GITHUB_TOKEN }}
    publish_dir: ./docs
```

## Trade-offs

| | TDD | BDD |
|---|---|---|
| **Linguagem** | Código | Gherkin (linguagem natural) |
| **Autor do teste** | Dev | PO/QA/Dev |
| **Granularidade** | Unitário/integração | Comportamento de negócio |
| **Documentação** | Não | Sim — living docs |
| **Overhead** | Baixo | Médio-alto |

BDD não substitui TDD — são complementares. TDD para o design interno, BDD para os contratos de comportamento visíveis ao negócio.

## Quando Usar / Quando Evitar

**Use BDD quando:**
- Domínio complexo com regras frequentemente mal-entendidas entre negócio e tech
- Time com QA dedicado que escreve specs
- Múltiplos stakeholders não-técnicos que precisam validar comportamentos
- Produto regulado (fintech, healthtech) onde specs auditáveis têm valor

**Evite quando:**
- Times pequenos (2-3 devs) — overhead de Gherkin não compensa
- Sistemas técnicos sem regras de negócio visíveis (infra, tooling)
- PO não está disposto a escrever ou revisar os cenários

**Armadilha**: BDD sem engajamento do negócio vira apenas testes com sintaxe mais verbosa. Se só o dev escreve os `.feature` files, você tem complexidade extra sem o benefício de alinhamento.

## Conceitos Relacionados

[[tdd]] · [[piramide-de-testes]] · [[contract-testing]] · [[living-documentation]]
