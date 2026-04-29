---
date: 2026-04-17
tags: [tech-mentor, sistemas-distribuidos, consistencia, causalidade]
skill: tech-mentor-system-design/references/distributed-systems
level: avançado
---

# Vector Clocks

## Contexto
Em sistemas distribuídos, não existe um relógio global confiável. Um timestamp de wall clock não é suficiente para determinar se o evento A causou o evento B — pode haver drift de NTP, skew entre nodes, etc.

**Vector Clocks** (Lamport, 1978; extendido por Fidge/Mattern) resolvem o problema de **causalidade**: dado dois eventos, é possível determinar se um aconteceu-antes-do-outro (*happened-before* ≺) ou se são concorrentes.

Usados em: DynamoDB, Riak, Amazon S3 (conditional writes), sistemas de CRDT.

## Como Funciona

Cada nó mantém um vetor de contadores — um por nó no sistema.

```
Nó A: [A:0, B:0, C:0]
Nó B: [A:0, B:0, C:0]
Nó C: [A:0, B:0, C:0]
```

**Regras:**
1. Ao realizar um evento local: incrementa seu próprio contador
2. Ao enviar uma mensagem: inclui o vetor atual
3. Ao receber uma mensagem: para cada posição, toma o `max(local, recebido)`, depois incrementa o próprio contador

```
Nó A envia msg para B:
  A incrementa: [A:1, B:0, C:0] → envia para B

Nó B recebe:
  B faz max([A:0, B:0, C:0], [A:1, B:0, C:0]) = [A:1, B:0, C:0]
  B incrementa próprio: [A:1, B:1, C:0]

Nó B envia msg para C:
  C recebe [A:1, B:1, C:0]
  C faz max + incrementa: [A:1, B:1, C:1]
```

## Determinando Causalidade

Dados dois vetores V1 e V2:
- **V1 ≺ V2** (V1 happened-before V2): V1[i] ≤ V2[i] para todo i, e V1[j] < V2[j] para algum j
- **V1 = V2**: idênticos
- **Concorrentes**: nem V1 ≺ V2 nem V2 ≺ V1 → **conflito**

```typescript
type VectorClock = Map<string, number>;

function happenedBefore(v1: VectorClock, v2: VectorClock): boolean {
  const allNodes = new Set([...v1.keys(), ...v2.keys()]);
  let strictlyLess = false;

  for (const node of allNodes) {
    const t1 = v1.get(node) ?? 0;
    const t2 = v2.get(node) ?? 0;
    if (t1 > t2) return false;   // v1 tem evento que v2 não viu → não é before
    if (t1 < t2) strictlyLess = true;
  }

  return strictlyLess; // pelo menos um componente é estritamente menor
}

function isConcurrent(v1: VectorClock, v2: VectorClock): boolean {
  return !happenedBefore(v1, v2) && !happenedBefore(v2, v1);
}

function merge(v1: VectorClock, v2: VectorClock): VectorClock {
  const result = new Map<string, number>();
  const allNodes = new Set([...v1.keys(), ...v2.keys()]);
  for (const node of allNodes) {
    result.set(node, Math.max(v1.get(node) ?? 0, v2.get(node) ?? 0));
  }
  return result;
}
```

## Resolução de Conflitos

Quando dois eventos são **concorrentes**, precisam ser resolvidos:
- **Last-Write-Wins (LWW):** descarta o mais antigo — simples mas perde dados
- **Merge automático:** CRDT resolve matematicamente (ex: G-Counter soma tudo)
- **Apresentar conflito ao usuário:** DynamoDB com versioning retorna ambas as versões

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Precisão | Causalidade exata, sem falsos positivos | Vetor cresce O(N nós) — em sistemas com muitos nós, overhead grande |
| Concorrência | Identifica conflitos reais vs. ordenação falsa | Implementação e debugging complexos |
| Disponibilidade | Funciona sem coordenação central | Resolução de conflito ainda é problema de domínio |

## Quando Usar / Quando Evitar

**Usar quando:**
- Sistemas com múltiplos writers sem coordenador central (multi-master replication)
- Implementando CRDTs ou sistemas de colaboração em tempo real
- Precisa detectar conflitos de escrita sem sacrificar disponibilidade

**Evitar quando:**
- O sistema tem um único writer ou coordenador central — um sequence number é suficiente
- Número de nós é grande e variável — o vetor ficaria enorme

## Conceitos Relacionados
[[modelos-de-consistencia]] · [[cap-theorem]] · [[quorum]] · [[raft-leader-election]] · [[crdt-colaboracao-tempo-real]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-17*
