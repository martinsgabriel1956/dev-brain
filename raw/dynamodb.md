---
date: 2026-04-17
tags: [tech-mentor, backend, banco, dynamodb, nosql, single-table, gsi, lsi, dax]
skill: tech-mentor-backend/references/banco
level: avançado
---

# DynamoDB — Single-Table Design, GSI/LSI, Streams e DAX

## Contexto

DynamoDB é um banco NoSQL totalmente gerenciado da AWS com latência garantida de single-digit milliseconds em qualquer escala. O diferencial e a armadilha central: não há query flexível como SQL. Você precisa conhecer todos os access patterns antes de modelar — o schema é construído ao redor das queries, não o contrário. Single-table design maximiza eficiência eliminando joins entre tabelas.

---

## Conceitos Fundamentais

```
Table          → coleção de items (equivalente a tabela)
Item           → documento JSON (equivalente a row)
Attribute      → campo do item (equivalente a coluna)

Primary Key:
  Partition Key (PK)  → hash key — distribui items entre shards
  Sort Key (SK)       → range key — ordena items dentro de uma partition

Capacity:
  On-demand   → pay-per-request, escala automática (variável imprevisível)
  Provisioned → RCU/WCU fixos com auto-scaling (mais barato e previsível)
```

---

## Single-Table Design — Modelagem por Access Pattern

A regra central: **defina todos os access patterns antes de criar a tabela**. O schema nasce das queries, não das entidades.

```typescript
import { DynamoDBClient, GetItemCommand, QueryCommand, PutItemCommand, TransactWriteItemsCommand } from "@aws-sdk/client-dynamodb";
import { marshall, unmarshall } from "@aws-sdk/util-dynamodb";

const client = new DynamoDBClient({ region: "us-east-1" });
const TABLE_NAME = "AppTable";

// Schema de chaves para um e-commerce single-table:
// PK                SK                       Entity
// USER#userId       PROFILE                  → perfil do usuário
// USER#userId       ORDER#orderId            → order do usuário
// ORDER#orderId     METADATA                 → detalhes do pedido
// PRODUCT#prodId    METADATA                 → produto
// CATEGORY#catId    PRODUCT#prodId           → produto por categoria (GSI invertido)

type UserProfile = {
  pk: string;   // "USER#uuid"
  sk: string;   // "PROFILE"
  userId: string;
  name: string;
  email: string;
  gsi1pk: string;  // "EMAIL#user@example.com" — para busca por email via GSI
  gsi1sk: string;  // "USER"
  createdAt: string;
};

// PUT — criar usuário
async function createUser(userId: string, name: string, email: string): Promise<void> {
  const item: UserProfile = {
    pk: `USER#${userId}`,
    sk: "PROFILE",
    userId,
    name,
    email,
    gsi1pk: `EMAIL#${email}`,
    gsi1sk: "USER",
    createdAt: new Date().toISOString()
  };

  await client.send(new PutItemCommand({
    TableName: TABLE_NAME,
    Item: marshall(item),
    ConditionExpression: "attribute_not_exists(pk)"  // prevenir sobrescrever se já existe
  }));
}

// GET — buscar usuário por ID (usa PK + SK diretamente — O(1))
async function getUserById(userId: string): Promise<UserProfile | null> {
  const response = await client.send(new GetItemCommand({
    TableName: TABLE_NAME,
    Key: marshall({ pk: `USER#${userId}`, sk: "PROFILE" })
  }));

  return response.Item ? unmarshall(response.Item) as UserProfile : null;
}

// QUERY — buscar todas as orders de um usuário (PK fixo, SK begins_with)
type Order = {
  pk: string;
  sk: string;
  orderId: string;
  userId: string;
  total: number;
  status: string;
  createdAt: string;
};

async function getUserOrders(userId: string): Promise<Order[]> {
  const response = await client.send(new QueryCommand({
    TableName: TABLE_NAME,
    KeyConditionExpression: "pk = :pk AND begins_with(sk, :skPrefix)",
    ExpressionAttributeValues: marshall({
      ":pk": `USER#${userId}`,
      ":skPrefix": "ORDER#"
    }),
    // Paginar se muitos resultados
    Limit: 50
  }));

  return (response.Items ?? []).map(item => unmarshall(item) as Order);
}

// Transação — criar order + decrementar inventário atomicamente
async function createOrderWithInventory(
  userId: string,
  orderId: string,
  productId: string,
  quantity: number,
  total: number
): Promise<void> {
  await client.send(new TransactWriteItemsCommand({
    TransactItems: [
      // 1. Criar order
      {
        Put: {
          TableName: TABLE_NAME,
          Item: marshall({
            pk: `USER#${userId}`,
            sk: `ORDER#${orderId}`,
            orderId,
            userId,
            total,
            status: "pending",
            createdAt: new Date().toISOString()
          } satisfies Order)
        }
      },
      // 2. Decrementar inventário com condição (não vai negativo)
      {
        Update: {
          TableName: TABLE_NAME,
          Key: marshall({ pk: `PRODUCT#${productId}`, sk: "INVENTORY" }),
          UpdateExpression: "SET stock = stock - :qty",
          ConditionExpression: "stock >= :qty",
          ExpressionAttributeValues: marshall({ ":qty": quantity })
        }
      }
    ]
  }));
}
```

---

## GSI (Global Secondary Index) e LSI (Local Secondary Index)

```typescript
import { CreateTableCommand } from "@aws-sdk/client-dynamodb";

// Criar tabela com GSI para busca por email e por status de order
await client.send(new CreateTableCommand({
  TableName: TABLE_NAME,
  BillingMode: "PAY_PER_REQUEST",

  AttributeDefinitions: [
    { AttributeName: "pk", AttributeType: "S" },
    { AttributeName: "sk", AttributeType: "S" },
    { AttributeName: "gsi1pk", AttributeType: "S" },
    { AttributeName: "gsi1sk", AttributeType: "S" },
    { AttributeName: "gsi2pk", AttributeType: "S" }
  ],

  KeySchema: [
    { AttributeName: "pk", KeyType: "HASH" },
    { AttributeName: "sk", KeyType: "RANGE" }
  ],

  GlobalSecondaryIndexes: [
    {
      IndexName: "GSI1",
      KeySchema: [
        { AttributeName: "gsi1pk", KeyType: "HASH" },
        { AttributeName: "gsi1sk", KeyType: "RANGE" }
      ],
      Projection: { ProjectionType: "ALL" }
      // ProjectionType: "KEYS_ONLY" → apenas PK+SK do item (menor custo)
      // ProjectionType: "INCLUDE"   → PK+SK + atributos específicos
      // ProjectionType: "ALL"       → todos os atributos (maior custo, mais flexível)
    },
    {
      IndexName: "GSI2",
      KeySchema: [
        { AttributeName: "gsi2pk", KeyType: "HASH" }
      ],
      Projection: { ProjectionType: "ALL" }
    }
  ]

  // LSI: não existe aqui pois deve ser declarado na criação — mesma PK, SK diferente
  // LocalSecondaryIndexes: só definível no CreateTable, limite de 5, mesma partition
}));

// Buscar usuário por email via GSI1
async function getUserByEmail(email: string): Promise<UserProfile | null> {
  const response = await client.send(new QueryCommand({
    TableName: TABLE_NAME,
    IndexName: "GSI1",
    KeyConditionExpression: "gsi1pk = :gsi1pk AND gsi1sk = :gsi1sk",
    ExpressionAttributeValues: marshall({
      ":gsi1pk": `EMAIL#${email}`,
      ":gsi1sk": "USER"
    })
  }));

  const items = response.Items ?? [];
  return items.length > 0 ? unmarshall(items[0]) as UserProfile : null;
}
```

```
GSI vs LSI:
  LSI  → mesma Partition Key, Sort Key diferente. Consistência forte possível. Criado só no CreateTable
  GSI  → Partition Key diferente. Sempre eventually consistent. Pode ser adicionado depois
  
  Custo GSI: replica os dados — cada GSI aumenta RCU/WCU de escrita proporcionalmente
  Sparse GSI: items sem o atributo GSI PK ficam fora do índice — economia de custo
```

---

## DynamoDB Streams + Lambda

Streams são CDC nativo — cada mutação (INSERT, MODIFY, REMOVE) gera um evento ordenado por shard.

```typescript
import type { DynamoDBStreamEvent, DynamoDBRecord } from "aws-lambda";
import { unmarshall } from "@aws-sdk/util-dynamodb";
import type { AttributeValue } from "@aws-sdk/client-dynamodb";

export async function handler(event: DynamoDBStreamEvent): Promise<void> {
  for (const record of event.Records) {
    if (!record.dynamodb) continue;

    const { eventName, dynamodb } = record;

    if (eventName === "INSERT" && dynamodb.NewImage) {
      const newItem = unmarshall(dynamodb.NewImage as Record<string, AttributeValue>);
      console.log({ message: "Item created", item: newItem });

      // Reagir a criação de order
      if (newItem.pk?.startsWith("USER#") && newItem.sk?.startsWith("ORDER#")) {
        await sendOrderConfirmationEmail(newItem.userId, newItem.orderId);
      }
    }

    if (eventName === "MODIFY" && dynamodb.OldImage && dynamodb.NewImage) {
      const old = unmarshall(dynamodb.OldImage as Record<string, AttributeValue>);
      const updated = unmarshall(dynamodb.NewImage as Record<string, AttributeValue>);

      if (old.status !== updated.status) {
        console.log({ message: "Status changed", from: old.status, to: updated.status });
      }
    }

    if (eventName === "REMOVE" && dynamodb.OldImage) {
      const deleted = unmarshall(dynamodb.OldImage as Record<string, AttributeValue>);
      console.log({ message: "Item deleted", item: deleted });
    }
  }
}

async function sendOrderConfirmationEmail(userId: string, orderId: string): Promise<void> {
  console.log({ message: "Sending order confirmation", userId, orderId });
}
```

---

## DynamoDB Accelerator (DAX)

DAX é um cache in-memory totalmente gerenciado e compatível com DynamoDB API — adiciona camada de cache sem mudar código (exceto endpoint):

```typescript
import * as AmazonDaxClient from "amazon-dax-client";
import { DynamoDB } from "aws-sdk";

// Substituir DynamoDB client por DAX client — API idêntica
const dax = new AmazonDaxClient({
  endpoints: ["mycluster.dax.us-east-1.amazonaws.com:8111"],
  region: "us-east-1"
});

const docClient = new DynamoDB.DocumentClient({ service: dax });

// GetItem com DAX: cache de item (TTL padrão 5 minutos)
// QueryItem com DAX: cache de query result
// Writes passam pelo DAX e invalidam o cache automaticamente

// DAX é ideal para:
// - Read-heavy workloads (leitura >> escrita)
// - Latência < 1ms necessária
// - Dados que podem ter até 5min de staleness

// DAX NÃO cacheia:
// - Scan operations (full table scan)
// - Transactional reads/writes
// - BatchWrite
```

---

## Trade-offs

| Aspecto | DynamoDB | PostgreSQL | MongoDB |
|---|---|---|---|
| **Modelo** | Key-Value + Document | Relacional | Document |
| **Query flexibilidade** | Limitada ao schema de chaves | SQL completo | Pipeline rico |
| **Latência** | <1ms garantido em escala | Variável com carga | Variável |
| **Joins** | Single-table ou múltiplas queries | JOIN nativo | $lookup |
| **Consistência** | Eventual (GSI) ou forte (tabela base) | ACID | Variável |
| **Escala horizontal** | Automático (sharding transparente) | Complexo | Sharding manual |
| **Custo previsibilidade** | On-demand pode surpreender | Instância fixa | Instância fixa |
| **Schema evolution** | Sem migrations | Migrations DDL | Sem migrations |

## Quando Usar / Quando Evitar

**Usar DynamoDB:** serverless backends (Lambda), jogos com leaderboards, sessões de usuário, IoT telemetria, catálogos de produto com access patterns definidos, sistemas com escala automática como requisito.

**Evitar DynamoDB:** queries ad-hoc e relatórios complexos, access patterns desconhecidos em fase de exploração, dados financeiros com transações complexas entre múltiplas entidades, times sem expertise em single-table design (a curva de aprendizado é alta).

**Regra crítica:** defina os access patterns ANTES de criar a tabela. Adição de GSI depois é possível mas custar caro e pode não ser suficiente — retrofit de schema em DynamoDB é doloroso.

## Conceitos Relacionados

[[mongodb]] · [[redis-avancado]] · [[cache-strategies]] · [[cdc-debezium]] · [[background-jobs]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-17*
