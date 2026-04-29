---
date: 2026-04-17
tags: [tech-mentor, networking, serialização, protobuf, avro, messagepack]
skill: tech-mentor-networking/references/serialization
level: intermediário
---

# Protocolos de Serialização — JSON, Protobuf, Avro, MessagePack

## Contexto
A escolha do formato de serialização impacta diretamente latência, throughput e custo de storage/bandwidth. JSON é legível mas ineficiente; formatos binários são compactos mas exigem schemas.

## Comparativo de Performance

| Formato | Tamanho | Velocidade | Schema | Legível |
|---|---|---|---|---|
| **JSON** | Baseline | Baseline | Opcional | Sim |
| **MessagePack** | ~30% menor que JSON | 2-3x mais rápido | Opcional | Não |
| **Protobuf** | ~60-80% menor que JSON | 5-10x mais rápido | Obrigatório | Não |
| **Avro** | ~60-70% menor | Rápido (com schema) | Obrigatório | Não |
| **FlatBuffers** | Similar ao Protobuf | Sem parsing (zero-copy) | Obrigatório | Não |
| **Thrift** | Similar ao Protobuf | Rápido | Obrigatório | Não |

---

## Protobuf — Schema Versionado

```protobuf
// order.proto
syntax = "proto3";
package orders;

message Order {
  string id = 1;
  string customer_id = 2;
  double total_amount = 3;
  OrderStatus status = 4;
  repeated OrderItem items = 5;
  // Campo adicionado na v2 — backward compatible
  string currency = 6;  // default "" para mensagens antigas
}

enum OrderStatus {
  PENDING = 0;     // proto3: default é o zero value
  CONFIRMED = 1;
  SHIPPED = 2;
  DELIVERED = 3;
}

message OrderItem {
  string product_id = 1;
  int32 quantity = 2;
  double unit_price = 3;
}
```

**Regras de compatibilidade:**
- ✅ Adicionar campo com novo field number
- ✅ Renomear campo (field number é o que importa, não o nome)
- ✅ Remover campo (campo ausente = zero value no consumer)
- ❌ Mudar tipo de campo existente
- ❌ Reutilizar field number de campo removido

```typescript
// TypeScript com @bufbuild/protobuf
import { create, toBinary, fromBinary } from "@bufbuild/protobuf";
import { OrderSchema, OrderStatus } from "./gen/order_pb";

const order = create(OrderSchema, {
  id: "123",
  customerId: "456",
  totalAmount: 99.90,
  status: OrderStatus.CONFIRMED
});

const bytes = toBinary(OrderSchema, order);
console.log(`JSON: ${JSON.stringify(order).length} bytes`);
console.log(`Protobuf: ${bytes.length} bytes`);  // tipicamente 3-5x menor

const decoded = fromBinary(OrderSchema, bytes);
```

---

## Avro — Schema com Registry

Avro serializa sem incluir o schema no payload (ao contrário do JSON). O schema é resolvido via Schema Registry usando o ID — por isso Avro + Schema Registry são inseparáveis.

```json
{
  "type": "record",
  "name": "Order",
  "namespace": "com.example.orders",
  "fields": [
    { "name": "id", "type": "string" },
    { "name": "customerId", "type": "string" },
    { "name": "totalAmount", "type": "double" },
    { "name": "currency", "type": ["null", "string"], "default": null }
  ]
}
```

**Evolução de schema Avro:**
- Union types `["null", "string"]` com `"default": null` permitem adicionar campos retroativamente
- Schema Registry valida compatibilidade antes de aceitar nova versão

---

## MessagePack — JSON Binário

MessagePack serializa os mesmos tipos do JSON (string, number, bool, null, array, object) mas em formato binário compacto. **Zero schema** — igual ao JSON, mas menor e mais rápido.

```typescript
import { pack, unpack } from "msgpackr";

const data = {
  id: "order-123",
  customerId: "user-456",
  items: [{ productId: "prod-1", quantity: 2 }],
  total: 99.90
};

const packed = pack(data);              // Buffer binário
const unpacked = unpack(packed);        // idêntico ao original

console.log(`JSON: ${JSON.stringify(data).length} bytes`);
console.log(`MsgPack: ${packed.length} bytes`);  // ~30% menor
```

**Quando usar MessagePack:** APIs internas onde JSON é suficiente mas o overhead importa; WebSockets onde o schema evolui frequentemente.

---

## FlatBuffers e Thrift

**FlatBuffers** (Google): zero-copy access — dados podem ser lidos sem parsing, acessando memória diretamente. Ideal para game engines e sistemas com latência ultra-crítica.

**Thrift** (Meta): schema + múltiplos protocolos de transporte. Usado internamente no Meta. Menos popular externamente que Protobuf.

## Quando Usar Cada Um

| Cenário | Recomendação |
|---|---|
| API pública REST | JSON — máxima compatibilidade |
| API interna de alta frequência | Protobuf — schema versionado + performance |
| Event streaming (Kafka) | Avro + Schema Registry — evolução controlada |
| WebSocket/IoT com payload variável | MessagePack — sem schema, menor que JSON |
| Leitura de estruturas grandes sem parse | FlatBuffers — zero-copy |
| Microsserviços com RPC bidirecional | Protobuf + gRPC |

## Conceitos Relacionados
[[grpc]] · [[schema-registry]] · [[kafka]] · [[http-tcp-quic]] · [[api-contracts-versioning]]

---
*Fonte: tech-mentor skill · tech-mentor-networking · 2026-04-17*
