---
date: 2026-04-16
tags: [tech-mentor, distributed-systems, database, read-replicas, pgbouncer, connection-pooling]
skill: tech-mentor-system-design/references/distributed-systems
level: intermediário
---

# Read Replicas e Connection Pooling

## Contexto

Dois problemas distintos que surgem quando o banco começa a ser o gargalo:

**Read Replicas:** a maioria das aplicações tem muito mais leituras do que escritas (tipicamente 80/20). Read replicas permitem escalar horizontalmente as leituras sem escalar o primário.

**Connection Pooling:** PostgreSQL cria um processo OS por conexão. Com 1000 conexões simultâneas, você tem 1000 processos — memória esgotada e context switching matam throughput. PgBouncer é um proxy que multiplexa conexões de aplicação em um pool menor de conexões reais ao banco.

## Read Replicas

### Como Funciona

O primário replica o WAL (Write-Ahead Log) para réplicas via streaming replication. Réplicas aplicam os logs em ordem e ficam segundos (ou milissegundos) atrasadas.

```
                    ┌─────────────┐
  Writes ─────────► │   Primary   │ ─── WAL stream ──► Replica 1
                    │  (escritas) │ ─── WAL stream ──► Replica 2
                    └─────────────┘                    Replica 3
  
  Reads ──► Replica 1 (qualquer uma)
            Replica 2
            Replica 3
```

**Replication lag:** réplicas ficam atrás por ms a segundos. Em carga alta, pode ser mais. Monitorar com:

```sql
-- No primary: mede o lag por réplica
SELECT
  client_addr,
  state,
  sent_lsn,
  write_lsn,
  flush_lsn,
  replay_lsn,
  (sent_lsn - replay_lsn) AS replication_lag_bytes
FROM pg_stat_replication;

-- Na réplica: mede o atraso em segundos
SELECT EXTRACT(EPOCH FROM (now() - pg_last_xact_replay_timestamp())) AS lag_seconds;
```

### Roteamento de Queries com Prisma

```typescript
import { PrismaClient } from "@prisma/client";

// Instâncias separadas para primary e replicas
const primaryDb = new PrismaClient({
  datasources: { db: { url: process.env.DATABASE_PRIMARY_URL } }
});

const replicaDb = new PrismaClient({
  datasources: { db: { url: process.env.DATABASE_REPLICA_URL } }
});

// Use case: ler do replica quando staleness é ok
async function listOrders(userId: string) {
  return replicaDb.order.findMany({
    where: { userId },
    orderBy: { createdAt: "desc" },
    take: 20
  });
}

// Escreve sempre no primary
async function createOrder(data: CreateOrderData) {
  return primaryDb.order.create({ data });
}

// Após escrita crítica — ler do primary para garantir read-your-writes
async function createOrderAndConfirm(data: CreateOrderData) {
  const order = await primaryDb.order.create({ data });
  // Busca no primary — não na replica, que pode estar stale
  return primaryDb.order.findUniqueOrThrow({ where: { id: order.id } });
}
```

### Multi-replica com Load Balancing

```typescript
// Pool de replicas com round-robin simples
class ReplicaPool {
  private replicas: PrismaClient[];
  private current = 0;

  constructor(urls: string[]) {
    this.replicas = urls.map(url => new PrismaClient({
      datasources: { db: { url } }
    }));
  }

  next(): PrismaClient {
    const replica = this.replicas[this.current];
    this.current = (this.current + 1) % this.replicas.length;
    return replica;
  }
}

const pool = new ReplicaPool([
  process.env.REPLICA_1_URL!,
  process.env.REPLICA_2_URL!,
  process.env.REPLICA_3_URL!
]);

// Em produção, usar PgBouncer na frente de cada réplica
```

### Quando Réplicas São Insuficientes

| Situação | Solução |
|---|---|
| Queries analíticas pesadas | Dedicated analytics replica ou DW separado |
| Leitura de dado recém-escrito | Forçar leitura no primário com flag |
| Lag inaceitável | Synchronous replication (mata performance de escrita) |
| Escrita é o gargalo | Sharding — réplicas não ajudam escrita |

---

## Connection Pooling com PgBouncer

### O Problema Sem Pool

```
1000 usuários simultâneos → 1000 conexões ao PostgreSQL
PostgreSQL: 1 processo por conexão × 1000 = ~2-3 GB de memória só em conexões
Context switching entre 1000 processos → throughput cai

PostgreSQL recomenda: max_connections = 100-400 para workloads típicos
```

### PgBouncer — Modos de Operação

**Session mode:** uma conexão do pool é dada por toda a sessão do cliente. Mínimo impacto, mas pouca multiplexação.

**Transaction mode:** conexão devolvida ao pool após cada transação. **O modo mais comum para aplicações web.**

**Statement mode:** conexão devolvida após cada statement. Incompatível com transações multi-statement.

```ini
; pgbouncer.ini
[databases]
production = host=postgres-primary port=5432 dbname=production

[pgbouncer]
listen_port = 6432
listen_addr = 0.0.0.0

; Transaction mode — retorna conexão ao pool após cada transação
pool_mode = transaction

; Conexões reais ao PostgreSQL
max_client_conn = 1000    ; clientes que podem conectar ao PgBouncer
default_pool_size = 25    ; conexões reais ao Postgres por database/user
min_pool_size = 5         ; mantém N conexões aquecidas
reserve_pool_size = 5     ; emergência para picos

; Timeouts
server_idle_timeout = 600
client_idle_timeout = 0   ; sem timeout para clientes (WebSocket, long-polling)

auth_type = scram-sha-256
auth_file = /etc/pgbouncer/userlist.txt
```

### Arquitetura com PgBouncer

```
App Servers (1000 conexões)
       │
       ▼
  PgBouncer (6432)         ← proxy leve, event-driven (sem processo por conexão)
  pool: 25 conexões reais
       │
       ▼
  PostgreSQL (5432)
  max_connections = 100
```

**Resultado:** 1000 clientes → PgBouncer → 25 conexões reais. PostgreSQL nunca vê mais de 25 conexões simultaneamente.

### Configuração no Prisma com PgBouncer

```typescript
// DATABASE_URL aponta para PgBouncer, não para PostgreSQL diretamente
// pgbouncer=true instrui o Prisma a desabilitar prepared statements
// (incompatíveis com transaction mode do PgBouncer)

// .env
// DATABASE_URL="postgresql://user:pass@pgbouncer:6432/production?pgbouncer=true"

const prisma = new PrismaClient({
  datasources: {
    db: {
      url: process.env.DATABASE_URL  // pgbouncer:6432 com ?pgbouncer=true
    }
  }
});
```

**Atenção:** Transaction mode do PgBouncer **quebra** features que dependem de estado de sessão:
- `SET LOCAL` — não funciona (conexão trocada entre statements)
- `LISTEN/NOTIFY` — requer session mode
- Prepared statements — desabilitar com `?pgbouncer=true` no Prisma
- Advisory locks baseados em sessão — usar transaction-level advisory locks

### RDS Proxy (AWS)

Para quem usa RDS, o RDS Proxy é o equivalente gerenciado do PgBouncer:

```typescript
// Trocar DATABASE_URL para o endpoint do RDS Proxy
// Benefícios: IAM auth, failover mais rápido, sem gerenciar PgBouncer
// Custo: ~0.015/hora por vCPU do RDS + 0.01/GB de tráfego
const prisma = new PrismaClient({
  datasources: {
    db: { url: process.env.RDS_PROXY_URL }  // *.proxy-*.rds.amazonaws.com
  }
});
```

## Trade-offs

| Aspecto | Read Replicas | Connection Pooling (PgBouncer) |
|---|---|---|
| **Problema que resolve** | Throughput de leitura | Sobrecarga de conexões |
| **Complexidade** | Média (roteamento de queries) | Baixa (troca a URL) |
| **Risco** | Stale reads se ignorar lag | Incompatibilidade de session features |
| **Custo** | Alto (outro servidor de banco) | Baixo (PgBouncer é leve) |
| **Escala** | Horizontal de leitura | Vertical de conexões |

## Quando Usar / Quando Evitar

**Read Replicas:**
- Carga de leitura > 70% das queries
- Relatórios e analytics que tolerem dados de segundos atrás
- Separar workloads de OLTP e OLAP

**Connection Pooling:**
- Qualquer aplicação web com mais de ~50 conexões simultâneas
- Funções serverless (Lambda) que criam/destroem conexões a cada invocação
- Microserviços com múltiplas réplicas de pod

**Evitar réplicas para:**
- Leitura imediatamente após escrita crítica (inventário, saldo)
- Dados com replication lag inaceitável sem monitoramento

## Conceitos Relacionados

[[db-sharding]] · [[postgresql-avancado]] · [[modelos-de-consistencia]] · [[quorum]] · [[cqrs]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-16*
