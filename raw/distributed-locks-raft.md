---
date: 2026-03-29
tags: [tech-mentor, system-design, avançado, distributed-locks, redlock, fencing, raft, consensus]
skill: tech-mentor-system-design/references/distributed-systems-core
level: arquiteto
---

# Distributed Locks, Redlock, Fencing Token e Consensus (Raft)

## Contexto

Em sistemas distribuídos, garantir que apenas um processo execute uma operação crítica ao mesmo tempo é um problema não trivial. Locks em memória só funcionam dentro de um único processo. Locks em banco de dados funcionam, mas não escalam. Redlock e fencing tokens são os padrões para exclusão mútua distribuída — mas ambos têm armadilhas sérias que um arquiteto precisa conhecer.

Raft e leader election resolvem um problema relacionado mas distinto: eleger um único nó responsável entre vários, com consenso tolerante a falhas.

---

## Por que Distributed Locks São Difíceis

O problema central: qualquer lock distribuído depende de tempo (TTL). E tempo em sistemas distribuídos é não confiável.

```
Cenário de falha clássico:

1. Processo A adquire lock, TTL = 10s
2. Processo A entra em GC pause de 12s
3. Lock expira
4. Processo B adquire o mesmo lock
5. Processo B começa a executar operação crítica
6. Processo A sai da GC pause, acredita ter o lock
7. Agora A e B executam a mesma operação simultaneamente → CORROMPIDO
```

Este não é um cenário hipotético. GC pauses longas, clock skew, e network delays criam exatamente essa situação em produção.

---

## Redis Lock Simples — SET NX

Para casos de baixo risco onde a operação protegida é idempotente ou tolerante a execução duplicada ocasional:

```typescript
async function acquireLock(key: string, ttlMs: number): Promise<string | null> {
  const token = crypto.randomUUID();
  const result = await redis.set(
    `lock:${key}`,
    token,
    "PX", ttlMs,   // TTL em ms
    "NX"           // só seta se não existir — atômico
  );
  return result === "OK" ? token : null;
}

async function releaseLock(key: string, token: string): Promise<void> {
  // Lua script: verifica owner ANTES de deletar — atômico
  // Sem isso: processo A verifica, processo B sobrescreve, A deleta lock de B
  const luaScript = `
    if redis.call("get", KEYS[1]) == ARGV[1] then
      return redis.call("del", KEYS[1])
    else
      return 0
    end
  `;
  await redis.eval(luaScript, 1, `lock:${key}`, token);
}

// Uso
const token = await acquireLock("payment:order-123", 5000);
if (!token) throw new Error("Lock não adquirido — outro processo está executando");

try {
  await processPayment("order-123");
} finally {
  await releaseLock("payment:order-123", token);
}
```

**Por que UUID como token?** Identificar o dono do lock. Na liberação, só o processo que adquiriu pode liberar — sem UUID, processo A poderia deletar o lock de processo B.

**Por que Lua script na liberação?** Atomicidade: GET + DEL em duas operações separadas cria race condition. O Lua script executa atomicamente no Redis.

---

## Redlock — Lock em Múltiplas Instâncias Redis

Redlock resolve o problema de uma única instância Redis falhar (SPOF). Em vez de um Redis, usa N instâncias **independentes** (não cluster, não réplicas).

**Algoritmo:**

```
1. Registrar tempo atual (t1)

2. Tentar adquirir lock nas N instâncias (com timeout curto por instância)
   - N=5 instâncias independentes
   - Timeout por tentativa: TTL/10 (não desperdiçar tempo em instância morta)

3. Lock adquirido SE:
   - Conseguiu em maioria: floor(N/2) + 1 = 3 de 5
   - E o tempo decorrido (t2 - t1) < TTL

4. Tempo válido do lock = TTL - (t2 - t1) - drift_clock
   Se tempo válido for muito curto → liberar e tentar de novo

5. Ao terminar (sucesso ou falha): liberar em TODAS as instâncias
   (mesmo nas que não responderam — chegam tarde mas precisam ser limpas)
```

```typescript
async function acquireRedlock(
  resource: string,
  ttlMs: number,
  instances: Redis[]
): Promise<{ token: string; validFor: number } | null> {
  const token = crypto.randomUUID();
  const start = Date.now();
  const quorum = Math.floor(instances.length / 2) + 1;

  let acquired = 0;
  for (const instance of instances) {
    try {
      const result = await instance.set(`lock:${resource}`, token, "PX", ttlMs, "NX");
      if (result === "OK") acquired++;
    } catch {
      // instância offline — continua tentando nas outras
    }
  }

  const elapsed = Date.now() - start;
  const validFor = ttlMs - elapsed - 50; // 50ms de clock drift buffer

  if (acquired >= quorum && validFor > 0) {
    return { token, validFor };
  }

  // Não conseguiu quorum — liberar onde adquiriu
  await releaseRedlock(resource, token, instances);
  return null;
}
```

### Crítica ao Redlock — Martin Kleppmann (2016)

Kleppmann demonstrou que Redlock **não é seguro** para operações que exigem correção estrita, por dois motivos:

1. **GC pause / process pause**: processo pode pausar após verificar o lock e antes de executar a operação. Lock expira, outro processo adquire. Ambos executam.

2. **Clock skew**: se o clock de uma instância Redis avançar, o TTL expira mais cedo que o esperado. O processo ainda acredita ter o lock.

**Resposta de Antirez (autor do Redis)**: Redlock é adequado para locks de "eficiência" (evitar trabalho duplicado desnecessário), não para locks de "correção" (garantir que nunca há execução dupla com efeitos irreversíveis).

**Regra prática**:
- Operação idempotente ou tolerante a retry? Redis SET NX simples é suficiente.
- Operação crítica não-idempotente (débito financeiro)? Use fencing token.

---

## Fencing Token — Proteção Correta

Fencing token resolve o problema de GC pause e clock skew adicionando um mecanismo de proteção no **recurso protegido**, não apenas no lock.

```
[Como funciona]

1. Lock service emite token MONOTONICAMENTE CRESCENTE ao conceder o lock
   → Token 33 para Processo A

2. Processo A inicia operação, entra em GC pause por 15s
3. Lock expira
4. Processo B adquire o lock → recebe token 34
5. Processo B executa operação com token=34

6. Processo A sai da GC, tenta executar com token=33
7. Recurso protegido verifica: já vi token=34, recuso token=33

→ CORRETO: Processo A é bloqueado, nenhuma corrupção
```

```typescript
// Lock service retorna token monotônico
async function acquireLockWithFencing(resource: string): Promise<{ token: number }> {
  // Redis INCR é atômico — garante monotonia
  const token = await redis.incr(`fencing:${resource}`);
  await redis.set(`lock:${resource}`, token, "EX", 30, "NX");
  return { token };
}

// Recurso protegido verifica o token antes de executar
async function executeWithFencing(
  resource: string,
  token: number,
  operation: () => Promise<void>
): Promise<void> {
  // No banco: coluna last_token por recurso
  const { lastToken } = await db.query(
    "SELECT last_fencing_token FROM resources WHERE id = $1 FOR UPDATE",
    [resource]
  );

  if (token <= lastToken) {
    throw new Error(`Token ${token} expirado — token atual é ${lastToken}`);
  }

  await db.query(
    "UPDATE resources SET last_fencing_token = $1 WHERE id = $2",
    [token, resource]
  );

  await operation();
}
```

**A garantia do fencing token**: mesmo que dois processos acreditem ter o lock ao mesmo tempo, apenas o detentor do token mais recente consegue escrever. O banco/recurso é o árbitro final.

---

## Leader Election com Raft

Raft é o algoritmo de consenso mais usado hoje (etcd, CockroachDB, Consul, TiKV). Resolve: como um cluster de N nós elege um único líder, com garantia de que não há dois líderes simultâneos, mesmo com falhas de rede e nós.

### Como Raft funciona

```
Estados de cada nó:
  Follower  → estado inicial, recebe heartbeats do líder
  Candidate → quando não recebe heartbeat por timeout, inicia eleição
  Leader    → ganhou a eleição, envia heartbeats, aceita writes

Eleição:
  1. Follower não recebe heartbeat por election timeout (150-300ms aleatório)
  2. Vira Candidate, incrementa term, vota em si mesmo
  3. Envia RequestVote para todos os outros nós
  4. Nó vota se: não votou ainda neste term E candidate está atualizado
  5. Maioria de votos → vira Leader
  6. Líder envia heartbeats → followers voltam ao estado normal

Proteção contra split-brain:
  Majority = floor(N/2) + 1
  Com 5 nós: precisa de 3 votos
  Em partição de rede: lado com 3+ nós elege líder, lado com 2 não consegue
  → Apenas um lado tem líder → sem split-brain
```

### Leader election simples com Redis (sem implementar Raft)

Para casos onde perda temporária do líder é tolerável e o nó pode reconstruir o estado:

```typescript
const LEADER_TTL = 30; // segundos
const HEARTBEAT_INTERVAL = 10_000; // ms

async function tryBecomeLeader(nodeId: string): Promise<boolean> {
  // SET NX: só seta se não existir — atômico
  const result = await redis.set("cluster:leader", nodeId, "EX", LEADER_TTL, "NX");
  return result === "OK";
}

async function renewLeadership(nodeId: string): Promise<boolean> {
  // Verifica se ainda é líder antes de renovar
  const current = await redis.get("cluster:leader");
  if (current !== nodeId) return false;

  // Lua: verifica e renova atomicamente
  const lua = `
    if redis.call("get", KEYS[1]) == ARGV[1] then
      return redis.call("expire", KEYS[1], ARGV[2])
    else
      return 0
    end
  `;
  const result = await redis.eval(lua, 1, "cluster:leader", nodeId, LEADER_TTL);
  return result === 1;
}

// Loop de liderança
async function leaderLoop(nodeId: string) {
  while (true) {
    const isLeader = await tryBecomeLeader(nodeId) || await renewLeadership(nodeId);

    if (isLeader) {
      await executeLeaderTasks(); // scheduled jobs, rebalancing, etc.
    }

    await sleep(HEARTBEAT_INTERVAL);
  }
}
```

**Limitação**: Redis SET NX não é Raft. Se o Redis falhar, todos os nós tentam se tornar líder simultaneamente. Para sistemas críticos (bancos de dados, coordenação de cluster), use etcd ou ZooKeeper.

---

## Trade-offs

| Abordagem | Garante | Quando usar |
|---|---|---|
| Redis SET NX simples | Exclusão mútua na maioria dos casos | Operações idempotentes, baixo risco |
| Redlock | Exclusão mútua com tolerância a falha de instância Redis | Locks de eficiência, não de correção |
| Fencing token | Exclusão mútua com proteção real contra GC/clock skew | Operações críticas não-idempotentes |
| etcd/ZooKeeper | Consenso distribuído com garantias formais | Leader election, coordenação de cluster |
| Raft (via etcd) | Consistência linearizável com tolerância a falhas | Infraestrutura crítica (K8s, databases) |

---

## Quando Não Usar Distributed Locks

Locks distribuídos são sintoma de um problema de design. Antes de implementar, pergunte:

**"A operação pode ser tornada idempotente?"**
Se sim, retries são seguros sem lock. Use idempotency key no banco.

**"Pode usar otimistic concurrency em vez de lock?"**
Tenta sem lock. Se conflito, detecta e re-executa. Melhor para baixa contenção.

```typescript
// Otimistic concurrency com versão
await db.query(
  "UPDATE accounts SET balance = $1, version = $2 WHERE id = $3 AND version = $4",
  [newBalance, version + 1, accountId, version]
);
// Se 0 rows afetadas → conflito → re-ler e tentar de novo
```

**"Pode usar serialização por partição (Kafka)?**
Mensagens para a mesma chave sempre vão para a mesma partição, consumidas por um único consumer. Serialização natural sem lock.

---

## Conceitos Relacionados

[[cap-pacelc-consistencia]] · [[cache]] · [[mensageria]] · [[banco-de-dados]] · [[retry-backoff]] · [[circuit-breaker]]

---

*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-29*
