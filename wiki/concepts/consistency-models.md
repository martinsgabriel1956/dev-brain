---
type: concept
title: "Modelos de Consistência"
aliases: ["modelos de consistência", "consistency models", "linearizability", "sequential consistency", "causal consistency", "eventual consistency"]
date_created: 2026-04-22
date_updated: 2026-07-03
source_count: 2
tags: [sistemas-distribuidos, consistencia, cap, linearizability, eventual, causal]
skill: tech-mentor-system-design
status: stable
---

# Modelos de Consistência

Espectro que define o que um cliente pode observar após uma escrita e qual ordenação é garantida entre operações concorrentes em sistemas distribuídos. O teorema CAP define que sob partição você escolhe entre Consistency e Availability — os modelos definem *o que* você garante quando escolhe "C".

## Espectro — Do Mais Forte ao Mais Fraco

### Linearizability (Strict Consistency)

Toda operação parece ocorrer atomicamente num ponto entre início e fim da chamada. Uma vez confirmada a escrita, qualquer leitura subsequente em qualquer nó a vê.

```
Client A: write(x=1) ─[ok]
Client B:                   read(x) → 1  ✅ garantido
Client C:               read(x) → 1      ✅ garantido (mesmo concurrent)
```

```typescript
// etcd — leitura linearizável vai ao líder, não à réplica
const client = new Etcd3();
await client.put("config/feature-flag").value("enabled");
const value = await client.get("config/feature-flag").string();
```

**Custo:** round-trip ao líder em cada operação, baixa disponibilidade sob partição.
**Usado em:** etcd, Zookeeper, CockroachDB (serializable), locks distribuídos, leader election.

---

### Sequential Consistency

Todas as operações aparecem em alguma ordem global consistente — mas sem obrigação de respeitar o tempo real do relógio. Todos os processos veem a mesma sequência.

```
Thread A: write(x=1), write(y=2)
Thread B: write(x=3)

✅ [x=1, y=2, x=3] ou [x=3, x=1, y=2]  — ambos válidos
❌ [x=3, y=2, x=1]  — viola ordem interna de A
```

**Diferença de linearizable:** não garante que a ordem reflita o tempo de relógio real.

---

### Causal Consistency

Operações com relação causa-efeito são vistas na ordem correta por todos. Operações sem relação causal podem divergir em ordem.

```
Alice: post("Oi") → reply("Olá, Alice!")
Bob vê: post antes de reply  ✅
Carol vê: post antes de reply ✅
Dave (sem relação causal): pode ver em ordem diferente ✅
```

Implementado via Vector Clocks:

```typescript
type VectorClock = Record<string, number>;

function happensBefore(a: VectorClock, b: VectorClock): boolean {
  const aNodes = Object.keys(a);
  return aNodes.every(node => (a[node] ?? 0) <= (b[node] ?? 0)) &&
    aNodes.some(node => (a[node] ?? 0) < (b[node] ?? 0));
}
```

**Usado em:** DynamoDB (causal sessions), MongoDB sessions, collaborative editing.

---

### Eventual Consistency

Se nenhuma nova escrita ocorrer, todos os nós convergem para o mesmo valor. Sem prazo, sem garantia de ordem em leituras intermediárias.

```typescript
// DynamoDB — eventual (barato, pode retornar stale)
dynamodb.getItem({ ..., ConsistentRead: false });

// Linearizável (2× o custo, vai ao primário)
dynamodb.getItem({ ..., ConsistentRead: true });
```

**Submodelos:**
- **Monotonic Read:** nunca lê valor mais antigo do que já leu
- **Read Your Writes:** sempre vê suas próprias escritas — ver [[concepts/read-your-writes]]
- **Monotonic Write:** escritas aplicadas na ordem enviada

**Usado em:** Cassandra (padrão), DynamoDB (padrão), DNS, feeds sociais, analytics.

---

## Comparativo

| Modelo | Garantia | Latência | Disponibilidade | Exemplos |
|---|---|---|---|---|
| Linearizable | Leitura sempre vê última escrita | Alta | Baixa sob partição | etcd, Zookeeper |
| Sequential | Mesma ordem global | Média | Média | Modelos de CPU |
| Causal | Causa antes do efeito | Baixa | Alta | DynamoDB sessions |
| Eventual | Convergência eventual | Muito baixa | Muito alta | Cassandra, DNS |

## Quando Usar

| Contexto | Modelo |
|---|---|
| Locks distribuídos, saldos, inventário, leader election | Linearizable |
| Comentários/replies, collaborative editing, sessões | Causal |
| Feeds, timelines, cache, analytics, view counts | Eventual |

**Armadilha:** eventual para inventário = overselling. Linearizable para view count = gargalo desnecessário.

## Eventual Consistency e o Acrônimo BASE

Eventual Consistency é o "E" de [[wiki/concepts/base-basically-available-soft-state-eventual|BASE]] — o conjunto de garantias mais fracas, comum em Cassandra/DynamoDB, contraposto a [[wiki/concepts/acid]]. Exemplo concreto de leitura desatualizada: escrever `saldo = 150` numa réplica e, no mesmo instante, ler `80` de outra réplica que ainda não recebeu a propagação — não é comum, mas é possível, e ilustra por que "consistência eventual" não tem prazo garantido. Ver [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]].

## Key Sources

- [[sources/modelos-de-consistencia]]
- [[wiki/sources/acid-vs-base-garantias-bancos-de-dados]] — exemplo de réplicas não sincronizadas e o acrônimo BASE
