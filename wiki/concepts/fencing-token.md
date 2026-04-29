---
type: concept
title: "Fencing Token"
aliases: ["fencing token", "monotonic token", "lock token"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [sistemas-distribuidos, distributed-locks, concorrencia, redis, etcd]
skill: tech-mentor-system-design
status: stable
---

# Fencing Token

Token monotonicamente crescente emitido junto com um [[concepts/distributed-lock]]. Resolve o problema de lock "fantasma": processo lento ressuscita após o TTL expirar e acredita ainda ter o lock.

## O Problema sem Fencing Token

```
Processo A obtém lock → token=33
Processo A fica lento (GC pause, swap, rede)
Lock TTL expira
Processo B obtém lock → token=34
Processo B escreve → aceito
Processo A "ressuscita" e tenta escrever → SEM fencing token, aceito também
→ dois processos operaram sobre o mesmo recurso simultaneamente
```

## A Solução

```
Storage protegido mantém o lastToken recebido.
Processo A tenta escrever com token=33 → 33 < 34 → REJEITADO
```

O recurso protegido — não o cliente — é responsável por validar o token.

## Implementação

```typescript
class LockServer {
  private fenceCounter = 0;

  async acquireLock(key: string, ttl: number): Promise<{ token: number } | null> {
    const acquired = await redis.set(key, "locked", { NX: true, EX: ttl });
    if (!acquired) return null;
    this.fenceCounter++;
    await redis.set(`${key}:token`, this.fenceCounter);
    return { token: this.fenceCounter };
  }
}

class ProtectedStorage {
  private lastToken = 0;

  async write(data: unknown, fencingToken: number): Promise<void> {
    if (fencingToken <= this.lastToken) {
      throw new Error(`Stale lock: token ${fencingToken} ≤ current ${this.lastToken}`);
    }
    this.lastToken = fencingToken;
    // persiste os dados
  }
}
```

## Redlock e a Ausência de Fencing Token

Redlock (algoritmo Redis multi-nó) não implementa fencing tokens. Em falha de nó, pode conceder o mesmo lock a dois processos. Para recursos onde **corretude > disponibilidade**: usar etcd ou ZooKeeper, que têm semântica de lease com token monotônico nativo.

## Key Sources

- [[sources/skip-locked-fencing-token]]
