---
date: 2026-04-16
tags: [tech-mentor, backend, banco, mongodb, nosql, aggregation, change-streams]
skill: tech-mentor-backend/references/banco
level: intermediário
---

# MongoDB — Aggregation Pipeline, Change Streams e Schema Validation

## Contexto

MongoDB é um banco de documentos — cada documento é um JSON independente, sem schema rígido. Isso permite modelar dados hierárquicos sem JOINs, mas o padrão de acesso deve guiar o schema (ao contrário do relacional, onde a normalização guia). A regra central: **embed se você sempre lê junto, referência se você lê independentemente**.

---

## Modelagem — Embed vs Referência

```javascript
// EMBED: dados sempre lidos juntos — sem JOIN necessário
{
  _id: ObjectId("..."),
  name: "Alice",
  address: {
    street: "Rua A, 123",
    city: "São Paulo",
    zip: "01234-567"
  },
  // Array embed: ok se o tamanho for limitado e sempre lido com o pai
  tags: ["developer", "backend", "typescript"]
}

// REFERÊNCIA: dados lidos independentemente ou array ilimitado
{
  _id: ObjectId("order-id"),
  userId: ObjectId("user-id"),  // referência — user pode ter milhares de orders
  items: [
    { productId: ObjectId("prod-id"), quantity: 2, price: 49.90 }
  ]
}

// Anti-pattern: arrays ilimitados embedded
// RUIM — um post com milhões de comentários vai explodir o documento (16MB limit)
{
  _id: ObjectId("post-id"),
  title: "Meu post",
  comments: [/* ... potencialmente milhares */]  // NUNCA
}

// BOM — comments como collection separada com referência ao post
// { _id, postId, text, authorId, createdAt }
```

---

## Aggregation Pipeline — Processamento de Dados

O pipeline processa documentos em estágios sequenciais. Cada estágio transforma a coleção.

```javascript
// Relatório de vendas por categoria — equivalente a GROUP BY com JOIN
db.orders.aggregate([
  // Estágio 1: Filtrar pedidos dos últimos 30 dias
  {
    $match: {
      status: "completed",
      createdAt: { $gte: new Date(Date.now() - 30 * 24 * 60 * 60 * 1000) }
    }
  },

  // Estágio 2: Expandir array de items (1 doc por item)
  { $unwind: "$items" },

  // Estágio 3: JOIN com products collection
  {
    $lookup: {
      from: "products",
      localField: "items.productId",
      foreignField: "_id",
      as: "product"
    }
  },

  // Estágio 4: Desnormalizar o array de 1 elemento
  { $unwind: "$product" },

  // Estágio 5: Agrupar por categoria
  {
    $group: {
      _id: "$product.categoryId",
      totalRevenue: { $sum: { $multiply: ["$items.price", "$items.quantity"] } },
      totalOrders: { $addToSet: "$_id" },  // set de order IDs únicos
      avgOrderValue: { $avg: { $multiply: ["$items.price", "$items.quantity"] } }
    }
  },

  // Estágio 6: Calcular count de orders
  {
    $addFields: {
      orderCount: { $size: "$totalOrders" }
    }
  },

  // Estágio 7: Ordenar por receita
  { $sort: { totalRevenue: -1 } },

  // Estágio 8: Limitar resultado
  { $limit: 10 },

  // Estágio 9: Formatar output
  {
    $project: {
      _id: 0,
      categoryId: "$_id",
      totalRevenue: { $round: ["$totalRevenue", 2] },
      orderCount: 1,
      avgOrderValue: { $round: ["$avgOrderValue", 2] }
    }
  }
]);
```

### Aggregation com TypeScript (Mongoose ou MongoDB driver)

```typescript
import { MongoClient, ObjectId } from "mongodb";

const client = new MongoClient(process.env.MONGODB_URL!);
const db = client.db("ecommerce");

type SalesReport = {
  categoryId: ObjectId;
  totalRevenue: number;
  orderCount: number;
  avgOrderValue: number;
};

async function getSalesByCategory(days = 30): Promise<SalesReport[]> {
  const since = new Date(Date.now() - days * 24 * 60 * 60 * 1000);

  return db.collection("orders").aggregate<SalesReport>([
    { $match: { status: "completed", createdAt: { $gte: since } } },
    { $unwind: "$items" },
    {
      $lookup: {
        from: "products",
        localField: "items.productId",
        foreignField: "_id",
        as: "product"
      }
    },
    { $unwind: "$product" },
    {
      $group: {
        _id: "$product.categoryId",
        totalRevenue: { $sum: { $multiply: ["$items.price", "$items.quantity"] } },
        uniqueOrders: { $addToSet: "$_id" },
        avgOrderValue: { $avg: { $multiply: ["$items.price", "$items.quantity"] } }
      }
    },
    {
      $project: {
        categoryId: "$_id",
        totalRevenue: { $round: ["$totalRevenue", 2] },
        orderCount: { $size: "$uniqueOrders" },
        avgOrderValue: { $round: ["$avgOrderValue", 2] }
      }
    },
    { $sort: { totalRevenue: -1 } }
  ]).toArray();
}
```

### Faceted Search — Resultados com Filtros

```javascript
// Retornar resultados + counts de facets em uma query
db.products.aggregate([
  { $match: { isActive: true, price: { $gte: 10, $lte: 500 } } },
  {
    $facet: {
      // Branch 1: produtos paginados
      results: [
        { $sort: { price: 1 } },
        { $skip: 0 },
        { $limit: 20 },
        { $project: { name: 1, price: 1, categoryId: 1 } }
      ],
      // Branch 2: contagem por categoria (para filtros na sidebar)
      byCategory: [
        { $group: { _id: "$categoryId", count: { $sum: 1 } } },
        { $sort: { count: -1 } }
      ],
      // Branch 3: total de resultados
      total: [{ $count: "count" }]
    }
  }
]);
```

---

## Change Streams — Reação a Mudanças em Tempo Real

Change Streams são o equivalente ao CDC do PostgreSQL WAL — permitem escutar mudanças na collection sem polling.

```typescript
import { ChangeStream, ChangeStreamDocument } from "mongodb";

type OrderDocument = {
  _id: ObjectId;
  status: string;
  userId: ObjectId;
  total: number;
};

// Escutar mudanças de status em orders
async function watchOrderStatusChanges(): Promise<void> {
  const collection = db.collection<OrderDocument>("orders");

  // Pipeline de filtro — só eventos que interessam
  const pipeline = [
    {
      $match: {
        operationType: { $in: ["update", "replace"] },
        "updateDescription.updatedFields.status": { $exists: true }
      }
    }
  ];

  const changeStream: ChangeStream = collection.watch(pipeline, {
    fullDocument: "updateLookup"  // incluir documento completo pós-atualização
  });

  changeStream.on("change", async (change: ChangeStreamDocument<OrderDocument>) => {
    if (change.operationType !== "update" && change.operationType !== "replace") return;

    const order = change.fullDocument;
    if (!order) return;

    console.log({ message: "Order status changed", orderId: order._id, newStatus: order.status });

    // Reagir a mudanças de status
    if (order.status === "completed") {
      await sendOrderCompletionEmail(order.userId, order._id);
    }

    if (order.status === "cancelled") {
      await processRefund(order._id, order.total);
    }
  });

  changeStream.on("error", error => {
    console.log({ message: "Change stream error", error: error.message });
  });

  // Graceful shutdown
  process.on("SIGTERM", async () => {
    await changeStream.close();
    await client.close();
  });
}

// Resume token — retomar o stream de onde parou após restart
async function watchWithResume(resumeToken?: object): Promise<void> {
  const changeStream = db.collection("orders").watch([], {
    resumeAfter: resumeToken,
    fullDocument: "updateLookup"
  });

  changeStream.on("change", async change => {
    // Salvar resume token periodicamente para poder retomar após crash
    await redis.set("orders:change-stream:resume-token", JSON.stringify(change._id));
    // processar...
  });
}
```

---

## Schema Validation — Garantias no Banco

MongoDB permite schema validation com JSON Schema — rejeita documentos inválidos no insert/update:

```javascript
db.createCollection("users", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "email", "createdAt"],
      properties: {
        name: {
          bsonType: "string",
          minLength: 2,
          maxLength: 100,
          description: "Nome é obrigatório"
        },
        email: {
          bsonType: "string",
          pattern: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
          description: "E-mail deve ser válido"
        },
        age: {
          bsonType: "int",
          minimum: 0,
          maximum: 150
        },
        role: {
          enum: ["admin", "user", "moderator"],
          description: "Role deve ser um dos valores permitidos"
        },
        createdAt: { bsonType: "date" }
      }
    }
  },
  validationAction: "error",  // rejeitar documentos inválidos (vs "warn")
  validationLevel: "strict"   // validar em insert e update (vs "moderate")
});
```

---

## Índices — Performance Crítica

```javascript
// Índice composto para queries frequentes — ordem importa (ESR: Equality, Sort, Range)
db.orders.createIndex(
  { userId: 1, status: 1, createdAt: -1 },
  { name: "idx_orders_user_status_date" }
);

// Índice parcial — só indexar documentos relevantes
db.orders.createIndex(
  { createdAt: 1 },
  {
    partialFilterExpression: { status: "pending" },
    name: "idx_orders_pending_date"
  }
);

// Índice de texto — full-text search
db.products.createIndex(
  { name: "text", description: "text" },
  { weights: { name: 10, description: 1 }, name: "idx_products_text" }
);

// TTL index — expirar documentos automaticamente
db.sessions.createIndex(
  { expiresAt: 1 },
  { expireAfterSeconds: 0 }  // expirar quando expiresAt < now()
);

// Verificar uso de índices
db.orders.explain("executionStats").find({ userId: ObjectId("..."), status: "pending" });
// Procurar: "IXSCAN" (usa índice) vs "COLLSCAN" (table scan)
```

---

## Trade-offs

| Aspecto | MongoDB | PostgreSQL |
|---|---|---|
| **Schema** | Flexível (schema-optional) | Rígido — migrations necessárias |
| **Joins** | $lookup (mais caro que JOIN) | JOIN nativo, otimizado |
| **Documentos hierárquicos** | Natural — nested objects | JSON/JSONB (funcional, mas diferente) |
| **Transações** | Multi-document (v4.0+), mais lento | ACID nativo, robusto |
| **Escalabilidade horizontal** | Sharding nativo | Sharding complexo |
| **Full-text search** | Text index básico | pg_trgm + tsvector (melhor) |
| **Analytics** | Aggregation Pipeline | SQL + Window Functions (mais expressivo) |
| **Consistência** | Eventual (padrão) ou linearizável (com readConcern "majority") | ACID + MVCC |

## Quando Usar / Quando Evitar

**Usar MongoDB:** catálogos com campos variáveis por produto, CMS com estrutura de conteúdo heterogênea, dados de sensores/IoT com schema evolutivo, aplicações que precisam de escala horizontal de escrita.

**Evitar MongoDB:** dados financeiros (transações complexas, ACID crítico), dados com muitos JOINs (relações complexas são caras no Mongo), equipes que já têm expertise em PostgreSQL (o JSONB do PG resolve muitos casos de uso do Mongo).

**Evitar Change Streams em:** aplicações serverless sem conexão persistente, volumes muito altos (>100k changes/s) sem infra dedicada.

## Conceitos Relacionados

[[redis]] · [[cdc-debezium]] · [[postgresql-avancado]] · [[kafka]] · [[event-sourcing]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-16*
