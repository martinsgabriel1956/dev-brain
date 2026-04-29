---
date: 2026-04-23
tags: [tech-mentor, mobile, offline-first, sync-queue, conflict-resolution, lww, crdt, delta-sync]
skill: tech-mentor-mobile/references/offline-first
level: avançado
---

# Offline-First Avançado — Sync Queue, Conflict Resolution, Delta Sync

## Contexto
Offline-first básico (LWW simples) quebra quando múltiplos usuários editam o mesmo dado offline simultaneamente, ou quando o usuário usa dois devices. Offline-first avançado resolve conflitos de forma determinística e sincroniza apenas o delta de mudanças — não re-baixa tudo a cada sync. É o que separa apps de campo profissionais de protótipos.

## Como Funciona

### 1. Conflict Resolution — Last Write Wins (LWW) com Timestamp

O mais simples: quem tem o timestamp mais recente ganha.

```typescript
type DocumentVersion = {
  id: string;
  data: Record<string, unknown>;
  updatedAt: number; // unix timestamp em ms
  deviceId: string;
};

// Resolver conflito no backend
function resolveConflictLWW(local: DocumentVersion, remote: DocumentVersion): DocumentVersion {
  return local.updatedAt > remote.updatedAt ? local : remote;
}
```

**Problema:** clocks de devices não são confiáveis — um device com relógio adiantado sempre "ganha", mesmo com dados obsoletos.

**Solução:** Lamport timestamps ou Vector clocks para ordering lógico:

```typescript
// Lamport Clock — contador lógico, não depende de relógio real
type LamportClock = number;

function incrementClock(clock: LamportClock): LamportClock {
  return clock + 1;
}

function mergeClock(local: LamportClock, remote: LamportClock): LamportClock {
  return Math.max(local, remote) + 1;
}

type VersionedDoc<T> = {
  id: string;
  data: T;
  clock: LamportClock;
  deviceId: string;
};

function resolveConflictLamport<T>(
  local: VersionedDoc<T>,
  remote: VersionedDoc<T>
): VersionedDoc<T> {
  if (local.clock !== remote.clock) {
    return local.clock > remote.clock ? local : remote;
  }
  // Tie-break por deviceId (determinístico)
  return local.deviceId > remote.deviceId ? local : remote;
}
```

### 2. Conflict Resolution — CRDT (Conflict-free Replicated Data Types)

CRDTs são estruturas de dados que se mesclam automaticamente sem conflito. Cada operação é comutativa e idempotente — pode ser aplicada em qualquer ordem, múltiplas vezes, com o mesmo resultado.

**G-Counter (Grow-Only Counter):** cada device tem seu próprio contador, o valor total é a soma.

```typescript
type GCounter = Record<string, number>; // deviceId → count

function increment(counter: GCounter, deviceId: string): GCounter {
  return { ...counter, [deviceId]: (counter[deviceId] ?? 0) + 1 };
}

function value(counter: GCounter): number {
  return Object.values(counter).reduce((sum, v) => sum + v, 0);
}

// Merge: pega o máximo de cada device
function merge(a: GCounter, b: GCounter): GCounter {
  const result: GCounter = { ...a };
  for (const [deviceId, count] of Object.entries(b)) {
    result[deviceId] = Math.max(result[deviceId] ?? 0, count);
  }
  return result;
}
```

**LWW-Element-Set (conjunto com timestamps):** cada elemento tem um timestamp de add/remove.

```typescript
type LWWSet<T> = {
  adds: Map<string, { value: T; timestamp: number }>;
  removes: Map<string, number>;
};

function add<T>(set: LWWSet<T>, key: string, value: T, timestamp: number): LWWSet<T> {
  return {
    ...set,
    adds: new Map([...set.adds, [key, { value, timestamp }]])
  };
}

function remove<T>(set: LWWSet<T>, key: string, timestamp: number): LWWSet<T> {
  return {
    ...set,
    removes: new Map([...set.removes, [key, timestamp]])
  };
}

function lookup<T>(set: LWWSet<T>, key: string): T | null {
  const added = set.adds.get(key);
  const removed = set.removes.get(key) ?? -1;
  if (!added) return null;
  return added.timestamp >= removed ? added.value : null;
}

function mergeSets<T>(a: LWWSet<T>, b: LWWSet<T>): LWWSet<T> {
  const adds = new Map(a.adds);
  for (const [key, entry] of b.adds) {
    const existing = adds.get(key);
    if (!existing || entry.timestamp > existing.timestamp) adds.set(key, entry);
  }

  const removes = new Map(a.removes);
  for (const [key, ts] of b.removes) {
    removes.set(key, Math.max(removes.get(key) ?? -1, ts));
  }

  return { adds, removes };
}
```

**Automerge / Yjs — CRDTs prontos para produção:**

```typescript
import * as Y from "yjs";
import { IndexeddbPersistence } from "y-indexeddb";

// Documento compartilhado
const doc = new Y.Doc();
const taskList = doc.getArray<Task>("tasks");

// Persistência local
const persistence = new IndexeddbPersistence("tasks-db", doc);

// Editar
doc.transact(() => {
  taskList.push([{ id: crypto.randomUUID(), title: "Nova tarefa", completed: false }]);
});

// Sync com servidor
const updates = Y.encodeStateAsUpdate(doc);
await sendToServer(updates);

// Aplicar update do servidor
const serverUpdate = await fetchServerUpdate();
Y.applyUpdate(doc, serverUpdate); // CRDT garante convergência sem conflito
```

### 3. Delta Sync — Sincronizar apenas mudanças

Baixar tudo a cada sync é ineficiente. Delta sync busca apenas o que mudou desde o último sync.

```typescript
// Servidor guarda versão de cada recurso
type SyncCheckpoint = {
  userId: string;
  lastSyncedAt: number; // unix timestamp
  version: number;      // número de sequência (mais confiável que timestamp)
};

// API de delta sync
// GET /sync?since_version=1234&device_id=abc
type DeltaSyncResponse = {
  changes: Array<{
    type: "created" | "updated" | "deleted";
    entity: string;
    id: string;
    data: Record<string, unknown> | null;
    version: number;
  }>;
  currentVersion: number;
  hasMore: boolean;
};

// Cliente
class DeltaSyncClient {
  private storage: MMKV;

  constructor() {
    this.storage = new MMKV({ id: "sync-state" });
  }

  getLastVersion(): number {
    return this.storage.getNumber("last_sync_version") ?? 0;
  }

  async sync(): Promise<void> {
    const since = this.getLastVersion();
    let hasMore = true;

    while (hasMore) {
      const { changes, currentVersion, hasMore: more } = await http.get<DeltaSyncResponse>(
        `/sync?since_version=${since}&device_id=${deviceId}`
      );

      await this.applyChanges(changes);
      this.storage.set("last_sync_version", currentVersion);
      hasMore = more;
    }
  }

  private async applyChanges(changes: DeltaSyncResponse["changes"]): Promise<void> {
    db.runSync("BEGIN TRANSACTION");
    try {
      for (const change of changes) {
        switch (change.type) {
          case "created":
          case "updated":
            db.runSync(
              `INSERT OR REPLACE INTO ${change.entity} SELECT * FROM json_each(?)`,
              [JSON.stringify(change.data)]
            );
            break;
          case "deleted":
            db.runSync(`DELETE FROM ${change.entity} WHERE id = ?`, [change.id]);
            break;
        }
      }
      db.runSync("COMMIT");
    } catch {
      db.runSync("ROLLBACK");
    }
  }
}
```

### Sync Queue Avançada — Operações com dependências

```typescript
// Problema: criar um comentário requer que o post exista no servidor
// Se o post foi criado offline, o ID local pode não existir no servidor ainda

type OperationWithDeps = {
  id: string;
  type: "create" | "update" | "delete";
  entity: string;
  payload: Record<string, unknown>;
  dependsOn: string | null; // ID de outra operação que deve ser executada antes
  serverIdMap: Record<string, string>; // localId → serverId
};

class OrderedSyncQueue {
  async processWithDependencies(operations: OperationWithDeps[]): Promise<void> {
    const serverIdMap: Record<string, string> = {};
    const sorted = this.topologicalSort(operations);

    for (const op of sorted) {
      // Substituir IDs locais por IDs do servidor
      const resolvedPayload = this.resolveLocalIds(op.payload, serverIdMap);

      const response = await this.execute({ ...op, payload: resolvedPayload });

      // Registrar mapeamento localId → serverId
      if (op.type === "create" && response.serverId) {
        serverIdMap[op.payload.id as string] = response.serverId;
      }
    }
  }

  private topologicalSort(ops: OperationWithDeps[]): OperationWithDeps[] {
    // Ordenação topológica para respeitar dependências
    const result: OperationWithDeps[] = [];
    const visited = new Set<string>();
    const opMap = new Map(ops.map(op => [op.id, op]));

    function visit(op: OperationWithDeps) {
      if (visited.has(op.id)) return;
      if (op.dependsOn) {
        const dep = opMap.get(op.dependsOn);
        if (dep) visit(dep);
      }
      visited.add(op.id);
      result.push(op);
    }

    ops.forEach(visit);
    return result;
  }
}
```

## Trade-offs

| Estratégia | Complexidade | Conflitos | Colaboração real-time | Ideal para |
|---|---|---|---|---|
| LWW simples (timestamp) | Baixa | Perde dados | Não | Um usuário, múltiplos devices |
| LWW + Lamport clock | Média | Determinístico | Não | Múltiplos usuários com edições raras |
| CRDT | Alta | Zero conflito | Sim | Documentos colaborativos |
| Delta Sync | Média | Depende da estratégia | Não | Reduzir payload de sync |

## Quando Usar / Quando Evitar

**LWW** para apps de usuário único ou onde perder a edição de um device é aceitável (ex: notas pessoais).

**CRDT** para colaboração em tempo real ou quando integridade de dados é crítica (documento legal, planilha compartilhada).

**Delta Sync** sempre que o dataset for grande — evita re-baixar 10MB de dados para sincronizar 3 registros.

**Evite CRDTs custom** — use Automerge ou Yjs que já estão testados em produção. Implementar CRDT do zero é arriscado.

## Conceitos Relacionados
[[mobile-offline-first-basico]] · [[mobile-armazenamento-local]] · [[cap-theorem]] · [[mobile-monitoramento]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
