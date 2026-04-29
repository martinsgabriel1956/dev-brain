---
date: 2026-03-27
tags: [tech-mentor, testes, contract-testing, pact, microservices, ci]
skill: tech-mentor-testing/references/api-testing-advanced.md
level: avançado
---
# Contract Testing

## Contexto

Contract Testing valida que dois serviços que se comunicam concordam com o **formato da comunicação** — sem precisar testá-los juntos ao mesmo tempo. É a solução para o problema de integração em sistemas distribuídos: com 20 serviços, testar integrações ponto-a-ponto é lento, frágil e não escala.

## Como Funciona

### Consumer-Driven Contracts — A Inversão

A abordagem tradicional é o **provider** definir a API e o consumer se adaptar. Consumer-Driven Contracts inverte: o **consumer** define o que precisa, o **provider** verifica que ainda satisfaz.

```
Consumer escreve teste → Pact gera arquivo de contrato
                                    ↓
                         Publica no Pact Broker
                                    ↓
              Provider baixa contratos → Verifica → Publica resultado
                                    ↓
              can-i-deploy consulta o Broker antes do release
```

`can-i-deploy` é o gate que impede o provider de fazer deploy se quebrar algum consumer.

## Código de Referência

### Consumer — Define o Contrato

Usa matchers flexíveis — não valores hardcoded. O consumer define o **mínimo que precisa**.

```typescript
// mobile-app/src/__tests__/pact-consumer.test.ts
import { PactV3, MatchersV3 } from "@pact-foundation/pact";

const { like, eachLike, integer, string, iso8601DateTime } = MatchersV3;

const pact = new PactV3({
  consumer: "MobileApp",
  provider: "PaymentAPI",
  dir: "./pacts", // arquivo de contrato gerado aqui
});

it("should fetch order by id", async () => {
  await pact
    .given("pedido 123 existe")             // estado que o provider deve preparar
    .uponReceiving("GET /orders/123")
    .withRequest({
      method: "GET",
      path: "/orders/123",
      headers: { Authorization: like("Bearer token") }, // like = qualquer string
    })
    .willRespondWith({
      status: 200,
      body: {
        id: string("123"),
        amount: integer(150),               // integer = qualquer número inteiro
        status: string("PENDING"),
        createdAt: iso8601DateTime(),
        items: eachLike({                   // eachLike = array com ao menos 1 item
          productId: string("prod-1"),
          quantity: integer(2),
        }),
      },
    })
    .executeTest(async mockServer => {
      const service = new OrderService(mockServer.url);
      const order = await service.getOrder("123");

      expect(order.id).toBe("123");
      expect(order.status).toBe("PENDING");
    });
});
```

### Provider — Verifica o Contrato

```typescript
// payment-api/src/__tests__/pact-provider.test.ts
import { Verifier } from "@pact-foundation/pact";

it("verifies published contracts", async () => {
  await new Verifier({
    provider: "PaymentAPI",
    providerBaseUrl: "http://localhost:3001",

    pactBrokerUrl: "https://pact-broker.empresa.com",
    pactBrokerToken: process.env.PACT_BROKER_TOKEN!,

    publishVerificationResult: true,
    providerVersion: process.env.GIT_SHA!,

    // Prepara o estado que cada cenário do consumer exige
    stateHandlers: {
      "pedido 123 existe": async () => {
        await db.orders.insert({ id: "123", amount: 150, status: "PENDING" });
      },
      "pedido 123 não existe": async () => {
        await db.orders.delete({ id: "123" });
      },
    },
  }).verifyProvider();
});
```

### can-i-deploy — Gate de Release

```bash
# No pipeline do provider — antes de fazer deploy
npx pact-broker can-i-deploy \
  --pacticipant PaymentAPI \
  --version $GIT_SHA \
  --to-environment production \
  --broker-base-url https://pact-broker.empresa.com

# Exit 0 = seguro para deploy | Exit 1 = algum consumer seria quebrado
```

### Pipeline Completo

```yaml
jobs:
  contract-tests:
    steps:
      - name: Consumer Pact Tests
        run: npm run test:pact:consumer

      - name: Publish Pacts to Broker
        run: npx pact-broker publish ./pacts --broker-base-url=${{ secrets.PACT_BROKER_URL }}

  can-i-deploy:
    needs: [contract-tests]
    steps:
      - name: Check if safe to deploy
        run: |
          npx pact-broker can-i-deploy \
            --pacticipant PaymentAPI \
            --version ${{ github.sha }} \
            --to-environment staging
```

## Trade-offs

| | Contract Testing (Pact) | Integration E2E | Schema Validation (OpenAPI) |
|---|---|---|---|
| **Velocidade** | Rápido (unitário) | Lento | Rápido |
| **Ambiente** | Sem dependências externas | Ambiente completo | Sem dependências |
| **O que valida** | Contrato consumer↔provider | Fluxo completo | Formato da resposta |
| **Detecta** | Quebra de contrato | Bugs de integração real | Desvio do schema |
| **Não detecta** | Bugs de lógica de negócio | — | Comportamento |
| **Escala com** | Muitos microservices | Mal | APIs públicas |

## Quando Usar / Quando Evitar

**Use contract testing quando:**
- Múltiplos microservices com dependências entre si
- Times diferentes owning consumer e provider — precisam de autonomia de deploy
- Precisa garantir que mudanças no provider não quebram consumers silenciosamente

**Evite / use alternativa quando:**
- API pública com consumers desconhecidos → OpenAPI + Schemathesis
- Mensageria com múltiplos consumers sem contrato explícito → schema registry (Confluent/AWS Glue)
- Monólito — não faz sentido sem serviços separados

Contract testing não substitui E2E de fluxo de usuário — são camadas diferentes da pirâmide. Use os dois.

## Conceitos Relacionados

[[piramide-de-testes]] · [[bdd]] · [[living-documentation]] · [[microservices]]
