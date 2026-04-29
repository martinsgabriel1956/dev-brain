---
date: 2026-04-16
tags: [tech-mentor, backend, apis, rest, openapi, api-first, versionamento]
skill: tech-mentor-backend/references/apis
level: intermediário
---

# REST e OpenAPI 3.1 — Design, Contratos e API-First

## Contexto

REST não é um protocolo — é um estilo arquitetural. A maioria dos "RESTful APIs" viola algum constraint do Roy Fielding, o que é ok na prática. O que importa é consistência interna, contrato explícito (OpenAPI) e uma estratégia de versionamento que não quebre consumers.

API-First inverte o fluxo: o contrato (OpenAPI spec) é escrito e revisado *antes* do código. Isso permite mock servers (Prism, Microcks) para consumers desenvolverem em paralelo.

---

## Design de Endpoints

### Nomenclatura de Recursos

```
# Substantivos no plural — recursos, não ações
GET    /users              → listar usuários
GET    /users/:id          → buscar usuário por ID
POST   /users              → criar usuário
PATCH  /users/:id          → atualizar parcialmente
DELETE /users/:id          → deletar

# Ações que não se encaixam em CRUD → sub-recurso ou verbo na URL
POST   /users/:id/activate    → ativar conta (ação)
POST   /orders/:id/cancel     → cancelar pedido
POST   /invoices/:id/send     → enviar fatura

# Relacionamentos aninhados — máximo 2 níveis
GET    /users/:id/orders      → pedidos de um usuário
GET    /users/:id/orders/:orderId → pedido específico de um usuário

# Evitar aninhamento profundo — cria coupling desnecessário
# RUIM: /users/:id/orders/:orderId/items/:itemId/reviews
# BOM:  /reviews?orderId=X&itemId=Y
```

### Status Codes Semânticos

```
200 OK         → leitura ou update com body de retorno
201 Created    → POST bem-sucedido que criou recurso (+ Location header)
204 No Content → DELETE ou PUT sem body de retorno
206 Partial    → streaming / range requests

400 Bad Request    → erro de validação (campo inválido, formato errado)
401 Unauthorized   → não autenticado (sem token ou token inválido)
403 Forbidden      → autenticado mas sem permissão
404 Not Found      → recurso não existe
409 Conflict       → conflito de estado (ex: email já cadastrado)
410 Gone           → recurso foi deletado permanentemente
422 Unprocessable  → payload válido sintaticamente mas inválido na lógica
429 Too Many Reqs  → rate limit atingido (+ Retry-After header)

500 Internal Error → erro inesperado (não vazar detalhes)
502 Bad Gateway    → upstream indisponível
503 Unavailable    → sobrecarga ou manutenção (+ Retry-After)
```

### Response Envelope Consistente

```typescript
// Sucesso — dados diretos ou com wrapper
type ApiSuccess<T> = {
  data: T;
  meta?: {
    page: number;
    limit: number;
    total: number;
  };
};

// Erro — estrutura previsível para o consumer
type ApiError = {
  error: {
    code: string;        // machine-readable: "USER_NOT_FOUND"
    message: string;     // human-readable em PT-BR
    details?: Record<string, string[]>;  // validações campo a campo
  };
};

// Exemplos de resposta
// POST /users → 201
{ "data": { "id": "uuid", "name": "Alice", "email": "alice@example.com" } }

// GET /users?page=1&limit=20 → 200
{
  "data": [...],
  "meta": { "page": 1, "limit": 20, "total": 150 }
}

// POST /users com email duplicado → 409
{
  "error": {
    "code": "EMAIL_ALREADY_EXISTS",
    "message": "Já existe um usuário com este e-mail"
  }
}

// POST /users com campos inválidos → 400
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dados inválidos",
    "details": {
      "email": ["Formato de e-mail inválido"],
      "name": ["Nome deve ter pelo menos 2 caracteres"]
    }
  }
}
```

---

## OpenAPI 3.1 — Spec como Contrato

### Estrutura de um Spec Completo

```yaml
# openapi.yaml
openapi: "3.1.0"

info:
  title: Orders API
  version: "1.0.0"
  description: |
    API de gerenciamento de pedidos.
    Autenticação via Bearer token (JWT).

servers:
  - url: https://api.empresa.com/v1
    description: Produção
  - url: https://api-staging.empresa.com/v1
    description: Staging

security:
  - bearerAuth: []  # default para todos os endpoints

paths:
  /orders:
    get:
      summary: Listar pedidos
      operationId: listOrders
      tags: [orders]
      parameters:
        - name: status
          in: query
          schema:
            type: string
            enum: [pending, processing, completed, cancelled]
        - name: page
          in: query
          schema:
            type: integer
            default: 1
            minimum: 1
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
            maximum: 100
      responses:
        "200":
          description: Lista de pedidos
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/OrderListResponse"
        "401":
          $ref: "#/components/responses/Unauthorized"
        "429":
          $ref: "#/components/responses/TooManyRequests"

    post:
      summary: Criar pedido
      operationId: createOrder
      tags: [orders]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/CreateOrderRequest"
      responses:
        "201":
          description: Pedido criado
          headers:
            Location:
              description: URL do pedido criado
              schema:
                type: string
                format: uri
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Order"
        "400":
          $ref: "#/components/responses/ValidationError"
        "409":
          $ref: "#/components/responses/Conflict"

  /orders/{orderId}:
    parameters:
      - name: orderId
        in: path
        required: true
        schema:
          type: string
          format: uuid
    get:
      summary: Buscar pedido por ID
      operationId: getOrder
      tags: [orders]
      responses:
        "200":
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Order"
        "404":
          $ref: "#/components/responses/NotFound"

components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

  schemas:
    Order:
      type: object
      required: [id, status, total, createdAt]
      properties:
        id:
          type: string
          format: uuid
          readOnly: true
        status:
          type: string
          enum: [pending, processing, completed, cancelled]
        total:
          type: number
          format: double
          minimum: 0
        currency:
          type: string
          default: BRL
          minLength: 3
          maxLength: 3
        createdAt:
          type: string
          format: date-time
          readOnly: true

    CreateOrderRequest:
      type: object
      required: [items]
      properties:
        items:
          type: array
          minItems: 1
          items:
            $ref: "#/components/schemas/OrderItem"

    OrderItem:
      type: object
      required: [productId, quantity]
      properties:
        productId:
          type: string
          format: uuid
        quantity:
          type: integer
          minimum: 1

    OrderListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: "#/components/schemas/Order"
        meta:
          $ref: "#/components/schemas/PaginationMeta"

    PaginationMeta:
      type: object
      properties:
        page:
          type: integer
        limit:
          type: integer
        total:
          type: integer

  responses:
    NotFound:
      description: Recurso não encontrado
      content:
        application/json:
          schema:
            type: object
            properties:
              error:
                type: object
                properties:
                  code: { type: string, example: "NOT_FOUND" }
                  message: { type: string }

    Unauthorized:
      description: Não autenticado
      content:
        application/json:
          schema:
            type: object

    ValidationError:
      description: Erro de validação
      content:
        application/json:
          schema:
            type: object

    Conflict:
      description: Conflito de estado
      content:
        application/json:
          schema:
            type: object

    TooManyRequests:
      description: Rate limit atingido
      headers:
        Retry-After:
          schema:
            type: integer
            description: Segundos até poder tentar novamente
      content:
        application/json:
          schema:
            type: object
```

---

## Versionamento de API

### Estratégias

```
1. URL Path (mais comum)     → /v1/users, /v2/users
2. Header                    → Accept: application/vnd.api+json;version=2
3. Query param               → /users?version=2
4. Subdomínio                → v2.api.empresa.com
```

**URL Path é o padrão de fato** — visível, cacheável, simples para o consumer.

```typescript
// Express — versionamento por prefixo
import { Router } from "express";

const v1Router = Router();
const v2Router = Router();

// V1 — formato antigo
v1Router.get("/users/:id", async (req, res) => {
  const user = await getUserById(req.params.id);
  res.json({ id: user.id, name: user.name });  // V1: flat
});

// V2 — formato novo com envelope + campos adicionais
v2Router.get("/users/:id", async (req, res) => {
  const user = await getUserById(req.params.id);
  res.json({
    data: {
      id: user.id,
      name: user.name,
      profile: user.profile  // campo novo em V2
    }
  });
});

app.use("/v1", v1Router);
app.use("/v2", v2Router);
```

### Sunset Policy (RFC 8594)

Quando deprecar uma versão, avisar com antecedência via headers:

```typescript
// Middleware de deprecation para V1
function deprecationMiddleware(req: Request, res: Response, next: NextFunction) {
  res.setHeader("Deprecation", "true");
  res.setHeader("Sunset", "Sat, 01 Jan 2027 00:00:00 GMT");
  res.setHeader(
    "Link",
    '<https://api.empresa.com/v2/users>; rel="successor-version"'
  );
  next();
}

app.use("/v1", deprecationMiddleware, v1Router);
```

---

## API-First com Mock Server

```bash
# Instalar Prism — mock server baseado no OpenAPI spec
npm install -g @stoplight/prism-cli

# Subir mock server — consumers podem desenvolver sem backend real
prism mock openapi.yaml --port 4010

# Validação de spec com Spectral (linting)
npm install -g @stoplight/spectral-cli
spectral lint openapi.yaml --ruleset @stoplight/spectral-owasp-ruleset
```

```typescript
// Gerar tipos TypeScript a partir do OpenAPI spec
// openapi-typescript converte spec → tipos sem runtime
// npm install -D openapi-typescript

import type { paths } from "./openapi.d.ts";  // gerado por openapi-typescript

type CreateOrderRequest = paths["/orders"]["post"]["requestBody"]["content"]["application/json"];
type OrderResponse = paths["/orders/{orderId}"]["get"]["responses"]["200"]["content"]["application/json"]["schema"];
```

---

## HATEOAS — Hipermídia como Motor de Estado

Na prática raramente implementado além do `Location` header no POST. Mas o conceito:

```json
{
  "data": {
    "id": "uuid",
    "status": "pending"
  },
  "_links": {
    "self": { "href": "/orders/uuid" },
    "cancel": { "href": "/orders/uuid/cancel", "method": "POST" },
    "pay": { "href": "/orders/uuid/pay", "method": "POST" }
  }
}
```

O consumer descobre ações disponíveis via links, sem hardcodar URLs. **Custo alto, adoção baixa** — use apenas em APIs públicas de longa vida.

---

## Trade-offs

| Aspecto | API-First (OpenAPI antes) | Code-First (gerar spec depois) |
|---|---|---|
| **Velocidade inicial** | Mais lento (spec antes do código) | Rápido para prototipar |
| **Qualidade do contrato** | Alto — revisável antes de implementar | Spec reflete o código, não o design |
| **Paralelismo** | Consumer pode desenvolver com mock | Consumer espera o backend |
| **Manutenção** | Spec é fonte de verdade | Risco de spec desatualizado |
| **Breaking changes** | Detectado no review da spec | Detectado em runtime |

## Quando Usar / Quando Evitar

**API-First:** APIs públicas, APIs consumidas por múltiplos times, APIs com SLA de estabilidade.

**Code-First:** prototipagem rápida, APIs internas com um único consumer controlado.

**HATEOAS:** APIs de longa vida com múltiplos clients heterogêneos onde os workflows mudam com frequência.

**Evitar URL versionamento profundo:** mais de 3 versões ativas simultâneas é sinal de que o processo de deprecação não funciona.

## Conceitos Relacionados

[[grpc]] · [[graphql]] · [[webhook]] · [[rate-limiting]] · [[pagination]] · [[idempotencia]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-16*
