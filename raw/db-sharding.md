---
date: 2026-03-27
tags: [tech-mentor, system-design, escalabilidade, sharding, banco-de-dados, consistent-hashing]
skill: tech-mentor-system-design/references/db-sharding.md
level: intermediário
---

# DB Sharding

## Contexto

Sharding é a última linha de defesa quando o banco virou o gargalo e vertical scaling não é mais suficiente. Diferente de replicação (cópias do mesmo dado), sharding distribui dados **diferentes** em nós diferentes — writes escalam linearmente. A maioria dos sistemas nunca chega aqui, mas entender sharding é o que diferencia um engenheiro sênior de um arquiteto.

## Como Funciona

### O Problema que Sharding Resolve

```
Single DB (limite prático):
~10TB de dados úteis
~100k QPS de writes
Vertical scaling chegou no teto de custo

Sharding — partição horizontal:
┌──────────┬──────────┬──────────┐
│ Shard 1  │ Shard 2  │ Shard 3  │
│ users    │ users    │ users    │
│ 1–33%    │ 34–66%   │ 67–100%  │
└──────────┴──────────┴──────────┘
Cada shard: banco independente, sem coordenação entre eles
```

### Os Três Algoritmos

**Range-based — por intervalo de valor:**
```
Shard 1: user_id 1        → 1.000.000
Shard 2: user_id 1.000.001 → 2.000.000
Shard 3: user_id 2.000.001 → 3.000.000
```
✅ Range queries eficientes · ✅ Fácil de debugar
❌ Hot spots: dados recentes sempre vão para o último shard

**Hash-based — por hash da chave:**
```typescript
const getShard = (userId: string, numShards: number) =>
  parseInt(crypto.createHash("md5").update(userId).digest("hex"), 16) % numShards;
```
✅ Distribuição uniforme · ✅ Determinístico
❌ Range queries ineficientes · ❌ Resharding move quase todos os dados

**Consistent Hashing — hash sem o problema de resharding:**
```
Ring circular com 360°

Shard A: 0°–90°
Shard B: 90°–180°
Shard C: 180°–270°
Shard D: 270°–360°

Key = CRC32(user_id) % 360 → posição no ring
Key vai para o primeiro shard no sentido horário

Adicionar Shard E entre A (45°) e B (90°):
→ Apenas keys entre 45° e 90° migram de A para E
→ ~25% dos dados se movem (1/N), não 100%
```
Usado por: Redis Cluster (16.384 slots), Cassandra, DynamoDB.

## Código de Referência

### Shard Key — A Decisão Mais Importante

```sql
-- ✅ Bom: user_id como shard key se queries são sempre por usuário
SELECT * FROM orders WHERE user_id = '123' AND status = 'pending';
-- → vai para exatamente 1 shard

-- ❌ Ruim: queries frequentes cross-shard
SELECT * FROM orders WHERE status = 'pending';
-- → fan-out: vai para TODOS os shards, agrega os resultados
```

**Critérios para uma boa shard key:**

| Critério | Por quê |
|---|---|
| **Alta cardinalidade** | Muitos valores distintos → distribuição uniforme |
| **Imutável** | Mudar a shard key exige mover o registro entre shards |
| **Alinhada com access patterns** | Maioria das queries deve acessar 1 shard |

### Cross-shard Operations

```typescript
// Scatter-gather: query vai para todos os shards
async function searchAllShards(query: string) {
  const results = await Promise.all(
    shards.map(shard => shard.query(query))
  );
  return results.flat().sort((a, b) => b.score - a.score);
}
// Latência = latência do shard mais lento — evitar para queries frequentes
```

**Cross-shard transactions:**
```
Transferência entre usuários em shards diferentes:

Opção 1: 2PC (Two-Phase Commit)
  → Complexo, lento, blocking se coordenador cair

Opção 2: Saga Pattern (preferida)
  → Debita shard 1, credita shard 3
  → Se shard 3 falhar: compensação (estorno em shard 1)
  → Eventual consistency aceita

Opção 3: Redesign
  → Desnormalizar para colocar dados relacionados no mesmo shard
  → A melhor opção quando possível
```

### Resharding — Dual-write + Backfill

```
1. Escrever no shard antigo E no novo simultaneamente
           ↓
2. Migrar dados históricos em background (sem bloquear)
           ↓
3. Validar consistência entre os dois
           ↓
4. Remover escritas para o shard antigo
```

## Trade-offs

| Aspecto | Single DB | Sharded DB |
|---|---|---|
| **Writes** | Limitado ao hardware | Escala linear |
| **JOINs** | Trivial | Cross-shard = caro ou impossível |
| **Transactions** | ACID nativo | Complexo (Saga/2PC) |
| **Operação** | Simples | Complexa — resharding, routing, monitoramento |
| **Resharding** | N/A | Trabalhoso sem consistent hashing |
| **Uso ideal** | < 10TB, < 100k QPS | Além disso |

## Quando Usar / Quando Evitar

**Alternativas antes de sharding (na ordem):**
```
1. Índices corretos               → EXPLAIN ANALYZE primeiro
2. Cache Redis                    → tira 80% das leituras do banco
3. Read Replicas                  → escala reads sem complexidade
4. Vertical no banco              → RDS r6g.16xlarge aguenta muito
5. PostgreSQL table partitioning  → partição local, sem distribuição
6. NoSQL nativo (Cassandra/DynDB) → sharding transparente no serviço
7. Sharding manual                → quando tudo acima não basta
```

**Ferramentas:**

| Ferramenta | Quando |
|---|---|
| **Vitess** | MySQL além de 1TB, sharding transparente |
| **Citus** | PostgreSQL com distributed queries |
| **CockroachDB** | SQL distribuído sem operação manual |
| **Cassandra** | Write-heavy, série temporal, IoT |

## Conceitos Relacionados

[[fase-2-escalabilidade]] · [[banco-de-dados]] · [[horizontal-vs-vertical-scaling]] · [[mensageria]] · [[cqrs]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-27*
