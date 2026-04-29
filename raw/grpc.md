---
date: 2026-04-14
tags: [tech-mentor, backend, apis, grpc, protobuf, streaming]
skill: tech-mentor-backend/references/apis
level: avançado
---

# gRPC

## Contexto

gRPC é um framework de RPC (Remote Procedure Call) criado pelo Google, construído sobre HTTP/2 e Protobuf. Resolve dois problemas que REST/JSON tem em comunicação entre serviços: **performance** (Protobuf é ~10x menor e mais rápido que JSON) e **contrato fortemente tipado** (schema primeiro, código gerado).

É a escolha natural para comunicação interna entre microsserviços onde você controla ambos os lados.

## Como Funciona

### Protobuf — Schema First

```protobuf
// orders.proto — fonte da verdade do contrato
syntax = "proto3";
package orders;

service OrderService {
  // Unary: request-response tradicional
  rpc CreateOrder(CreateOrderRequest) returns (Order);
  rpc GetOrder(GetOrderRequest) returns (Order);

  // Server Streaming: servidor envia múltiplas respostas
  rpc ListOrders(ListOrdersRequest) returns (stream Order);

  // Client Streaming: cliente envia múltipla requisições
  rpc BulkCreateOrders(stream CreateOrderRequest) returns (BulkCreateResponse);

  // Bidirectional Streaming: ambos os lados streamam
  rpc TrackOrders(stream TrackRequest) returns (stream OrderUpdate);
}

message CreateOrderRequest {
  string user_id = 1;
  repeated OrderItem items = 2;
  string currency = 3;
}

message Order {
  string id = 1;
  string user_id = 2;
  repeated OrderItem items = 3;
  double total = 4;
  OrderStatus status = 5;
  int64 created_at = 6;  // Unix timestamp
}

message OrderItem {
  string product_id = 1;
  int32 quantity = 2;
  double unit_price = 3;
}

enum OrderStatus {
  ORDER_STATUS_UNSPECIFIED = 0;  // proto3: sempre ter o zero value
  ORDER_STATUS_PENDING = 1;
  ORDER_STATUS_CONFIRMED = 2;
  ORDER_STATUS_SHIPPED = 3;
}
```

```bash
# Gerar código TypeScript a partir do .proto
npx grpc-tools-node-protoc \
  --js_out=import_style=commonjs:./generated \
  --grpc_out=grpc_js:./generated \
  --ts_out=./generated \
  orders.proto
```

### Server TypeScript

```typescript
import grpc from "@grpc/grpc-js";
import { OrderServiceService } from "./generated/orders_grpc_pb";
import { Order, CreateOrderRequest } from "./generated/orders_pb";

const orderServiceImpl = {
  async createOrder(
    call: grpc.ServerUnaryCall<CreateOrderRequest, Order>,
    callback: grpc.sendUnaryData<Order>
  ) {
    try {
      const req = call.request;
      const order = await createOrderUseCase.execute({
        userId: req.getUserId(),
        items: req.getItemsList().map(item => ({
          productId: item.getProductId(),
          quantity: item.getQuantity(),
          unitPrice: item.getUnitPrice()
        })),
        currency: req.getCurrency()
      });

      const response = new Order();
      response.setId(order.id);
      response.setUserId(order.userId);
      response.setTotal(order.total);
      response.setStatus(order.status);

      callback(null, response);
    } catch (error) {
      // gRPC status codes
      callback({
        code: grpc.status.INTERNAL,
        message: "Failed to create order"
      });
    }
  },

  // Server Streaming
  listOrders(call: grpc.ServerWritableStream<ListOrdersRequest, Order>) {
    const cursor = createOrderCursor(call.request.getUserId());

    cursor.on("data", order => {
      const response = new Order();
      response.setId(order.id);
      call.write(response);
    });

    cursor.on("end", () => call.end());
    cursor.on("error", err => call.destroy(err));
  }
};

const server = new grpc.Server();
server.addService(OrderServiceService, orderServiceImpl);
server.bindAsync("0.0.0.0:50051", grpc.ServerCredentials.createInsecure(), () => {
  server.start();
});
```

### Client TypeScript

```typescript
import { OrderServiceClient } from "./generated/orders_grpc_pb";
import { CreateOrderRequest, OrderItem } from "./generated/orders_pb";

const client = new OrderServiceClient(
  "orders-service:50051",
  grpc.credentials.createInsecure()
);

// Unary call com promisify
import { promisify } from "util";
const createOrder = promisify(client.createOrder.bind(client));

const req = new CreateOrderRequest();
req.setUserId("user-123");
req.setCurrency("BRL");

const item = new OrderItem();
item.setProductId("prod-456");
item.setQuantity(2);
item.setUnitPrice(49.90);
req.addItems(item);

const order = await createOrder(req);
console.log(order.getId());

// Server Streaming
const stream = client.listOrders(new ListOrdersRequest());
stream.on("data", order => console.log(order.getId()));
stream.on("end", () => console.log("Stream completed"));
stream.on("error", err => console.log({ message: "Stream error", err }));
```

### Interceptors (Middleware)

```typescript
// Interceptor para logging e tracing
function loggingInterceptor(
  options: grpc.InterceptorOptions,
  nextCall: (options: grpc.InterceptorOptions) => grpc.InterceptingCall
) {
  return new grpc.InterceptingCall(nextCall(options), {
    start(metadata, listener, next) {
      const start = Date.now();
      const method = options.method_definition.path;

      next(metadata, {
        ...listener,
        onReceiveStatus(status, next) {
          console.log({
            message: "gRPC call completed",
            method,
            code: status.code,
            durationMs: Date.now() - start
          });
          next(status);
        }
      });
    }
  });
}
```

### gRPC Status Codes

```typescript
// Mapear erros de domínio para status codes gRPC corretos
function mapDomainErrorToGrpcStatus(error: Error): grpc.StatusObject {
  if (error instanceof OrderNotFoundError) {
    return { code: grpc.status.NOT_FOUND, message: error.message };
  }
  if (error instanceof ValidationError) {
    return { code: grpc.status.INVALID_ARGUMENT, message: error.message };
  }
  if (error instanceof UnauthorizedError) {
    return { code: grpc.status.UNAUTHENTICATED, message: error.message };
  }
  return { code: grpc.status.INTERNAL, message: "Internal error" };
}
```

## gRPC vs. REST

| Aspecto | gRPC | REST/JSON |
|---|---|---|
| **Serialização** | Protobuf — binário, ~10x menor | JSON — texto, legível por humanos |
| **Contrato** | Strongly typed, schema first | OpenAPI (opcional, não enforced) |
| **Streaming** | 4 modos nativos (HTTP/2) | SSE, WebSocket (separados) |
| **Code gen** | Automático e bidirecional | Geração parcial via OpenAPI |
| **Browser** | Requer grpc-web proxy | Nativo |
| **Debug** | Requer ferramentas (grpcurl, Postman) | curl, qualquer browser |
| **Caso de uso** | Comunicação interna entre serviços | API pública, frontend, mobile |

## Quando Usar / Quando Evitar

**Usar gRPC quando:**
- Comunicação interna entre microsserviços onde você controla cliente e servidor
- Performance crítica — Protobuf reduz payload e latência significativamente
- Streaming bidirecional nativo (ex: chat, telemetria, live feeds)
- Múltiplas linguagens no sistema — Protobuf gera código para todas

**Usar REST quando:**
- API pública consumida por terceiros
- Frontend web ou mobile que não quer grpc-web overhead
- Time não quer manter .proto files e pipeline de code gen
- Debug simples com curl é importante para produtividade

## Conceitos Relacionados

[[microsservicos]] · [[service-mesh]] · [[api-gateway-bff]] · [[kafka]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-14*
