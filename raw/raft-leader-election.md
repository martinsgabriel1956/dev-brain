---
date: 2026-04-14
tags: [tech-mentor, distributed-systems, consenso, raft, coordenação]
skill: tech-mentor-system-design/references/distributed-systems
level: avançado
---

# Raft e Leader Election

## Contexto

Em sistemas distribuídos, múltiplos nós precisam concordar sobre quem é o líder, qual é o valor correto de um dado, ou em qual ordem as operações ocorreram. Isso é o **problema de consenso distribuído**.

Paxos foi o algoritmo original (Lamport, 1989), mas é notoriamente difícil de entender e implementar. Raft (Ongaro & Ousterhout, 2014) foi projetado especificamente para ser compreensível — e é o algoritmo por trás do etcd, CockroachDB e HashiCorp Consul.

## Como Funciona

### Os Três Papéis

Todo nó em um cluster Raft está em um de três estados:

```
Follower  → estado inicial, ouve o líder
Candidate → candidato a líder, solicita votos
Leader    → recebe escritas, replica para followers
```

### Eleição de Líder

```
1. Todos os nós começam como Followers
2. Cada Follower tem um "election timeout" aleatório (150-300ms)
3. Se não recebe heartbeat do líder antes do timeout → vira Candidate
4. Candidate incrementa seu "term" (mandato), vota em si mesmo, pede votos
5. Se recebe maioria (N/2 + 1) → vira Leader
6. Leader envia heartbeats periódicos para suprimir novas eleições
```

O **election timeout aleatório** é o truque que evita split votes: é improvável que dois nós expirem exatamente ao mesmo tempo.

```
Cluster de 5 nós (maioria = 3):

t=0ms:   [F:A, F:B, F:C, F:D, F:E]  ← todos Followers, sem líder

t=150ms: Nó A timeout primeiro
         A vira Candidate, term=1, vota em si mesmo
         A envia RequestVote para B, C, D, E

t=151ms: B e C respondem "sim" (term=1 é novo, não votaram ainda)
         A recebe 3 votos (si mesmo + B + C) = maioria
         A vira Leader para term=1

t=152ms: A começa a enviar heartbeats para B, C, D, E
         D e E recebem heartbeat antes de fazer timeout → ficam como Followers
```

### Replicação de Log

O leader não apenas coordena eleições — ele também garante que todas as operações sejam replicadas de forma consistente antes de confirmar para o cliente.

```
Cliente → Leader: "SET x = 5"

1. Leader adiciona a entrada no seu log (index=42, term=1, SET x=5)
2. Leader envia AppendEntries para todos os Followers
3. Followers adicionam ao seu log e respondem "OK"
4. Quando maioria confirmou: entrada é "committed"
5. Leader aplica ao state machine, responde ao cliente "OK"
6. Próximo heartbeat notifica Followers que a entrada foi committed
7. Followers aplicam ao state machine

Se algum Follower cai e volta: Leader envia as entradas que faltam
→ logs sempre convergem para o do Leader
```

```
Leader log:  [1:SET x=1, 1:SET y=2, 1:SET x=5]  ← committed
Follower B:  [1:SET x=1, 1:SET y=2]              ← atrasado, será sincronizado
Follower C:  [1:SET x=1, 1:SET y=2, 1:SET x=5]  ← atualizado
```

### Safety — Por que Raft é Seguro

**Garantia de eleição:** um candidato só vence se seu log estiver tão atualizado quanto a maioria dos nós. Isso garante que nenhuma entrada committed seja perdida em uma eleição.

**Um líder por term:** dois nós não podem ser líderes no mesmo term simultaneamente — cada nó vota apenas uma vez por term.

**Commit em maioria:** uma entrada só é committed quando replicada em N/2+1 nós. Se o cluster tolera F falhas, precisa de 2F+1 nós (para ter maioria mesmo com F falhados).

```
Tolerância a falhas:
  3 nós  → tolera 1 falha  (maioria = 2)
  5 nós  → tolera 2 falhas (maioria = 3)
  7 nós  → tolera 3 falhas (maioria = 4)
```

### Raft na Prática — etcd

```bash
# Kubernetes usa etcd para armazenar todo o estado do cluster
# etcd usa Raft internamente

# Ver status do cluster etcd
etcdctl endpoint status --cluster -w table

# Ver líder atual
etcdctl endpoint status | grep -i leader

# Simular falha de um nó e observar re-eleição
# (o cluster continua funcionando enquanto maioria está viva)
```

### Snap e Log Compaction

O log Raft cresce indefinidamente. Snapshots compactam o log periodicamente: o state machine é serializado e as entradas antigas são descartadas.

```
Antes do snapshot:
Log: [SET x=1, SET x=2, SET x=3, SET y=10, DEL y]
State: {x: 3}

Após snapshot no index 5:
Snapshot: {x: 3} (representa o estado após aplicar entradas 1-5)
Log: [] (entradas 1-5 descartadas)

Novo Follower pode receber o snapshot em vez de replay completo do log
```

## Trade-offs

| Aspecto | Raft | Paxos |
|---|---|---|
| **Compreensibilidade** | Alta — projetado para ser legível | Baixa — notoriamente difícil |
| **Implementações** | etcd, CockroachDB, TiKV, Consul | Chubby (Google), Zookeeper (ZAB, similar) |
| **Performance** | Boa para clusters pequenos (3-7 nós) | Comparável |
| **Leader único** | Single leader — pode ser bottleneck de escrita | Multi-Paxos similar |
| **Eleição** | Rápida com random timeouts | Mais complexa |

## Quando Usar / Quando Evitar

**Não implementar Raft diretamente** — use uma biblioteca ou sistema que já o implementa:
- **etcd:** coordenação de configuração e leader election em K8s e serviços distribuídos
- **CockroachDB / TiKV:** banco de dados distribuído com Raft por shard
- **HashiCorp Consul:** service discovery e distributed locks com Raft

**Entender Raft é fundamental para:**
- Diagnosticar problemas de split-brain em clusters etcd/CockroachDB
- Dimensionar corretamente o número de nós (sempre ímpar)
- Entender por que quorum-based writes têm latência maior que writes para um único nó
- Projetar sistemas que dependem de coordenação distribuída

## Conceitos Relacionados

[[distributed-locks]] · [[cap-pacelc-consistencia]] · [[consistent-hashing]] · [[db-sharding]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-14*
