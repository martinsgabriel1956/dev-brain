---
date: 2026-04-17
tags: [tech-mentor, mensageria, kafka, schema, avro, protobuf]
skill: tech-mentor-backend/references/messaging
level: avançado
---

# Schema Registry

## Contexto
Em sistemas event-driven, producer e consumer evoluem independentemente. Sem um contrato explícito, o producer pode mudar o formato do evento e quebrar silenciosamente todos os consumers. O **Schema Registry** é o serviço que centraliza e versiona os schemas dos eventos, validando compatibilidade antes de permitir mudanças.

O mais usado é o **Confluent Schema Registry** (open source), que integra nativamente com Kafka. Suporta Avro, Protobuf e JSON Schema.

## Como Funciona

```
Producer                Schema Registry              Consumer
   │                          │                          │
   │── POST /subjects/        │                          │
   │   orders-value/versions  │                          │
   │   (schema Avro v1) ─────►│ valida compatibilidade   │
   │◄── schema_id: 42 ────────│                          │
   │                          │                          │
   │── publish msg:           │                          │
   │   [magic byte][schema_id=42][payload Avro] ────────►Kafka
   │                          │                          │
   │                          │     msg com schema_id=42►│
   │                          │◄─── GET /schemas/ids/42 ─│
   │                          │─── schema Avro v1 ───────►│
   │                          │                   deserializa
```

O payload no Kafka tem formato: `[0x00][4 bytes schema_id][payload serializado]`

## Avro com Schema Registry (TypeScript)

```typescript
import { SchemaRegistry, SchemaType } from "@kafkajs/confluent-schema-registry";
import { Kafka } from "kafkajs";

const registry = new SchemaRegistry({ host: "http://localhost:8081" });
const kafka = new Kafka({ brokers: ["localhost:9092"] });

// Schema Avro para o evento
const orderCreatedSchema = {
  type: "record",
  name: "OrderCreated",
  namespace: "com.example.orders",
  fields: [
    { name: "orderId", type: "string" },
    { name: "customerId", type: "string" },
    { name: "totalAmount", type: "double" },
    { name: "createdAt", type: "string" }
    // Novos campos opcionais podem ser adicionados com default
    // { name: "currency", type: ["null", "string"], default: null }
  ]
};

// Registrar schema (idempotente — retorna ID existente se igual)
const { id: schemaId } = await registry.register(
  { type: SchemaType.AVRO, schema: JSON.stringify(orderCreatedSchema) },
  { subject: "orders-value" }
);

// Publicar — serializa e inclui schema_id no payload
const producer = kafka.producer();
await producer.connect();

await producer.send({
  topic: "orders",
  messages: [{
    key: order.id,
    value: await registry.encode(schemaId, {
      orderId: order.id,
      customerId: order.customerId,
      totalAmount: order.total,
      createdAt: new Date().toISOString()
    })
  }]
});

// Consumir — deserializa usando o schema_id embutido na mensagem
const consumer = kafka.consumer({ groupId: "order-processor" });
await consumer.connect();
await consumer.subscribe({ topic: "orders" });

await consumer.run({
  eachMessage: async ({ message }) => {
    const order = await registry.decode(message.value!);
    console.log({ message: "Order received", order });
  }
});
```

## Regras de Compatibilidade

O Schema Registry valida a compatibilidade antes de aceitar uma nova versão. Configure por subject:

| Modo | Significado | Quando usar |
|---|---|---|
| `BACKWARD` | Consumers novos leem dados antigos | Padrão — consumer evolui antes do producer |
| `FORWARD` | Consumers antigos leem dados novos | Producer evolui antes do consumer |
| `FULL` | Ambos os anteriores | Máxima segurança |
| `NONE` | Sem validação | Desenvolvimento |

**BACKWARD compatibility rules:**
- ✅ Adicionar campo com `default`
- ✅ Remover campo sem `default` (consumers antigos ignoram ausência)
- ❌ Remover campo com `default` (consumers antigos precisam do default)
- ❌ Alterar tipo de campo

```bash
# Configurar compatibilidade do subject
curl -X PUT http://localhost:8081/config/orders-value \
  -H "Content-Type: application/json" \
  -d '{"compatibility": "BACKWARD"}'

# Verificar compatibilidade antes de publicar
curl -X POST http://localhost:8081/compatibility/subjects/orders-value/versions/latest \
  -H "Content-Type: application/json" \
  -d '{"schema": "{...novo schema...}"}'
```

## Schema Registry vs. AsyncAPI

| Ferramenta | Propósito |
|---|---|
| **Schema Registry** | Validação de compatibilidade em runtime + serialização binária |
| **AsyncAPI** | Documentação legível por humanos dos tópicos e eventos |

Complementares: AsyncAPI documenta, Schema Registry valida.

## Conceitos Relacionados
[[kafka]] · [[cdc-debezium]] · [[tolerant-reader]] · [[expand-contract]] · [[dlq-event-patterns]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-17*
