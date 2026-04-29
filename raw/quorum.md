---
date: 2026-04-16
tags: [tech-mentor, distributed-systems, quorum, dynamo, replicacao]
skill: tech-mentor-system-design/references/distributed-systems
level: avançado
---

# Quorum — Leitura, Escrita e o Modelo Dynamo

## Contexto

Quorum é o mecanismo que permite sistemas distribuídos balancear consistência e disponibilidade na replicação. Em vez de exigir que *todos* os nós confirmem uma operação (forte mas lento) ou apenas *um* (rápido mas inconsistente), quorum permite configurar o mínimo de nós que devem participar para garantir que leituras e escritas sejam consistentes entre si.

Usado no modelo original do DynamoDB (paper da Amazon, 2007), Cassandra, Riak e qualquer sistema que suporte replicação configurável.

## Como Funciona

### A Fórmula Fundamental

Dado `N` = número de réplicas, `W` = write quorum (mínimo de confirmações de escrita), `R` = read quorum (mínimo de nós a consultar na leitura):

```
Para leitura consistente (strong read): R + W > N
Para escrita durável:                   W > N/2
```

**Por quê `R + W > N` garante consistência?**

```
N=3, W=2, R=2:
  Escrita confirma em nós {A, B}       → nó C pode estar stale
  Leitura consulta    {A, C} ou {B, C} → ao menos 1 nó tem dado recente (A ou B)
  R + W = 4 > N=3: overlap garantido → ao menos 1 nó na leitura tem dado novo
```

### Configurações Comuns

```
N=3 → fault tolerance de 1 nó (maioria = 2)

| W | R | Característica |
|---|---|----------------|
| 3 | 1 | Escrita lenta, leitura rápida. Qualquer réplica pode servir leitura |
| 1 | 3 | Escrita rápida, leitura lenta (full scan) |
| 2 | 2 | Balanceado — R+W=4>3, consistente. Padrão Cassandra LOCAL_QUORUM |
| 1 | 1 | Eventual consistency — sem garantia de sobreposição |
```

### Implementação no Modelo Dynamo

O DynamoDB original usa consistent hashing + quorum + vector clocks para resolver conflitos:

```
Escrita (W=2, N=3):
  Coordinator escolhe 3 nós no anel
  Envia escrita para os 3
  Aguarda confirmação de 2 (W)
  Retorna sucesso ao cliente
  Terceiro nó atualiza em background (eventual)

Leitura (R=2, N=3):
  Coordinator consulta os 3 nós
  Aguarda resposta de 2 (R)
  Compara versões via vector clock
  Retorna a mais recente (ou lista para resolução pelo cliente)
```

```typescript
class DynamoStyleStore<T> {
  private replicas: ReplicaNode<T>[];
  private readonly N: number;
  private readonly W: number;
  private readonly R: number;

  constructor(replicas: ReplicaNode<T>[], { n = 3, w = 2, r = 2 } = {}) {
    this.replicas = replicas;
    this.N = n;
    this.W = w;
    this.R = r;
  }

  async write(key: string, value: T): Promise<void> {
    const targetReplicas = this.selectReplicas(key, this.N);
    const results = await Promise.allSettled(
      targetReplicas.map(replica => replica.put(key, value))
    );

    const successes = results.filter(r => r.status === "fulfilled").length;
    if (successes < this.W) {
      throw new Error(`Write quorum not met: ${successes}/${this.W} replicas confirmed`);
    }
    // As demais réplicas completam em background (hinted handoff)
  }

  async read(key: string): Promise<T> {
    const targetReplicas = this.selectReplicas(key, this.N);
    const results = await Promise.allSettled(
      targetReplicas.map(replica => replica.get(key))
    );

    const successful = results
      .filter((r): r is PromiseFulfilledResult<VersionedValue<T>> => r.status === "fulfilled")
      .map(r => r.value);

    if (successful.length < this.R) {
      throw new Error(`Read quorum not met: ${successful.length}/${this.R} replicas responded`);
    }

    // Retorna o valor com maior vector clock (mais recente)
    return this.resolveConflict(successful);
  }

  private resolveConflict(versions: VersionedValue<T>[]): T {
    // Last-Write-Wins pela timestamp — Dynamo usa vector clocks
    return versions.sort((a, b) => b.timestamp - a.timestamp)[0].value;
  }

  private selectReplicas(key: string, count: number): ReplicaNode<T>[] {
    // Consistent hashing — aqui simplificado
    const start = this.hashKey(key) % this.replicas.length;
    return [...this.replicas.slice(start), ...this.replicas.slice(0, start)].slice(0, count);
  }

  private hashKey(key: string): number {
    return key.split("").reduce((acc, char) => acc + char.charCodeAt(0), 0);
  }
}
```

### Cassandra — Consistency Levels

Cassandra expõe o modelo de quorum diretamente na API de query:

```typescript
import { Client, types } from "cassandra-driver";

const client = new Client({
  contactPoints: ["cassandra-1", "cassandra-2", "cassandra-3"],
  localDataCenter: "datacenter1"
});

// LOCAL_QUORUM: quorum dentro do datacenter local (W=2, R=2 para N=3)
// Garante R+W>N sem atravessar datacenters (menor latência)
await client.execute(
  "INSERT INTO orders (id, status, total) VALUES (?, ?, ?)",
  [orderId, "pending", 99.90],
  { consistency: types.consistencies.localQuorum }
);

// Leitura com LOCAL_QUORUM — ao menos 2 réplicas devem concordar
const result = await client.execute(
  "SELECT * FROM orders WHERE id = ?",
  [orderId],
  { consistency: types.consistencies.localQuorum }
);

// ALL — todas as 3 réplicas (máxima consistência, menor disponibilidade)
// ONE — qualquer réplica (máxima disponibilidade, eventual consistency)
// QUORUM — maioria absoluta (N/2 + 1)
```

### Sloppy Quorum e Hinted Handoff

Quando os nós alvo estão indisponíveis, Dynamo usa **sloppy quorum**: aceita confirmações de nós substitutos temporários, armazenando os dados com "hint" de que pertencem a outro nó.

```
Nó B está down:
  Escrita {A, B, C} → aceita {A, C, D} (D é substituto com hint)
  Quando B volta: D repassa os dados com hint para B (hinted handoff)
  → W=2 é mantido mesmo com nó down → alta disponibilidade
```

**Trade-off:** consistência é sacrificada temporariamente. Se ler antes de B voltar, pode obter dado stale.

## Trade-offs

| Aspecto | W+R alto (ex: W=3, R=3) | W+R baixo (ex: W=1, R=1) |
|---|---|---|
| **Consistência** | Forte — overlap garantido | Eventual — sem overlap |
| **Disponibilidade** | Baixa — precisa de mais nós saudáveis | Alta — qualquer nó serve |
| **Latência** | Alta — espera mais nós responderem | Baixa — primeira resposta |
| **Throughput de escrita** | Baixo | Alto |
| **Tolerância a falha** | Limitada | Alta (sloppy quorum) |

## Quando Usar / Quando Evitar

**Quorum forte (R+W>N):**
- Inventário (sem oversell)
- Dados financeiros onde stale causa perda
- Qualquer operação onde "ler o que acabou de escrever" é obrigatório

**Quorum fraco / eventual:**
- Feeds e timelines
- Contadores aproximados (views, likes)
- Cache distribuído
- Dados de sessão onde staleness por milissegundos é aceitável

**Armadilha:** `W=1, R=1` com `N=3` significa que escreve em 1 nó e lê de qualquer 1 — há 2/3 de chance de ler dado stale.

## Conceitos Relacionados

[[modelos-de-consistencia]] · [[consistent-hashing]] · [[gossip-protocol]] · [[raft-leader-election]] · [[cap-pacelc-consistencia]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-16*
