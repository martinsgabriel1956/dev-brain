---
date: 2026-04-14
tags: [tech-mentor, backend, mensageria, cdc, debezium, kafka]
skill: tech-mentor-backend/references/mensageria
level: avançado
---

# CDC — Change Data Capture com Debezium

## Contexto

CDC é a técnica de capturar mudanças em um banco de dados (INSERT, UPDATE, DELETE) e transformá-las em eventos, sem modificar a aplicação que escreve. É a alternativa ao polling periódico (`SELECT WHERE updated_at > ?`) — que é lento, pesado e perde deletes.

Debezium é o conector CDC open-source mais usado. Lê o **WAL do PostgreSQL** (Write-Ahead Log) ou o **Binlog do MySQL** diretamente, como se fosse um replica, e publica os eventos no Kafka.

## Como Funciona

### Arquitetura

```
Application → PostgreSQL (escreve normalmente)
                   │
                   │ WAL (Write-Ahead Log)
                   ▼
              Debezium Connector (lê WAL via replicação lógica)
                   │
                   │ eventos de mudança
                   ▼
              Kafka Topic: "postgres.public.orders"
                   │
         ┌─────────┼─────────┐
         ▼         ▼         ▼
   Search Index  Cache    Analytics DB
  (Elasticsearch) (Redis)  (BigQuery)
```

A aplicação **não precisa mudar nada** — Debezium lê o WAL como se fosse uma replica de banco.

### Configurando Debezium no PostgreSQL

```sql
-- Habilitar replicação lógica (requer restart do PostgreSQL)
-- postgresql.conf:
-- wal_level = logical

-- Criar publicação para as tabelas que você quer capturar
CREATE PUBLICATION debezium_pub FOR TABLE orders, payments, users;

-- Criar usuário com permissão de replicação
CREATE USER debezium WITH REPLICATION LOGIN PASSWORD 'secret';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO debezium;
```

```json
// Configuração do Debezium Connector via Kafka Connect REST API
{
  "name": "postgres-orders-connector",
  "config": {
    "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
    "database.hostname": "postgres",
    "database.port": "5432",
    "database.user": "debezium",
    "database.password": "secret",
    "database.dbname": "production",
    "database.server.name": "postgres",

    "table.include.list": "public.orders,public.payments",
    "plugin.name": "pgoutput",

    // Snapshot inicial: captura estado atual antes de começar o streaming
    "snapshot.mode": "initial",

    // Schema registry para Avro
    "key.converter": "io.confluent.kafka.serializers.KafkaAvroSerializer",
    "value.converter": "io.confluent.kafka.serializers.KafkaAvroSerializer",
    "schema.registry.url": "http://schema-registry:8081"
  }
}
```

### Formato dos Eventos

```json
// Evento de UPDATE na tabela orders
{
  "before": {
    "id": "order-123",
    "status": "pending",
    "updated_at": 1713103200000
  },
  "after": {
    "id": "order-123",
    "status": "confirmed",
    "updated_at": 1713103260000
  },
  "source": {
    "db": "production",
    "table": "orders",
    "lsn": 2048576,      // posição no WAL
    "ts_ms": 1713103260000
  },
  "op": "u",  // c=create, u=update, d=delete, r=read (snapshot)
  "ts_ms": 1713103260100
}
```

### Consumer TypeScript

```typescript
import { Kafka } from "kafkajs";

const kafka = new Kafka({ clientId: "search-indexer", brokers: ["kafka:9092"] });
const consumer = kafka.consumer({ groupId: "search-indexer-group" });

await consumer.subscribe({ topic: "postgres.public.orders" });

await consumer.run({
  eachMessage: async ({ message }) => {
    const event = JSON.parse(message.value.toString());
    const { op, after, before } = event.payload;

    switch (op) {
      case "c": // create
        await searchIndex.upsert(after.id, after);
        break;

      case "u": // update
        await searchIndex.upsert(after.id, after);
        break;

      case "d": // delete
        await searchIndex.delete(before.id);
        break;

      case "r": // read — snapshot inicial
        await searchIndex.upsert(after.id, after);
        break;
    }
  }
});
```

### Outbox Pattern + CDC

A combinação mais robusta para garantir exatamente-uma-vez na publicação de eventos:

```typescript
// A aplicação escreve no banco de forma transacional
await prisma.$transaction(async tx => {
  // 1. Operação de negócio
  const order = await tx.order.create({ data: orderData });

  // 2. Evento na tabela outbox (dentro da mesma transação)
  await tx.outbox.create({
    data: {
      aggregateId: order.id,
      aggregateType: "Order",
      eventType: "OrderCreated",
      payload: JSON.stringify(order)
    }
  });
});

// Debezium captura o INSERT na tabela outbox e publica no Kafka
// → Garantia transacional sem 2PC
// → A aplicação nunca escreve diretamente no Kafka
```

```sql
-- Tabela outbox que Debezium monitora
CREATE TABLE outbox (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  aggregate_id UUID NOT NULL,
  aggregate_type VARCHAR(255) NOT NULL,
  event_type VARCHAR(255) NOT NULL,
  payload JSONB NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Após Debezium capturar e publicar, pode deletar (ou usar TTL)
-- Opcional: job para limpar registros processados
DELETE FROM outbox WHERE created_at < NOW() - INTERVAL '7 days';
```

### Gestão de Schema com Avro + Schema Registry

CDC é sensível a mudanças de schema — adicionar ou remover colunas pode quebrar consumers:

```
Regra de ouro: mudanças backward-compatible no banco = mudanças backward-compatible nos eventos
  ✅ Adicionar coluna nullable com default → campo opcional no Avro com default
  ✅ Renomear via Expand-Contract → campo antigo + campo novo temporariamente
  ❌ Remover coluna que consumer usa → breaking change — notificar consumers antes
```

## Trade-offs

| Aspecto | CDC (Debezium) | Polling (`WHERE updated_at >`) | Dual Write (app escreve em DB + Kafka) |
|---|---|---|---|
| **Completude** | Captura deletes, todos os updates | Não captura deletes facilmente | Depende da implementação |
| **Latência** | Milissegundos (WAL stream) | Segundos a minutos | Milissegundos |
| **Consistência** | Eventual, mas sem perda | Eventual, com possível perda | Risco de dual write problem |
| **Impacto na app** | Zero — lê WAL diretamente | Requer campo `updated_at` | Requer mudança na app |
| **Complexidade operacional** | Alta (Kafka Connect, Debezium) | Baixa | Média |

## Quando Usar / Quando Evitar

**Usar CDC quando:**
- Precisar sincronizar banco de dados com Elasticsearch, Redis, ou outro sistema
- Implementando Outbox Pattern de forma transparente
- Migração de banco com sincronização bidirecional durante transição
- Auditoria de todas as mudanças de dados (trail imutável no Kafka)
- Analytics em real-time sobre dados operacionais

**Evitar quando:**
- Volume de mudanças é muito baixo — polling simples é suficiente
- Precisar de lógica de negócio no evento (transformação complexa) → melhor Outbox Pattern explícito na app
- Time não tem experiência com Kafka Connect — overhead operacional é significativo

## Conceitos Relacionados

[[outbox-pattern]] · [[kafka]] · [[event-sourcing]] · [[event-driven-architecture]] · [[postgresql-avancado]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-14*
