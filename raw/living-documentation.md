---
date: 2026-03-27
tags: [tech-mentor, testes, documentação, bdd, openapi, ci]
skill: tech-mentor-testing/references/test-patterns.md
level: intermediário
---

# Living Documentation

## Contexto

Living Documentation é a prática de manter a documentação **gerada automaticamente a partir do código ou dos testes** — garantindo que nunca fique desatualizada. O princípio: se a documentação precisa de manutenção manual separada do código, ela vai divergir. É o oposto de um Confluence cheio de páginas que ninguém atualiza.

A distinção crítica: **living documentation quebra o build se ficar desatualizada** — ou é gerada automaticamente, eliminando a possibilidade de divergir.

## Como Funciona

```
Fluxo tradicional (problemático):
  Dev implementa feature → atualiza doc manualmente (talvez)
  3 meses depois: código mudou, doc não → doc é fonte de desinformação

Living Documentation:
  Dev escreve spec/teste → CI executa e gera doc do resultado
  Doc sempre reflete o estado atual do sistema
```

## Código de Referência

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

Resultado: página navegável com todos os cenários, status e histórico — legível por PO e stakeholders.

### 2 — OpenAPI como documentação de API

Spec gerada a partir de annotations do código — nunca escrita à mão.

```typescript
// NestJS — documentação gerada do código
@ApiOperation({ summary: "Create order" })
@ApiResponse({ status: 201, type: OrderResponseDTO })
@ApiResponse({ status: 400, description: "Invalid items" })
@Post("/orders")
async createOrder(@Body() dto: CreateOrderDTO): Promise<OrderResponseDTO> {
  return this.createOrderUseCase.execute(dto);
}

// Setup do Swagger
const config = new DocumentBuilder().setTitle("Orders API").setVersion("1.0").build();
const document = SwaggerModule.createDocument(app, config);
SwaggerModule.setup("api/docs", app, document);
```

### 3 — Testes como documentação técnica

Um teste bem escrito é a melhor documentação do comportamento esperado.

```typescript
describe("Order.applyDiscount", () => {
  it("should reduce total by the given percentage");
  it("should throw when discount exceeds 50%");
  it("should not apply discount to already-paid orders");
  it("should stack with free shipping when total exceeds threshold");
});
```

Ler os `it()` descreve o comportamento completo sem precisar ler a implementação.

### 4 — Arquitetura como Código (Structurizr)

Diagramas C4 gerados de código — nunca desenhados no Miro.

```javascript
// Workspace.dsl — vive no repositório, diff no PR
workspace {
  model {
    user   = person "Customer"
    system = softwareSystem "E-commerce" {
      web = container "Web App" { technology "Next.js" }
      api = container "API"     { technology "Node.js" }
      db  = container "Database" { technology "PostgreSQL" }
    }
    user -> web "Uses"
    web  -> api "Calls"
    api  -> db  "Reads/Writes"
  }
  views {
    container system "Containers" { include * autoLayout }
  }
}
```

## Trade-offs

| Ferramenta | Contexto | Output |
|---|---|---|
| Cucumber HTML Reporter, Allure | BDD / Gherkin | Portal de specs navegável |
| Swagger/OpenAPI, Redoc | API REST | Documentação interativa |
| GraphQL Playground | API GraphQL | Schema navegável |
| Structurizr DSL | Arquitetura C4 | Diagramas gerados de código |
| Istanbul, c8 | Cobertura | Report linkado ao código |
| semantic-release | Changelog | CHANGELOG.md gerado de commits |

## Quando Usar / Quando Evitar

**O que NÃO é Living Documentation:**
- README escrito à mão e atualizado manualmente
- Wiki no Confluence sem vínculo com o código
- Comentários JSDoc sem garantia de correção
- Diagramas no Miro que "alguém vai atualizar"

**Use quando:**
- Times com múltiplos stakeholders não-técnicos que consomem documentação
- APIs públicas ou consumidas por outros times
- Sistemas regulados que exigem specs auditáveis
- Arquitetura complexa que muda frequentemente

**Evite overhead de setup quando:**
- MVP ou protótipo descartável
- Time pequeno com comunicação direta — doc informal suficiente

## Conceitos Relacionados

[[bdd]] · [[tdd]] · [[contract-testing]] · [[openapi]]
