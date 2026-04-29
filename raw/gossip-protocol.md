---
date: 2026-04-14
tags: [tech-mentor, distributed-systems, protocolos, coordenação, escalabilidade]
skill: tech-mentor-system-design/references/distributed-systems
level: avançado
---

# Gossip Protocol

## Contexto

Gossip Protocol (também chamado de Epidemic Protocol) é um mecanismo de propagação de informação em sistemas distribuídos inspirado na forma como rumores se espalham numa rede social: cada nó periodicamente seleciona vizinhos aleatórios e troca informações com eles. Com isso, a informação se propaga exponencialmente pelo cluster.

Usado em Cassandra, DynamoDB, Redis Cluster, Consul e outros sistemas para membership (quais nós estão vivos), estado e configuração — sem precisar de um nó central de coordenação.

## Como Funciona

### O Algoritmo Básico

```
A cada ciclo (tipicamente a cada 1 segundo):
  1. Nó atual seleciona aleatoriamente K nós do cluster (K = fanout)
  2. Troca informações com eles (quem está vivo, versão de estado)
  3. Receptor atualiza sua visão do cluster e propaga adiante no próximo ciclo
```

```typescript
type NodeState = {
  nodeId: string;
  version: number;   // incrementa a cada mudança local
  data: Record<string, unknown>;
  lastSeen: Date;
};

class GossipNode {
  private state: Map<string, NodeState> = new Map();
  private readonly fanout = 3; // fala com 3 nós por ciclo

  // Inicia gossip periódico
  startGossip(peers: string[]) {
    setInterval(() => this.gossipCycle(peers), 1000);
  }

  private async gossipCycle(allPeers: string[]) {
    // Seleciona peers aleatórios
    const selectedPeers = this.selectRandom(allPeers, this.fanout);

    for (const peer of selectedPeers) {
      try {
        // Envia meu estado, recebe o estado do peer
        const peerState = await this.exchangeState(peer, this.state);
        this.mergeState(peerState);
      } catch {
        // Peer pode estar down — marcar como suspeito após N falhas consecutivas
        this.markSuspect(peer);
      }
    }
  }

  private mergeState(incoming: Map<string, NodeState>) {
    for (const [nodeId, incomingNodeState] of incoming) {
      const localState = this.state.get(nodeId);

      // Aceita informação mais recente (maior version)
      if (!localState || incomingNodeState.version > localState.version) {
        this.state.set(nodeId, incomingNodeState);
      }
    }
  }

  private selectRandom<T>(arr: T[], k: number): T[] {
    return arr.sort(() => Math.random() - 0.5).slice(0, k);
  }
}
```

### Convergência — Quão Rápido a Informação Chega a Todos?

Com N nós e fanout K, a informação chega a todos os nós em aproximadamente `log(N) / log(K)` ciclos.

```
100 nós, fanout = 3, ciclo = 1 segundo:
  Ciclo 1: 1 nó sabe → 3 sabem
  Ciclo 2: 3 sabem → ~9 sabem
  Ciclo 3: ~9 sabem → ~27 sabem
  Ciclo 4: ~27 sabem → todos sabem
  → ~4 segundos para convergência total

1.000 nós:
  log(1000) / log(3) ≈ 6.3 ciclos → ~7 segundos

10.000 nós:
  log(10000) / log(3) ≈ 8.4 ciclos → ~9 segundos
  → Gossip escala logaritmicamente!
```

### SWIM — Membership com Detecção de Falhas

O protocolo SWIM (Scalable Weakly-consistent Infection-style Membership) combina Gossip com detecção de falhas mais precisa:

```
Problema do heartbeat simples: se A não consegue pingar B, B está morto?
  → Pode ser uma falha de rede apenas entre A e B (falso positivo)

SWIM resolve com indirect probing:
  1. A tenta pingar B diretamente → timeout
  2. A pede para C, D, E pingarem B indiretamente
  3. Se nenhum consegue → B é declarado suspeito
  4. Após timeout de suspeito sem resposta → B é removido do cluster
```

### Anti-Entropy com Merkle Trees

Para sincronizar dados (não apenas membership), Gossip usa Merkle Trees para detectar eficientemente quais partes do dataset divergem:

```
Nó A e Nó B precisam sincronizar dados:

1. Ambos constroem Merkle Tree dos seus dados
2. Trocam o hash raiz via Gossip
3. Se hash raiz igual → dados iguais, nada a fazer
4. Se hash diferente → descem na árvore para encontrar quais folhas divergem
5. Sincronizam apenas os dados das folhas divergentes

→ Em vez de comparar todos os dados, apenas comparamos hashes
→ Custo: O(log N) comparações para N chaves
```

### Gossip na Prática — Cassandra

```
Cada nó Cassandra faz gossip a cada segundo com até 3 peers:
  - Troca EndpointState: schema version, ring tokens, datacenter
  - Usa HeartBeat com geração + versão (incrementa a cada mudança)
  - SWIM para detectar nós mortos

Resultado: qualquer mudança no cluster (novo nó, nó morto, schema change)
chega a todos os nós em segundos, sem coordenador central
```

## Trade-offs

| Aspecto | Gossip | Coordenação Centralizada (Zookeeper/etcd) |
|---|---|---|
| **Escalabilidade** | Alta — O(log N) | Moderada — coordenador é bottleneck |
| **Consistência** | Eventual — convergência em segundos | Forte — Raft/ZAB |
| **Disponibilidade** | Alta — sem SPOF | Menor — coordenador pode ser SPOF |
| **Latência de propagação** | Segundos | Milissegundos |
| **Complexidade** | Moderada | Alta (operação do cluster de coordenadores) |
| **Uso** | Membership, anti-entropy, estado difuso | Locks, leader election, configuração crítica |

## Quando Usar / Quando Evitar

**Gossip é ideal para:**
- Membership: descobrir quais nós estão vivos no cluster
- Propagação de configuração que tolera latência de segundos
- Sistemas com dezenas a milhares de nós onde coordenação central seria bottleneck
- Anti-entropy em databases distribuídas (Cassandra, DynamoDB)

**Não usar Gossip para:**
- Operações que precisam de consistência forte (locks, transações) → use Raft/etcd
- Dados que não podem ser eventualmente consistentes (saldo financeiro)
- Clusters muito pequenos (< 5 nós) — overhead não compensa

## Conceitos Relacionados

[[raft-leader-election]] · [[cap-pacelc-consistencia]] · [[consistent-hashing]] · [[db-sharding]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-14*
