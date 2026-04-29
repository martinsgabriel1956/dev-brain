---
date: 2026-04-14
tags: [tech-mentor, distributed-systems, escala, sharding, cache]
skill: tech-mentor-system-design/references/distributed-systems
level: avançado
---

# Consistent Hashing

## Contexto

Quando você distribui dados entre N servidores usando `hash(key) % N`, adicionar ou remover um servidor invalida quase todas as chaves — o módulo muda e `hash(key) % (N+1)` aponta para servidores completamente diferentes. Para caches distribuídos, isso significa um cache miss massivo. Para shards de banco, significa migrar quase todos os dados.

Consistent Hashing resolve isso fazendo com que a adição/remoção de um nó impacte apenas `K/N` chaves, onde K é o número total de chaves e N é o número de nós.

## Como Funciona

### O Ring

Imagine um círculo (ring) de 0 a 2³² - 1. Cada nó é mapeado para uma posição no ring via hash. Cada chave também é mapeada via hash, e é atribuída ao **primeiro nó no sentido horário** a partir de sua posição.

```
           0
          / \
  Node C /   \ Node A
(hash=350)   (hash=100)
        \   /
         \ /
      Node B
      (hash=200)

key "user:123" → hash=150 → Node B (próximo no sentido horário)
key "order:456" → hash=80  → Node A (próximo no sentido horário)
key "product:789" → hash=300 → Node C (próximo no sentido horário)
```

### Adição/Remoção de Nó

Quando um nó é adicionado entre dois nós existentes, apenas as chaves que ficam entre ele e seu predecessor precisam ser remapeadas — tipicamente `K/N` chaves.

```typescript
class ConsistentHashRing {
  private ring: Map<number, string> = new Map();
  private sortedHashes: number[] = [];
  private readonly virtualNodes: number;

  constructor(virtualNodes = 150) {
    this.virtualNodes = virtualNodes;
  }

  private hash(key: string): number {
    // Simplified — em prod use MurmurHash ou SHA-1
    let h = 0;
    for (let i = 0; i < key.length; i++) {
      h = (Math.imul(31, h) + key.charCodeAt(i)) | 0;
    }
    return Math.abs(h);
  }

  addNode(nodeId: string) {
    // Virtual nodes: cada nó físico tem múltiplas posições no ring
    // Sem virtual nodes, a distribuição fica desequilibrada
    for (let i = 0; i < this.virtualNodes; i++) {
      const virtualKey = `${nodeId}:vnode:${i}`;
      const position = this.hash(virtualKey);
      this.ring.set(position, nodeId);
      this.sortedHashes.push(position);
    }
    this.sortedHashes.sort((a, b) => a - b);
  }

  removeNode(nodeId: string) {
    for (let i = 0; i < this.virtualNodes; i++) {
      const virtualKey = `${nodeId}:vnode:${i}`;
      const position = this.hash(virtualKey);
      this.ring.delete(position);
    }
    this.sortedHashes = this.sortedHashes.filter(h => this.ring.has(h));
  }

  getNode(key: string): string {
    if (this.ring.size === 0) throw new Error("Ring is empty");

    const keyHash = this.hash(key);

    // Encontra o primeiro nó no sentido horário (binary search)
    let idx = this.sortedHashes.findIndex(h => h >= keyHash);
    if (idx === -1) idx = 0; // wrap around

    return this.ring.get(this.sortedHashes[idx])!;
  }
}

// Uso
const ring = new ConsistentHashRing(150);
ring.addNode("cache-1");
ring.addNode("cache-2");
ring.addNode("cache-3");

const node = ring.getNode("user:123"); // sempre o mesmo node para essa key
```

### Virtual Nodes

Sem virtual nodes, a distribuição de chaves entre nós físicos é desigual — alguns nós recebem muito mais carga que outros. Virtual nodes resolvem isso: cada nó físico aparece múltiplas vezes no ring com posições diferentes.

```
Sem virtual nodes (desequilibrado):
Node A: 33% das chaves
Node B: 12% das chaves  ← menos sorte no hash
Node C: 55% das chaves  ← mais sorte no hash

Com 150 virtual nodes por nó físico (equilibrado):
Node A: ~33% das chaves
Node B: ~33% das chaves
Node C: ~33% das chaves
```

### Onde é Usado na Prática

**Redis Cluster:** usa consistent hashing com 16384 hash slots distribuídos entre os nós.

```
# Redis Cluster divide em 16384 slots
# CLUSTER KEYSLOT calcula o slot de uma chave
# CRC16(key) % 16384

# Hash tags: {user}.session e {user}.data vão para o mesmo slot
CLUSTER KEYSLOT "{user:123}.session"  # → mesmo slot que
CLUSTER KEYSLOT "{user:123}.profile"
```

**Cassandra:** usa consistent hashing para distribuir partições entre nós com fator de replicação configurável.

**CDN e Load Balancers:** sticky sessions baseadas em consistent hashing garantem que requests do mesmo IP ou sessão vão para o mesmo servidor.

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| **Resharding** | Apenas K/N chaves movidas ao adicionar/remover nó | Implementação mais complexa que modulo simples |
| **Distribuição** | Equilibrada com virtual nodes | Sem virtual nodes, altamente desequilibrado |
| **Cache warming** | Impacto mínimo no cache ao escalar | Período transitório de cache miss durante resharding |
| **Hot keys** | — | Chaves muito acessadas concentram carga em um nó — use replication |

## Quando Usar / Quando Evitar

**Usar quando:**
- Cache distribuído com adição/remoção dinâmica de nós (Redis Cluster, Memcached)
- Sharding de dados onde resharding frequente deve ser minimizado
- Load balancing com sticky sessions

**Evitar quando:**
- Dataset estático com número fixo de shards → hash + modulo é mais simples
- Precisar de range queries → consistent hashing não preserva ordem; use range-based sharding
- Sistema pequeno com 2-3 shards → a complexidade não compensa

## Conceitos Relacionados

[[db-sharding]] · [[cache]] · [[rate-limiting]] · [[distributed-locks]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-14*
