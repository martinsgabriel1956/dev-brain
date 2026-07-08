---
type: concept
title: "Contract Testing"
aliases: ["teste de contrato", "pact", "consumer-driven contracts", "can-i-deploy"]
date_created: 2026-04-22
date_updated: 2026-07-07
source_count: 2
tags: [testes, contract-testing, pact, microservices, ci, distribuídos]
skill: tech-mentor-testing
status: stable
---

# Contract Testing

Valida que dois serviços que se comunicam **concordam com o formato da comunicação** — sem precisar rodá-los juntos ao mesmo tempo. Solução para o problema de integração em sistemas distribuídos.

## Consumer-Driven Contracts — A inversão

Abordagem tradicional: provider define a API, consumer se adapta.
Consumer-Driven: **consumer define o que precisa**, provider verifica que ainda satisfaz.

```
Consumer escreve teste → Pact gera arquivo de contrato
                                  ↓
                       Publica no Pact Broker
                                  ↓
          Provider baixa contratos → Verifica → Publica resultado
                                  ↓
          can-i-deploy consulta o Broker antes do release
```

`can-i-deploy` é o gate: se o provider quebrou algum consumer, o deploy é bloqueado.

## Matchers — não hardcode valores

O consumer define o **mínimo que precisa**, com matchers flexíveis:

```typescript
body: {
  id: string("123"),          // string() = qualquer string
  amount: integer(150),       // integer() = qualquer inteiro
  createdAt: iso8601DateTime(),
  items: eachLike({           // eachLike() = array com ao menos 1 item
    productId: string("prod-1"),
    quantity: integer(2),
  }),
}
```

## Comparativo

| | Contract Testing | Integration E2E | Schema (OpenAPI) |
|---|---|---|---|
| Velocidade | Rápido (unitário) | Lento | Rápido |
| Detecta | Quebra de contrato | Bugs de integração real | Desvio do schema |
| Não detecta | Bugs de lógica | — | Comportamento |
| Escala com | Muitos microservices | Mal | APIs públicas |

## Quando usar / evitar

**Use:** múltiplos microsserviços com dependências, times diferentes owning consumer e provider.
**Evite:** API pública com consumers desconhecidos → OpenAPI + Schemathesis; monólito — não faz sentido.

Contract testing não substitui E2E — são camadas diferentes da [[piramide-de-testes]].

## Papel no teste de integração estreito (Fowler)

[[teste-de-integracao-estreito-vs-amplo|Martin Fowler]] descreve o combo narrow integration test + contract test como substituto do teste de integração amplo: o narrow test roda contra um double do serviço externo, e o contract test garante que esse double é fiel ao provider real. Sem o contract test, o ponto fraco do teste estreito é justamente não saber se o double mentiu.

## Ver também

- [[piramide-de-testes]] — onde contract testing se encaixa
- [[bdd]] — complementar para specs de comportamento
- [[race-condition]] — problema que contract testing não resolve (lógica de negócio)
- [[teste-de-integracao-estreito-vs-amplo]] — onde contract testing entra na estratégia de Fowler

## Key Sources

- [[wiki/sources/contract-testing]]
- [[wiki/sources/integration-test-martin-fowler]]
