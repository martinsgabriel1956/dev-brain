---
type: concept
title: "Living Documentation"
aliases: ["documentação viva", "docs from tests", "cucumber report", "structurizr"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [testes, documentação, bdd, openapi, ci, living-docs]
skill: tech-mentor-testing
status: stable
---

# Living Documentation

Documentação **gerada automaticamente a partir do código ou testes** — nunca escrita à mão, nunca desatualizada. Princípio central: se precisa de manutenção manual separada do código, vai divergir. É o oposto de um Confluence cheio de páginas que ninguém atualiza.

A distinção crítica: **living documentation quebra o build se ficar desatualizada** — ou é gerada automaticamente, eliminando a possibilidade de divergir.

## As quatro abordagens

### 1 — BDD como documentação (Cucumber)

A própria spec Gherkin é a documentação. O CI publica o relatório após cada execução.

```yaml
- name: Run Cucumber
  run: npx cucumber-js --format json:reports/cucumber.json
- name: Generate HTML Report
  run: npx cucumber-html-reporter --input reports/cucumber.json --output docs/specs/
- name: Deploy to GitHub Pages
  uses: peaceiris/actions-gh-pages@v3
  with:
    publish_dir: ./docs
```

Resultado: portal navegável com todos os cenários, status e histórico — legível por PO e stakeholders.

### 2 — OpenAPI como documentação de API

Spec gerada de annotations do código — nunca escrita à mão.

```typescript
@ApiOperation({ summary: "Create order" })
@ApiResponse({ status: 201, type: OrderResponseDTO })
@Post("/orders")
async createOrder(@Body() dto: CreateOrderDTO): Promise<OrderResponseDTO> {
  return this.createOrderUseCase.execute(dto);
}
```

### 3 — Testes como documentação técnica

Um teste bem escrito é a melhor documentação do comportamento esperado.

```typescript
describe("Order.applyDiscount", () => {
  it("should reduce total by the given percentage");
  it("should throw when discount exceeds 50%");
  it("should not apply discount to already-paid orders");
});
```

Ler os `it()` descreve o comportamento completo sem precisar ler a implementação.

### 4 — Arquitetura como código (Structurizr DSL)

Diagramas C4 gerados de código — nunca desenhados no Miro, com diff rastreável no PR.

## Ferramentas

| Ferramenta | Contexto | Output |
|---|---|---|
| Cucumber HTML Reporter, Allure | BDD / Gherkin | Portal de specs navegável |
| Swagger / Redoc | API REST | Documentação interativa |
| Structurizr DSL | Arquitetura C4 | Diagramas gerados de código |
| Istanbul, c8 | Cobertura | Report linkado ao código |
| semantic-release | Changelog | CHANGELOG.md de commits |

## O que NÃO é Living Documentation

- README escrito à mão e atualizado manualmente
- Wiki no Confluence sem vínculo com o código
- Comentários JSDoc sem garantia de correção
- Diagramas no Miro que "alguém vai atualizar"

## Quando usar / evitar

**Use:** múltiplos stakeholders não-técnicos, APIs públicas ou consumidas por outros times, sistemas regulados, arquitetura complexa que muda frequentemente.
**Evite:** MVP ou protótipo descartável, time pequeno com comunicação direta.

## Ver também

- [[bdd]] — principal gerador de living documentation
- [[tdd]] — testes como documentação técnica
- [[contract-testing]] — documentação de contratos entre serviços
- [[piramide-de-testes]] — contexto estratégico

## Key Sources

- [[wiki/sources/living-documentation]]
