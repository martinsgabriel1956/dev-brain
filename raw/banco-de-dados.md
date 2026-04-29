---
date: 2026-03-27
tags: [tech-mentor, system-design, infraestrutura, banco-de-dados, postgresql, nosql, acid]
skill: tech-mentor-system-design/references/read-replicas-pooling.md
level: fundamento
---

# Banco de Dados

## Contexto

Banco de dados é onde o estado persiste. A decisão de qual banco usar — e como usá-lo — tem impacto direto em consistência, escalabilidade e custo. Não existe escolha universal. Use PostgreSQL como padrão e só migre para outro banco quando ele claramente não serve para o caso.

## Como Funciona

### ACID — A Fundação do Relacional

```
Atomicity   → a transação toda ocorre ou nada ocorre
              (não existe "cobrou mas não criou o pedido")

Consistency → o banco nunca fica em estado inválido
              (constraints, foreign keys, checks sempre respeitados)

Isolation   → transações concorrentes não interferem entre si
              (dois usuários comprando o último item — só um vence)

Durability  → dado commitado sobrevive a falha de hardware
              (gravado no WAL antes de confirmar)
```

### Relacional vs NoSQL

| Tipo | Exemplos | Use para |
|---|---|---|
| **Relacional** | PostgreSQL, MySQL | Financeiro, multi-entidade, transações |
| **Document** | MongoDB, Firestore | Dados semi-estruturados, schema flexível |
| **Key-Value** | Redis, DynamoDB | Acesso por chave única, alta performance |
| **Wide-Column** | Cassandra, DynamoDB | Escrita massiva, série temporal, IoT |
| **Graph** | Neo4j, Neptune | Relacionamentos complexos |
| **Search** | Elasticsearch | Full-text search, faceted search |

## Código de Referência

### Índices

```sql
-- Índice simples
CREATE INDEX idx_orders_user_id ON orders(user_id);

-- Índice composto — otimiza WHERE user_id = ? AND status = ?
CREATE INDEX idx_orders_user_status ON orders(user_id, status);

-- Índice parcial — só indexa subset dos dados
CREATE INDEX idx_orders_pending ON orders(created_at)
WHERE status = 'pending';

-- Diagnóstico: veja o que o banco está fazendo
EXPLAIN ANALYZE
SELECT * FROM orders WHERE user_id = '123' AND status = 'pending';
-- Seq Scan → full table scan → precisa de índice
-- Index Scan → usando índice → OK
-- Index Only Scan → resposta direto do índice → melhor caso
```

**Regra**: indexe colunas em `WHERE`, `JOIN ON`, `ORDER BY`, `GROUP BY`. Índice tem custo: cada `INSERT`/`UPDATE`/`DELETE` atualiza todos os índices. Tabela com 15 índices faz 15x mais trabalho por escrita.

### Transações

```typescript
// ❌ Sem transação: se a segunda falhar, a primeira já foi executada
await db.account.update({ where: { id: fromId }, data: { balance: { decrement: 100 } } });
await db.account.update({ where: { id: toId }, data: { balance: { increment: 100 } } });

// ✅ Com transação: ou as duas ocorrem, ou nenhuma
await db.$transaction(async tx => {
  await tx.account.update({ where: { id: fromId }, data: { balance: { decrement: 100 } } });
  await tx.account.update({ where: { id: toId }, data: { balance: { increment: 100 } } });
});
```

### Read Replicas

```typescript
// Roteamento explícito read/write
const primary = new PrismaClient({ datasourceUrl: PRIMARY_URL });
const replica = new PrismaClient({ datasourceUrl: REPLICA_URL });

const orders = await replica.order.findMany({ where: { userId } }); // leitura → réplica
const order = await primary.order.create({ data: orderData });      // escrita → primário
```

**Read-your-writes** — após escrever, force leitura do primário por N segundos:
```typescript
async function createOrder(data: CreateOrderDTO) {
  const order = await primary.order.create({ data });
  await redis.set(`force_primary:${data.userId}`, "1", "EX", 2);
  return order;
}

async function getOrders(userId: string) {
  const forcePrimary = await redis.get(`force_primary:${userId}`);
  const db = forcePrimary ? primary : replica;
  return db.order.findMany({ where: { userId } });
}
```

### Connection Pooling — PgBouncer

```
50 pods × 20 conexões = 1000 conexões → PgBouncer → 20 conexões reais no PostgreSQL
```

```ini
# pgbouncer.ini
[databases]
mydb = host=postgres port=5432 dbname=mydb

[pgbouncer]
pool_mode = transaction    # recomendado: pool por transação
max_client_conn = 1000     # máximo de conexões de entrada
default_pool_size = 20     # conexões reais no banco
```

### N+1 — O Bug de Performance Mais Comum

```typescript
// ❌ N+1: 1 query para orders + N queries para cada user
const orders = await db.order.findMany();
for (const order of orders) {
  const user = await db.user.findUnique({ where: { id: order.userId } });
  // 100 pedidos = 101 queries
}

// ✅ 1 query com JOIN
const orders = await db.order.findMany({
  include: { user: true },
});
```

## Trade-offs

| Aspecto | Relacional | NoSQL |
|---|---|---|
| **Consistência** | ACID completo | Eventual (geralmente) |
| **Queries** | JOINs complexos, agregações | Simples, por chave |
| **Escala de escrita** | Vertical (um primário) | Horizontal nativo |
| **Schema** | Rígido — segurança + integridade | Flexível — agilidade |

## Quando Usar / Quando Evitar

**Read replicas:**
- ✅ Workload read-heavy (>80% reads)
- ✅ Queries analíticas pesadas que não podem afetar o primário
- ❌ Quando consistência imediata é obrigatória (saldos, inventário crítico)
- ❌ Como substituto para queries lentas — otimize os índices primeiro

**PostgreSQL consegue mais do que parece:**
- `JSONB` → flexibilidade de documento sem MongoDB
- Full-text search básico → evita Elasticsearch para casos simples
- `pg_vector` → busca vetorial para IA
- Timescaledb extension → série temporal

## Conceitos Relacionados

[[fase-1-fundamentos-infraestrutura]] · [[cache]] · [[db-sharding]] · [[read-replicas]] · [[mensageria]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-27*
