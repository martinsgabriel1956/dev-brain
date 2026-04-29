---
date: 2026-04-16
tags: [tech-mentor, distributed-systems, consistencia, linearizability, eventual-consistency]
skill: tech-mentor-system-design/references/distributed-systems
level: avançado
---

# Modelos de Consistência

## Contexto

Em sistemas distribuídos, "consistência" não é binária — é um espectro. Cada modelo define o que um cliente pode *observar* após uma escrita, e qual a ordenação garantida entre operações concorrentes. Escolher o modelo errado causa bugs sutis (stale reads em contextos críticos) ou mata performance desnecessariamente (serializable onde eventual bastaria).

O teorema CAP diz que, sob partição de rede, você escolhe entre Consistency e Availability. Os modelos de consistência definem *o que* você garante quando escolhe "C".

## Os Modelos — Do Mais Forte ao Mais Fraco

### 1. Linearizability (Strict Consistency)

Toda operação parece ocorrer atomicamente num ponto entre o início e o fim da chamada. Uma vez que uma escrita é confirmada, qualquer leitura subsequente (em qualquer nó) a vê.

```
Timeline:
  Client A: write(x=1)  ─────[ok]
  Client B:                        read(x) → 1  ✅ garantido
  Client C:                    read(x) → 1  ✅ garantido (mesmo concurrent)
```

**Implementação:** requer coordenação via Raft/Paxos. Cada escrita passa pelo líder antes de confirmar.

```typescript
// etcd — leitura linearizável por padrão
import { Etcd3 } from "etcd3";

const client = new Etcd3();

// Escrita confirmada somente após quorum do Raft
await client.put("config/feature-flag").value("enabled");

// Leitura linearizável — vai ao líder, não a réplica
const value = await client.get("config/feature-flag").string();
```

**Usado em:** etcd, Zookeeper, CockroachDB (modo serializable), locks distribuídos, leader election.

**Custo:** alta latência (round-trip ao líder), baixa disponibilidade sob partição.

---

### 2. Sequential Consistency

Todas as operações aparecem em alguma ordem global — mas essa ordem não precisa respeitar o tempo real do relógio. Todos os processos veem a mesma sequência de operações.

```
Thread A: write(x=1), write(y=2)
Thread B: write(x=3)

Sequential: ambos podem ver [x=1, y=2, x=3] ou [x=3, x=1, y=2]
            mas NUNCA [x=3, y=2, x=1] (viola ordem de A)
```

**Diferença do linearizable:** não garante que a ordem reflita o tempo de relógio real — só garante consistência interna por processo.

**Usado em:** modelos de memória de CPUs (com barreiras), alguns sistemas de cache.

---

### 3. Causal Consistency

Operações que têm relação de causa-e-efeito são vistas na ordem correta por todos os nós. Operações sem relação causal podem ser vistas em ordens diferentes.

```
Alice: post("Oi") → reply("Olá, Alice!")
Bob vê: post antes de reply  ✅
Carol vê: post antes de reply ✅

Mas operações de Dave (sem relação com Alice):
  Dave: write(x=1)
  Bob pode ver x=1 antes que Carol — ok, sem causalidade
```

**Implementação:** Vector Clocks rastreiam dependências causais.

```typescript
type VectorClock = Record<string, number>;

function happensBefore(a: VectorClock, b: VectorClock): boolean {
  const aNodes = Object.keys(a);
  // a happens-before b se todo counter de a <= b e ao menos um <
  return aNodes.every(node => (a[node] ?? 0) <= (b[node] ?? 0)) &&
    aNodes.some(node => (a[node] ?? 0) < (b[node] ?? 0));
}
```

**Usado em:** DynamoDB (com conditional writes), MongoDB causal sessions, sistemas de colaboração em tempo real.

---

### 4. Eventual Consistency

Se nenhuma nova escrita ocorrer, eventualmente todos os nós convergem para o mesmo valor. Sem garantia de quando, sem garantia de ordem para leituras intermediárias.

```
Escrita em Node A: x = 1
  t=0: Node A vê x=1, Node B vê x=0  (stale)
  t=1: Node A vê x=1, Node B vê x=1  (convergido)
```

**Submodelos importantes:**
- **Monotonic Read:** uma vez lido um valor, nunca se lê um mais antigo
- **Read Your Writes:** você sempre vê suas próprias escritas
- **Monotonic Write:** suas escritas são aplicadas na ordem que você enviou

```typescript
// DynamoDB — eventual consistency por padrão (mais barato)
const result = await dynamodb.getItem({
  TableName: "orders",
  Key: { id: { S: orderId } },
  ConsistentRead: false  // eventual — pode ser stale
}).promise();

// Strong consistency — vai à réplica primária
const result = await dynamodb.getItem({
  TableName: "orders",
  Key: { id: { S: orderId } },
  ConsistentRead: true  // linearizável, 2x o custo de leitura
}).promise();
```

**Usado em:** Cassandra (padrão), DynamoDB (padrão), DNS, caches, feeds de redes sociais.

---

### Comparação Prática

| Modelo | Garantia | Latência | Disponibilidade | Exemplo |
|---|---|---|---|---|
| **Linearizable** | Leitura sempre vê última escrita | Alta | Baixa sob partição | etcd, Zookeeper |
| **Sequential** | Mesma ordem global para todos | Média | Média | Memória de CPU |
| **Causal** | Causa antes do efeito | Baixa | Alta | DynamoDB sessions, MongoDB |
| **Eventual** | Convergência eventual | Muito baixa | Muito alta | Cassandra, DynamoDB padrão |

### Read Your Writes — O Caso Mais Comum

O problema mais frequente em produção: usuário escreve dado e imediatamente lê — mas lê de réplica ainda desatualizada.

```typescript
// Solução 1: sessão sticky (mesma réplica)
// Solução 2: ler do primário por N segundos após escrita
// Solução 3: timestamp de escrita no cliente

async function createUserAndRead(data: UserData): Promise<User> {
  const user = await primaryDb.user.create({ data });

  // Leitura imediata — forçar primary para garantir read-your-writes
  return primaryDb.user.findUniqueOrThrow({ where: { id: user.id } });
}

// Após N segundos, leituras podem ir para réplicas
```

## Trade-offs

| Aspecto | Forte (Linearizable) | Fraca (Eventual) |
|---|---|---|
| **Latência de leitura** | Alta — vai ao primário | Baixa — qualquer réplica |
| **Throughput** | Limitado pelo líder | Escala horizontalmente |
| **Complexidade** | Simples para o dev | Requer tratar inconsistências |
| **Disponibilidade** | Cai com o primário | Alta — any node serve |
| **Casos de uso** | Locks, saldos, inventário | Feeds, timelines, cache |

## Quando Usar / Quando Evitar

**Linearizability:** locks distribuídos, transações financeiras, inventário com oversell proibido, leader election.

**Causal:** sistemas de comentários/replies, collaborative editing, sessões de usuário onde "read my writes" importa.

**Eventual:** feeds sociais, analytics, caches, qualquer dado onde stale temporário é aceitável, sistemas com escrita intensiva.

**Armadilha comum:** usar eventual consistency para inventário de e-commerce → overselling. Usar linearizable para contagem de views de vídeo → gargalo desnecessário.

## Conceitos Relacionados

[[raft-leader-election]] · [[cap-pacelc-consistencia]] · [[gossip-protocol]] · [[quorum]] · [[cqrs]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-16*
