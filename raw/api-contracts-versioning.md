---
date: 2026-04-17
tags: [tech-mentor, apis, contratos, versionamento, openapi]
skill: tech-mentor-backend/references/apis
level: intermediário
---

# API Contracts e Versioning

## Contexto
API contracts definem o acordo formal entre producer e consumer — o que cada endpoint aceita, retorna e garante. Sem contratos explícitos e validados, mudanças em APIs quebram consumers silenciosamente.

**API-First** é a prática de definir o contrato (OpenAPI) antes de implementar, permitindo que consumers mockem a API imediatamente.

## Ferramentas de Contratos

### TypeSpec — definição de API agnóstica de formato

Microsoft TypeSpec gera OpenAPI, Protobuf, JSON Schema a partir de uma definição única.

```typescript
// orders.tsp
import "@typespec/http";
import "@typespec/rest";
import "@typespec/openapi3";

using TypeSpec.Http;
using TypeSpec.Rest;

@service({ title: "Orders API", version: "2.0" })
namespace OrdersAPI {
  model Order {
    id: string;
    customerId: string;
    totalAmount: float64;
    status: "pending" | "confirmed" | "shipped" | "delivered";
    createdAt: utcDateTime;
  }

  model CreateOrderRequest {
    customerId: string;
    items: Array<{ productId: string; quantity: int32 }>;
  }

  @route("/orders")
  interface Orders {
    @get list(@query customerId?: string): Order[];
    @post create(@body body: CreateOrderRequest): Order;
    @get @route("{id}") get(@path id: string): Order | NotFoundResponse;
  }
}
```

### Spectral — linting do OpenAPI

```yaml
# .spectral.yml
extends: ["spectral:oas"]
rules:
  operation-operationId: error
  operation-tags: error
  info-contact: warn
  # Regra customizada: todos os endpoints precisam de security scheme
  security-defined:
    given: "$.paths[*][*]"
    severity: error
    then:
      field: security
      function: defined
```

```bash
spectral lint openapi.yaml
```

### Prism — mock server a partir do OpenAPI

```bash
# Sobe servidor mock com as respostas do OpenAPI
prism mock openapi.yaml

# Consumers já podem integrar antes do backend estar pronto
curl http://localhost:4010/orders -H "Prefer: example=success"
```

## API Versioning — Estratégias

| Estratégia | Exemplo | Prós | Contras |
|---|---|---|---|
| URL path | `/v1/orders` | Explícito, fácil de rotear | URL feia, versão vira lixo |
| Header | `API-Version: 2024-11-01` | URL limpa | Invisível em links |
| Query param | `?version=2` | Simples de testar | Cacheable por URL fica complicado |
| Content-Type | `application/vnd.orders.v2+json` | REST purista | Difícil de consumir |

**Recomendação prática:** URL path para breaking changes maiores (`/v1` → `/v2`). Para mudanças menores, use Expand-Contract dentro da mesma versão.

## Sunset Policy (RFC 8594)

Ao deprecar uma versão, anuncie com antecedência via headers HTTP:

```typescript
// Middleware que adiciona headers de sunset para endpoints V1
function sunsetMiddleware(req: Request, res: Response, next: NextFunction) {
  if (req.path.startsWith("/v1/")) {
    // Data de encerramento da V1
    res.setHeader("Sunset", "Sat, 01 Jan 2027 00:00:00 GMT");
    res.setHeader("Deprecation", "Mon, 01 Jul 2026 00:00:00 GMT");
    res.setHeader("Link", '</v2/orders>; rel="successor-version"');
  }
  next();
}
```

Consumers que monitoram esses headers podem alertar suas equipes automaticamente.

## Breaking vs. Non-Breaking Changes

**Non-breaking (seguro sem nova versão):**
- Adicionar campo opcional na resposta
- Adicionar endpoint novo
- Tornar campo obrigatório opcional
- Adicionar novo valor de enum (com Tolerant Reader no consumer)

**Breaking (requer nova versão ou Expand-Contract):**
- Remover campo da resposta
- Renomear campo
- Mudar tipo de campo
- Remover endpoint
- Mudar semântica de status codes

## Microcks — Contract Testing em CI

```yaml
# Testa se a implementação satisfaz o contrato OpenAPI
services:
  microcks:
    image: quay.io/microcks/microcks-uber:latest
    ports:
      - "8080:8080"
    volumes:
      - ./openapi.yaml:/deployments/openapi.yaml

# No CI: valida que a implementação retorna os exemplos corretos
microcks-cli test 'Orders API:2.0' \
  --microcksURL=http://localhost:8080/api \
  --testEndpoint=http://api:3000 \
  --runner=OPEN_API_SCHEMA
```

## Conceitos Relacionados
[[rest-openapi]] · [[graphql]] · [[grpc]] · [[contract-testing]] · [[expand-contract]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-17*
