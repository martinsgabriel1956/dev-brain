---
date: 2026-04-17
tags: [tech-mentor, banco, graph, time-series, vector, embedded, distribuido]
skill: tech-mentor-backend/references/databases
level: intermediário
---

# Bancos Especializados — Graph, Time-Series, Vector, Embedded, Distribuído

## Graph DB — Neo4j

### Contexto
Bancos de grafos armazenam dados como **nós** (entidades) e **arestas** (relacionamentos). A vantagem sobre SQL é que relacionamentos são cidadãos de primeira classe — queries de múltiplos graus de separação que seriam joins caros em SQL são O(1) por hop no grafo.

**Casos de uso reais:** detecção de fraude (rede de contas), recomendação ("quem você talvez conheça"), grafos de permissão (ReBAC/Zanzibar), análise de dependências, knowledge graphs.

```cypher
-- Cypher — linguagem de query do Neo4j
-- Encontrar todos os amigos de amigos do usuário "Alice" em até 2 graus
MATCH (alice:User { name: "Alice" })-[:FRIEND*1..2]-(suggested:User)
WHERE suggested <> alice
  AND NOT (alice)-[:FRIEND]-(suggested)
RETURN suggested.name, count(*) AS mutual_friends
ORDER BY mutual_friends DESC
LIMIT 10;

-- Detectar ciclos de transação suspeitos (fraude)
MATCH path = (a:Account)-[:TRANSFERRED_TO*3..5]->(a)
WHERE all(r IN relationships(path) WHERE r.amount > 1000)
RETURN path;
```

---

## Time-Series DB

### Contexto
Bancos de séries temporais são otimizados para **inserção contínua de dados com timestamp** (métricas, IoT, logs financeiros). O problema que resolvem: PostgreSQL comum degrada ao inserir milhões de pontos por segundo com alto volume histórico.

| Banco | Melhor para | Destaque |
|---|---|---|
| **TimescaleDB** | Extensão do PostgreSQL — SQL completo | Hypertables, continuous aggregates |
| **InfluxDB** | Métricas de infraestrutura | Flux language, integração nativa com Grafana |
| **QuestDB** | Alta performance de ingestão | SQL com time-series extensions, SIMD |

```sql
-- TimescaleDB — hypertable particionada por tempo automaticamente
SELECT create_hypertable('metrics', 'time', chunk_time_interval => INTERVAL '1 day');

-- Inserção normal via SQL
INSERT INTO metrics (time, device_id, temperature, humidity)
VALUES (NOW(), 'sensor-001', 23.5, 65.2);

-- Continuous aggregate — pre-computa média horária automaticamente
CREATE MATERIALIZED VIEW metrics_hourly
WITH (timescaledb.continuous) AS
SELECT
  time_bucket('1 hour', time) AS bucket,
  device_id,
  avg(temperature) AS avg_temp,
  max(temperature) AS max_temp
FROM metrics
GROUP BY bucket, device_id;

-- Retention policy — deleta dados > 90 dias automaticamente
SELECT add_retention_policy('metrics', INTERVAL '90 days');
```

---

## Vector DB

### Contexto
Armazena vetores de alta dimensão (embeddings de texto, imagem, áudio) e permite busca por similaridade semântica — ao contrário da busca exata, encontra "documentos semanticamente próximos".

**HNSW (Hierarchical Navigable Small World):** o índice mais usado. Constrói um grafo hierárquico que permite busca aproximada por vizinhos mais próximos em O(log N) vs. O(N) da busca exata (flat/brute force).

```typescript
// pgvector — Vector DB diretamente no PostgreSQL
// Ideal para volumes < 10M vetores sem infra adicional

// Criar índice HNSW
await db.query(`
  CREATE INDEX ON documents USING hnsw (embedding vector_cosine_ops)
  WITH (m = 16, ef_construction = 64);
`);

// Busca híbrida: semântica (vetor) + keyword (FTS)
const results = await db.query(`
  SELECT id, content,
    embedding <=> $1 AS semantic_distance,
    ts_rank(search_vector, query) AS keyword_score,
    (1 - (embedding <=> $1)) * 0.7 + ts_rank(search_vector, query) * 0.3 AS hybrid_score
  FROM documents,
    plainto_tsquery('portuguese', $2) query
  WHERE search_vector @@ query
  ORDER BY hybrid_score DESC
  LIMIT 10
`, [queryEmbedding, queryText]);
```

```typescript
// Qdrant — quando precisar de > 10M vetores ou features avançadas
import { QdrantClient } from "@qdrant/js-client-rest";

const qdrant = new QdrantClient({ url: process.env.QDRANT_URL });

// Busca com filtro de metadata
const results = await qdrant.search("documents", {
  vector: queryEmbedding,
  filter: {
    must: [{ key: "category", match: { value: "technical" } }]
  },
  with_payload: true,
  limit: 10
});
```

---

## Embedded DB — SQLite, DuckDB, libSQL

### Contexto
Bancos que rodam **no mesmo processo** da aplicação — sem servidor separado. Eliminam latência de rede e overhead de conexão. Ideais para edge computing, apps mobile e analytics local.

| Banco | Uso | Destaque |
|---|---|---|
| **SQLite** | OLTP leve, apps mobile, testes | Confiabilidade extrema, zero config |
| **DuckDB** | OLAP in-process, analytics | SQL sobre Parquet/CSV, vetorização SIMD |
| **libSQL** | SQLite com replicação | Fork do SQLite, Turso para edge |

```typescript
// DuckDB — analytics diretamente sobre arquivos Parquet na S3
import Database from "duckdb";

const db = new Database(":memory:");

const result = await db.all(`
  SELECT
    date_trunc('month', created_at) AS month,
    country,
    sum(revenue) AS total_revenue,
    count(*) AS order_count
  FROM read_parquet('s3://data-lake/orders/2025/*.parquet')
  WHERE created_at >= '2025-01-01'
  GROUP BY month, country
  ORDER BY month, total_revenue DESC
`);
```

---

## Banco Distribuído — CockroachDB, Spanner, YugabyteDB, TiDB

### Contexto
Bancos que distribuem dados automaticamente por múltiplos nodes mantendo **ACID completo** — combinando o melhor do SQL com a escalabilidade horizontal do NoSQL.

| Banco | Base | Compatibilidade |
|---|---|---|
| **CockroachDB** | Raft + MVCC | PostgreSQL wire protocol |
| **Spanner** | TrueTime + Paxos | PostgreSQL/JDBC dialeto próprio |
| **YugabyteDB** | Raft | PostgreSQL + Cassandra |
| **TiDB** | Raft | MySQL protocol |

**Quando usar sobre PostgreSQL + sharding manual:**
- Múltiplos data centers com consistência forte (ativo-ativo)
- Resharding automático sem downtime
- Crescimento imprevisível de dados onde particionar manualmente é inviável

**Cuidados:**
- Latência de escrita maior (Raft requer quorum)
- Queries cross-shard são mais lentas
- Custo operacional e de licença significativamente maior

## Conceitos Relacionados
[[postgresql-avancado]] · [[rag-retrieval]] · [[cap-theorem]] · [[db-sharding]] · [[elasticsearch-opensearch]]

---
*Fonte: tech-mentor skill · tech-mentor-backend · 2026-04-17*
