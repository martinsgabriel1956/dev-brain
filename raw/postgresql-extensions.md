---
date: 2026-04-17
tags: [tech-mentor, banco, postgresql, particionamento, replicacao]
skill: tech-mentor-backend/references/databases
level: avançado
---

# PostgreSQL Avançado — pg_partman, pglogical, pg_repack, Savepoints

## pg_partman — Particionamento Automático

### Contexto
Particionamento nativo do PostgreSQL (declarativo, desde v10) divide uma tabela grande em partições físicas menores. `pg_partman` automatiza a criação e manutenção dessas partições — sem ele, você criaria partições manualmente ou escreveria jobs de manutenção.

### Tipos de Particionamento

| Tipo | Caso de uso | Exemplo |
|---|---|---|
| **RANGE** | Dados temporais | Partição por mês em `events` |
| **LIST** | Categorias fixas | Partição por `country_code` |
| **HASH** | Distribuição uniforme | Partição por `user_id % N` |

```sql
-- Tabela particionada por RANGE (mês)
CREATE TABLE events (
  id          UUID NOT NULL DEFAULT gen_random_uuid(),
  user_id     UUID NOT NULL,
  event_type  TEXT NOT NULL,
  payload     JSONB,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
) PARTITION BY RANGE (created_at);

-- pg_partman cria e mantém as partições automaticamente
SELECT partman.create_parent(
  p_parent_table   => 'public.events',
  p_control        => 'created_at',
  p_type           => 'native',
  p_interval       => 'monthly',
  p_premake        => 3  -- cria 3 partições futuras com antecedência
);

-- Configurar retenção: manter apenas 12 meses
UPDATE partman.part_config
SET retention = '12 months', retention_keep_table = false
WHERE parent_table = 'public.events';

-- Job de manutenção (rodar via pg_cron ou cron externo)
SELECT partman.run_maintenance();
```

**Benefícios arquiteturais:**
- Queries com filtro em `created_at` fazem **partition pruning** — varrendo apenas a partição relevante
- `DROP` de partição antiga é O(1) vs. `DELETE` que é O(N) com vacuum necessário
- Índices menores por partição → melhor performance de escrita

---

## pglogical — Replicação Lógica entre Versões

### Contexto
Permite replicação lógica seletiva entre instâncias PostgreSQL de **versões diferentes**. Essencial para zero-downtime upgrades: sobe PostgreSQL nova versão em paralelo, replica os dados, faz o cutover.

```sql
-- No nó origem (PostgreSQL 14)
CREATE EXTENSION pglogical;

SELECT pglogical.create_node(
  node_name => 'provider',
  dsn       => 'host=pg14.internal port=5432 dbname=myapp'
);

-- Publicar tabelas específicas (não precisa publicar todas)
SELECT pglogical.replication_set_add_table('default', 'orders', true);
SELECT pglogical.replication_set_add_table('default', 'users', true);

-- No nó destino (PostgreSQL 16)
CREATE EXTENSION pglogical;

SELECT pglogical.create_node(
  node_name => 'subscriber',
  dsn       => 'host=pg16.internal port=5432 dbname=myapp'
);

SELECT pglogical.create_subscription(
  subscription_name => 'pg14_to_pg16',
  provider_dsn      => 'host=pg14.internal port=5432 dbname=myapp user=replicator password=...'
);
```

**Fluxo de upgrade sem downtime:**
1. Sobe nova versão em paralelo com pglogical replicando
2. Monitora o lag de replicação até chegar próximo de zero
3. Pausa writes no app (ou usa feature flag)
4. Aguarda lag zerar
5. Muda DNS/connection string para nova versão
6. Retoma writes

---

## pg_repack — Desfragmentação sem Lock Exclusivo

### Contexto
`VACUUM FULL` compacta uma tabela mas exige **lock exclusivo** — a tabela fica inacessível durante a operação, que pode demorar horas. `pg_repack` faz o mesmo sem lock exclusivo, usando uma tabela temporária e replicação lógica interna.

```bash
# Instalar
apt-get install postgresql-16-repack

# Repack de tabela específica (sem lock exclusivo)
pg_repack -h localhost -d myapp -t orders

# Repack de índice específico
pg_repack -h localhost -d myapp --index idx_orders_customer_id

# Repack de todo o banco (com paralelismo)
pg_repack -h localhost -d myapp --jobs 4
```

**Quando usar:**
- Tabela com alto índice de dead tuples (bloat > 30%) detectado via `pgstats_buddy` ou query manual
- Após grandes operações de DELETE/UPDATE que não foram seguidas de VACUUM adequado
- Antes de criar índices em tabelas muito fragmentadas

---

## Savepoints — Nested Transactions

```sql
BEGIN;

INSERT INTO orders (id, customer_id, total) VALUES (gen_random_uuid(), '123', 100.00);

SAVEPOINT before_payment;

INSERT INTO payments (order_id, amount, provider) VALUES (..., 100.00, 'stripe');

-- Stripe retornou erro — reverter só o pagamento, manter o pedido
ROLLBACK TO SAVEPOINT before_payment;

-- Tentar com outro provider
INSERT INTO payments (order_id, amount, provider) VALUES (..., 100.00, 'paypal');

COMMIT; -- se paypal OK, commita tudo (pedido + pagamento via paypal)
```

```typescript
// Prisma — savepoints via $transaction interativa
await prisma.$transaction(async tx => {
  const order = await tx.order.create({ data: orderData });

  try {
    // Prisma não expõe savepoints diretamente — usar $queryRaw
    await tx.$queryRaw`SAVEPOINT payment_attempt`;
    await tx.payment.create({ data: { orderId: order.id, provider: "stripe" } });
  } catch {
    await tx.$queryRaw`ROLLBACK TO SAVEPOINT payment_attempt`;
    await tx.payment.create({ data: { orderId: order.id, provider: "paypal" } });
  }

  return order;
});
```

**Uso prático:** saga patterns locais, retry de sub-operações dentro de uma transação maior, validações parciais com rollback seletivo.

## Conceitos Relacionados
[[postgresql-avancado]] · [[outbox-pattern]] · [[expand-contract]] · [[zero-downtime-deploy]] · [[cdc-debezium]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-17*
