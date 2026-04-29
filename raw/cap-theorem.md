---
date: 2026-04-17
tags: [tech-mentor, system-design, distribuidos, cap, pacelc, consistencia, disponibilidade]
skill: tech-mentor-system-design/references/distribuidos
level: arquiteto
---

# CAP Theorem, PACELC e Modelos de Consistência

## Contexto

CAP é o framework teórico mais citado em sistemas distribuídos — e o mais mal-interpretado. A maioria dos sistemas não escolhe entre C e A de forma binária; eles ajustam o trade-off por operação. PACELC complementa o CAP adicionando a dimensão de latência, que é o que realmente importa em produção quando a rede não está particionada.

---

## CAP Theorem

```
Em um sistema distribuído, você pode ter no máximo 2 das 3 propriedades:

C — Consistency (Consistência)
    Toda leitura retorna o valor mais recente ou um erro.
    Todos os nós veem os mesmos dados ao mesmo tempo.

A — Availability (Disponibilidade)
    Toda requisição recebe uma resposta (sem erro), mesmo que não seja o dado mais recente.
    Garantia: sem timeouts, sem erros de serviço.

P — Partition Tolerance (Tolerância a Partição)
    O sistema continua operando mesmo que mensagens sejam perdidas ou atrasadas entre nós.

Por que P é obrigatório na prática:
  → Redes falham. Pacotes são perdidos. Links ficam lentos.
  → Sem P, o sistema simplesmente para quando há falha de rede.
  → A escolha real é entre CP e AP — P não é opcional.
```

### CP vs AP — A Escolha Real

```
CP (Consistency + Partition Tolerance):
  → Recusa requisições quando há incerteza sobre consistência
  → Nós que não conseguem confirmar o dado retornam erro
  → Exemplos: HBase, Zookeeper, etcd, MongoDB (com majority write concern), Redis Cluster

AP (Availability + Partition Tolerance):
  → Serve o dado que tem, mesmo que potencialmente desatualizado
  → Eventual consistency — os nós convergem quando a partição resolve
  → Exemplos: Cassandra, DynamoDB, CouchDB, DNS

CA (sem Partition Tolerance):
  → Existe apenas em sistemas single-node ou redes confiáveis (intranet controlada)
  → RDBMS tradicional em single-node é CA na teoria
  → Em produção com replicação, você cai em CP ou AP obrigatoriamente
```

---

## PACELC — A Extensão Prática

CAP só fala sobre comportamento durante partição. PACELC adiciona: **e quando não há partição?**

```
PACELC: if Partition → tradeoff(A, C) else → tradeoff(L, C)

Legenda:
  P  = Partition
  A  = Availability
  C  = Consistency
  E  = Else (sem partição)
  L  = Latency
  C  = Consistency (mesmo símbolo, contexto diferente)

Durante partição:     escolha entre Availability e Consistency
Sem partição:         escolha entre Latency e Consistency
```

### Classificação PACELC dos Principais Sistemas

```
Sistema          | Partição  | Sem Partição | Classificação
-----------------|-----------|--------------|---------------
DynamoDB         | PA        | EL           | PA/EL
Cassandra        | PA        | EL           | PA/EL
Riak             | PA        | EL           | PA/EL
MongoDB          | PC        | EC           | PC/EC
HBase            | PC        | EC           | PC/EC
BigTable         | PC        | EC           | PC/EC
MySQL (sync rep) | PC        | EC           | PC/EC
Zookeeper        | PC        | EC           | PC/EC
PostgreSQL       | PC        | EC           | PC/EC (single-node: CA)

PA/EL = sacrifica consistência em partição E prioriza latência normalmente
PC/EC = mantém consistência em partição E aceita latência adicional para consistir
```

---

## Modelos de Consistência

Do mais forte para o mais fraco:

```
1. Linearizability (Strong Consistency)
   → Toda operação parece instantânea e atômica para todos os observers
   → Leitura sempre retorna o write mais recente
   → Custo: alta latência (requer round-trip para confirmar)
   → Usado em: Zookeeper, etcd, Google Spanner

2. Sequential Consistency
   → Operações de cada processo aparecem em ordem, mas clocks globais não sincronizados
   → Todos os processos veem a mesma ordem global de operações
   → Mais fraco que linearizability (sem garantia de real-time)

3. Causal Consistency
   → Operações causalmente relacionadas são vistas na ordem correta por todos
   → Operações concorrentes podem ser vistas em ordens diferentes
   → MongoDB com causally consistent sessions
   → Implementado via Vector Clocks ou Lamport Timestamps

4. Read-Your-Writes (Session Consistency)
   → Você sempre vê seus próprios writes, mesmo em réplicas
   → Outros usuários podem ver versões antigas
   → Padrão em sessões de banco com stickiness

5. Eventual Consistency
   → Se não houver novos writes, eventualmente todos os nós convergem
   → Sem garantia de quando — pode ser ms ou segundos
   → Cassandra, DynamoDB, DNS
```

---

## Vector Clocks — Causalidade sem Relógio Global

```typescript
// Vector Clock simplificado para rastrear causalidade entre eventos
type VectorClock = Record<string, number>;

function increment(clock: VectorClock, nodeId: string): VectorClock {
  return { ...clock, [nodeId]: (clock[nodeId] ?? 0) + 1 };
}

// Merge: pegar o máximo de cada posição ao receber mensagem
function merge(local: VectorClock, received: VectorClock): VectorClock {
  const allKeys = new Set([...Object.keys(local), ...Object.keys(received)]);
  const merged: VectorClock = {};
  for (const key of allKeys) {
    merged[key] = Math.max(local[key] ?? 0, received[key] ?? 0);
  }
  return merged;
}

// Comparar: A "happened before" B?
function happenedBefore(a: VectorClock, b: VectorClock): boolean {
  const allKeys = new Set([...Object.keys(a), ...Object.keys(b)]);
  let strictlyLess = false;
  for (const key of allKeys) {
    const aVal = a[key] ?? 0;
    const bVal = b[key] ?? 0;
    if (aVal > bVal) return false;            // A tem evento que B não viu
    if (aVal < bVal) strictlyLess = true;     // B tem eventos a mais
  }
  return strictlyLess;
}

function isConcurrent(a: VectorClock, b: VectorClock): boolean {
  return !happenedBefore(a, b) && !happenedBefore(b, a);
}

// Exemplo de uso em sistema de mensagens distribuído
type Message = {
  id: string;
  content: string;
  clock: VectorClock;
  sender: string;
};

function receiveMessage(
  localClock: VectorClock,
  nodeId: string,
  msg: Message
): VectorClock {
  // Merge local clock com o clock da mensagem recebida
  const merged = merge(localClock, msg.clock);
  // Incrementar o próprio nó para marcar que processou
  return increment(merged, nodeId);
}

// Uso:
// node-A: { A: 1, B: 0 }  → envia para node-B
// node-B: recebe { A: 1, B: 0 }, merge com seu { A: 0, B: 2 } → { A: 1, B: 2 }
// node-B incrementa: { A: 1, B: 3 }
```

---

## Quorum — Consistência Configurável

```
Sistema Dynamo-like (ex: Cassandra, Riak):
  N = número de réplicas
  W = writes confirmados antes de retornar sucesso
  R = reads consultados antes de retornar resultado

Regras de consistência:
  Strong consistency: W + R > N
  → Garante que toda leitura vê o write mais recente

  Latência otimizada: W = 1, R = 1
  → Alta performance, eventual consistency

Exemplos práticos com N=3:
  W=2, R=2: W+R=4 > 3 → strong consistency
  W=1, R=3: W+R=4 > 3 → strong consistency, write rápido, read lento
  W=3, R=1: W+R=4 > 3 → write lento (todos confirmam), read rápido
  W=1, R=1: W+R=2 < 3 → eventual consistency, máxima performance

CockroachDB/Spanner usa Raft para strong consistency automaticamente.
```

---

## Trade-offs em Produção

| Sistema | Modelo | Trade-off Principal | Caso de Uso |
|---|---|---|---|
| **PostgreSQL** | Forte (linearizable com WAL) | Latência de replicação síncrona | Financeiro, inventário |
| **Cassandra** | Eventual (AP) | Tunable via quorum | Séries temporais, IoT |
| **DynamoDB** | Eventual / Forte por opção | Custo de strongly consistent reads | E-commerce, gaming |
| **Redis Cluster** | Eventual (assíncrono) | Perda de dados se falha antes de sync | Cache, sessões |
| **etcd/Zookeeper** | Linearizable (CP) | Throughput baixo | Config, service discovery |
| **Spanner** | Linearizable global | Latência global (TrueTime API) | Multi-region financeiro |

## Quando Usar / Quando Evitar

**CP (priorize consistência):** dados financeiros, inventário com constraint de stock, sistemas de voto, leader election, config distribuída.

**AP (priorize disponibilidade):** DNS, CDN, analytics, feeds de redes sociais, sistemas de recomendação, contadores aproximados.

**Eventual Consistency com cuidado:** use idempotência em operações e deduplicação em consumers para lidar com leituras desatualizadas sem bugs.

**Evitar confundir CAP com ACID:** ACID é sobre transações em um banco. CAP é sobre nós distribuídos. PostgreSQL pode ser ACID E CP ao mesmo tempo.

## Conceitos Relacionados

[[db-sharding]] · [[redis-avancado]] · [[dynamodb]] · [[kafka]] · [[distributed-locks]] · [[sre-sli-slo-sla]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-17*
